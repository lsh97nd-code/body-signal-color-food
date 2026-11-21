export function debounce(callback, delay) {
  let timer = null;

  return (...args) => {
    if (timer !== null) {
      window.clearTimeout(timer);
    }

    timer = window.setTimeout(() => {
      timer = null;
      callback(...args);
    }, delay);
  };
}
