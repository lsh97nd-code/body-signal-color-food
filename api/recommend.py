import asyncio
import json
import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from openai import AsyncOpenAI


# --------------------------------------------------
# 기본 설정
# --------------------------------------------------

MODEL_NAME = "gpt-5.6-luna"

MAX_REQUEST_BYTES = 16_384

REQUIRED_RESPONSE_KEYS = [
    "recommended_color",
    "representative_food",
    "reason",
    "nutrition",
    "alternative_foods",
    "food_guide",
    "caution",
    "health_notice",
]

ALLOWED_COLORS = {
    "Yellow",
    "Purple",
    "Red",
    "Green",
}

ALLOWED_BODY_SIGNALS = {
    "피로감을 자주 느낌",
    "배변이 불편함",
    "식사가 불규칙함",
    "과일·채소 섭취가 부족함",
    "소화가 부담스러움",
}

ALLOWED_FRUIT_VEGETABLE_INTAKE = {
    "",
    "부족함",
    "보통",
    "충분함",
}

ALLOWED_EATING_HABITS = {
    "",
    "식사가 불규칙함",
    "간편식이나 외식을 자주 이용함",
    "비교적 규칙적으로 식사함",
}


# --------------------------------------------------
# 서비스 기준 데이터
# --------------------------------------------------

COLOR_FOOD_DATA = {
    "Yellow": {
        "representative_foods": [
            "레몬",
            "감귤류",
        ],
        "nutrition": [
            "비타민 C",
            "플라보노이드",
        ],
    },
    "Purple": {
        "representative_foods": [
            "블루베리",
            "포도",
        ],
        "nutrition": [
            "안토시아닌",
        ],
    },
    "Red": {
        "representative_foods": [
            "체리",
            "복분자",
            "토마토",
            "사과",
        ],
        "nutrition": [
            "안토시아닌",
            "라이코펜",
        ],
    },
    "Green": {
        "representative_foods": [
            "키위",
            "아보카도",
            "멜론",
        ],
        "nutrition": [
            "비타민 C",
            "비타민 E",
            "엽산",
            "칼륨",
            "식이섬유",
        ],
    },
}


REFERENCE_DATA = {
    "color_foods": COLOR_FOOD_DATA,
    "whole_food": {
        "summary": (
            "과일과 채소의 먹을 수 있는 부분을 가능한 범위에서 "
            "버리지 않고 활용하는 개념이다."
        ),
        "rules": [
            "모든 식품의 껍질을 먹을 수 있는 것은 아니다.",
            "섭취 가능한 부분과 먹지 않는 부분을 구분한다.",
            (
                "껍질째 섭취 가능한 식품도 충분한 세척과 "
                "위생 관리가 필요하다."
            ),
        ],
    },
    "whole_grain": {
        "foods": [
            "현미",
            "통밀",
            "통메밀",
        ],
        "nutrition": [
            "식이섬유",
            "비타민",
            "미네랄",
            "단백질",
        ],
        "rules": [
            "개인의 소화 상태와 식습관을 고려한다.",
            "모든 사용자에게 동일하게 적합하다고 단정하지 않는다.",
        ],
    },
}


# --------------------------------------------------
# Structured Outputs Schema
# --------------------------------------------------

AI_RESPONSE_SCHEMA = {
    "type": "json_schema",
    "name": "food_guide_result",
    "description": (
        "오늘의 몸 신호 AI 컬러푸드 가이드의 식생활 안내 결과"
    ),
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "recommended_color": {
                "type": "string",
                "enum": [
                    "Yellow",
                    "Purple",
                    "Red",
                    "Green",
                ],
            },
            "representative_food": {
                "type": "string",
            },
            "reason": {
                "type": "string",
            },
            "nutrition": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "alternative_foods": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "food_guide": {
                "type": "string",
            },
            "caution": {
                "type": "string",
            },
            "health_notice": {
                "type": "string",
            },
        },
        "required": REQUIRED_RESPONSE_KEYS,
        "additionalProperties": False,
    },
}


# --------------------------------------------------
# OpenAI Client
# --------------------------------------------------

_openai_client = None
_openai_client_lock = asyncio.Lock()


