/**
 * Aplica animación de entrada cuando los elementos .reveal entran al viewport.
 * Aplica también un stagger basado en la posición dentro del contenedor padre
 * (custom property --i, leída por CSS).
 */
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function initReveal() {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;

  if (reduceMotion) {
    els.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  // Asignar índice por hermanos para crear cascada elegante
  els.forEach((el) => {
    if (!el.parentElement) return;
    const siblings = Array.from(el.parentElement.children).filter((c) =>
      c.classList.contains('reveal'),
    );
    const i = siblings.indexOf(el);
    el.style.setProperty('--i', String(Math.min(i, 6)));
  });

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' },
  );

  els.forEach((el) => observer.observe(el));
}
