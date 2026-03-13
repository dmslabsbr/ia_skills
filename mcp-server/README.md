# Skills MCP Server

This server exposes all skills in the `ia_skills` repository as MCP tools and resources. This allows any MCP-compatible client (like Cursor or Antigravity/Claude Code) to access these skills globally.

## 🛠️ Tools
- `list_available_skills`: Lists all skills in the repository.
- `get_skill_manual`: Returns the full content of `SKILL.md` and `README.md` for a specific skill.

## 🚀 Installation

### Prerequisites
- Python 3.10+
- `mcp` package: `pip install mcp`

---

### 1. For Antigravity (Claude Code / Gemini CLI)
Add the following to your `claude_config.json` or run the add command:

```bash
claude mcp add skills-mcp python3 /Users/dms/Documents/source/ia_skills/mcp-server/main.py
```

### 3. Using Docker (Global & Clean)
If you prefer not to manage local Python environments, you can run the MCP server via Docker.

1. **Build the image** (from the root `ia_skills` folder):
   ```bash
   docker build -t skills-mcp .
   ```

2. **Configure Cursor/Antigravity** to use Docker:
   - **Command**: `docker`
   - **Args**: `run -i --rm -v /Users/dms/Documents/source/ia_skills:/app/ia_skills skills-mcp`

---

## 📖 Why use this?
Instead of copying `.agents/skills` or `.cursorrules` to every new project, you can now simply tell the AI:
*"Use the django-audit skill from my MCP server to review this project."*

The AI will call `get_skill_manual`, read the instructions, and apply them instantly to your current workspace.
