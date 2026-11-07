"""Genera `CV_Rolando_Vasquez_Tavera.pdf` con ReportLab.

Uso (desde la raíz de cv-web):
    python -m venv tools/.venv
    tools/.venv/Scripts/pip install -r tools/requirements.txt   (Linux/macOS: tools/.venv/bin/)
    tools/.venv/Scripts/python tools/generar_cv_pdf.py

El contenido está en las constantes de abajo: para actualizar el CV se edita el texto y se vuelve
a generar el PDF. El texto va como marcado de ReportLab, así que `&`, `<` y `>` se escapan.
"""

from pathlib import Path
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

OUTPUT = Path(__file__).resolve().parent.parent / "CV_Rolando_Vasquez_Tavera.pdf"

# --- Contenido ------------------------------------------------------------------------------

NAME = "Rolando César Vásquez Tavera"
ROLE = "Desarrollador móvil y full stack — Flutter · Firebase · QA"
CONTACT = ["Tarija, Bolivia", "+591 78249575", "rolando.sha256@gmail.com"]
PROFILE_LINKS = [
    ("Portafolio web", "https://rolandocesar-prog-dev.github.io/cv-web/"),
    ("GitHub", "https://github.com/rolandocesar-prog-dev"),
]

PROFILE = (
    "Desarrollador de software con más de cinco años como profesional independiente en "
    "aplicaciones móviles multiplataforma (Flutter), sistemas web a medida y aseguramiento de "
    "calidad. Manejo el ciclo completo del producto: requerimientos, diseño UX/UI, desarrollo, "
    "pruebas, despliegue y publicación en Google Play y App Store bajo cuenta propia de "
    "desarrollador. Estudiante de Ingeniería en Sistemas; desarrollo mi proyecto de grado, un "
    "asistente conversacional con RAG para trámites municipales. Orientado a buenas prácticas, "
    "código mantenible y entregas documentadas."
)

APPS_INTRO = (
    "Desarrolladas y publicadas bajo cuenta propia de desarrollador en Google Play Console y Apple "
    "Developer Program. Fui contratado para el desarrollo y la publicación; el lanzamiento "
    "comercial lo gestionó cada empresa."
)
APPS = [
    (
        "Aplicación de movilidad — módulo pasajero",
        [
            ("Google Play", "https://play.google.com/store/apps/details?id=com.goplus.customerapp"),
            ("App Store", "https://apps.apple.com/bo/app/id6787314464"),
        ],
    ),
    (
        "Aplicación de movilidad — módulo conductor",
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
        "Freelance remoto · En desarrollo activo",
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
            "conductor) y publicación en App Store bajo cuenta propia de desarrollador.",
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
        "Asistente conversacional para trámites municipales — Proyecto de grado (UAB, en curso)",
        "RAG / LLM · App móvil · Panel de administración · Scrum",
        "Asistente basado en RAG que orienta a los ciudadanos sobre trámites del Gobierno Autónomo "
        "Municipal de Tarija. Incluye app móvil y panel de administración; la Alcaldía actúa como "
        "Product Owner.",
        [],
    ),
    (
        "Asistente RAG sobre documentación — Proyecto propio",
        "Python · FastAPI · PostgreSQL + pgvector · Docker · RAG / LLM",
        "Responde preguntas sobre la documentación de Kubernetes en español citando cada fuente, y "
        "avisa cuando la respuesta no está. Búsqueda híbrida, modelo intercambiable (local o en la "
        "nube) y evaluación automática: trae el documento correcto en el 100 % de las preguntas de "
        "prueba y el 89 % de sus respuestas es fiel a las fuentes citadas.",
        [("Código y demo", "https://github.com/rolandocesar-prog-dev/docs-rag-assistant")],
    ),
    (
        "Suite de pruebas E2E con Playwright — Proyecto propio",
        "Playwright · TypeScript · axe-core · Docker · GitHub Actions",
        "Pruebas end-to-end de un sitio de comercio electrónico de práctica (Sauce Demo), a partir "
        "de un plan de pruebas priorizado: 139 pruebas en cuatro navegadores, 13 defectos reales "
        "documentados, accesibilidad, rendimiento y regresión visual, y 0 pruebas inestables en "
        "30 ejecuciones del CI.",
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
        "Test Político Boliviano",
        "Angular · TypeScript",
        "Plataforma web interactiva de cuestionario ciudadano con procesamiento y visualización de "
        "resultados en tiempo real.",
        [],
    ),
    (
        "Sitio web institucional — Voz Liberal Tarija",
        "HTML5 · CSS3 · JavaScript",
        "Sitio institucional desarrollado sin frameworks, con foco en rendimiento, accesibilidad y "
        "tiempos de carga reducidos.",
        [],
    ),
]

