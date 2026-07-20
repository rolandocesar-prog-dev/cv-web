/**
 * Easter egg en consola para curiosos que abren DevTools.
 * Mantiene el branding y un canal directo de contacto.
 */
export function printConsoleBanner() {
  const accent = '#b1441f';
  const text = '#1c1a16';

  const banner = `
%c
╭──────────────────────────────────────────╮
│                                          │
│   R  O  L  A  N  D  O  -  D  E  V       │
│                                          │
╰──────────────────────────────────────────╯

%cDesarrollador Web · Mobile · QA  —  Tarija, Bolivia
%c¿Te interesa colaborar? %crolando.sha256@gmail.com
`;

  // eslint-disable-next-line no-console
  console.log(
    banner,
    `color:${accent};font-weight:bold`,
    `color:${text};font-weight:600`,
    `color:#4a453d`,
    `color:${accent};font-weight:bold;text-decoration:underline`,
  );
}
