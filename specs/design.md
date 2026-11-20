# Diseño — Rediseño oscuro del CV web

## 1. Decisiones

| Tema                     | Decisión                                                               | Motivo                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Tema                     | Solo oscuro (`color-scheme: dark`)                                     | Es la propuesta elegida; un tema claro sería otro diseño que mantener.                                  |
| Tipografía               | Geist + Geist Mono (Google Fonts, `display=swap`)                      | Sans neutra y técnica con mono de la misma familia; reemplaza a Newsreader, Manrope y JetBrains Mono.   |
| Datos del panel de repos | Escritos en el HTML                                                    | Sin llamadas a la API de GitHub: sin límites de uso, sin JS para el contenido y legible por buscadores. |
| Demo del asistente RAG   | Copia propia en `img/demo-rag.gif` (960×720, 0,2 MB), `loading="lazy"` | Sin depender de otro repositorio; el tamaño reservado evita saltos de diseño.                           |
| Habilidades              | Tres grupos visibles, sin pestañas                                     | Se lee de un vistazo; se elimina `js/modules/tabs.js`.                                                  |
| Navegación en celular    | Se reutiliza el menú a pantalla completa (`js/modules/menu.js`)        | Ya es accesible (foco, Escape, bloqueo del fondo en iOS).                                               |
| Iconos                   | Flechas de texto (↗ ↓ →) y los símbolos existentes del sprite          | El sprite se genera con PowerShell; no se regenera en este cambio.                                      |
| PDF                      | Sin cambios                                                            | El contenido del CV no cambia; solo cambia la presentación web.                                         |

## 2. Tokens (`:root` en `css/styles.css`)

```css
--bg: #0c0d0f; /* fondo */
--bg-raised: #121417; /* paneles y tarjetas destacadas */
--bg-card: #0f1013; /* tarjetas */
--line: #23262b; /* bordes */
--line-strong: #3a3e45; /* bordes de botones y nodos */
--text: #ecedee; /* 16,9:1 sobre --bg */
--text-soft: #c4c8cd; /* stack, 11,6:1 */
--text-muted: #9ba1a8; /* textos secundarios, 7,3:1 */
--text-faint: #8a9098; /* etiquetas pequeñas, 5,9:1 */
--accent: #f0b450; /* ámbar, 10,8:1; texto sobre ámbar: --bg */
```

Escala: contenedor de 1200 px con margen lateral `clamp(16px, 4vw, 48px)`; secciones con
`clamp(64px, 8vw, 112px)` de relleno vertical; títulos con `clamp()`.

## 3. Estructura de la página

```
header.header            nombre · nav (≥ 860 px) · English · botón Menú (< 860 px)
nav#site-menu.menu       menú a pantalla completa (sin cambios de comportamiento)
main#main
  section#hero           disponibilidad · h1 · rol y propuesta · resumen · acciones
                         + aside.repo-status (table con caption)
  section.figures        ul de 4 cifras
  section#ecosystem      01 / caso principal — ul.eco de 4 nodos + conectores aria-hidden
  section#projects       02 / proyectos — article.featured (RAG + GIF) + 6 article.project-card
  section#apps           03 / en producción — 4 apps con enlaces a tiendas
  section#skills         04 / stack — núcleo · IA y calidad · complementario · idiomas
  section#education      05 / trayectoria — formación + otros trabajos (filas con etiqueta)
  section#contact        06 / contacto — CTA, correo, teléfono, LinkedIn, GitHub, CV
footer.footer            © año · nombre
button.back-to-top
```

Los `id` de las secciones existentes se conservan (`hero`, `projects`, `apps`, `skills`,
`education`, `contact`) para no romper enlaces ya compartidos; `about` desaparece porque su
contenido pasa a la portada y a las cifras.

## 4. CSS

Un solo `css/styles.css`, por bloques en este orden: tokens, base y reset, utilidades (`.container`,
`.sr-only`, `.mono`, `.skip-link`, `.reveal`), botones y enlaces, cabecera, menú, portada y panel de
repos, cifras, ecosistema, proyectos, apps, stack, trayectoria, contacto, pie, volver arriba y
movimiento reducido. Nomenclatura `bloque__elemento--modificador`, como hasta ahora.

Diseño adaptable sin consultas de medios salvo en la cabecera (860 px): flex con `flex-wrap` y
cuadrículas `repeat(auto-fit, minmax(min(Npx, 100%), 1fr))`. Las líneas entre celdas se dibujan con
`gap: 1px` sobre el color de borde, para que no queden bordes sueltos al apilarse.

## 5. JavaScript

`js/main.js` inicia `header`, `menu`, `reveal`, `year`, `back-to-top` y `console-banner` (con los
colores nuevos). Se borra `tabs.js`. El contenido no depende de JS: sin JS todo es visible porque
`.reveal` solo se oculta con la clase `js` en `<html>`.

## 6. Inglés

Se mantiene `tools/build-en.mjs` sin cambios de lógica. Cada texto nuevo lleva su entrada en
`tools/en.json`, **también los que no tienen tildes** (el script solo detecta español por las
tildes, así que «Trayectoria» pasaría sin traducir). El script falla si sobra una entrada, lo que
limpia las que ya no se usan. Se conservan los textos exactos que el script reemplaza (`swap`): el
enlace `.lang-switch`, el `href` del PDF, el asunto `Oportunidad%20laboral` y los
`data-label-open/close` del menú.

Comprobación adicional: tras generar, se buscan en `en/index.html` palabras españolas frecuentes
sin tilde (`de`, `con`, `para`, `pruebas`, `proyectos`…) fuera de los nombres propios.

## 7. Buscadores

- `<meta name="theme-color" content="#0c0d0f">` y `<meta name="color-scheme" content="dark">`.
- `sitemap.xml` con `<lastmod>` en las dos URL.
- `img/og-image.svg` rehecha en oscuro con el titular vigente y exportada a PNG 1200×630 con
  Chromium (Playwright) y las fuentes Geist locales.

## 8. Verificación

1. `npm run build:en`, `npm run check:en`, `npm run lint`, `npm run format:check`.
2. Capturas con Playwright a 1440 px y a 390 px, en español y en inglés: sin desplazamiento
   horizontal, sin textos cortados.
3. axe (WCAG A/AA) sin violaciones críticas ni graves.
4. Enlaces a los dos PDF presentes y con `download`.