SKILLS = [
    (
        "Núcleo",
        "Flutter, Dart, Firebase (Firestore, Auth, Storage), JavaScript, TypeScript, Git, GitHub, "
        "pruebas de software",
    ),
    (
        "Complementario",
        "React, React Native, Angular, Spring Boot, PHP, Java, Python, APIs REST, PostgreSQL, "
        "MySQL, Supabase",
    ),
    ("En foco ahora", "IA aplicada (RAG), Docker y CI/CD, testing automatizado"),
    ("Metodologías", "Scrum, control de versiones con Git, buenas prácticas de código"),
]

EDUCATION = [
    ("Ingeniería en Sistemas", "Universidad Adventista de Bolivia (en curso)"),
    ("Técnico Superior en Sistemas Informáticos", "Instituto Técnico Superior «INCOS»"),
    ("Bachiller en Humanidades", "Colegio Nacional San Luis / CEA San Jerónimo"),
]

PERSONAL = [
    ("Idiomas:", "Español (nativo) · Inglés B1 (lectura y documentación técnica)"),
    (
        "Competencias:",
        "Resolución de problemas, trabajo en equipo, liderazgo, adaptabilidad y aprendizaje "
        "continuo.",
    ),
]

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


def header() -> list[Flowable]:
    contact_lines = [text(line) for line in CONTACT]
    links = f' <font color="{GREY.hexval()}">·</font> '.join(
        link(label, url) for label, url in PROFILE_LINKS
    )
    table = Table(
        [
            [
                [Paragraph(text(NAME), STYLES["name"]), Paragraph(text(ROLE), STYLES["role"])],
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


def apps() -> list[Flowable]:
    blocks: list[Block] = [[Paragraph(text(APPS_INTRO), STYLES["body"])]]
    for title, stores in APPS:
        blocks.append(
            [
                Paragraph(text(title), STYLES["item"]),
                *(link_line(store, url) for store, url in stores),
            ]
        )
    return section("Apps desarrolladas y publicadas en tiendas oficiales", *blocks)


def experience() -> list[Flowable]:
    blocks: list[Block] = []
    for title, meta, bullets in EXPERIENCE:
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
    return section("Experiencia profesional", *blocks)


def projects() -> list[Flowable]:
    blocks: list[Block] = []
    for title, stack, description, links in PROJECTS:
        blocks.append(
            [
                Paragraph(text(title), STYLES["item"]),
                Paragraph(text(stack), STYLES["meta"]),
                Paragraph(text(description), STYLES["body"]),
                *(link_line(label, url) for label, url in links),
            ]
        )
    return section("Proyectos destacados", *blocks)


def skills() -> list[Flowable]:
    label_width = 32 * mm
    table = Table(
        [
            [Paragraph(text(label), STYLES["label"]), Paragraph(text(value), STYLES["body"])]
            for label, value in SKILLS
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
    return section("Competencias técnicas", [table])


def labeled_lines(title: str, rows: list[tuple[str, str]], separator: str) -> list[Flowable]:
    lines = [
        Paragraph(f"<b>{text(label)}</b>{separator}{text(value)}", STYLES["line"])
        for label, value in rows
    ]
    return section(title, lines)


def build(output: Path = OUTPUT) -> None:
    document = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=f"CV — {NAME}",
        author=NAME,
    )
    story: list[Flowable] = [
        *header(),
        *section("Perfil profesional", [Paragraph(text(PROFILE), STYLES["body"])]),
        *apps(),
        *experience(),
        *projects(),
        *skills(),
        *labeled_lines("Formación académica", EDUCATION, " — "),
        *labeled_lines("Idiomas y competencias personales", PERSONAL, " "),
    ]
    document.build(story)


if __name__ == "__main__":
    build()
    print(f"Generado: {OUTPUT.name}")
