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
│   ├── og-image.svg
│   ├── perfil-web.webp
│   └── perfil.ico
├── robots.txt
├── sitemap.xml
└── README.md
```

## Uso local

Abre `index.html` directamente en el navegador o sírvelo con cualquier servidor estático de tu preferencia.

> El sitio usa módulos ES nativos (`type="module"`), por lo que algunas funciones requieren servirse vía HTTP en lugar de abrirse como archivo local (`file://`).

## Pendiente

- [ ] **Añadir `RolandoVasquez-CV.pdf` en la raíz del repo.** El botón
      "Descargar CV" del hero ya apunta a ese nombre de archivo; hasta que
      exista, el enlace devuelve 404.
- [ ] Reemplazar `img/og-image.svg` por PNG o JPG. LinkedIn, WhatsApp y X no
      renderizan SVG en las previsualizaciones, y además la imagen actual
      conserva los colores del tema oscuro anterior.

## Licencia

MIT — ver [LICENSE](./LICENSE).
