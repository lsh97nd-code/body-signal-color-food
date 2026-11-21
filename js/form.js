import {
  requestRecommendation,
} from "./api.js";
import {
  clearCurrentRecommendation,
  getResultSection,
  hideResult,
  renderResult,
  resetSaveButton,
} from "./result.js";
import {
  validateRequestData,
} from "./validation.js";


let elements = null;


function getElements() {
  return {
    bodySignalForm:
      document.getElementById("bodySignalForm"),
    customSignal:
      document.getElementById("customSignal"),
    fruitVegetableIntake:
      document.getElementById("fruitVegetableIntake"),
    eatingHabits:
      document.getElementById("eatingHabits"),
    allergies:
      document.getElementById("allergies"),
    avoidFoods:
      document.getElementById("avoidFoods"),
    notes:
      document.getElementById("notes"),
    formError:
      document.getElementById("formError"),
    recommendButton:
      document.getElementById("recommendButton"),
    aiFoodGuideSection:
      document.getElementById("ai-food-guide"),
    loadingState:
      document.getElementById("loadingState"),
    apiError:
      document.getElementById("apiError"),
    apiErrorMessage:
      document.getElementById("apiErrorMessage"),
  };
}


function getTrimmedValue(element) {
  if (!element) {
    return "";
  }

  return element.value.trim();
}


function scrollToElement(element) {
  if (!element) {
    return;
  }

  element.scrollIntoView({
    block: "start",
  });
}


function hideFormError() {
  const formError = elements?.formError;

  if (!formError) {
    return;
  }

  formError.textContent = "";
  formError.hidden = true;
}


function showFormError(message) {
  const formError = elements?.formError;

  if (!formError) {
    return;
  }

  formError.textContent = message;
  formError.hidden = false;
  formError.focus?.();
}


function hideApiError() {
  const apiError = elements?.apiError;
  const apiErrorMessage =
    elements?.apiErrorMessage;

  if (!apiError) {
    return;
  }

  apiError.hidden = true;

  if (apiErrorMessage) {
    apiErrorMessage.textContent = "";
  }
}


function showApiError(message) {
  const apiError = elements?.apiError;
  const apiErrorMessage =
    elements?.apiErrorMessage;

  if (!apiError) {
    return;
  }

  if (apiErrorMessage) {
    apiErrorMessage.textContent =
      message;
  }

  apiError.hidden = false;
}


function setLoading(isLoading) {
  const loadingState =
    elements?.loadingState;
  const recommendButton =
    elements?.recommendButton;

  if (loadingState) {
    loadingState.hidden = !isLoading;
  }

  if (recommendButton) {
    recommendButton.disabled =
      isLoading;
    recommendButton.classList.toggle(
      "is-loading",
      isLoading
    );
    recommendButton.setAttribute(
      "aria-busy",
      String(isLoading)
    );
  }
}


function getSelectedBodySignals() {
  return Array.from(
    document.querySelectorAll(
      'input[name="bodySignals"]:checked'
    )
  ).map(
    (checkbox) =>
      checkbox.value.trim()
  );
}


function collectRequestData() {
  return {
    body_signals:
      getSelectedBodySignals(),
    custom_signal:
      getTrimmedValue(
        elements?.customSignal
      ),
    fruit_vegetable_intake:
      elements?.fruitVegetableIntake
        ? elements.fruitVegetableIntake.value
        : "",
    eating_habits:
      elements?.eatingHabits
        ? elements.eatingHabits.value
        : "",
    allergies:
      getTrimmedValue(
        elements?.allergies
      ),
    avoid_foods:
      getTrimmedValue(
        elements?.avoidFoods
      ),
    notes:
      getTrimmedValue(
        elements?.notes
      ),
  };
}


function clearFormErrorIfVisible() {
  const formError = elements?.formError;

  if (
    formError
    && !formError.hidden
  ) {
    hideFormError();
  }
}


async function handleSubmit(event) {
  event.preventDefault();

  hideFormError();
  hideApiError();
  hideResult();

  const requestData =
    collectRequestData();
  const validation =
    validateRequestData(requestData);

  if (!validation.valid) {
    showFormError(validation.message);
    return;
  }

  setLoading(true);
  scrollToElement(
    elements?.aiFoodGuideSection
  );

  try {
    const resultData =
      await requestRecommendation(
        requestData
      );

    renderResult(resultData);
    scrollToElement(
      getResultSection()
    );
  } catch (error) {
    clearCurrentRecommendation();
    resetSaveButton();
    hideResult();

    if (error?.name === "AbortError") {
      showApiError(
        "응답 시간이 오래 걸리고 있습니다. 잠시 후 다시 시도해 주세요."
      );
    } else if (
      error?.name
      === "RequestValidationError"
    ) {
      showApiError(error.message);
    } else if (
      error instanceof TypeError
    ) {
      showApiError(
        "네트워크 연결을 확인한 후 다시 시도해 주세요."
      );
    } else {
      showApiError(
        "AI 식생활 안내서를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요."
      );
    }

    scrollToElement(
      elements?.aiFoodGuideSection
    );

    console.error(
      "AI Food Guide Error:",
      error?.name ?? "UnknownError"
    );
  } finally {
    setLoading(false);
  }
}


export function initFoodGuide() {
  elements = getElements();

  if (!elements.bodySignalForm) {
    return;
  }

  elements.bodySignalForm.addEventListener(
    "submit",
    handleSubmit
  );
  elements.bodySignalForm.addEventListener(
    "input",
    clearFormErrorIfVisible
  );
  elements.bodySignalForm.addEventListener(
    "change",
    clearFormErrorIfVisible
  );
}
