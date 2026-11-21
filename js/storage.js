import {
  MAX_SAVED_FOODS,
  STORAGE_KEY,
} from "./config.js";
import {
  getCurrentRecommendation,
  getSaveFoodButton,
  resetSaveButton,
} from "./result.js";
import {
  isNonEmptyString,
} from "./validation.js";


const savedFoodsContainer =
  document.getElementById("savedFoods");

let saveErrorTimerId = null;


function createRecommendationKey(data) {
  return JSON.stringify({
    recommended_color: data.recommended_color,
    representative_food: data.representative_food,
    reason: data.reason,
  });
}


export function loadSavedFoods() {
  try {
    const rawValue =
      localStorage.getItem(STORAGE_KEY);

    if (!rawValue) {
      return [];
    }

    const parsedValue =
      JSON.parse(rawValue);

    if (!Array.isArray(parsedValue)) {
      return [];
    }

    return parsedValue.filter(
      (item) =>
        item
        && typeof item === "object"
        && isNonEmptyString(
          item.recommended_color
        )
        && isNonEmptyString(
          item.representative_food
        )
    );
  } catch (error) {
    console.warn(
      "My Foods Load Error:",
      error?.name ?? "UnknownError"
    );

    return [];
  }
}


function saveSavedFoods(items) {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(items)
  );
}


function createSavedFoodCard(item) {
  const article =
    document.createElement("article");
  article.className = "saved-food-card";

  const title = document.createElement("h3");
  title.textContent =
    `${item.recommended_color} · ${item.representative_food}`;

  const reason = document.createElement("p");
  reason.textContent = item.reason;

  article.append(title, reason);

  if (isNonEmptyString(item.saved_at)) {
    const savedAt =
      document.createElement("p");
    const date = new Date(item.saved_at);

    if (!Number.isNaN(date.getTime())) {
      savedAt.textContent =
        `저장일: ${date.toLocaleDateString("ko-KR")}`;
      article.appendChild(savedAt);
    }
  }

  return article;
}


export function renderSavedFoods(
  savedFoods = loadSavedFoods()
) {
  if (!savedFoodsContainer) {
    return;
  }

  savedFoodsContainer.replaceChildren();

  if (savedFoods.length === 0) {
    const emptyMessage =
      document.createElement("p");
    emptyMessage.className =
      "saved-foods-empty";
    emptyMessage.textContent =
      "아직 저장한 식품이 없습니다.";
    savedFoodsContainer.appendChild(
      emptyMessage
    );
    return;
  }

  savedFoods.forEach((item) => {
    savedFoodsContainer.appendChild(
      createSavedFoodCard(item)
    );
  });
}


function isSaved(
  savedFoods,
  recommendation
) {
  if (!recommendation) {
    return false;
  }

  const recommendationKey =
    createRecommendationKey(recommendation);

  return savedFoods.some(
    (item) =>
      createRecommendationKey(item)
      === recommendationKey
  );
}


function updateSaveButtonState(
  savedFoods = loadSavedFoods()
) {
  const saveFoodButton =
    getSaveFoodButton();
  const currentRecommendation =
    getCurrentRecommendation();

  if (
    !saveFoodButton
    || !currentRecommendation
  ) {
    return;
  }

  if (
    isSaved(
      savedFoods,
      currentRecommendation
    )
  ) {
    saveFoodButton.classList.add(
      "is-saved"
    );
    saveFoodButton.textContent =
      "My Foods에 저장됨";
  } else {
    resetSaveButton();
  }
}


function saveCurrentRecommendation() {
  const saveFoodButton =
    getSaveFoodButton();
  const currentRecommendation =
    getCurrentRecommendation();

  if (
    !currentRecommendation
    || !saveFoodButton
  ) {
    return;
  }

  const savedFoods = loadSavedFoods();

  if (
    isSaved(
      savedFoods,
      currentRecommendation
    )
  ) {
    updateSaveButtonState(savedFoods);
    return;
  }

  const savedItem = {
    ...currentRecommendation,
    saved_at: new Date().toISOString(),
  };

  const nextSavedFoods = [
    savedItem,
    ...savedFoods,
  ].slice(0, MAX_SAVED_FOODS);

  try {
    saveSavedFoods(nextSavedFoods);
    renderSavedFoods(nextSavedFoods);
    updateSaveButtonState(nextSavedFoods);
  } catch (error) {
    console.warn(
      "My Foods Save Error:",
      error?.name ?? "UnknownError"
    );

    saveFoodButton.classList.remove(
      "is-saved"
    );
    saveFoodButton.textContent =
      "저장하지 못했습니다.";

    if (saveErrorTimerId !== null) {
      window.clearTimeout(saveErrorTimerId);
    }

    saveErrorTimerId = window.setTimeout(
      () => {
        saveErrorTimerId = null;
        if (getCurrentRecommendation()) {
          updateSaveButtonState();
        }
      },
      1800
    );
  }
}


export function initStorage() {
  const saveFoodButton =
    getSaveFoodButton();

  if (saveFoodButton) {
    saveFoodButton.addEventListener(
      "click",
      saveCurrentRecommendation
    );
  }

  renderSavedFoods();
}
