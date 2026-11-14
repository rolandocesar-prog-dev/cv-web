"""Genera el CV en PDF con ReportLab, en español y en inglés.

Uso (desde la raíz de cv-web):
    python -m venv tools/.venv
    tools/.venv/Scripts/pip install -r tools/requirements.txt   (Linux/macOS: tools/.venv/bin/)
    tools/.venv/Scripts/python tools/generar_cv_pdf.py

Escribe `CV_Rolando_Vasquez_Tavera.pdf` (español) y `CV_Rolando_Vasquez_Tavera_EN.pdf` (inglés).
El contenido en español está en las constantes de abajo y el inglés en `cv_en.py`: para
actualizar el CV se editan los dos y se vuelve a generar. El texto va como marcado de ReportLab,
así que `&`, `<` y `>` se escapan.
"""

from pathlib import Path
from types import SimpleNamespace
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Table,
    TableStyle,
)

from cv_en import EN

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "CV_Rolando_Vasquez_Tavera.pdf"
OUTPUT_EN = ROOT / "CV_Rolando_Vasquez_Tavera_EN.pdf"

# --- Contenido ------------------------------------------------------------------------------

NAME = "Rolando César Vásquez Tavera"
ROLE = "Desarrollador full stack y móvil — Flutter · TypeScript · Python · IA"
CONTACT = ["Tarija, Bolivia", "+591 78249575", "rolando.sha256@gmail.com"]
PROFILE_LINKS = [
    ("Portafolio web", "https://rolandocesar-prog-dev.github.io/cv-web/"),
    ("GitHub", "https://github.com/rolandocesar-prog-dev"),
]

PROFILE = (
    "Desarrollador full stack y móvil con más de cinco años como profesional independiente. "
    "Construyo apps con Flutter, interfaces web con React y backends con TypeScript (NestJS) y "
    "Python, con pruebas "
    "automatizadas y CI. Publiqué 4 apps en Google Play y App Store para empresas de delivery y "
    "movilidad, con experiencia en QA. Aplico IA a problemas concretos: RAG con evaluación "
    "medible, agentes con MCP y aprobación humana, y lectura de documentos con modelos de visión. "
    "Siete proyectos propios con código abierto, más de 1.000 pruebas automatizadas y demos en "
    "línea."
)

APPS_INTRO = (
    "Desarrolladas y publicadas bajo cuenta propia de desarrollador en Google Play Console y Apple "
    "Developer Program. Fui contratado para el desarrollo y la publicación; el lanzamiento "
    "comercial lo gestionó cada empresa."
)
APPS = [
    (
        "App de delivery y servicios — módulo cliente",
        [
            ("Google Play", "https://play.google.com/store/apps/details?id=com.goplus.customerapp"),
            ("App Store", "https://apps.apple.com/bo/app/id6787314464"),
        ],
    ),
    (
        "App de delivery y servicios — módulo repartidor",
        [
            ("Google Play", "https://play.google.com/store/apps/details?id=com.goplus.driverapp"),
            ("App Store", "https://apps.apple.com/bo/app/id6787321937"),
        ],
    ),
    (
        "Llévame App — módulo pasajero",
        [("App Store", "https://apps.apple.com/bo/app/llévame-app/id6450678669")],
    ),
    (
        "Llévame Driver — módulo conductor",
        [("App Store", "https://apps.apple.com/bo/app/llévame-driver/id6469526845")],
    ),
]

EXPERIENCE = [
    (
        "Desarrollador móvil y web — Startup tecnológica (Santa Cruz de la Sierra)",
        "Freelance remoto · Proyecto completado",
        [
            "Desarrollo de aplicaciones móviles multiplataforma con Flutter para Android e iOS, y "
            "panel web administrativo en React.",
            "Arquitectura de backend en tiempo real sobre Firebase (autenticación, base de datos, "
            "notificaciones push y almacenamiento).",
            "Publicación y versionado de las aplicaciones en Google Play y App Store.",
        ],
    ),
    (
        "Desarrollador de aplicaciones móviles — Llévame",
        "Startup de movilidad · Freelance",
        [
            "Desarrollo de las aplicaciones móviles de la plataforma (módulos pasajero y "
            "conductor) y publicación en App Store.",
            "Aseguramiento de calidad (QA): pruebas de funcionalidad, usabilidad, rendimiento y "
            "seguridad sobre aplicación React Native.",
        ],
    ),
    (
        "Desarrollador full stack — Proyectos independientes",
        "Tarija, Bolivia · 2020 – actualidad",
        [
            "Desarrollo de sistemas web a medida y sitios institucionales para empresas y "
            "organizaciones locales.",
            "Integración de servicios y APIs REST, modelado de bases de datos relacionales y "
            "despliegue en producción.",
        ],
    ),
]

