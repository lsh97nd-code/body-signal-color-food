# Backend에서 함께 사용하는 설정값과 서비스 기준 데이터를 관리한다.

import os


# 현재 공개 API 모델을 기본값으로 사용하되, 배포 환경에서 AI_MODEL로 교체할 수 있다.
MODEL_NAME = os.getenv("AI_MODEL", "gpt-6-luna").strip() or "gpt-6-luna"
MAX_REQUEST_BYTES = 16_384

AI_RESPONSE_MAX_LENGTHS = {
    "representative_food": 50,
    "reason": 500,
    "food_guide": 800,
    "caution": 500,
    "health_notice": 500,
}

AI_RESPONSE_ARRAY_LIMITS = {
    "nutrition": {"max_items": 10, "max_item_length": 100},
    "alternative_foods": {"max_items": 10, "max_item_length": 100},
}

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

ALLOWED_COLORS = {"Yellow", "Purple", "Red", "Green"}

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

COLOR_FOOD_DATA = {
    "Yellow": {
        "representative_foods": ["레몬", "감귤류"],
        "food_nutrition": {  # PRIORITY-2
            "레몬": ['비타민 C', '플라보노이드', '구연산'],
            "감귤류": ['비타민 C', '플라보노이드', '식이섬유'],
        },
        "nutrition": ["비타민 C", "플라보노이드"],
        "daily_use_examples": [
            "감귤류를 간식이나 식사 후 과일로 활용한다.",
            "레몬은 물이나 샐러드 드레싱 등에 소량 활용할 수 있다.",
        ],
    },
    "Purple": {
        "representative_foods": ["블루베리", "포도"],
        "food_nutrition": {  # PRIORITY-2
            "블루베리": ['안토시아닌', '비타민 C', '식이섬유'],
            "포도": ['안토시아닌', '레스베라트롤', '비타민 K'],
        },
        "nutrition": ["안토시아닌"],
        "daily_use_examples": [
            "블루베리를 요거트나 오트밀에 곁들일 수 있다.",
            "포도를 간식으로 활용할 수 있다.",
        ],
    },
    "Red": {
        "representative_foods": ["체리", "복분자", "토마토", "사과"],
        "food_nutrition": {  # PRIORITY-2
            "체리": ['안토시아닌', '비타민 C', '칼륨'],
            "복분자": ['안토시아닌', '비타민 C', '식이섬유'],
            "토마토": ['라이코펜', '비타민 C', '칼륨'],
            "사과": ['식이섬유', '비타민 C', '플라보노이드'],
        },
        "nutrition": ["안토시아닌", "라이코펜"],
        "daily_use_examples": [
            "토마토를 샐러드나 반찬에 곁들일 수 있다.",
            "사과를 간식이나 식사와 함께 활용할 수 있다.",
        ],
    },
    "Green": {
        "representative_foods": ["키위", "아보카도", "멜론"],
        "food_nutrition": {  # PRIORITY-2
            "키위": ['비타민 C', '비타민 K', '식이섬유', '엽산'],
            "아보카도": ['비타민 E', '칼륨', '식이섬유', '건강한 지방'],
            "멜론": ['비타민 A', '비타민 C', '칼륨'],
        },
        "nutrition": [
            "비타민 C",
            "비타민 E",
            "엽산",
            "칼륨",
            "식이섬유",
        ],
        "daily_use_examples": [
            "키위를 간식이나 요거트에 곁들일 수 있다.",
            "아보카도를 샐러드나 샌드위치에 활용할 수 있다.",
        ],
    },
}

# PRIORITY-1: 서비스에 등록된 식품의 명칭/별칭. 의료적 교차반응 판정 자료는 아니다.
FOOD_ALIASES = {
    "레몬": ("레몬", "lemon"),
    "감귤류": ("감귤류", "감귤", "귤", "오렌지", "자몽", "시트러스", "citrus", "orange", "grapefruit"),
    "블루베리": ("블루베리", "blueberry"),
    "포도": ("포도", "grape"),
    "체리": ("체리", "cherry"),
    "복분자": ("복분자",),
    "토마토": ("토마토", "tomato"),
    "사과": ("사과", "apple"),
    "키위": ("키위", "kiwi"),
    "아보카도": ("아보카도", "avocado"),
    "멜론": ("멜론", "메론", "melon"),
}

# '감귤류 전체 제외'처럼 폭넓게 입력한 경우, 식품군에 포함되는 레몬도 차단한다.
# 오렌지처럼 개별 감귤 과일만 언급한 경우 레몬까지 자동 차단하지 않는다.
FOOD_GROUP_EXCLUSIONS = {
    "감귤류": ("레몬", "감귤류"),
    "시트러스": ("레몬", "감귤류"),
    "citrus": ("레몬", "감귤류"),
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
            "껍질째 섭취 가능한 식품도 충분한 세척과 위생 관리가 필요하다.",
        ],
    },
    "whole_grain": {
        "foods": ["현미", "통밀", "통메밀"],
        "nutrition": ["식이섬유", "비타민", "미네랄", "단백질"],
        "rules": [
            "개인의 소화 상태와 식습관을 고려한다.",
            "모든 사용자에게 동일하게 적합하다고 단정하지 않는다.",
        ],
    },
}

AI_RESPONSE_SCHEMA = {
    "type": "json_schema",
    "name": "food_guide_result",
    "description": "오늘의 몸 신호 AI 컬러푸드 가이드의 식생활 안내 결과",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "recommended_color": {
                "type": "string",
                "enum": ["Yellow", "Purple", "Red", "Green"],
            },
            "representative_food": {"type": "string"},
            "reason": {"type": "string"},
            "nutrition": {
                "type": "array",
                "items": {"type": "string"},
            },
            "alternative_foods": {
                "type": "array",
                "items": {"type": "string"},
            },
            "food_guide": {"type": "string"},
            "caution": {"type": "string"},
            "health_notice": {"type": "string"},
        },
        "required": REQUIRED_RESPONSE_KEYS,
        "additionalProperties": False,
    },
}
