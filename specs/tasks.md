# Tareas — Rediseño oscuro del CV web

Cada tarea es un commit (Conventional Commits en español). Se marca `[x]` al terminarla.

## Hito R1 — Especificación

- [x] 1. Specs del rediseño (`requirements.md`, `design.md`, `tasks.md`).

## Hito R2 — Página

- [x] 2. Rediseño oscuro de la página en español e inglés: estructura nueva en `index.html`,
      `css/styles.css` reescrito con los tokens, `js/main.js` sin pestañas (se borra `tabs.js`),
      banner de consola con los colores nuevos, demo del RAG en `img/demo-rag.gif`, traducciones
      en `tools/en.json` y `en/index.html` regenerado (RF-01 a RF-11, RNF-01 a RNF-05).

## Hito R3 — Buscadores y redes

- [x] 3. Metadatos del tema oscuro (`theme-color`, `color-scheme`) y `lastmod` en el sitemap
      (RF-12.1, RF-12.3).
- [x] 4. Imagen de previsualización oscura: `img/og-image.svg` y `img/og-image.png` (RF-12.2).

- [x] 6. Verificación del sitio en Google Search Console: archivo `googlebf3e1cb51b9db208.html`
      en la raíz, tal como lo entrega Google (excluido de Prettier).

## Hito R4 — Cierre

- [x] 5. Verificación en escritorio y celular, en español e inglés (capturas, axe, enlaces a los
      PDF) y README actualizado (tipografías, dirección visual, estructura).

## Fuera de este cambio

- Regenerar `img/icons.svg` sin los símbolos que ya no se usan (`build-sprite.ps1`, en Windows).
- Foto profesional nueva y fechas de cada experiencia (pendientes de Rolando).
- Registrar el sitio en Bing Webmaster Tools (con la cuenta de Rolando; se puede importar desde Search Console).
