import {
  ALLOWED_COLORS,
  REQUIRED_RESULT_KEYS,
} from "./config.js";


export function isNonEmptyString(value) {
  return (
    typeof value === "string"
    && value.trim().length > 0
  );
}


export function isNonEmptyStringArray(value) {
  return (
    Array.isArray(value)
    && value.length > 0
    && value.every(
      (item) => isNonEmptyString(item)
    )
  );
}


export function validateRequestData(data) {
  const bodySignals = Array.isArray(data?.body_signals)
    ? data.body_signals
    : [];
  const customSignal = String(data?.custom_signal ?? "").trim();
  const notes = String(data?.notes ?? "").trim();
  const allergies = String(data?.allergies ?? "").trim();
  const avoidFoods = String(data?.avoid_foods ?? "").trim();

  if (
    bodySignals.length === 0
    && !customSignal
  ) {
    return {
      valid: false,
      message:
        "생활 속 이상 신호 등 몸 상태를 한 가지 이상 선택하거나 기타 상태를 입력해 주세요.",
    };
  }

  if (
    customSignal.length > 300
    || notes.length > 300
  ) {
    return {
      valid: false,
      message:
        "직접 입력 내용은 최대 300자까지 입력해 주세요.",
    };
  }

  if (
    allergies.length > 100
    || avoidFoods.length > 100
  ) {
    return {
      valid: false,
      message:
        "알레르기와 피하고 싶은 음식은 각각 최대 100자까지 입력해 주세요.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}


export function validateResultData(data) {
  if (
    !data
    || typeof data !== "object"
    || Array.isArray(data)
  ) {
    return false;
  }

  const hasRequiredKeys =
    REQUIRED_RESULT_KEYS.every(
      (key) =>
        Object.prototype.hasOwnProperty.call(
          data,
          key
        )
    );

  if (!hasRequiredKeys) {
    return false;
  }

  if (!ALLOWED_COLORS.has(data.recommended_color)) {
    return false;
  }

  const stringKeys = [
    "representative_food",
    "reason",
    "food_guide",
    "caution",
    "health_notice",
  ];

  if (
    !stringKeys.every(
      (key) => isNonEmptyString(data[key])
    )
  ) {
    return false;
  }

  return (
    isNonEmptyStringArray(data.nutrition)
    && isNonEmptyStringArray(
      data.alternative_foods
    )
  );
}
