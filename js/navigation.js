import { debounce } from "./utils.js";


export function initNavigation() {
  const menuToggle =
    document.getElementById("menuToggle");
  const mainNav =
    document.getElementById("mainNav");
  const navLinks =
    document.querySelectorAll(".main-nav a");
  const header =
    document.querySelector(".site-header");

  const navSections =
    Array.from(navLinks)
      .map((link) => {
        const targetId =
          link.getAttribute("href");

        if (
          !targetId
          || !targetId.startsWith("#")
        ) {
          return null;
        }

        return document.querySelector(
          targetId
        );
      })
      .filter(Boolean);

  function getScrollOffset() {
    const headerHeight =
      header ? header.offsetHeight : 72;
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
      isOpen ? "✕" : "☰";
  }

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
      setActiveLink(
        navSections[
          navSections.length - 1
        ].id
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
        currentSectionId = section.id;
      }
    });

    setActiveLink(currentSectionId);
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

  const handleResize = debounce(
    () => {
      if (window.innerWidth > 900) {
        closeMobileMenu();
      }
      updateActiveNavigation();
    },
    150
  );

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
        mainNav.classList.contains(
          "open"
        );
      const clickedOutsideMenu =
        !mainNav.contains(event.target)
        && !menuToggle.contains(
          event.target
        );

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
        && mainNav.classList.contains(
          "open"
        )
      ) {
        closeMobileMenu();
        menuToggle.focus();
      }
    }
  );

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
}
