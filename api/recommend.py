import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from .ai_service import call_openai
from .config import COLOR_FOOD_DATA, MAX_REQUEST_BYTES
from .validation import filter_excluded_foods, validate_ai_result, validate_request_data


app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent

app.mount("/css", StaticFiles(directory=BASE_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=BASE_DIR / "js"), name="js")
app.mount("/images", StaticFiles(directory=BASE_DIR / "images"), name="images")


@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/api/recommend")
async def health_check():
    """Serverless Function의 실행 여부를 확인하는 Health Check."""
    return {
        "success": True,
        "message": "AI Food Guide API가 정상적으로 실행 중입니다.",
    }


def _error_response(status_code, message):
    """API 오류 응답 형식을 한 곳에서 관리한다."""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
        },
    )


def _apply_static_data(result):
    """정적 영양정보를 확정하고 허용 식품 중에서만 대안을 채택한다."""
    if not isinstance(result, dict):
        raise ValueError("AI 추천 결과가 객체 형식이 아닙니다.")

    color = result.get("recommended_color")
    food = result.get("representative_food")
    if not isinstance(color, str) or color not in COLOR_FOOD_DATA:
        raise ValueError("알 수 없는 컬러입니다.")
    info = COLOR_FOOD_DATA[color]
    if not isinstance(food, str) or food not in info["representative_foods"]:
        raise ValueError("컬러와 대표 식품이 일치하지 않습니다.")

    nutrition = info.get("food_nutrition", {}).get(food)
    if not nutrition:
        raise ValueError("대표 식품의 기준 영양정보가 없습니다.")

    # 후보가 정적 기준 식품 목록에 존재하는 경우에만 채택한다.
    # AI의 순서는 존중하지만 허용되지 않은 음식과 중복 제안은 제외한다.
    all_foods = [
        candidate
        for group in COLOR_FOOD_DATA.values()
        for candidate in group["representative_foods"]
    ]
    allowed = set(all_foods) - {food}
    ai_candidates = result.get("alternative_foods", [])
    if not isinstance(ai_candidates, list):
        ai_candidates = []
    chosen = [
        candidate for candidate in ai_candidates
        if isinstance(candidate, str) and candidate in allowed
    ]

    # AI가 허용 식품을 충분히 제안하지 않으면 동일 컬러 식품부터 보충한다.
    same_color = [candidate for candidate in info["representative_foods"] if candidate != food]
    other_colors = [candidate for candidate in all_foods if candidate not in info["representative_foods"]]
    unique_chosen = list(dict.fromkeys(chosen))
    # 기본 2개를 제시하되, 유효한 AI 제안이 3개이면 최대 3개까지 유지한다.
    desired_count = max(2, min(3, len(unique_chosen)))
    alternatives = list(dict.fromkeys(unique_chosen + same_color + other_colors))[:desired_count]
    if not alternatives:
        raise ValueError("대안 식품 기준 후보가 없습니다.")

    return {
        **result,
        "nutrition": list(nutrition),
        "alternative_foods": alternatives,
    }


@app.post("/api/recommend")
async def recommend(request: Request):
    """입력과 AI 결과를 각각 검증한 뒤 Frontend에 반환한다."""
    try:
        content_length_header = request.headers.get("content-length")

        if content_length_header:
            try:
                content_length = int(content_length_header)
            except ValueError:
                return _error_response(
                    400,
                    "입력 데이터 형식이 올바르지 않습니다.",
                )

            if content_length > MAX_REQUEST_BYTES:
                return _error_response(
                    413,
                    "입력 내용이 너무 깁니다.",
                )

        raw_body = await request.body()

        if not raw_body:
            return _error_response(
                400,
                "입력 내용을 확인해 주세요.",
            )

        if len(raw_body) > MAX_REQUEST_BYTES:
            return _error_response(
                413,
                "입력 내용이 너무 깁니다.",
            )

        try:
            request_data = json.loads(raw_body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return _error_response(
                400,
                "입력 데이터 형식이 올바르지 않습니다.",
            )

        try:
            validated_input = validate_request_data(request_data)
        except ValueError as error:
            return _error_response(400, str(error))

        ai_result = await call_openai(validated_input)

        try:
            # PRIORITY-2: AI 후보를 허용 식품으로 제한하고 정적 영양정보를 먼저 적용
            static_result = _apply_static_data(ai_result)
            validated_result = validate_ai_result(static_result)
        except ValueError as error:
            # 사용자 입력 문제가 아니라 AI 응답이 서비스 계약을 지키지 못한 경우다.
            # 따라서 4xx가 아닌 Upstream 응답 오류(502)로 처리한다.
            print(
                "AI Result Validation Error:",
                type(error).__name__,
                str(error),
            )
            return _error_response(
                502,
                (
                    "AI 응답 형식을 확인할 수 없습니다. "
                    "잠시 후 다시 시도해 주세요."
                ),
            )

        # PRIORITY-1: 사용자 제외 음식 차단, 대안 목록 재구성, 최종 응답 검증
        try:
            validated_result = filter_excluded_foods(
                validated_result,
                validated_input["allergies"],
                validated_input["avoid_foods"],
            )
            validated_result = validate_ai_result(validated_result)
        except ValueError as error:
            print("Excluded Food Validation Error:", type(error).__name__, str(error))
            return _error_response(
                502,
                "제외 식품 조건을 충족하는 식생활 안내서를 생성하지 못했습니다."
            )

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "data": validated_result,
            },
        )

    except Exception as error:
        # Vercel Runtime Logs용.
        # API Key와 사용자 입력 전체는 기록하지 않는다.
        print(
            "recommend.py Error:",
            type(error).__name__,
            str(error),
        )

        return _error_response(
            500,
            (
                "AI 식생활 안내서를 불러오지 못했습니다. "
                "잠시 후 다시 시도해 주세요."
            ),
        )
