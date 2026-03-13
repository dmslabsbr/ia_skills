# AI Coding Skills 🚀

Welcome to the collection of specialized skills for modern AI coding assistants. These skills are designed to enhance the capabilities of tools like **Antigravity**, **Cursor**, and **Claude Code**, providing them with expert-level knowledge and structured workflows.

## 🛠️ Integrated Tools

This repository is optimized for:

- **Antigravity**: These skills follow the official `SKILL.md` specification. Antigravity can automatically discover and use these skills to perform complex tasks with high precision.
- **Cursor**: You can use these files as references in your "Chat" or "Composer" sessions, or integrate them into your `.cursorrules` to define persistent project behavior.
- **Claude Code**: Use these files as context or copy the content into your project instructions to guide Claude's behavior during deep technical tasks.

---

## 📂 Available Skills

### 🐍 Django Audit
**Complete technical audit for Django applications.**
- **Focus**: Security (vulnerabilities), Architecture (best practices), Performance (N+1 queries), and Code Quality.
- **Output**: Detailed reports with severity levels and actionable fix plans.
- **Location**: [`/django-audit`](./django-audit)

### 🎨 Dashboard Cloner
**Deep UI/UX analysis from visual references.**
- **Focus**: Extracting design tokens, layout structures, typography, and responsive behavior.
- **Output**: Structured JSONC analysis and a high-fidelity Developer Brief.
- **Location**: [`/dashboard-cloner`](./dashboard-cloner)

---

## 🚀 How to Use

### In Antigravity
Antigravity automatically detects skills in the workspace. Simply ask the AI to perform an action related to the skill (e.g., *"Perform a security audit on my Django app"*), and it will use the defined patterns.

### In Cursor
1. Press `Cmd+K` or `Cmd+L`.
2. Reference the skill file using `@SKILL.md` (e.g., `@django-audit/SKILL.md`).
3. Instruct Cursor: *"Use the instructions in this file to analyze my code."*

### In Claude Code
Add the skill to your context or project prompt:
```bash
claude "Analyze my Django project using the patterns in /path/to/django-audit/SKILL.md"
```

---

## 🌐 Language Support

All skills are available in both **English** and **Portuguese (pt-BR)**. The AI will automatically respond in the language you use.

- Documentation: `README.md` / `README.pt-BR.md`
- Skill Definitions: `SKILL.md` / `SKILL.pt-BR.md`

---

*Curated with ❤️ for the AI coding community.*
