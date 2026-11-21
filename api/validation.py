from .config import (
    ALLOWED_BODY_SIGNALS,
    ALLOWED_COLORS,
    ALLOWED_EATING_HABITS,
    ALLOWED_FRUIT_VEGETABLE_INTAKE,
    COLOR_FOOD_DATA,
    FOOD_ALIASES,
    FOOD_GROUP_EXCLUSIONS,
    REQUIRED_RESPONSE_KEYS,
    AI_RESPONSE_ARRAY_LIMITS,
    AI_RESPONSE_MAX_LENGTHS,
)


def clean_text(value, max_length):
    """문자열 입력값의 앞뒤 공백을 제거하고 허용 길이를 확인한다."""
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError("문자열 형식이 아닌 입력값이 포함되어 있습니다.")

    cleaned_value = value.strip()
    if len(cleaned_value) > max_length:
        raise ValueError(f"입력값은 {max_length}자 이하로 입력해 주세요.")
    return cleaned_value


def clean_string_list(value, max_items=10, max_length=100):
    """문자열 배열을 검증하고 빈 문자열을 제거한다."""
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("목록 형식의 입력값이 올바르지 않습니다.")
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
        result.append(cleaned_item)

    return result


def validate_request_data(data):
    """Frontend에서 전달된 JSON을 Backend에서 다시 검증한다."""
    if not isinstance(data, dict):
        raise ValueError("요청 데이터 형식이 올바르지 않습니다.")

    body_signals = clean_string_list(
        data.get("body_signals"), max_items=5, max_length=100
    )
    custom_signal = clean_text(data.get("custom_signal"), max_length=300)
    fruit_vegetable_intake = clean_text(
        data.get("fruit_vegetable_intake"), max_length=20
    )
    eating_habits = clean_text(data.get("eating_habits"), max_length=100)
    allergies = clean_text(data.get("allergies"), max_length=100)
    avoid_foods = clean_text(data.get("avoid_foods"), max_length=100)
    notes = clean_text(data.get("notes"), max_length=300)

    if not body_signals and not custom_signal:
        raise ValueError(
            "생활 속 이상 신호 등 몸 상태를 한 가지 이상 "
            "선택하거나 기타 상태를 입력해 주세요."
        )

    invalid_body_signals = [
        item for item in body_signals if item not in ALLOWED_BODY_SIGNALS
    ]
    if invalid_body_signals:
        raise ValueError(
            "허용되지 않은 몸 상태 선택값이 포함되어 있습니다."
        )

    if fruit_vegetable_intake not in ALLOWED_FRUIT_VEGETABLE_INTAKE:
        raise ValueError(
            "과일·채소 섭취 정도 선택값이 올바르지 않습니다."
        )

    if eating_habits not in ALLOWED_EATING_HABITS:
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


def validate_ai_result(result):
    """AI가 반환한 JSON 구조와 결과값을 서비스 기준으로 다시 검증한다."""
    if not isinstance(result, dict):
        raise ValueError("AI 응답이 JSON Object 형식이 아닙니다.")

    missing_keys = [
        key for key in REQUIRED_RESPONSE_KEYS if key not in result
    ]
    if missing_keys:
        raise ValueError("AI 응답에 필요한 항목이 누락되었습니다.")

    unexpected_keys = [
        key for key in result if key not in REQUIRED_RESPONSE_KEYS
    ]
    if unexpected_keys:
        raise ValueError(
            "AI 응답에 예상하지 않은 항목이 포함되어 있습니다."
        )

    recommended_color = result["recommended_color"]
    if (
        not isinstance(recommended_color, str)
        or recommended_color not in ALLOWED_COLORS
    ):
        raise ValueError("AI가 허용되지 않은 Color를 반환했습니다.")

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
        if not isinstance(value, str):
            raise ValueError(
                f"{key} 값의 자료형이 올바르지 않습니다."
            )
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError(f"{key} 값이 비어 있습니다.")

        max_length = AI_RESPONSE_MAX_LENGTHS.get(key)
        if max_length and len(cleaned_value) > max_length:
            raise ValueError(
                f"{key} 값이 허용 길이 {max_length}자를 초과했습니다."
            )

        cleaned_strings[key] = cleaned_value

    cleaned_arrays = {}
    for key in ["nutrition", "alternative_foods"]:
        value = result[key]
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"{key} 값이 올바른 Array 형식이 아닙니다."
            )

        limits = AI_RESPONSE_ARRAY_LIMITS[key]
        if len(value) > limits["max_items"]:
            raise ValueError(
                f"{key} 항목 수가 허용 범위를 초과했습니다."
            )

        cleaned_items = []
        for item in value:
            if not isinstance(item, str):
                raise ValueError(
                    f"{key} 안에 문자열이 아닌 값이 있습니다."
                )
            cleaned_item = item.strip()
            if not cleaned_item:
                raise ValueError(
                    f"{key} 안에 빈 값이 있습니다."
                )
            if len(cleaned_item) > limits["max_item_length"]:
                raise ValueError(
                    f"{key} 항목의 문자열 길이가 허용 범위를 초과했습니다."
                )
            cleaned_items.append(cleaned_item)
        cleaned_arrays[key] = cleaned_items

    representative_food = cleaned_strings["representative_food"]
    allowed_foods = COLOR_FOOD_DATA[
        recommended_color
    ]["representative_foods"]

    if representative_food not in allowed_foods:
        raise ValueError(
            "추천 대표 식품이 서비스 기준 컬러푸드 정보와 "
            "일치하지 않습니다."
        )

    return {
        "recommended_color": recommended_color,
        "representative_food": representative_food,
        "reason": cleaned_strings["reason"],
        "nutrition": cleaned_arrays["nutrition"],
        "alternative_foods": cleaned_arrays["alternative_foods"],
        "food_guide": cleaned_strings["food_guide"],
        "caution": cleaned_strings["caution"],
        "health_notice": cleaned_strings["health_notice"],
    }


