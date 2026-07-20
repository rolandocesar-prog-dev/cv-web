/**
 * Entry point — orquesta todos los módulos.
 * Estructura: cada feature vive en js/modules/* y exporta una función init().
 */
import { initHeaderScroll } from './modules/header.js';
import { initMenu } from './modules/menu.js';
import { initReveal } from './modules/reveal.js';
import { initTypewriter } from './modules/typewriter.js';
import { initYear } from './modules/year.js';
import { initBackToTop } from './modules/back-to-top.js';
import { initSkillTabs } from './modules/tabs.js';
import { printConsoleBanner } from './modules/console-banner.js';

const ready = (fn) =>
  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', fn, { once: true })
    : fn();

ready(() => {
  initHeaderScroll();
  initMenu();
  initReveal();
  initTypewriter();
  initYear();
  initBackToTop();
  initSkillTabs();
  printConsoleBanner();
});