# (título, tecnologías, descripción, enlaces)
PROJECTS: list[tuple[str, str, str, list[tuple[str, str]]]] = [
    (
        "Asistente RAG sobre documentación — Proyecto propio",
        "Python · FastAPI · PostgreSQL + pgvector · Docker · RAG / LLM",
        "Responde preguntas sobre la documentación de Kubernetes citando cada fuente y avisa si la "
        "respuesta no está. Búsqueda híbrida y evaluación automática: documento correcto en el "
        "100 % de las preguntas.",
        [("Código y demo", "https://github.com/rolandocesar-prog-dev/docs-rag-assistant")],
    ),
    (
        "API de inventario — Proyecto propio",
        "NestJS · TypeScript · PostgreSQL · Prisma · Docker · GitHub Actions",
        "API REST con historial auditable, JWT con renovación rotativa y stock que nunca queda "
        "negativo con operaciones simultáneas. 184 pruebas y CI. Demo (operador): "
        "demo@inventario.test / demo-inventario-2026.",
        [
            ("Código y demo", "https://github.com/rolandocesar-prog-dev/inventory-api-nestjs"),
            ("API en vivo", "https://inventory-api-c5yi.onrender.com/docs"),
        ],
    ),
    (
        "Panel web de inventario — Proyecto propio",
        "React · TypeScript · TanStack Query · Tailwind · Playwright · GitHub Actions",
        "Interfaz web de la API de inventario: catálogo, kardex, movimientos y administración. "
        "Tokens rotativos con una sola renovación y escrituras sin reintento automático. 143 "
        "pruebas, 16 E2E con accesibilidad y CI que lo publica.",
        [
            ("Código y demo", "https://github.com/rolandocesar-prog-dev/inventory-web-react"),
            ("En línea", "https://rolandocesar-prog-dev.github.io/inventory-web-react/"),
        ],
    ),
    (
        "Reservas de turnos — Proyecto propio",
        "Flutter · Riverpod · Firebase (Firestore, Auth, Cloud Functions, FCM) · TypeScript",
        "Reservas sin turnos duplicados para canchas y consultorios: transacciones y reglas de "
        "Firestore probadas, panel del negocio, recordatorios push con Cloud Functions y web "
        "publicada. 173 pruebas y CI.",
        [
            ("Código y demo", "https://github.com/rolandocesar-prog-dev/turnos-app-flutter"),
            ("Web", "https://turnos-rv-portafolio.web.app"),
        ],
    ),
    (
        "Escáner de facturas con IA — Proyecto propio",
        "Flutter · Dart · Riverpod · Ollama (modelo de visión local) · GitHub Actions",
        "App Android y web que lee la foto de una factura con un modelo de visión local y, tras la "
        "revisión humana, registra las entradas sin duplicados. 10/10 facturas de prueba "
        "perfectas; 123 pruebas y CI.",
        [("Código y demo", "https://github.com/rolandocesar-prog-dev/invoice-scanner-flutter")],
    ),
    (
        "Agente de inventario con MCP — Proyecto propio",
        "TypeScript · Model Context Protocol · Ollama (LLM local) · zod · Vitest · GitHub Actions",
        "Servidor MCP y agente que mueven el inventario conversando en español con un modelo "
        "local; nada se registra sin aprobación humana (0 escrituras sin aprobación en 18 "
        "escenarios). 126 pruebas y CI.",
        [("Código y demo", "https://github.com/rolandocesar-prog-dev/inventory-agent-mcp")],
    ),
    (
        "Suite de pruebas E2E con Playwright — Proyecto propio",
        "Playwright · TypeScript · axe-core · Docker · GitHub Actions",
        "Pruebas end-to-end de un comercio de práctica (Sauce Demo): 139 pruebas en cuatro "
        "navegadores, 13 defectos reales documentados, accesibilidad, rendimiento, regresión "
        "visual y 0 pruebas inestables.",
        [
            ("Código", "https://github.com/rolandocesar-prog-dev/qa-e2e-playwright"),
            ("Reporte", "https://rolandocesar-prog-dev.github.io/qa-e2e-playwright/"),
        ],
    ),
    (
        "App OTN-PB — Monitoreo de estaciones meteorológicas",
        "Flutter · Spring Boot · PostgreSQL",
        "Aplicación móvil para visualización y monitoreo en tiempo real de estaciones "
        "meteorológicas satelitales en el valle central de Tarija, orientada a apoyar la actividad "
        "agrícola de la región.",
        [],
    ),
    (
        "Sistema de Radio Móvil Andaluz",
        "PHP · JavaScript · Ajax · MySQL",
        "Sistema completo para control y despacho de llamadas radiales: registro de clientes, "
        "historial de servicios y panel de operadores en tiempo real.",
        [],
    ),
    (
        "Cuestionario ciudadano interactivo",
        "Angular · TypeScript",
        "Plataforma web interactiva de cuestionario ciudadano con procesamiento y visualización de "
        "resultados en tiempo real.",
        [],
    ),
    (
        "Sitio web institucional",
        "HTML5 · CSS3 · JavaScript",
        "Sitio institucional desarrollado sin frameworks, con foco en rendimiento, accesibilidad y "
        "tiempos de carga reducidos.",
        [],
    ),
]

