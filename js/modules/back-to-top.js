/** Muestra un botón flotante para volver al inicio cuando se ha hecho scroll. */
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function initBackToTop() {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  const toggle = () => {
    btn.classList.toggle('is-visible', window.scrollY > 600);
  };

  toggle();
  window.addEventListener('scroll', toggle, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
  });
}
