/** Menú overlay a pantalla completa.
 *  Usa la técnica de body-lock para evitar que el fondo
 *  se filtre en iOS Safari cuando la página está scrolleada.
 *  El overlay se superpone al header, así que el cierre vive dentro
 *  del propio overlay ("Cerrar", Escape o cualquier enlace). */
export function initMenu() {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.getElementById('site-menu');
  if (!toggle || !menu) return;

  const closeBtn = menu.querySelector('.menu__close');

  const lockBody = () => {
    const scrollY = window.scrollY;
    document.body.style.position = 'fixed';
    document.body.style.top = `-${scrollY}px`;
    document.body.style.width = '100%';
    document.body.dataset.scrollY = String(scrollY);
  };

  const unlockBody = () => {
    const scrollY = parseInt(document.body.dataset.scrollY || '0', 10);
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.width = '';
    delete document.body.dataset.scrollY;
    window.scrollTo({ top: scrollY, behavior: 'instant' });
  };

  const isOpen = () => toggle.getAttribute('aria-expanded') === 'true';

  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    menu.hidden = !open;

    if (open) {
      lockBody();
      // El toggle queda tapado por el overlay: llevamos el foco adentro.
      if (closeBtn) closeBtn.focus();
    } else {
      unlockBody();
      toggle.focus();
    }
  };

  toggle.addEventListener('click', () => setOpen(!isOpen()));

  if (closeBtn) {
    closeBtn.addEventListener('click', () => setOpen(false));
  }

  menu.querySelectorAll('a').forEach((a) => {
    a.addEventListener('click', () => setOpen(false));
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen()) setOpen(false);
  });
}
