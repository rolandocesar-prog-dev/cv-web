# Portfolio — Rolando César Vásquez Tavera

Sitio estático de CV / portfolio. HTML semántico, CSS moderno con tokens y JavaScript en módulos ES, sin frameworks ni build.

## Stack

- HTML5 + CSS3 (custom properties)
- JavaScript ES Modules (vanilla)
- Iconos self-hosted (sprite SVG)
- Newsreader + Manrope + JetBrains Mono (Google Fonts)

## Estructura

```
cv-web/
├── index.html
├── css/styles.css
├── js/
│   ├── main.js
│   └── modules/
├── img/
│   ├── icons.svg        (sprite SVG)
│   ├── icons-src/       (SVG fuente para regenerar el sprite)
│   ├── og-image.png     (previsualización al compartir)
│   ├── og-image.svg     (fuente editable del PNG)
│   ├── perfil-web.webp
│   └── perfil.ico
├── robots.txt
├── sitemap.xml
└── README.md
```

## Uso local

Abre `index.html` directamente en el navegador o sírvelo con cualquier servidor estático de tu preferencia.

> El sitio usa módulos ES nativos (`type="module"`), por lo que algunas funciones requieren servirse vía HTTP en lugar de abrirse como archivo local (`file://`).

## Imagen de previsualización

`img/og-image.png` (1200×630) es la que usan LinkedIn, WhatsApp y X. `img/og-image.svg` es su fuente editable: tras cambiarla, vuelve a exportarla a PNG.

## Licencia

MIT — ver [LICENSE](./LICENSE).