async def get_openai_client():
    """
    Vercel의 같은 실행 환경이 재사용되는 경우
    AsyncOpenAI Client도 재사용한다.

    첫 요청이 동시에 들어와도 Lock을 사용해
    Client가 중복 생성되지 않도록 한다.
    """

    global _openai_client

    if _openai_client is not None:
        return _openai_client

    async with _openai_client_lock:
        if _openai_client is not None:
            return _openai_client

        api_key = os.getenv("AI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "AI_API_KEY 환경변수가 설정되어 있지 않습니다."
            )

        _openai_client = AsyncOpenAI(
            api_key=api_key,
        )

    return _openai_client

    api_key = os.getenv("AI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "AI_API_KEY 환경변수가 설정되어 있지 않습니다."
        )

    _openai_client = OpenAI(
        api_key=api_key,
    )

    return _openai_client


# --------------------------------------------------
# Backend 입력값 정리
# --------------------------------------------------

def clean_text(value, max_length):
    """
    문자열 입력값의 앞뒤 공백을 제거하고
    허용 길이를 확인한다.
    """

    if value is None:
        return ""

    if not isinstance(value, str):
        raise ValueError(
            "문자열 형식이 아닌 입력값이 포함되어 있습니다."
        )

    cleaned_value = value.strip()

    if len(cleaned_value) > max_length:
        raise ValueError(
            f"입력값은 {max_length}자 이하로 입력해 주세요."
        )

    return cleaned_value


def clean_string_list(
    value,
    max_items=10,
    max_length=100,
):
    """
    문자열 배열을 검증하고 빈 문자열을 제거한다.
    """

    if value is None:
        return []

    if not isinstance(value, list):
        raise ValueError(
            "목록 형식의 입력값이 올바르지 않습니다."
        )

    if len(value) > max_items:
        raise ValueError(
            f"선택 항목은 최대 {max_items}개까지 입력할 수 있습니다."
        )

    result = []

    for item in value:
        if not isinstance(item, str):
            raise ValueError(
                "목록에는 문자열 형식의 값만 사용할 수 있습니다."
            )

        cleaned_item = item.strip()

        if not cleaned_item:
            continue

        if len(cleaned_item) > max_length:
            raise ValueError(
                f"각 항목은 {max_length}자 이하로 입력해 주세요."
            )

        result.append(
            cleaned_item
        )

    return result


# --------------------------------------------------
# Frontend 요청값 검증
# --------------------------------------------------

def validate_request_data(data):
    """
    main.js에서 전달된 JSON을 Backend에서 다시 검증한다.
    """

    if not isinstance(data, dict):
        raise ValueError(
            "요청 데이터 형식이 올바르지 않습니다."
        )

    body_signals = clean_string_list(
        data.get("body_signals"),
        max_items=5,
        max_length=100,
    )

    custom_signal = clean_text(
        data.get("custom_signal"),
        max_length=300,
    )

    fruit_vegetable_intake = clean_text(
        data.get("fruit_vegetable_intake"),
        max_length=20,
    )

    eating_habits = clean_text(
        data.get("eating_habits"),
        max_length=100,
    )

    allergies = clean_text(
        data.get("allergies"),
        max_length=100,
    )

    avoid_foods = clean_text(
        data.get("avoid_foods"),
        max_length=100,
    )

    notes = clean_text(
        data.get("notes"),
        max_length=300,
    )

    if (
        not body_signals
        and not custom_signal
    ):
        raise ValueError(
            "생활 속 이상 신호 등 몸 상태를 한 가지 이상 "
            "선택하거나 기타 상태를 입력해 주세요."
        )

    invalid_body_signals = [
        item
        for item in body_signals
        if item not in ALLOWED_BODY_SIGNALS
    ]

    if invalid_body_signals:
        raise ValueError(
            "허용되지 않은 몸 상태 선택값이 포함되어 있습니다."
        )

    if (
        fruit_vegetable_intake
        not in ALLOWED_FRUIT_VEGETABLE_INTAKE
    ):
        raise ValueError(
            "과일·채소 섭취 정도 선택값이 올바르지 않습니다."
        )

    if (
        eating_habits
        not in ALLOWED_EATING_HABITS
    ):
        raise ValueError(
            "식생활 습관 선택값이 올바르지 않습니다."
        )

    return {
        "body_signals": body_signals,
        "custom_signal": custom_signal,
        "fruit_vegetable_intake": fruit_vegetable_intake,
        "eating_habits": eating_habits,
        "allergies": allergies,
        "avoid_foods": avoid_foods,
        "notes": notes,
    }


# --------------------------------------------------
# OpenAI Prompt 구성
# --------------------------------------------------

