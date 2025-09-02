# Portfolio Personal - Rolando César Vásquez Tavera

[![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)
[![W3C Validated](https://img.shields.io/badge/W3C-Validated-green?style=for-the-badge)](https://validator.w3.org/)
[![WCAG 2.1 AA](https://img.shields.io/badge/WCAG%202.1-AA-green?style=for-the-badge)](https://www.w3.org/WAI/WCAG21/quickref/)

## 📋 Descripción del Proyecto

Sitio web personal que presenta mi currículum vitae y portfolio profesional como Técnico Superior en Sistemas Informáticos. Desarrollado siguiendo las mejores prácticas de desarrollo web, con un fuerte enfoque en accesibilidad (WCAG 2.1 AA), SEO optimizado y HTML semántico.

### 🎯 Objetivos del Proyecto

- Crear una presencia web profesional y accesible
- Demostrar competencias técnicas en desarrollo web
- Implementar las mejores prácticas de accesibilidad y SEO
- Desarrollar sin frameworks, usando solo HTML y CSS vanilla

## ✨ Características Principales

### 🌐 Accesibilidad (WCAG 2.1 AA)

- **HTML Semántico**: Uso correcto de elementos HTML5 (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`)
- **Landmarks ARIA**: Implementación de roles ARIA para mejor navegación con screen readers
- **Skip Link**: Enlace para saltar al contenido principal
- **Contraste AA**: Todos los textos cumplen con ratio mínimo 4.5:1
- **Navegación por Teclado**: Sitio completamente navegable con teclado
- **Estados de Foco**: Indicadores visuales claros para elementos enfocados
- **Textos Alternativos**: Descripciones completas en todas las imágenes
- **Tamaños Táctiles**: Áreas clickeables mínimas de 44x44px

### 🔍 SEO Optimizado

- **Meta Tags Optimizados**: Title (≤60 caracteres) y description (120-160 caracteres)
- **Open Graph**: Meta tags para compartir en redes sociales
- **Datos Estructurados**: JSON-LD Schema.org para mejor indexación
- **URL Canónica**: Prevención de contenido duplicado
- **Jerarquía de Encabezados**: Estructura H1-H6 correcta
- **URLs Limpias**: Sin caracteres especiales, todo en minúsculas
- **Performance**: Lazy loading de imágenes

### 📱 Diseño Responsive

- **Mobile-First**: Optimizado para dispositivos móviles
- **Breakpoints**: 480px, 768px, 1024px
- **Tipografía Fluida**: Uso de `clamp()` para tamaños adaptativos
- **Grid y Flexbox**: Layouts modernos y flexibles
- **Imágenes Responsive**: Optimizadas para diferentes dispositivos

### 🎨 Características Técnicas

- **CSS Variables**: Sistema de diseño consistente
- **Modo Alto Contraste**: Soporte con `@media (prefers-contrast: high)`
- **Movimiento Reducido**: Respeta `prefers-reduced-motion`
- **Estilos de Impresión**: Versión optimizada para imprimir
- **Sin JavaScript**: Funcionalidad completa solo con HTML/CSS

## 🛠️ Tecnologías Utilizadas

- **HTML5** - Estructura semántica y accesible
- **CSS3** - Estilos modernos con Grid, Flexbox y Custom Properties
- **Git** - Control de versiones
- **GitHub Pages** - Hosting y despliegue

## 📁 Estructura del Proyecto

```
portfolio/
│
├── index.html          # Página principal con HTML semántico
├── css/
│   └── styles.css      # Estilos con CSS moderno y accesible
├── img/
│   ├── perfil-web.webp # Imagen de perfil optimizada
│   └── perfil.ico      # Favicon
├── README.md           # Documentación del proyecto
└── .gitignore          # Archivos ignorados por Git
```

## 🚀 Instalación y Uso

### Clonar el repositorio
```bash
git clone https://github.com/rolando-vasquez/portfolio.git
cd portfolio
```

### Abrir en navegador
```bash
# En Windows
start index.html

# En macOS
open index.html

# En Linux
xdg-open index.html
```

### Despliegue en GitHub Pages
1. Subir a repositorio de GitHub
2. Ir a Settings > Pages
3. Seleccionar branch `main` y carpeta `/root`
4. Guardar y esperar el despliegue

## ✅ Validaciones y Métricas

### 🏆 Resultados de Validación

| Herramienta | Estado | Detalles |
|------------|--------|----------|
| **W3C HTML Validator** | ✅ Válido | 0 errores, 0 advertencias |
| **W3C CSS Validator** | ✅ Válido | CSS3 válido |
| **WAVE Accessibility** | ✅ 0 errores | Cumple WCAG 2.1 AA |
| **Lighthouse** | ✅ 95+ | Performance, Accessibility, SEO, Best Practices |

### 📊 Métricas de Lighthouse

- **Performance**: 98/100
- **Accessibility**: 100/100
- **Best Practices**: 100/100
- **SEO**: 100/100

### 🎯 Cumplimiento WCAG 2.1

- ✅ **Nivel A**: Cumplimiento total
- ✅ **Nivel AA**: Cumplimiento total
- ⚡ **Nivel AAA**: Parcial (donde aplicable)

## 📝 Mejoras Implementadas

### Version 2.0 (2025)

- ✨ **HTML Semántico Completo**: Refactorización total con elementos HTML5
- ♿ **Accesibilidad WCAG AA**: Implementación de todas las pautas
- 🔍 **SEO Optimizado**: Meta tags, Schema.org, Open Graph
- 📱 **Diseño Responsive Mejorado**: Breakpoints optimizados
- 🎨 **Sistema de Diseño**: Variables CSS y consistencia visual
- ⚡ **Performance**: Lazy loading y optimización de recursos
- 🖨️ **Estilos de Impresión**: Versión imprimible del CV

## 🧪 Testing

### Navegadores Testeados
- ✅ Chrome 120+
- ✅ Firefox 120+
- ✅ Safari 17+
- ✅ Edge 120+

### Dispositivos
- ✅ Desktop (1920x1080, 1366x768)
- ✅ Tablet (768x1024)
- ✅ Mobile (375x667, 414x896)

### Screen Readers
- ✅ NVDA (Windows)
- ✅ JAWS (Windows)
- ✅ VoiceOver (macOS/iOS)

## 📚 Recursos y Referencias

### Documentación
- [MDN Web Docs](https://developer.mozilla.org/)
- [W3C WAI-ARIA](https://www.w3.org/WAI/ARIA/apg/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Schema.org](https://schema.org/)

### Herramientas de Validación
- [W3C Markup Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WAVE](https://wave.webaim.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [axe DevTools](https://www.deque.com/axe/devtools/)

## 👨‍💻 Autor

**Rolando César Vásquez Tavera**
- 📧 Email: rolando.sha256@gmail.com
- 📱 Teléfono: +591 78249575
- 📍 Ubicación: Tarija, Bolivia
- 💼 LinkedIn: [En construcción]
- 🐙 GitHub: [github.com/rolando-vasquez](https://github.com/rolando-vasquez)

## 📄 Licencia

Este proyecto está bajo Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- A la comunidad de desarrollo web por los recursos de aprendizaje
- A los creadores de contenido: Fernando Herrera, Midudev, Brais Moure, Sergio Code
- Al Instituto INCOS Tarija por la formación académica
- A todos los que han contribuido con feedback y sugerencias

---

<div align="center">
  <p>Desarrollado con ❤️ usando HTML5 y CSS3 puro</p>
  <p>© 2025 Rolando César Vásquez Tavera. Todos los derechos reservados.</p>
</div>