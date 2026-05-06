# Portfolio — Rolando César Vásquez Tavera

Sitio estático de CV / portfolio. HTML semántico, CSS moderno con tokens y JavaScript en módulos ES, sin frameworks ni build.

## Stack

- HTML5 + CSS3 (custom properties)
- JavaScript ES Modules (vanilla)
- Iconos self-hosted (sprite SVG)
- Inter + JetBrains Mono (Google Fonts)

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
│   ├── og-image.svg
│   ├── perfil-web.webp
│   └── perfil.ico
├── robots.txt
├── sitemap.xml
└── README.md
```

## Uso local

```bash
npx serve .
```

> El sitio usa módulos ES nativos, por lo que debe servirse vía HTTP (no abrirse con `file://`).

## Despliegue

Publicado en GitHub Pages: <https://rolandocesar-prog-dev.github.io/cv-web/>

## Licencia

MIT — ver [LICENSE](./LICENSE).
