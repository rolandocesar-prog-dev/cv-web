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
├── index.html           (versión en español, la fuente)
├── en/index.html        (versión en inglés, generada: no se edita a mano)
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
├── tools/
│   ├── build-en.mjs      (genera en/index.html)
│   ├── en.json           (traducciones de la página)
│   ├── generar_cv_pdf.py (genera los dos PDF del CV)
│   ├── cv_en.py          (contenido en inglés del PDF)
│   └── requirements.txt
├── CV_Rolando_Vasquez_Tavera.pdf
├── CV_Rolando_Vasquez_Tavera_EN.pdf
├── robots.txt
├── sitemap.xml
└── README.md
```

## Uso local

Abre `index.html` directamente en el navegador o sírvelo con cualquier servidor estático de tu preferencia.

> El sitio usa módulos ES nativos (`type="module"`), por lo que algunas funciones requieren servirse vía HTTP en lugar de abrirse como archivo local (`file://`).

## Versión en inglés

`en/index.html` se genera desde `index.html` con las traducciones de `tools/en.json`. Tras cambiar
la página en español, actualiza la tabla y vuelve a generarla:

```bash
npm run build:en
```

El script falla si queda un texto en español sin traducir o una traducción que ya no se usa, y el
CI comprueba con `npm run check:en` que `en/index.html` esté al día.

## CV en PDF

`CV_Rolando_Vasquez_Tavera.pdf` (español) y `CV_Rolando_Vasquez_Tavera_EN.pdf` (inglés) se generan
con ReportLab desde `tools/generar_cv_pdf.py`. El contenido en español está en ese script y el
inglés en `tools/cv_en.py`: al cambiar uno, cambia también el otro y vuelve a generarlos:

```bash
python -m venv tools/.venv
tools/.venv/Scripts/pip install -r tools/requirements.txt   # Linux/macOS: tools/.venv/bin/
tools/.venv/Scripts/python tools/generar_cv_pdf.py
```

## Imagen de previsualización

`img/og-image.png` (1200×630) es la que usan LinkedIn, WhatsApp y X. `img/og-image.svg` es su fuente editable: tras cambiarla, vuelve a exportarla a PNG.

## Licencia

MIT — ver [LICENSE](./LICENSE).
