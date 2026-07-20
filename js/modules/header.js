/** Cambia el estado visual del header al hacer scroll. */
export function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  const onScroll = () => {
    header.dataset.scrollState = window.scrollY > 10 ? 'scrolled' : 'top';
  };

  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}
