# Skills MCP Server

This server exposes all skills in the `ia_skills` repository as MCP tools and resources. This allows any MCP-compatible client (like Cursor or Antigravity) to access these skills globally.

## 🛠️ Tools
- `list_available_skills`: Lists all skills in the repository.
- `get_skill_manual`: Returns the full content of `SKILL.md` and `README.md` for a specific skill.

## 🚀 Configuration

### 1. Antigravity (Gemini Code Assistant)
The configuration is stored in `~/.gemini/antigravity/mcp_config.json`. 

#### Option A: Local (Direct)
Use this if the server is on the same machine:
```json
{
  "mcpServers": {
    "skills-mcp": {
      "command": "/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python",
      "args": [
        "/Users/dms/Documents/source/ia_skills/mcp-server/main.py"
      ]
    }
  }
}
```

#### Option B: Remote / OrbStack (via Bridge)
If your server is running in a container or a remote URL (like `skills-mcp.ia-skills.orb.local`), use the `mcp-proxy` bridge for compatibility:
```json
{
  "mcpServers": {
    "skills-mcp": {
      "command": "/Users/dms/Documents/skills-claude/mcp-server/.venv/bin/mcp-proxy",
      "args": [
        "http://skills-mcp.ia-skills.orb.local/sse"
      ]
    }
  }
}
```

---

### 2. Cursor
To use these skills in Cursor, go to **Settings > Cursor Settings > Features > MCP**.

#### Option A: Local (command)
- **Name**: `skills-mcp`
- **Type**: `command`
- **Command**: `/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python /Users/dms/Documents/source/ia_skills/mcp-server/main.py`

#### Option B: Remote (SSE)
- **Name**: `skills-mcp`
- **Type**: `SSE`
- **URL**: `http://skills-mcp.ia-skills.orb.local/sse`

---

### 3. Using Docker (Clean)
You can run the MCP server via Docker to keep your local machine clean.

1. **Build the image**:
   ```bash
   docker build -t skills-mcp /Users/dms/Documents/source/ia_skills/mcp-server/
   ```

2. **Run Configuration**:
   - **Command**: `docker`
   - **Args**: `run -i --rm -v /Users/dms/Documents/source/ia_skills:/app/ia_skills skills-mcp`

---

## 📖 Why use this?
Instead of copying `.agents/skills` or `.cursorrules` to every new project, you can simply tell the AI:
*"Use the django-audit skill from my MCP server to review this project."*

The AI will call `get_skill_manual`, read the instructions, and apply them instantly to your current workspace.