SKILLS = [
    (
        "Núcleo",
        "Flutter, Dart, TypeScript, JavaScript, React, NestJS, Python (FastAPI), PostgreSQL, "
        "Firebase, Docker, Git y GitHub",
    ),
    (
        "Complementario",
        "React Native, Angular, Spring Boot, Java, PHP, MySQL, Supabase",
    ),
    (
        "IA y calidad",
        "RAG y búsqueda híbrida, agentes con MCP, pruebas E2E con Playwright, "
        "CI/CD con GitHub Actions",
    ),
    ("Metodologías", "Scrum, control de versiones con Git, buenas prácticas de código"),
]

EDUCATION = [
    (
        "Ingeniería en Sistemas",
        "Universidad Adventista de Bolivia (en curso). Proyecto de grado: asistente con RAG para "
        "trámites del Gobierno Autónomo Municipal de Tarija, con Scrum y la Alcaldía como "
        "Product Owner",
    ),
    ("Técnico Superior en Sistemas Informáticos", "Instituto Técnico Superior «INCOS»"),
    ("Bachiller en Humanidades", "Colegio Nacional San Luis / CEA San Jerónimo"),
]

PERSONAL = [
    ("Idiomas:", "Español (nativo) · Inglés B1 (lectura y documentación técnica)"),
]

ES = SimpleNamespace(
    NAME=NAME,
    ROLE=ROLE,
    CONTACT=CONTACT,
    PROFILE_LINKS=PROFILE_LINKS,
    PROFILE=PROFILE,
    APPS_INTRO=APPS_INTRO,
    APPS=APPS,
    EXPERIENCE=EXPERIENCE,
    PROJECTS=PROJECTS,
    SKILLS=SKILLS,
    EDUCATION=EDUCATION,
    PERSONAL=PERSONAL,
    HEADINGS=SimpleNamespace(
        profile="Perfil profesional",
        apps="Apps desarrolladas y publicadas en tiendas oficiales",
        experience="Experiencia profesional",
        projects="Proyectos destacados",
        skills="Competencias técnicas",
        education="Formación académica",
        languages="Idiomas",
    ),
)

# --- Estilo -----------------------------------------------------------------------------------

GREEN = colors.HexColor("#1B3A2F")
ORANGE = colors.HexColor("#C8621D")
GREY = colors.HexColor("#555555")
BLUE = colors.HexColor("#1F5FA8")
TABLE_WIDTH = 175 * mm  # el encabezado y las competencias usan todo el ancho

STYLES = {
    "name": ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=GREEN
    ),
    "role": ParagraphStyle(
        "role", fontName="Helvetica", fontSize=10.5, leading=14, textColor=ORANGE
    ),
    "contact": ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=GREY
    ),
    "heading": ParagraphStyle(
        "heading",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=GREEN,
        spaceBefore=9,
    ),
    "body": ParagraphStyle(
        "body", fontName="Helvetica", fontSize=9, leading=12.2, alignment=TA_JUSTIFY
    ),
    "item": ParagraphStyle(
        "item", fontName="Helvetica-Bold", fontSize=9.2, leading=12, spaceBefore=4
    ),
    "meta": ParagraphStyle(
        "meta", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.5, textColor=GREY
    ),
    "link": ParagraphStyle(
        "link", fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=GREY
    ),
    "label": ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=9, leading=12.2),
    "line": ParagraphStyle("line", fontName="Helvetica", fontSize=9, leading=12.2),
}


def text(value: str) -> str:
    return escape(value)


def link(label: str, url: str) -> str:
    return f'<a href="{escape(url)}" color="{BLUE.hexval()}">{text(label)}</a>'


