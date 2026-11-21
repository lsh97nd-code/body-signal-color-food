"use strict";

/* ========================================
   Navigation
======================================== */

const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");
const navLinks = document.querySelectorAll(".main-nav a");
const header = document.querySelector(".site-header");

const navSections = Array.from(navLinks)
  .map((link) => {
    const targetId = link.getAttribute("href");

    if (!targetId || !targetId.startsWith("#")) {
      return null;
    }

    return document.querySelector(targetId);
  })
  .filter(Boolean);


function debounce(callback, delay) {
  let timer;

  return (...args) => {
    clearTimeout(timer);

    timer = setTimeout(() => {
      callback(...args);
    }, delay);
  };
}


function getScrollOffset() {
  const headerHeight = header
    ? header.offsetHeight
    : 72;

  return headerHeight + 30;
}


function closeMobileMenu() {
  if (!menuToggle || !mainNav) {
    return;
  }

  mainNav.classList.remove("open");

  menuToggle.setAttribute(
    "aria-expanded",
    "false"
  );

  menuToggle.setAttribute(
    "aria-label",
    "메뉴 열기"
  );

  menuToggle.textContent = "☰";
}


function toggleMobileMenu() {
  if (!menuToggle || !mainNav) {
    return;
  }

  const isOpen =
    mainNav.classList.toggle("open");

  menuToggle.setAttribute(
    "aria-expanded",
    String(isOpen)
  );

  menuToggle.setAttribute(
    "aria-label",
    isOpen
      ? "메뉴 닫기"
      : "메뉴 열기"
  );

  menuToggle.textContent =
    isOpen
      ? "✕"
      : "☰";
}


if (menuToggle && mainNav) {
  menuToggle.addEventListener(
    "click",
    toggleMobileMenu
  );
}


navLinks.forEach((link) => {
  link.addEventListener(
    "click",
    closeMobileMenu
  );
});


const handleResize = debounce(() => {
  if (window.innerWidth > 900) {
    closeMobileMenu();
  }

  updateActiveNavigation();
}, 150);


window.addEventListener(
  "resize",
  handleResize
);


document.addEventListener(
  "click",
  (event) => {
    if (!menuToggle || !mainNav) {
      return;
    }

    const isMenuOpen =
      mainNav.classList.contains("open");

    const clickedOutsideMenu =
      !mainNav.contains(event.target)
      && !menuToggle.contains(event.target);

    if (
      isMenuOpen
      && clickedOutsideMenu
    ) {
      closeMobileMenu();
    }
  }
);


document.addEventListener(
  "keydown",
  (event) => {
    if (!menuToggle || !mainNav) {
      return;
    }

    if (
      event.key === "Escape"
      && mainNav.classList.contains("open")
    ) {
      closeMobileMenu();
      menuToggle.focus();
    }
  }
);


function setActiveLink(sectionId) {
  navLinks.forEach((link) => {
    const targetId =
      link
        .getAttribute("href")
        ?.replace("#", "");

    const isActive =
      targetId === sectionId;

    link.classList.toggle(
      "active",
      isActive
    );

    if (isActive) {
      link.setAttribute(
        "aria-current",
        "page"
      );
    } else {
      link.removeAttribute(
        "aria-current"
      );
    }
  });
}


function updateActiveNavigation() {
  if (navSections.length === 0) {
    return;
  }

  const isAtBottom =
    window.innerHeight
    + window.scrollY
    >= document.documentElement.scrollHeight - 4;

  if (isAtBottom) {
    const lastSection =
      navSections[
        navSections.length - 1
      ];

    setActiveLink(
      lastSection.id
    );

    return;
  }

  const scrollPosition =
    window.scrollY
    + getScrollOffset();

  let currentSectionId =
    navSections[0].id;

  navSections.forEach((section) => {
    if (
      scrollPosition
      >= section.offsetTop
    ) {
      currentSectionId =
        section.id;
    }
  });

  setActiveLink(
    currentSectionId
  );
}


