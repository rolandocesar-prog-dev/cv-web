// Genera en/index.html (versión en inglés) a partir de index.html y tools/en.json.
//
//   node tools/build-en.mjs          escribe en/index.html
//   node tools/build-en.mjs --check  falla si en/index.html no está al día (para el CI)
//
// La página en español es la fuente: se traduce cada texto y atributo visible con la tabla de
// tools/en.json. Si aparece un texto en español sin traducción, o una entrada de la tabla que ya
// no se usa, el script falla: así las dos versiones no se desincronizan en silencio.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const source = readFileSync(join(root, 'index.html'), 'utf8').replace(/\r\n/g, '\n');
const table = JSON.parse(readFileSync(join(root, 'tools', 'en.json'), 'utf8'));
const used = new Set();

/** Nombres propios y textos que se quedan igual aunque tengan tildes. */
const KEEP = [
  'Vásquez',
  'Rolando César Vásquez Tavera',
  'Llévame App',
  'Llévame Driver',
  'Instituto Técnico Superior «INCOS»',
  'Colegio Nacional San Luis / CEA San Jerónimo',
];
const SPANISH = /[áéíóúñ¿¡«»]/i;
const untranslated = [];

/** Traduce un texto conservando los espacios de alrededor (la sangría del HTML). */
function translate(raw) {
  const text = raw.replace(/\s+/g, ' ').trim();
  if (!text) return raw;
  const english = table[text];
  if (english === undefined) {
    if (SPANISH.test(text) && !KEEP.includes(text)) untranslated.push(text);
    return raw;
  }
  used.add(text);
  const [, lead, trail] = raw.match(/^(\s*)[\s\S]*?(\s*)$/);
  return lead + english + trail;
}

// El JSON-LD y los scripts no son texto visible: se apartan y se traducen aparte.
const scripts = [];
let html = source.replace(/<script[\s\S]*?<\/script>/g, (block) => {
  scripts.push(block);
  return `<!--script:${scripts.length - 1}-->`;
});

html = html
  .replace(/\b(aria-label|alt|content)="([^"]*)"/g, (_, name, value) => {
    return `${name}="${translate(value)}"`;
  })
  .replace(/>([^<>]+)</g, (_, text) => `>${translate(text)}<`);

html = html.replace(/<!--script:(\d+)-->/g, (_, index) =>
  scripts[Number(index)]
    .replace(
      '"jobTitle": "Desarrollador full stack y móvil"',
      '"jobTitle": "Full stack and mobile developer"',
    )
    .replace(
      '"url": "https://rolandocesar-prog-dev.github.io/cv-web/"',
      '"url": "https://rolandocesar-prog-dev.github.io/cv-web/en/"',
    ),
);

/** Reemplazo exacto que debe ocurrir al menos una vez. */
function swap(from, to) {
  if (!html.includes(from)) throw new Error(`No se encontró en index.html: ${from}`);
  html = html.replaceAll(from, to);
}

swap('<html lang="es">', '<html lang="en">');
swap(
  '<link rel="canonical" href="https://rolandocesar-prog-dev.github.io/cv-web/" />',
  '<link rel="canonical" href="https://rolandocesar-prog-dev.github.io/cv-web/en/" />',
);
swap(
  '<meta property="og:url" content="https://rolandocesar-prog-dev.github.io/cv-web/" />',
  '<meta property="og:url" content="https://rolandocesar-prog-dev.github.io/cv-web/en/" />',
);
swap(
  '<a href="en/" class="lang-switch" hreflang="en" lang="en">',
  '<a href="../" class="lang-switch" hreflang="es" lang="es">',
);
swap('href="CV_Rolando_Vasquez_Tavera.pdf"', 'href="../CV_Rolando_Vasquez_Tavera_EN.pdf"');
swap('subject=Oportunidad%20laboral', 'subject=Job%20opportunity');
swap('data-label-open="Abrir menú"', 'data-label-open="Open menu"');
swap('data-label-close="Cerrar menú"', 'data-label-close="Close menu"');
// La página vive un nivel más abajo: los recursos propios suben uno.
html = html.replace(/\b(href|src)="(css|img|js)\//g, '$1="../$2/');

const stale = Object.keys(table).filter((key) => !used.has(key));
if (untranslated.length > 0 || stale.length > 0) {
  for (const text of untranslated) console.error(`Sin traducción en tools/en.json: ${text}`);
  for (const key of stale) console.error(`Entrada de tools/en.json que ya no se usa: ${key}`);
  process.exit(1);
}

const target = join(root, 'en', 'index.html');
if (process.argv.includes('--check')) {
  const current = existsSync(target) ? readFileSync(target, 'utf8').replace(/\r\n/g, '\n') : '';
  if (current !== html) {
    console.error('en/index.html no está al día. Ejecuta: npm run build:en');
    process.exit(1);
  }
  console.log('en/index.html está al día.');
} else {
  mkdirSync(dirname(target), { recursive: true });
  writeFileSync(target, html);
  console.log(`Generado en/index.html (${used.size} textos traducidos).`);
}
