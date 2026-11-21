import json

from .config import REFERENCE_DATA


def build_prompt(user_data):
    """사용자 입력과 서비스 기준 데이터를 AI 요청 Prompt로 구성한다."""
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
9. nutrition은 선택한 대표 식품의 food_nutrition에 수록된 정보만 참고한다.
   alternative_foods는 서비스 기준 정보의 representative_foods에 수록된 식품 중
   선택한 대표 식품을 제외하고 사용자에게 적합한 후보를 최대 3개 제안한다.
   다른 컬러에 속한 식품도 선택할 수 있지만 기준 목록 밖의 식품은 제안하지 않는다.
   최종 nutrition 값은 Backend가 정적 기준 데이터로 확정하고,
   alternative_foods는 Backend가 허용 목록으로 검증·보완한다.
   알레르기·기피 식품은 제안하지 않는다.
10. 과장된 의학적 표현이나 치료 효과를 작성하지 않는다.
11. food_guide에는 가능한 경우 daily_use_examples를 참고하여
    사용자가 일상에서 적용하기 쉬운 활용 예시를 포함한다.
12. 응답은 간결하게 작성하고 다음 길이를 넘기지 않는다.
    - representative_food: 50자
    - reason: 500자
    - food_guide: 800자
    - caution: 500자
    - health_notice: 500자
13. nutrition은 최대 10개, alternative_foods는 최대 3개 항목으로 작성하고,
    각 항목은 100자 이하의 짧은 문장 또는 구문으로 작성한다.

[사용자 입력]

{json.dumps(user_data, ensure_ascii=False, indent=2)}

[서비스 기준 정보]

{json.dumps(REFERENCE_DATA, ensure_ascii=False, indent=2)}
""".strip()