# PRIORITY-1: 등록된 식품명·별칭과 사용자 제외 조건의 교차 검증

def _normalize_food_text(text):
    """입력의 공백 및 유니코드 표기를 정규화한다."""
    import unicodedata
    return unicodedata.normalize("NFKC", text).casefold()


def _contains_alias(text, alias):
    """한글은 공백 무시, 영문은 단어 경계를 지켜 오검출을 줄인다."""
    import re
    normalized = _normalize_food_text(text)
    normalized_alias = _normalize_food_text(alias)
    if normalized_alias.isascii() and normalized_alias.isalpha():
        return re.search(
            rf"(?<![a-z]){re.escape(normalized_alias)}(?![a-z])",
            normalized,
        ) is not None
    return "".join(normalized_alias.split()) in "".join(normalized.split())


def detect_excluded_foods(allergies_text, avoid_foods_text):
    """두 입력에서 등록된 식품과 식품군 별칭을 찾아 차단 목록으로 반환한다.

    자유 입력의 모든 알레르겐을 식별하거나 의학적으로 안전한지 보증하는 기능은 아니다.
    """
    entries = []
    for raw in (allergies_text, avoid_foods_text):
        if isinstance(raw, str):
            raw = raw.strip()
            if raw and _normalize_food_text(raw).replace(" ", "") not in {
                "없음", "해당없음", "없습니다", "none", "no", "해당사항없음"
            }:
                entries.append(raw)

    excluded = set()
    for entry in entries:
        for food, aliases in FOOD_ALIASES.items():
            if any(_contains_alias(entry, alias) for alias in aliases):
                excluded.add(food)
        for group_alias, foods in FOOD_GROUP_EXCLUSIONS.items():
            if _contains_alias(entry, group_alias):
                excluded.update(foods)
    return excluded


def filter_excluded_foods(result, allergies_text, avoid_foods_text):
    """대표 식품 충돌 차단, 대안 후보 제외·보완 및 추천 설명 검사.

    대안 식품은 이미 등록된 목록 안에서만 보완하며, 다른 의학적 안전을 보증하지 않는다.
    """
    excluded = detect_excluded_foods(allergies_text, avoid_foods_text)
    if not excluded:
        return result

    representative_food = result["representative_food"]
    if representative_food in excluded:
        # 대표 식품만 바꾸면 AI가 작성한 추천 이유/식생활 안내가 불일치할 수 있다.
        raise ValueError("사용자가 제외한 식품이 대표 식품에 포함되었습니다.")

    # 추천 이유·활용 안내에 제외 식품의 섭취 권장이 섞일 위험이 있어 보수적으로 차단.
    # '알레르기가 있으므로 피하세요' 같은 언급도 차단될 수 있는 한계가 있다.
    for key in ("reason", "food_guide"):
        text = result[key]
        for food in excluded:
            if any(_contains_alias(text, alias) for alias in FOOD_ALIASES[food]):
                raise ValueError("제외 식품이 AI 추천 설명에 포함되었습니다.")

    all_foods = [
        food
        for group in COLOR_FOOD_DATA.values()
        for food in group["representative_foods"]
    ]
    allowed = set(all_foods) - excluded - {representative_food}
    chosen = [
        food for food in result["alternative_foods"]
        if isinstance(food, str) and food in allowed
    ]

    # 우선순위 2가 선택한 유효한 AI 후보의 순서를 우선하며, 부족할 때만 목록에서 보완.
    # 후보는 같은 색상의 다른 식품 -> 다른 색상 식품의 순서로 보완한다.
    same_color = [
        food for food in COLOR_FOOD_DATA[result["recommended_color"]]["representative_foods"]
        if food in allowed
    ]
    other_colors = [food for food in all_foods if food in allowed and food not in same_color]
    desired_count = max(2, min(3, len(chosen)))
    alternatives = list(dict.fromkeys(chosen + same_color + other_colors))[:desired_count]
    if not alternatives:
        raise ValueError("제외 조건을 충족하는 대안 식품이 없습니다.")

    return {**result, "alternative_foods": alternatives}
