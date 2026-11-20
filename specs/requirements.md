# Requisitos — Rediseño oscuro del CV web («Dossier técnico»)

## Contexto

El CV web (`cv-web`, GitHub Pages) tiene hoy una dirección editorial crema y terracota. Se evaluaron
dos propuestas en un lienzo de diseño y Rolando eligió la **Propuesta A — Dossier técnico**: tema
oscuro, una sola tipografía sans con su mono, un solo acento ámbar y los proyectos presentados con
evidencia (pruebas, CI, cifras medidas) antes que con adjetivos.

Público: reclutadores y equipos técnicos que revisan el sitio en escritorio y en celular, en
español o en inglés.

## Alcance

- Dentro: `index.html`, `css/styles.css`, `js/`, la versión en inglés generada (`en/index.html` +
  `tools/en.json`), metadatos para buscadores y redes, imagen de previsualización y README.
- Fuera: el contenido y el diseño de los PDF del CV (`tools/generar_cv_pdf.py`); el texto del CV
  no cambia, así que los PDF siguen válidos y no se regeneran. El sprite `img/icons.svg` no se
  regenera (su script es de PowerShell); se usan solo los símbolos que ya contiene.

## Requisitos funcionales

### RF-01 Identidad visual

- RF-01.1 El sitio DEBE usar un tema oscuro único (fondo `#0c0d0f`), la tipografía Geist para el
  texto y Geist Mono para metadatos, y un solo color de acento (ámbar `#f0b450`).
- RF-01.2 El acento DEBE usarse solo para estado, cifras clave, etiquetas de sección y la acción
  principal; nunca como relleno decorativo.
- RF-01.3 El sitio NO DEBE usar degradados de fondo, emoji ni tarjetas con borde lateral de color.

### RF-02 Cabecera y navegación

- RF-02.1 La cabecera DEBE mostrar el nombre, los enlaces a las secciones y el cambio de idioma.
- RF-02.2 CUANDO el ancho de la ventana sea menor que 860 px, la navegación DEBE pasar al menú a
  pantalla completa existente (botón «Menú», cierre con «Cerrar», Escape o cualquier enlace).
- RF-02.3 La página DEBE conservar el enlace «Saltar al contenido principal».

### RF-03 Portada

- RF-03.1 La portada DEBE mostrar disponibilidad y ubicación, el nombre como único `h1`, el rol,
  la propuesta de valor, el resumen profesional actual y las acciones «Ver proyectos» y «Descargar
  CV (PDF)», más enlaces a GitHub y LinkedIn.
- RF-03.2 La portada DEBE mostrar un panel «estado de los repositorios» con los 7 proyectos
  propios, su número de pruebas y su CI, como tabla accesible (encabezados de columna y título).
- RF-03.3 Las cifras del panel DEBEN coincidir con las de las tarjetas de proyecto.

### RF-04 Cifras

- RF-04.1 La página DEBE mostrar las cuatro cifras actuales: 5+ años, 4 apps publicadas,
  7 proyectos abiertos con CI y 1.000+ pruebas automatizadas.

### RF-05 Caso principal: ecosistema de inventario

- RF-05.1 La página DEBE presentar la API de inventario, el panel web, el agente MCP y el escáner
  de facturas como un sistema, con la API al centro y la relación de cada cliente con ella.
- RF-05.2 El diagrama DEBE entenderse sin las líneas: los nodos son una lista con texto, cada
  conector lleva su etiqueta en texto (por ejemplo «HTTP · JWT») y las líneas son decorativas.

### RF-06 Proyectos

- RF-06.1 La página DEBE destacar el asistente RAG con su demo animada, su cifra medida (100 %), su
  stack y sus enlaces.
- RF-06.2 La página DEBE mostrar los otros 6 proyectos como tarjetas con área, título, descripción
  breve, una cifra medida, stack y enlaces (código y demo o prueba en línea).
- RF-06.3 La tarjeta de la API DEBE conservar la cuenta de demostración pública y la del panel, la
  indicación «Usar la cuenta de demostración».
- RF-06.4 La demo animada DEBE cargarse de forma diferida y con dimensiones reservadas.

### RF-07 Apps publicadas

- RF-07.1 La página DEBE listar GoPlus, GoPlus Driver, Llévame App y Llévame Driver con su
  categoría y sus enlaces a las tiendas, y la aclaración de que el lanzamiento comercial lo
  gestionó cada empresa. NO DEBE mostrar cifras de usuarios, descargas ni pedidos.

### RF-08 Stack e idiomas

- RF-08.1 La página DEBE mostrar las habilidades en tres grupos visibles a la vez (núcleo, IA y
  calidad, complementario), sin pestañas, e incluir los idiomas (español nativo, inglés técnico B1).

### RF-09 Trayectoria

- RF-09.1 La página DEBE mostrar la formación (Ingeniería en Sistemas en curso con su proyecto de
  grado, Técnico Superior del INCOS, bachillerato) y los otros trabajos con su stack.
- RF-09.2 El trabajo de grado DEBE llamarse «proyecto de grado».

### RF-10 Contacto y pie

- RF-10.1 La sección de contacto DEBE ofrecer correo (con asunto prellenado), teléfono, LinkedIn,
  GitHub y la descarga del CV en PDF.
- RF-10.2 El pie DEBE mostrar el año actual y el nombre completo.

### RF-11 Versión en inglés

- RF-11.1 `en/index.html` DEBE seguir generándose desde `index.html` con `npm run build:en`, sin
  textos en español visibles salvo los nombres propios de la lista `KEEP`.
- RF-11.2 La versión en inglés DEBE enlazar el PDF en inglés y el asunto del correo en inglés.

### RF-12 Buscadores y redes

- RF-12.1 La página DEBE declarar `color-scheme: dark` y un `theme-color` igual al fondo.
- RF-12.2 La imagen de previsualización (`img/og-image.png`, 1200×630) DEBE usar el nuevo estilo y
  el titular vigente; `img/og-image.svg` es su fuente editable.
- RF-12.3 El sitemap DEBE indicar la fecha de la última modificación de cada versión.
- RF-12.4 Se DEBEN conservar `canonical`, `hreflang`, Open Graph, Twitter y el JSON-LD `Person`.

## Requisitos no funcionales

- RNF-01 Adaptable: SIN desplazamiento horizontal desde 320 px; las cuadrículas pasan a una
  columna en celular y los objetivos táctiles miden al menos 44 px.
- RNF-02 Accesible: contraste de texto ≥ 4,5:1 (≥ 3:1 en texto de 24 px o más), foco visible,
  HTML semántico, y animaciones desactivadas CUANDO el usuario pida movimiento reducido.
- RNF-03 Sin dependencias nuevas de ejecución ni frameworks: HTML, CSS con variables y módulos ES.
- RNF-04 Calidad: `npm run check:en`, `npm run lint` y `npm run format:check` en verde (son los
  pasos del CI).
- RNF-05 Sin código muerto: se borran los módulos y estilos que el nuevo diseño ya no usa.