let scrollAnimationFrame = null;


window.addEventListener(
  "scroll",
  () => {
    if (
      scrollAnimationFrame !== null
    ) {
      return;
    }

    scrollAnimationFrame =
      window.requestAnimationFrame(
        () => {
          updateActiveNavigation();

          scrollAnimationFrame = null;
        }
      );
  },
  {
    passive: true,
  }
);


updateActiveNavigation();


/* ========================================
   Body Signal / AI Food Guide
======================================== */

const bodySignalForm =
  document.getElementById(
    "bodySignalForm"
  );

const customSignal =
  document.getElementById(
    "customSignal"
  );

const fruitVegetableIntake =
  document.getElementById(
    "fruitVegetableIntake"
  );

const eatingHabits =
  document.getElementById(
    "eatingHabits"
  );

const allergies =
  document.getElementById(
    "allergies"
  );

const avoidFoods =
  document.getElementById(
    "avoidFoods"
  );

const notes =
  document.getElementById(
    "notes"
  );

const formError =
  document.getElementById(
    "formError"
  );

const recommendButton =
  document.getElementById(
    "recommendButton"
  );

const aiFoodGuideSection =
  document.getElementById(
    "ai-food-guide"
  );

const loadingState =
  document.getElementById(
    "loadingState"
  );

const apiError =
  document.getElementById(
    "apiError"
  );

const apiErrorMessage =
  document.getElementById(
    "apiErrorMessage"
  );

const resultSection =
  document.getElementById(
    "result"
  );


/* ========================================
   Result 요소
======================================== */

const resultColor =
  document.getElementById(
    "resultColor"
  );

const resultFood =
  document.getElementById(
    "resultFood"
  );

const resultReason =
  document.getElementById(
    "resultReason"
  );

const resultNutrition =
  document.getElementById(
    "resultNutrition"
  );

const resultAlternativeFoods =
  document.getElementById(
    "resultAlternativeFoods"
  );

const resultFoodGuide =
  document.getElementById(
    "resultFoodGuide"
  );

const resultCaution =
  document.getElementById(
    "resultCaution"
  );

const resultHealthNotice =
  document.getElementById(
    "resultHealthNotice"
  );

const saveFoodButton =
  document.getElementById(
    "saveFoodButton"
  );


/* ========================================
   Frontend 설정
======================================== */

const API_ENDPOINT =
  "/api/recommend";

const REQUEST_TIMEOUT_MS =
  15000;

const ALLOWED_COLORS =
  new Set([
    "Yellow",
    "Purple",
    "Red",
    "Green",
  ]);

const REQUIRED_RESULT_KEYS = [
  "recommended_color",
  "representative_food",
  "reason",
  "nutrition",
  "alternative_foods",
  "food_guide",
  "caution",
  "health_notice",
];

const STORAGE_KEY =
  "bodySignalColorFood.savedFoods";

const MAX_SAVED_FOODS = 20;

let currentRecommendation = null;


/* ========================================
   공통 Utility
======================================== */

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
  if (!formError) {
    return;
  }

  formError.textContent = "";
  formError.hidden = true;
}


function showFormError(message) {
  if (!formError) {
    return;
  }

  formError.textContent = message;
  formError.hidden = false;

  formError.focus?.();
}


function hideApiError() {
  if (!apiError) {
    return;
  }

  apiError.hidden = true;

  if (apiErrorMessage) {
    apiErrorMessage.textContent = "";
  }
}