def build_prompt(user_data):
    """
    사용자 입력과 서비스 기준 데이터를
    OpenAI에 전달할 Prompt로 구성한다.
    """

    return f"""
다음은 건강한 식생활 참고 정보를 제공하는
'오늘의 몸 신호, AI 컬러푸드 가이드' 웹 서비스이다.

사용자의 입력과 아래 제공된 서비스 기준 정보만을 참고하여
사용자가 이해하기 쉬운 식생활 안내 정보를 생성하라.

중요한 원칙:

1. 질병을 진단하지 않는다.
2. 특정 음식이 질병을 치료하거나 예방한다고 단정하지 않는다.
3. 특정 증상과 특정 음식을 1:1 치료 관계로 연결하지 않는다.
4. 제공된 컬러푸드·Whole Food·Whole Grain 정보를 우선 사용한다.
5. 사용자가 입력한 알레르기 관련 정보와 피하고 싶은 음식을 고려한다.
6. 건강한 식생활을 위한 참고 정보라는 점을 명확하게 안내한다.
7. recommended_color는 Yellow, Purple, Red, Green 중 하나만 사용한다.
8. representative_food는 추천 Color의 representative_foods 안에서 하나만 선택한다.
9. nutrition과 alternative_foods는 비어 있지 않은 문자열 배열로 작성한다.
10. 과장된 의학적 표현이나 치료 효과를 작성하지 않는다.

[사용자 입력]

{json.dumps(user_data, ensure_ascii=False, indent=2)}

[서비스 기준 정보]

{json.dumps(REFERENCE_DATA, ensure_ascii=False, indent=2)}
""".strip()


# --------------------------------------------------
# OpenAI API 호출
# --------------------------------------------------

async def call_openai(user_data):
    """
    OpenAI Responses API를 비동기로 호출하고
    Structured Outputs 결과를 Dictionary로 변환한다.
    """

    client = await get_openai_client()

    response = await client.responses.create(
        model=MODEL_NAME,
        input=build_prompt(
            user_data
        ),
        text={
            "format": AI_RESPONSE_SCHEMA,
        },
    )

    response_text = (
        response.output_text
        or ""
    ).strip()

    if not response_text:
        raise RuntimeError(
            "AI가 비어 있는 응답을 반환했습니다."
        )

    try:
        result = json.loads(
            response_text
        )
    except json.JSONDecodeError as error:
        raise RuntimeError(
            "AI 응답을 JSON 형식으로 해석할 수 없습니다."
        ) from error

    return result


# --------------------------------------------------
# AI 응답 검증
# --------------------------------------------------

def validate_ai_result(result):
    """
    AI가 반환한 JSON 구조와 결과값을 다시 검증한다.

    Structured Outputs를 사용하더라도
    서비스 기준값 검증은 Backend에서 한 번 더 수행한다.
    """

    if not isinstance(result, dict):
        raise ValueError(
            "AI 응답이 JSON Object 형식이 아닙니다."
        )

    missing_keys = [
        key
        for key in REQUIRED_RESPONSE_KEYS
        if key not in result
    ]

    if missing_keys:
        raise ValueError(
            "AI 응답에 필요한 항목이 누락되었습니다."
        )

    unexpected_keys = [
        key
        for key in result
        if key not in REQUIRED_RESPONSE_KEYS
    ]

    if unexpected_keys:
        raise ValueError(
            "AI 응답에 예상하지 않은 항목이 포함되어 있습니다."
        )

    recommended_color = (
        result["recommended_color"]
    )

    if (
        not isinstance(
            recommended_color,
            str,
        )
        or recommended_color
        not in ALLOWED_COLORS
    ):
        raise ValueError(
            "AI가 허용되지 않은 Color를 반환했습니다."
        )

    string_keys = [
        "representative_food",
        "reason",
        "food_guide",
        "caution",
        "health_notice",
    ]

    cleaned_strings = {}

    for key in string_keys:
        value = result[key]

        if not isinstance(
            value,
            str,
        ):
            raise ValueError(
                f"{key} 값의 자료형이 올바르지 않습니다."
            )

        cleaned_value = (
            value.strip()
        )

        if not cleaned_value:
            raise ValueError(
                f"{key} 값이 비어 있습니다."
            )

        cleaned_strings[key] = (
            cleaned_value
        )

    array_keys = [
        "nutrition",
        "alternative_foods",
    ]

    cleaned_arrays = {}

    for key in array_keys:
        value = result[key]

        if (
            not isinstance(
                value,
                list,
            )
            or not value
        ):
            raise ValueError(
                f"{key} 값이 올바른 Array 형식이 아닙니다."
            )

        cleaned_items = []

        for item in value:
            if not isinstance(
                item,
                str,
            ):
                raise ValueError(
                    f"{key} 안에 문자열이 아닌 값이 있습니다."
                )

            cleaned_item = (
                item.strip()
            )

            if not cleaned_item:
                raise ValueError(
                    f"{key} 안에 빈 값이 있습니다."
                )

            cleaned_items.append(
                cleaned_item
            )

        cleaned_arrays[key] = (
            cleaned_items
        )

    representative_food = (
        cleaned_strings[
            "representative_food"
        ]
    )

    allowed_foods = (
        COLOR_FOOD_DATA[
            recommended_color
        ]["representative_foods"]
    )

    if (
        representative_food
        not in allowed_foods
    ):
        raise ValueError(
            "추천 대표 식품이 서비스 기준 컬러푸드 정보와 "
            "일치하지 않습니다."
        )

    return {
        "recommended_color": (
            recommended_color
        ),
        "representative_food": (
            representative_food
        ),
        "reason": (
            cleaned_strings[
                "reason"
            ]
        ),
        "nutrition": (
            cleaned_arrays[
                "nutrition"
            ]
        ),
        "alternative_foods": (
            cleaned_arrays[
                "alternative_foods"
            ]
        ),
        "food_guide": (
            cleaned_strings[
                "food_guide"
            ]
        ),
        "caution": (
            cleaned_strings[
                "caution"
            ]
        ),
        "health_notice": (
            cleaned_strings[
                "health_notice"
            ]
        ),
    }