def link_line(label: str, url: str) -> Paragraph:
    return Paragraph(f"{text(label)}: {link(url, url)}", STYLES["link"])


Block = list[Flowable]


def section(title: str, *blocks: Block) -> list[Flowable]:
    """Cada bloque va junto en una página, y el título con su línea va junto al primero.

    Los bloques son listas y no `KeepTogether`: anidar `KeepTogether` hace que el de afuera crea
    que no cabe (el de adentro informa una altura enorme para forzar su división).
    """
    heading: Block = [
        Paragraph(text(title.upper()), STYLES["heading"]),
        HRFlowable(width="100%", thickness=0.8, color=GREEN, spaceBefore=1, spaceAfter=4),
    ]
    first, *rest = blocks
    return [KeepTogether([*heading, *first]), *(KeepTogether(block) for block in rest)]


def header(c: SimpleNamespace) -> list[Flowable]:
    contact_lines = [text(line) for line in c.CONTACT]
    links = f' <font color="{GREY.hexval()}">·</font> '.join(
        link(label, url) for label, url in c.PROFILE_LINKS
    )
    table = Table(
        [
            [
                [
                    Paragraph(text(c.NAME), STYLES["name"]),
                    Paragraph(text(c.ROLE), STYLES["role"]),
                ],
                Paragraph("<br/>".join([*contact_lines, links]), STYLES["contact"]),
            ]
        ],
        colWidths=[110 * mm, TABLE_WIDTH - 110 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [table, HRFlowable(width="100%", thickness=1.2, color=ORANGE, spaceBefore=4)]


def apps(c: SimpleNamespace) -> list[Flowable]:
    blocks: list[Block] = [[Paragraph(text(c.APPS_INTRO), STYLES["body"])]]
    for title, stores in c.APPS:
        blocks.append(
            [
                Paragraph(text(title), STYLES["item"]),
                *(link_line(store, url) for store, url in stores),
            ]
        )
    return section(c.HEADINGS.apps, *blocks)


def experience(c: SimpleNamespace) -> list[Flowable]:
    blocks: list[Block] = []
    for title, meta, bullets in c.EXPERIENCE:
        items = ListFlowable(
            [ListItem(Paragraph(text(b), STYLES["body"]), leftIndent=10) for b in bullets],
            bulletType="bullet",
            start="•",
            bulletFontName="Helvetica",
            bulletFontSize=8,
            leftIndent=10,
        )
        blocks.append(
            [
                Paragraph(text(title), STYLES["item"]),
                Paragraph(text(meta), STYLES["meta"]),
                items,
            ]
        )
    return section(c.HEADINGS.experience, *blocks)


def projects(c: SimpleNamespace) -> list[Flowable]:
    blocks: list[Block] = []
    for title, stack, description, links in c.PROJECTS:
        blocks.append(
            [
                Paragraph(text(title), STYLES["item"]),
                Paragraph(text(stack), STYLES["meta"]),
                Paragraph(text(description), STYLES["body"]),
                *(link_line(label, url) for label, url in links),
            ]
        )
    return section(c.HEADINGS.projects, *blocks)


def skills(c: SimpleNamespace) -> list[Flowable]:
    label_width = 32 * mm
    table = Table(
        [
            [Paragraph(text(label), STYLES["label"]), Paragraph(text(value), STYLES["body"])]
            for label, value in c.SKILLS
        ],
        colWidths=[label_width, TABLE_WIDTH - label_width],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]
        )
    )
    return section(c.HEADINGS.skills, [table])


def labeled_lines(title: str, rows: list[tuple[str, str]], separator: str) -> list[Flowable]:
    lines = [
        Paragraph(f"<b>{text(label)}</b>{separator}{text(value)}", STYLES["line"])
        for label, value in rows
    ]
    return section(title, lines)


def build(c: SimpleNamespace, output: Path) -> None:
    document = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=f"CV — {c.NAME}",
        author=c.NAME,
    )
    story: list[Flowable] = [
        *header(c),
        *section(c.HEADINGS.profile, [Paragraph(text(c.PROFILE), STYLES["body"])]),
        *apps(c),
        *experience(c),
        *projects(c),
        *skills(c),
        *labeled_lines(c.HEADINGS.education, c.EDUCATION, " — "),
        *labeled_lines(c.HEADINGS.languages, c.PERSONAL, " "),
    ]
    document.build(story)


if __name__ == "__main__":
    for content, target in ((ES, OUTPUT), (EN, OUTPUT_EN)):
        build(content, target)
        print(f"Generado: {target.name}")