function showApiError(message) {
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
  if (loadingState) {
    loadingState.hidden =
      !isLoading;
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


function hideResult() {
  if (resultSection) {
    resultSection.hidden = true;
    resultSection.removeAttribute("data-color-theme");
  }
}


function resetSaveButton() {
  if (!saveFoodButton) {
    return;
  }

  saveFoodButton.classList.remove(
    "is-saved"
  );

  saveFoodButton.textContent =
    "My Foods에 저장";
}


/* ========================================
   사용자 입력 수집
======================================== */

function getSelectedBodySignals() {
  return Array.from(
    document.querySelectorAll(
      'input[name="bodySignals"]:checked'
    )
  ).map((checkbox) =>
    checkbox.value.trim()
  );
}


function collectRequestData() {
  return {
    body_signals:
      getSelectedBodySignals(),

    custom_signal:
      getTrimmedValue(
        customSignal
      ),

    fruit_vegetable_intake:
      fruitVegetableIntake
        ? fruitVegetableIntake.value
        : "",

    eating_habits:
      eatingHabits
        ? eatingHabits.value
        : "",

    allergies:
      getTrimmedValue(
        allergies
      ),

    avoid_foods:
      getTrimmedValue(
        avoidFoods
      ),

    notes:
      getTrimmedValue(
        notes
      ),
  };
}


/* ========================================
   Frontend 입력 검증
======================================== */

function validateRequestData(data) {
  if (
    data.body_signals.length === 0
    && !data.custom_signal
  ) {
    return {
      valid: false,
      message:
        "생활 속 이상 신호 등 몸 상태를 한 가지 이상 선택하거나 기타 상태를 입력해 주세요.",
    };
  }

  if (
    data.custom_signal.length > 300
    || data.notes.length > 300
  ) {
    return {
      valid: false,
      message:
        "직접 입력 내용은 최대 300자까지 입력해 주세요.",
    };
  }

  if (
    data.allergies.length > 100
    || data.avoid_foods.length > 100
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


/* ========================================
   AI 응답 구조 검증
======================================== */

function isNonEmptyString(value) {
  return (
    typeof value === "string"
    && value.trim().length > 0
  );
}


function isNonEmptyStringArray(value) {
  return (
    Array.isArray(value)
    && value.length > 0
    && value.every(
      (item) =>
        isNonEmptyString(item)
    )
  );
}


function validateResultData(data) {
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

  if (
    !ALLOWED_COLORS.has(
      data.recommended_color
    )
  ) {
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
      (key) =>
        isNonEmptyString(data[key])
    )
  ) {
    return false;
  }

  if (
    !isNonEmptyStringArray(
      data.nutrition
    )
    || !isNonEmptyStringArray(
      data.alternative_foods
    )
  ) {
    return false;
  }

  return true;
}


/* ========================================
   Result 안전한 출력
======================================== */

function renderStringList(
  listElement,
  items
) {
  if (!listElement) {
    return;
  }

  listElement.replaceChildren();

  items.forEach((item) => {
    const listItem =
      document.createElement("li");

    listItem.textContent =
      item.trim();

    listElement.appendChild(
      listItem
    );
  });
}


function renderResult(data) {
  if (
    !resultSection
    || !resultColor
    || !resultFood
    || !resultReason
    || !resultNutrition
    || !resultAlternativeFoods
    || !resultFoodGuide
    || !resultCaution
    || !resultHealthNotice
  ) {
    throw new Error(
      "Result 화면 요소를 찾을 수 없습니다."
    );
  }

  if (!ALLOWED_COLORS.has(data.recommended_color)) {
    throw new Error("허용되지 않은 추천 컬러푸드입니다.");
  }

  resultColor.textContent =
    data.recommended_color;

  resultFood.textContent =
    data.representative_food;

  resultReason.textContent =
    data.reason;

  renderStringList(
    resultNutrition,
    data.nutrition
  );

  renderStringList(
    resultAlternativeFoods,
    data.alternative_foods
  );

  resultFoodGuide.textContent =
    data.food_guide;

  resultCaution.textContent =
    data.caution;

  resultHealthNotice.textContent =
    data.health_notice;

  currentRecommendation = {
    recommended_color:
      data.recommended_color,

    representative_food:
      data.representative_food,

    reason:
      data.reason,

    nutrition:
      [...data.nutrition],

    alternative_foods:
      [...data.alternative_foods],

    food_guide:
      data.food_guide,

    caution:
      data.caution,

    health_notice:
      data.health_notice,
  };

  resetSaveButton();

  // API 결과의 Color를 결과 영역에만 적용한다.
  resultSection.dataset.colorTheme =
    data.recommended_color.toLowerCase();

  resultSection.hidden = false;
}


/* ========================================
   API 요청
======================================== */

async function requestRecommendation(
  requestData
) {
  const controller =
    new AbortController();

  const timeoutId =
    window.setTimeout(
      () => {
        controller.abort();
      },
      REQUEST_TIMEOUT_MS
    );

  try {
    const response = await fetch(
      API_ENDPOINT,
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json",
        },

        body:
          JSON.stringify(
            requestData
          ),

        signal:
          controller.signal,
      }
    );

    let payload = null;

    try {
      payload =
        await response.json();
    } catch {
      throw new Error(
        "INVALID_RESPONSE"
      );
    }

    if (!response.ok) {
      if (
        response.status === 400
        && isNonEmptyString(
          payload?.message
        )
      ) {
        const error =
          new Error(
            payload.message
          );

        error.name =
          "RequestValidationError";

        throw error;
      }

      throw new Error(
        "API_ERROR"
      );
    }

    if (
      payload?.success !== true
      || !validateResultData(
        payload.data
      )
    ) {
      throw new Error(
        "INVALID_RESPONSE"
      );
    }

    return payload.data;
  } finally {
    window.clearTimeout(
      timeoutId
    );
  }
}


/* ========================================
   Form 제출
======================================== */

if (bodySignalForm) {
  bodySignalForm.addEventListener(
    "submit",
    async (event) => {
      event.preventDefault();

      hideFormError();
      hideApiError();
      hideResult();

      const requestData =
        collectRequestData();

      const validation =
        validateRequestData(
          requestData
        );

      if (!validation.valid) {
        showFormError(
          validation.message
        );

        return;
      }

      setLoading(true);

      scrollToElement(
        aiFoodGuideSection
      );

      try {
        const resultData =
          await requestRecommendation(
            requestData
          );

        renderResult(
          resultData
        );

        scrollToElement(
          resultSection
        );
      } catch (error) {
        currentRecommendation =
          null;

        resetSaveButton();
        hideResult();

        if (
          error?.name
          === "AbortError"
        ) {
          showApiError(
            "응답 시간이 오래 걸리고 있습니다. 잠시 후 다시 시도해 주세요."
          );
        } else if (
          error?.name
          === "RequestValidationError"
        ) {
          showApiError(
            error.message
          );
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
          aiFoodGuideSection
        );

        console.error(
          "AI Food Guide Error:",
          error?.name
            ?? "UnknownError"
        );
      } finally {
        setLoading(false);
      }
    }
  );
}


/* ========================================
   입력 변경 시 Form Error 정리
======================================== */

function clearFormErrorIfVisible() {
  if (
    formError
    && !formError.hidden
  ) {
    hideFormError();
  }
}


if (bodySignalForm) {
  bodySignalForm.addEventListener(
    "input",
    clearFormErrorIfVisible
  );

  bodySignalForm.addEventListener(
    "change",
    clearFormErrorIfVisible
  );
}


/* ========================================
   My Foods - localStorage
======================================== */

const savedFoodsContainer =
  document.getElementById(
    "savedFoods"
  );


function createRecommendationKey(data) {
  return [
    data.recommended_color,
    data.representative_food,
    data.reason,
  ].join("|");
}


function loadSavedFoods() {
  try {
    const rawValue =
      localStorage.getItem(
        STORAGE_KEY
      );

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
      error?.name
        ?? "UnknownError"
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


// 최근 삭제한 한 건은 이 페이지가 열려 있는 동안만 취소할 수 있다.
// 민감한 식생활 정보의 별도 영구 사본은 만들지 않는다.
let lastDeletedFood = null;
let myFoodsFeedback = null;


function restoreLastDeletedFood() {
  if (!lastDeletedFood) {
    return;
  }

  const { item, index } = lastDeletedFood;
  const savedFoods = loadSavedFoods();
  const targetKey = createRecommendationKey(item);
  const targetDate = item.saved_at ?? "";

  // 다른 탭에서 이미 되돌렸다면 중복 저장하지 않는다.
  const alreadySaved = savedFoods.some((saved) =>
    createRecommendationKey(saved) === targetKey
    && (saved.saved_at ?? "") === targetDate
  );

  if (alreadySaved) {
    lastDeletedFood = null;
    myFoodsFeedback = `${item.recommended_color} · ${item.representative_food}가 이미 저장되어 있습니다.`;
    renderSavedFoods(savedFoods);
    updateSaveButtonState(savedFoods);
    return;
  }

  // 복원 때문에 다른 항목이 조용히 밀려나 삭제되는 것을 방지한다.
  if (savedFoods.length >= MAX_SAVED_FOODS) {
    window.alert("저장 공간이 가득 찼습니다. 다른 항목을 정리한 뒤 삭제 취소를 다시 눌러 주세요.");
    return;
  }

  const restored = [...savedFoods];
  restored.splice(Math.min(index, restored.length), 0, item);

  try {
    saveSavedFoods(restored);
  } catch (error) {
    console.warn("My Foods Restore Error:", error?.name ?? "UnknownError");
    window.alert("식품을 복원하지 못했습니다. 다시 시도해 주세요.");
    return;
  }

  lastDeletedFood = null;
  myFoodsFeedback = `${item.recommended_color} · ${item.representative_food}가 복원되었습니다.`;
  renderSavedFoods(restored);
  updateSaveButtonState(restored);
}


function renderMyFoodsFeedback() {
  if (!savedFoodsContainer || (!lastDeletedFood && !myFoodsFeedback)) {
    return;
  }

  const notice = document.createElement("div");
  notice.className = "saved-food-feedback";
  notice.setAttribute("role", "status");
  notice.setAttribute("aria-live", "polite");

  const message = document.createElement("span");
  message.textContent = lastDeletedFood
    ? `${lastDeletedFood.item.recommended_color} · ${lastDeletedFood.item.representative_food}를 삭제했습니다.`
    : myFoodsFeedback;
  notice.appendChild(message);

  if (lastDeletedFood) {
    const undoButton = document.createElement("button");
    undoButton.type = "button";
    undoButton.className = "saved-food-undo-button";
    undoButton.textContent = "삭제 취소";
    undoButton.addEventListener("click", restoreLastDeletedFood);
    notice.appendChild(undoButton);
  }

  savedFoodsContainer.appendChild(notice);
}


function deleteSavedFood(item) {
  const savedFoods = loadSavedFoods();
  const targetKey = createRecommendationKey(item);
  const targetDate = item.saved_at ?? "";

  const targetIndex = savedFoods.findIndex((saved) =>
    createRecommendationKey(saved) === targetKey
    && (saved.saved_at ?? "") === targetDate
  );

  if (targetIndex < 0) {
    // 다른 탭에서 이미 삭제된 경우 화면만 최신화한다.
    renderSavedFoods(savedFoods);
    updateSaveButtonState(savedFoods);
    return;
  }

  // 브라우저 기본 확인창. 버튼 이름은 브라우저 언어에 따라 '확인/취소' 등으로 표시된다.
  if (!window.confirm(
    `${item.recommended_color} · ${item.representative_food}를 삭제하시겠습니까?`
  )) {
    return;
  }

  const nextSavedFoods = savedFoods.filter((_, index) => index !== targetIndex);

  try {
    saveSavedFoods(nextSavedFoods);
  } catch (error) {
    console.warn("My Foods Delete Error:", error?.name ?? "UnknownError");
    window.alert("저장한 식품을 삭제하지 못했습니다. 다시 시도해 주세요.");
    return;
  }

  lastDeletedFood = { item: { ...savedFoods[targetIndex] }, index: targetIndex };
  myFoodsFeedback = null;
  renderSavedFoods(nextSavedFoods);
  updateSaveButtonState(nextSavedFoods);
}


function createSavedFoodCard(item) {
  const article =
    document.createElement(
      "article"
    );

  article.className =
    "saved-food-card";

  const title =
    document.createElement("h3");

  title.textContent =
    `${item.recommended_color} · ${item.representative_food}`;

  const reason =
    document.createElement("p");

  reason.textContent =
    item.reason;

  article.append(
    title,
    reason
  );

  if (
    isNonEmptyString(
      item.saved_at
    )
  ) {
    const savedAt =
      document.createElement("p");

    const date =
      new Date(
        item.saved_at
      );

    if (
      !Number.isNaN(
        date.getTime()
      )
    ) {
      savedAt.textContent =
        `저장일: ${date.toLocaleDateString("ko-KR")}`;

      article.appendChild(
        savedAt
      );
    }
  }

  // 저장 목록의 각 카드에만 삭제 버튼을 추가한다.
  const actions = document.createElement("div");
  actions.className = "saved-food-actions";

  const deleteButton = document.createElement("button");
  deleteButton.type = "button";
  deleteButton.className = "saved-food-delete-button";
  deleteButton.textContent = "삭제";
  deleteButton.setAttribute(
    "aria-label",
    `${item.recommended_color} · ${item.representative_food} 저장 목록에서 삭제`
  );
  deleteButton.addEventListener(
    "click",
    () => deleteSavedFood(item)
  );

  actions.appendChild(deleteButton);
  article.appendChild(actions);

  return article;
}


function renderSavedFoods(
  savedFoods = loadSavedFoods()
) {
  if (!savedFoodsContainer) {
    return;
  }

  savedFoodsContainer.replaceChildren();
  renderMyFoodsFeedback();

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

  savedFoods.forEach(
    (item) => {
      savedFoodsContainer.appendChild(
        createSavedFoodCard(item)
      );
    }
  );
}


function isSaved(
  savedFoods,
  recommendation
) {
  if (!recommendation) {
    return false;
  }

  const recommendationKey =
    createRecommendationKey(
      recommendation
    );

  return savedFoods.some(
    (item) =>
      createRecommendationKey(item)
      === recommendationKey
  );
}


function updateSaveButtonState(
  savedFoods = loadSavedFoods()
) {
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
  if (
    !currentRecommendation
    || !saveFoodButton
  ) {
    return;
  }

  const savedFoods =
    loadSavedFoods();

  if (
    isSaved(
      savedFoods,
      currentRecommendation
    )
  ) {
    updateSaveButtonState(
      savedFoods
    );

    return;
  }

  const savedItem = {
    ...currentRecommendation,
    saved_at:
      new Date().toISOString(),
  };

  const nextSavedFoods = [
    savedItem,
    ...savedFoods,
  ].slice(
    0,
    MAX_SAVED_FOODS
  );

  try {
    saveSavedFoods(
      nextSavedFoods
    );

    renderSavedFoods(
      nextSavedFoods
    );

    updateSaveButtonState(
      nextSavedFoods
    );
  } catch (error) {
    console.warn(
      "My Foods Save Error:",
      error?.name
        ?? "UnknownError"
    );

    saveFoodButton.classList.remove(
      "is-saved"
    );

    saveFoodButton.textContent =
      "저장하지 못했습니다.";

    window.setTimeout(
      () => {
        if (
          currentRecommendation
        ) {
          updateSaveButtonState();
        }
      },
      1800
    );
  }
}


if (saveFoodButton) {
  saveFoodButton.addEventListener(
    "click",
    saveCurrentRecommendation
  );
}


/* ========================================
   초기 실행
======================================== */

renderSavedFoods();
