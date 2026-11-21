"""body-signal-color-food 로컬 검증: OpenAI 호출 없는 FastAPI 모의 테스트.

실행 환경: WSL, 프로젝트 루트에서 `python /path/to/check_excluded_foods_no_api.py`
API Key가 필요하지 않습니다. 기존 프로젝트 코드를 수정하지 않습니다.
"""
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import sys
from types import ModuleType

from fastapi.testclient import TestClient

# 스크립트가 프로젝트 바깥에 있어도 현재 작업 디렉터리의 프로젝트를 읽습니다.
project = Path.cwd()
expected = [project / "api" / name for name in ("recommend.py", "validation.py", "config.py")]
if not all(path.is_file() for path in expected):
    raise SystemExit("오류: 먼저 body-signal-color-food 프로젝트 폴더로 이동하세요.")
sys.path.insert(0, str(project))

# 네트워크 호출 방지를 위해 AI 서비스 모듈을 가져오는 단계부터 차단합니다.
service_stub = ModuleType("api.ai_service")
async def _blocked_live_api(*args, **kwargs):
    raise AssertionError("실제 AI API 호출을 차단했습니다.")
service_stub.call_openai = _blocked_live_api
sys.modules["api.ai_service"] = service_stub

from api.recommend import app  # noqa: E402
import api.recommend as recommend_module  # noqa: E402
from api.config import COLOR_FOOD_DATA  # noqa: E402
from api.validation import detect_excluded_foods, validate_ai_result  # noqa: E402

REQUEST = {
    "body_signals": ["피로감을 자주 느낌"],
    "custom_signal": "",
    "fruit_vegetable_intake": "보통",
    "eating_habits": "식사가 불규칙함",
    "allergies": "",
    "avoid_foods": "",
    "notes": "",
}

def result(color="Yellow", food="감귤류", alternatives=None, reason="균형 잡힌 식생활을 참고하세요."):
    if alternatives is None:
        alternatives = ["레몬", "블루베리", "아보카도"]
    return {
        "recommended_color": color,
        "representative_food": food,
        "reason": reason,
        "nutrition": ["AI가 작성한 임의 영양소"],
        "alternative_foods": alternatives,
        "food_guide": "다양한 과일과 채소를 섭취하세요.",
        "caution": "개인의 건강 상태를 고려하세요.",
        "health_notice": "의학적 진단 및 치료 목적으로 사용하지 마세요.",
    }


def post(client, ai_result, **changes):
    request = deepcopy(REQUEST)
    request.update(changes)
    async def fake_ai(_validated_request):
        return deepcopy(ai_result)
    # 유료 AI API를 호출하는 함수를 완전히 대체합니다.
    with patch.object(recommend_module, "call_openai", new=fake_ai):
        return client.post("/api/recommend", json=request)


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    print("통과:", message)


def main():
    with TestClient(app) as client:
        # 1. 사진의 키위/아보카도/멜론 제외 입력
        response = post(client, result(alternatives=["레몬", "키위", "아보카도", "멜론"]),
                        allergies="키위 알레르기", avoid_foods="아보카도, 멜론")
        check(response.status_code == 200, "제외 입력 후 유효한 결과는 HTTP 200")
        data = response.json()["data"]
        check(data["nutrition"] == COLOR_FOOD_DATA["Yellow"]["food_nutrition"]["감귤류"],
              "감귤류 영양정보는 식이섬유를 포함한 정적 기준값")
        excluded = detect_excluded_foods("키위 알레르기", "아보카도, 멜론")
        check(excluded == {"키위", "아보카도", "멜론"}, "키위·아보카도·멜론 제외 입력 인식")
        check(data["representative_food"] not in excluded and
              not any(f in excluded for f in data["alternative_foods"]),
              "대표 및 대안 식품에서 제외 음식 제거")
        check(len(data["alternative_foods"]) >= 2,
              "사용 가능한 대안이 있으면 두 개 이상 보완")

        # 2. 대표 식품이 알레르기인 경우 차단
        response = post(client, result(color="Green", food="키위", alternatives=["아보카도", "멜론"]),
                        allergies="키위 알레르기")
        check(response.status_code == 502, "알레르기 식품이 대표 식품이면 결과 차단")

        # 3. 대안 하나 제외
        response = post(client, result(color="Green", food="키위", alternatives=["아보카도", "멜론"]),
                        avoid_foods="아보카도")
        check(response.status_code == 200 and "아보카도" not in response.json()["data"]["alternative_foods"],
              "기피 식품 아보카도를 대안에서 제외")

        # 4. 대안 두 개 제외 후 대체 식품 보완
        response = post(client, result(color="Green", food="키위", alternatives=["아보카도", "멜론"]),
                        avoid_foods="아보카도, 멜론")
        check(response.status_code == 200 and len(response.json()["data"]["alternative_foods"]) >= 2 and
              not {"아보카도", "멜론"}.intersection(response.json()["data"]["alternative_foods"]),
              "기피 식품 두 개 제외 후 안전성 미확인 후보를 추가하지 않고 등록 식품으로 보완")

        # 5. 대표 식품 제외 나머지 등록 식품 모두 차단
        remaining = [f for info in COLOR_FOOD_DATA.values() for f in info["representative_foods"] if f != "감귤류"]
        response = post(client, result(color="Yellow", food="감귤류"), avoid_foods=", ".join(remaining))
        check(response.status_code == 502, "가능한 모든 대안을 제외하면 결과 차단")

        # 6. 설명에 제외 식품이 있는 경우 차단
        response = post(client, result(reason="키위를 간식으로 권장합니다."), allergies="키위 알레르기")
        check(response.status_code == 502, "설명에 제외 식품 추천이 포함되면 결과 차단")

        # 7. 필터 적용 후 두 번째 응답 검증 실제 호출 확인
        original_validator = recommend_module.validate_ai_result
        with patch.object(recommend_module, "validate_ai_result", wraps=original_validator) as validator:
            response = post(client, result(), allergies="키위 알레르기", avoid_foods="아보카도, 멜론")
        check(response.status_code == 200 and validator.call_count == 2,
              "정적 데이터 적용 후 및 제외 필터링 후 두 차례 결과 검증")
    print("\n모든 모의 테스트 통과 · 실제 OpenAI API 호출 0회")

if __name__ == "__main__":
    main()
