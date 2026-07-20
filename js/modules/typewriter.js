/** Efecto máquina de escribir con pausa al final de cada palabra. */
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function initTypewriter() {
  const el = document.querySelector('[data-typewriter]');
  if (!el) return;

  let words;
  try {
    words = JSON.parse(el.getAttribute('data-typewriter'));
  } catch {
    return;
  }

  if (!Array.isArray(words) || !words.length) return;

  if (reduceMotion) {
    el.textContent = words[0];
    return;
  }

  const TYPE_MS = 70;
  const ERASE_MS = 35;
  const HOLD_MS = 1600;
  const PAUSE_MS = 400;
  const START_MS = 600;

  let wordIndex = 0;
  let charIndex = 0;
  let deleting = false;

  const tick = () => {
    const word = words[wordIndex];
    el.textContent = word.slice(0, charIndex);

    let delay = deleting ? ERASE_MS : TYPE_MS;

    if (!deleting && charIndex === word.length) {
      deleting = true;
      delay = HOLD_MS;
    } else if (deleting && charIndex === 0) {
      deleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      delay = PAUSE_MS;
    } else {
      charIndex += deleting ? -1 : 1;
    }

    window.setTimeout(tick, delay);
  };

  window.setTimeout(tick, START_MS);
}