# --------------------------------------------------
# Vercel Serverless Function
# FastAPI / ASGI Entry Point
# --------------------------------------------------

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

app.mount(
    "/css",
    StaticFiles(directory=BASE_DIR / "css"),
    name="css",
)

app.mount(
    "/js",
    StaticFiles(directory=BASE_DIR / "js"),
    name="js",
)

app.mount(
    "/images",
    StaticFiles(directory=BASE_DIR / "images"),
    name="images",
)


@app.get("/")
async def home():
    return FileResponse(
        BASE_DIR / "index.html"
    )


@app.get("/api/recommend")
async def health_check():
    """
    Browser에서 /api/recommend를 직접 열어
    Serverless Function의 실행 여부를 확인한다.
    """

    return {
        "success": True,
        "message": "AI Food Guide API가 정상적으로 실행 중입니다.",
    }


@app.post("/api/recommend")
async def recommend(request: Request):
    """
    POST /api/recommend

    Frontend에서 전달된 JSON을 검증하고,
    OpenAI API를 호출한 뒤 검증된 결과를 반환한다.
    """

    try:
        content_length_header = request.headers.get("content-length")

        if content_length_header:
            try:
                content_length = int(content_length_header)
            except ValueError:
                return JSONResponse(
                    status_code=400,
                    content={
                        "success": False,
                        "message": "입력 데이터 형식이 올바르지 않습니다.",
                    },
                )

            if content_length <= 0:
                return JSONResponse(
                    status_code=400,
                    content={
                        "success": False,
                        "message": "입력 내용을 확인해 주세요.",
                    },
                )

            if content_length > MAX_REQUEST_BYTES:
                return JSONResponse(
                    status_code=413,
                    content={
                        "success": False,
                        "message": "입력 내용이 너무 깁니다.",
                    },
                )

        raw_body = await request.body()

        if not raw_body:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "입력 내용을 확인해 주세요.",
                },
            )

        if len(raw_body) > MAX_REQUEST_BYTES:
            return JSONResponse(
                status_code=413,
                content={
                    "success": False,
                    "message": "입력 내용이 너무 깁니다.",
                },
            )

        try:
            request_data = json.loads(
                raw_body.decode("utf-8")
            )
        except (
            json.JSONDecodeError,
            UnicodeDecodeError,
        ):
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "입력 데이터 형식이 올바르지 않습니다.",
                },
            )

        # Backend 입력값 재검증
        try:
            validated_input = validate_request_data(
                request_data
            )
        except ValueError as error:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": str(error),
                },
            )

        # OpenAI API 호출

        ai_result = await call_openai(
            validated_input
        )

        # AI 결과 재검증
        validated_result = validate_ai_result(
            ai_result
        )

        # main.js가 기대하는 정상 응답
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

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": (
                    "AI 식생활 안내서를 불러오지 못했습니다. "
                    "잠시 후 다시 시도해 주세요."
                ),
            },
        )

