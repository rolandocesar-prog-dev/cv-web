"""Contenido en inglés del CV. Misma estructura que las constantes de `generar_cv_pdf.py`.

Al cambiar el CV en español hay que reflejar el cambio aquí y volver a generar los dos PDF.
"""

from types import SimpleNamespace

GITHUB = "https://github.com/rolandocesar-prog-dev"

EN = SimpleNamespace(
    NAME="Rolando César Vásquez Tavera",
    ROLE="Full stack & mobile developer — Flutter · TypeScript · Python · AI",
    CONTACT=["Tarija, Bolivia", "+591 78249575", "rolando.sha256@gmail.com"],
    PROFILE_LINKS=[
        ("Web portfolio", "https://rolandocesar-prog-dev.github.io/cv-web/en/"),
        ("GitHub", GITHUB),
        ("LinkedIn", "https://www.linkedin.com/in/rolando-cesar-vasquez-tavera-b62235222"),
    ],
    PROFILE=(
        "Full stack and mobile developer with more than five years as a freelance professional. "
        "I build apps with Flutter, web interfaces with React and backends with TypeScript "
        "(NestJS) and Python, with automated tests and CI. I published 4 apps on Google Play and "
        "the App Store for delivery and ride-hailing companies, and I have QA experience. I apply "
        "AI to concrete problems: RAG with measurable evaluation, agents with MCP and human "
        "approval, and document reading with vision models. Seven open source projects of my own, "
        "more than 1,000 automated tests and online demos."
    ),
    APPS_INTRO=(
        "Built and published under my own developer account on Google Play Console and the Apple "
        "Developer Program. I was hired for development and release; each company managed its own "
        "commercial launch."
    ),
    APPS=[
        (
            "Delivery and services app — customer module",
            [
                (
                    "Google Play",
                    "https://play.google.com/store/apps/details?id=com.goplus.customerapp",
                ),
                ("App Store", "https://apps.apple.com/bo/app/id6787314464"),
            ],
        ),
        (
            "Delivery and services app — courier module",
            [
                (
                    "Google Play",
                    "https://play.google.com/store/apps/details?id=com.goplus.driverapp",
                ),
                ("App Store", "https://apps.apple.com/bo/app/id6787321937"),
            ],
        ),
        (
            "Llévame App — passenger module",
            [("App Store", "https://apps.apple.com/bo/app/llévame-app/id6450678669")],
        ),
        (
            "Llévame Driver — driver module",
            [("App Store", "https://apps.apple.com/bo/app/llévame-driver/id6469526845")],
        ),
    ],
    EXPERIENCE=[
        (
            "Mobile and web developer — Tech startup (Santa Cruz de la Sierra)",
            "Remote freelance · Project completed",
            [
                "Built cross-platform mobile apps with Flutter for Android and iOS, and a web "
                "admin dashboard in React.",
                "Designed a real-time backend on Firebase (authentication, database, push "
                "notifications and storage).",
                "Released and versioned the apps on Google Play and the App Store.",
            ],
        ),
        (
            "Mobile app developer — Llévame",
            "Ride-hailing startup · Freelance",
            [
                "Built the platform's mobile apps (passenger and driver modules) and released "
                "them on the App Store.",
                "Quality assurance (QA): functional, usability, performance and security testing "
                "of a React Native application.",
            ],
        ),
        (
            "Full stack developer — Independent projects",
            "Tarija, Bolivia · 2020 – present",
            [
                "Built custom web systems and institutional websites for local companies and "
                "organizations.",
                "Integrated services and REST APIs, modeled relational databases and deployed to "
                "production.",
            ],
        ),
    ],
    PROJECTS=[
        (
            "RAG assistant for documentation — Own project",
            "Python · FastAPI · PostgreSQL + pgvector · Docker · RAG / LLM",
            "Answers questions about the Kubernetes documentation, citing every source, and says "
            "so when the answer is not there. Hybrid search and automated evaluation: the right "
            "document for 100% of the questions.",
            [("Code and demo", f"{GITHUB}/docs-rag-assistant")],
        ),
        (
            "Inventory API — Own project",
            "NestJS · TypeScript · PostgreSQL · Prisma · Docker · GitHub Actions",
            "REST API with an auditable history, JWT with rotating refresh tokens and stock that "
            "never goes negative under concurrent operations. 184 tests and CI. Demo (operator): "
            "demo@inventario.test / demo-inventario-2026.",
            [
                ("Code and demo", f"{GITHUB}/inventory-api-nestjs"),
                ("Live API", "https://inventory-api-c5yi.onrender.com/docs"),
            ],
        ),
        (
            "Inventory web dashboard — Own project",
            "React · TypeScript · TanStack Query · Tailwind · Playwright · GitHub Actions",
            "Web interface for the Inventory API: catalog, stock ledger, movements and admin "
            "screens. Rotating tokens with a single refresh and writes that are never retried "
            "automatically. 143 tests, 16 E2E tests with accessibility checks, and CI that "
            "deploys it.",
            [
                ("Code and demo", f"{GITHUB}/inventory-web-react"),
                ("Live", "https://rolandocesar-prog-dev.github.io/inventory-web-react/"),
            ],
        ),
        (
            "Appointment booking — Own project",
            "Flutter · Riverpod · Firebase (Firestore, Auth, Cloud Functions, FCM) · TypeScript",
            "Booking without double bookings for sports courts and clinics: tested Firestore "
            "transactions and rules, business dashboard, push reminders with Cloud Functions and "
            "a published web version. 173 tests and CI.",
            [
                ("Code and demo", f"{GITHUB}/turnos-app-flutter"),
                ("Web", "https://turnos-rv-portafolio.web.app"),
            ],
        ),
        (
            "AI invoice scanner — Own project",
            "Flutter · Dart · Riverpod · Ollama (local vision model) · GitHub Actions",
            "Android and web app that reads a photo of an invoice with a local vision model and, "
            "after a person reviews it, records the stock entries without duplicates. 10/10 test "
            "invoices perfect; 123 tests and CI.",
            [("Code and demo", f"{GITHUB}/invoice-scanner-flutter")],
        ),
        (
            "Inventory agent with MCP — Own project",
            "TypeScript · Model Context Protocol · Ollama (local LLM) · zod · Vitest · "
            "GitHub Actions",
            "MCP server and agent that update the inventory through a conversation in Spanish "
            "with a local model; nothing is recorded without human approval (0 writes without "
            "approval in 18 scenarios). 126 tests and CI.",
            [("Code and demo", f"{GITHUB}/inventory-agent-mcp")],
        ),
        (
            "E2E test suite with Playwright — Own project",
            "Playwright · TypeScript · axe-core · Docker · GitHub Actions",
            "End-to-end tests for a practice store (Sauce Demo): 139 tests on four browsers, 13 "
            "real defects documented, accessibility, performance, visual regression and 0 flaky "
            "tests.",
            [
                ("Code", f"{GITHUB}/qa-e2e-playwright"),
                ("Report", "https://rolandocesar-prog-dev.github.io/qa-e2e-playwright/"),
            ],
        ),
        (
            "OTN-PB app — Weather station monitoring",
            "Flutter · Spring Boot · PostgreSQL",
            "Mobile app to view and monitor satellite weather stations in real time in the "
            "central valley of Tarija, to support the region's farming.",
            [],
        ),
        (
            "Radio Móvil Andaluz dispatch system",
            "PHP · JavaScript · Ajax · MySQL",
            "Complete system for call control and dispatch: customer records, service history "
            "and a real-time operator dashboard.",
            [],
        ),
        (
            "Interactive citizen questionnaire",
            "Angular · TypeScript",
            "Interactive web questionnaire that processes and displays results in real time.",
            [],
        ),
        (
            "Institutional website",
            "HTML5 · CSS3 · JavaScript",
            "Institutional site built without frameworks, focused on performance, accessibility "
            "and short loading times.",
            [],
        ),
    ],
    SKILLS=[
        (
            "Core",
            "Flutter, Dart, TypeScript, JavaScript, React, NestJS, Python (FastAPI), PostgreSQL, "
            "Firebase, Docker, Git and GitHub",
        ),
        ("Also used", "React Native, Angular, Spring Boot, Java, PHP, MySQL, Supabase"),
        (
            "AI and quality",
            "RAG and hybrid search, agents with MCP, E2E tests with Playwright, CI/CD with "
            "GitHub Actions",
        ),
        ("Methods", "Scrum, version control with Git, clean code practices"),
    ],
    EDUCATION=[
        (
            "Systems Engineering",
            "Universidad Adventista de Bolivia (in progress). Degree project: RAG assistant for "
            "procedures of the Municipal Government of Tarija, with Scrum and the City Hall as "
            "Product Owner",
        ),
        ("Advanced Technician in Computer Systems", "Instituto Técnico Superior «INCOS»"),
        ("High school diploma (Humanities)", "Colegio Nacional San Luis / CEA San Jerónimo"),
    ],
    PERSONAL=[
        ("Languages:", "Spanish (native) · English B1 (reading and technical documentation)"),
    ],
    HEADINGS=SimpleNamespace(
        profile="Professional profile",
        apps="Apps built and published on the official stores",
        experience="Professional experience",
        projects="Featured projects",
        skills="Technical skills",
        education="Education",
        languages="Languages",
    ),
)
