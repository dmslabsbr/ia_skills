# AI Coding Skills 🚀

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Antigravity](https://img.shields.io/badge/Antigravity-Gemini-blue?style=flat) ![MCP Server](https://img.shields.io/badge/MCP-Server-4285F4?style=flat) ![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat)

Read in Portuguese: [README.pt-BR.md](README.pt-BR.md)

A curated collection of specialized skills designed to enhance modern AI coding assistants like **Antigravity** and **Cursor**. This repository provides expert-level workflows and a global Model Context Protocol (MCP) server.

## 📂 Available Skills

- **[📱 Android Expert](./android-expert)**: Best practices for Android development (Java/Kotlin, Material Design, Firebase).
- **[✅ Code Review Standards](./code-review-standards)**: PEP 8, type hints, Docker, and comprehensive testing reviews.
- **[🎨 Dashboard Cloner](./dashboard-cloner)**: UI/UX analysis to extract design tokens and layouts.
- **[🐍 Django Audit](./django-audit)**: Deep technical auditing for Django applications.
- **[🐙 Git Platforms Expert](./git-platforms-expert)**: Workflow master for GitHub/GitLab and CI/CD.
- **[🏗️ New App Bootstrap](./new-app-bootstrap)**: Scaffolding for new applications.
- **[📋 Phase Execution](./phase-execution)**: Structured delivery methodology via five distinct phases.
- **[🌍 README Bilingual](./readme-bilingual)**: Automated dual-language GitHub documentation.
- **[📝 Technical Documentation](./technical-documentation)**: Creation of structured `analise.md` and `plano.md`.
- **[🔄 Update Funcoes.md](./update-funcoes-md)**: Automated function tracking in `funcoes.md`.

## 🚀 Getting Started

You can use these skills in two ways:

### 1. Global (MCP) - Recommended
Running the included MCP server grants your AI agents instant access to all skills across any project.

**Run the server:**
- **Windows (local)**: From the repo root, run `run-server.bat` to start the server with Python (listens on `http://localhost:8001/sse`).
- **Linux (Docker)**: From the repo root, run `./run-docker.sh` to build and start the container (requires `chmod +x run-docker.sh` once).

**Configure your client:**
- **Setup Antigravity**: [English](./mcp-server/antigravity_setup.md) | [Português](./mcp-server/antigravity_setup.pt-BR.md)
- **Setup Cursor**: [English](./mcp-server/cursor_setup.md) | [Português](./mcp-server/cursor_setup.pt-BR.md)

### 2. Local (Copy/Paste)
If you prefer adding skills individually per project:
- **Folders**: Copy the skill folder into `.agents/skills/` (for Antigravity).
- **Rules**: Copy content into `.cursorrules` (for Cursor).

For more details on the server implementation and run options, check the [MCP Server README](./mcp-server/README.md).
