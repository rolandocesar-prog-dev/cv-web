/**
 * Easter egg en consola para curiosos que abren DevTools.
 * Mantiene el branding y un canal directo de contacto.
 */
export function printConsoleBanner() {
  const accent = '#f0b450';
  const text = '#ecedee';

  const banner = `
%c
╭──────────────────────────────────────────╮
│                                          │
│   R  O  L  A  N  D  O  -  D  E  V       │
│                                          │
╰──────────────────────────────────────────╯

%cDesarrollador full stack y móvil · IA aplicada  —  Tarija, Bolivia
%c¿Te interesa colaborar? %crolando.sha256@gmail.com
`;

  // eslint-disable-next-line no-console
  console.log(
    banner,
    `color:${accent};font-weight:bold`,
    `color:${text};font-weight:600`,
    `color:#9ba1a8`,
    `color:${accent};font-weight:bold;text-decoration:underline`,
  );
}
