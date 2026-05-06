/** Tabs accesibles (WAI-ARIA Authoring Practices: tabs pattern). */
export function initSkillTabs() {
  const tablist = document.querySelector('[role="tablist"].skills__tablist');
  if (!tablist) return;

  const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
  const panels = Array.from(document.querySelectorAll('[role="tabpanel"].skills__panel'));

  const select = (tab) => {
    tabs.forEach((t) => {
      const isSelected = t === tab;
      t.setAttribute('aria-selected', String(isSelected));
      t.tabIndex = isSelected ? 0 : -1;
    });
    panels.forEach((p) => {
      p.hidden = p.getAttribute('aria-labelledby') !== tab.id;
    });
  };

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => select(tab));

    tab.addEventListener('keydown', (e) => {
      const i = tabs.indexOf(tab);
      let next = null;

      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        next = tabs[(i + 1) % tabs.length];
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        next = tabs[(i - 1 + tabs.length) % tabs.length];
      } else if (e.key === 'Home') {
        next = tabs[0];
      } else if (e.key === 'End') {
        next = tabs[tabs.length - 1];
      }

      if (next) {
        e.preventDefault();
        next.focus();
        select(next);
      }
    });
  });
}
