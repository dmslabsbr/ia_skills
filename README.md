# AI Coding Skills 🚀

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Claude Code](https://img.shields.io/badge/Claude-Code-d97757?style=flat) ![MCP Server](https://img.shields.io/badge/MCP-Server-4285F4?style=flat) ![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat)

Read in Portuguese: [README.pt-BR.md](README.pt-BR.md)

A curated collection of specialized skills designed to enhance modern AI coding assistants like Antigravity, Cursor, and Claude Code. This repository provides expert-level workflows, system prompts, and a global Model Context Protocol (MCP) server to instantly expand your agent's technical capabilities across any project.

## 📂 Available Skills

- **[📱 Android Expert](./android-expert)**: Best practices for Android development with Java/Kotlin, Material Design, Firebase, and Google Play Store publishing guidelines.
- **[✅ Code Review Standards](./code-review-standards)**: Quality, security, and project standards reviews encompassing PEP 8, type hints, Docker, and comprehensive testing.
- **[🎨 Dashboard Cloner](./dashboard-cloner)**: UI/UX analysis from visual references to extract design tokens, layouts, and responsive behavior into a Developer Brief.
- **[🐍 Django Audit](./django-audit)**: Deep technical auditing for Django applications focusing on security, architecture, performance, and code quality.
- **[🐙 Git Platforms Expert](./git-platforms-expert)**: Workflow master for GitHub/GitLab, branch strategies, CI/CD pipelines, and semantic commit message generation.
- **[🏗️ New App Bootstrap](./new-app-bootstrap)**: Rapid scaffolding for new applications including README, VERSION, dependencies, Docker, ER diagrams, and test setups.
- **[📋 Phase Execution](./phase-execution)**: Structured project delivery methodology via five distinct phases (analysis, planning, implementation, validation, delivery) with checklists.
- **[🌍 README Bilingual](./readme-bilingual)**: Automated creation and maintenance of dual-language GitHub documentation.
- **[📝 Technical Documentation](./technical-documentation)**: Creation and maintenance of `analise.md` and `plano.md` for structured technical discussions and implementation planning.
- **[🔄 Update Funcoes.md](./update-funcoes-md)**: Automated documentation maintenance tracking when project functions are created, updated, or removed in `funcoes.md`.

## 🚀 Installation & Usage

### 1. The Global MCP Server (Recommended)
The most powerful way to use these skills is by running the included MCP server. This grants your AI agents instant access to all skills globally, without copying files.

**Via Docker:**
```bash
docker-compose up -d --build
```
*Then, add the SSE client to your IDE (Cursor/Antigravity) pointing to `http://localhost:8001/sse`.*

### 2. Local Project Setup (Symlinks)
If you prefer adding skills individually per project:
```bash
mkdir -p .agents/skills
ln -s /path/to/ia_skills/django-audit $(pwd)/.agents/skills/django-audit
```

### 3. Cursor Rules
For ad-hoc usage in Cursor, just mention the skill file in your prompt (e.g., `@django-audit/SKILL.md`) or copy its contents into your `.cursorrules`.

## 🤝 Contributing
Feel free to add new AI skills or improve existing ones. Ensure your contributions include both `SKILL.md` (English) and `SKILL.pt-BR.md` (Portuguese) formats.
