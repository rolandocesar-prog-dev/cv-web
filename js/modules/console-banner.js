/**
 * Easter egg en consola para curiosos que abren DevTools.
 * Mantiene el branding y un canal directo de contacto.
 */
export function printConsoleBanner() {
  const accent = '#3b82f6';
  const text = '#e2e8f0';

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
    `color:#94a3b8`,
    `color:${accent};font-weight:bold;text-decoration:underline`,
  );
}
