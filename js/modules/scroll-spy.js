/**
 * Marca el enlace activo de la nav según la sección visible,
 * usando IntersectionObserver (más eficiente que escuchar scroll).
 */
export function initScrollSpy() {
  const links = Array.from(document.querySelectorAll('.nav__link[data-spy]'));
  if (!links.length) return;

  const sections = links
    .map((l) => document.querySelector(l.getAttribute('href')))
    .filter(Boolean);

  const setActive = (id) => {
    links.forEach((link) => {
      const isActive = link.getAttribute('href') === `#${id}`;
      link.classList.toggle('is-active', isActive);
      if (isActive) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  };

  // Threshold balanceado para considerar visible la sección "central"
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]) setActive(visible[0].target.id);
    },
    {
      rootMargin: '-40% 0px -50% 0px',
      threshold: [0, 0.25, 0.5, 0.75, 1],
    },
  );

  sections.forEach((s) => observer.observe(s));

  if (sections[0]) setActive(sections[0].id);
}
