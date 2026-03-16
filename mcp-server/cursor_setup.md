# How to use IA Skills in Cursor

Cursor can use these skills via **MCP (SSE or Direct Command)** or locally via **.cursorrules**.

## 1. Global Setup (via MCP) - Recommended 🚀

### Step 1: Add Server

You can configure the MCP server **via UI** or **via `mcp.json`**.

#### Option A: Configuration file (`mcp.json`)

Create or edit the MCP config file:

- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **macOS / Linux**: `~/.cursor/mcp.json`

Example for a remote server (HTTP/SSE):

```json
{
  "mcpServers": {
    "is-skills-mcp-server": {
      "url": "http://10.234.10.87:8001/sse"
    }
  }
}
```

Replace the URL with your server address (host and port where the MCP server is running). Restart Cursor or reload the window after changing `mcp.json`.

#### Option B: Cursor Settings UI

1. Open Cursor Settings (**Settings > Cursor Settings > Features > MCP**).
2. Click **+ Add New MCP Server**.

![Cursor MCP Settings](../images/Cursor%20Tools_MCP.png)

**For Local Python Execution:**
- **Name**: `ia-skills` (or any name you prefer)
- **Type**: `command`
- **Command**: `python path/to/ia_skills/mcp-server/main.py` (use your venv Python and full path)

**For Remote / Docker (SSE):**
- **Name**: `is-skills-mcp-server` (or any name)
- **Type**: `SSE`
- **URL**: `http://<host>:8001/sse` (e.g. `http://10.234.10.87:8001/sse` or `http://skills-mcp.ia-skills.orb.local/sse`)

### Step 2: Usage

In Chat (Cmd+L) or Composer (Cmd+I), use the `@` symbol:
- Type `@is-skills-mcp-server` (or the name you configured) to see available tools.
- Use the `list_available_skills` tool to browse the repository skills.
- Use `get_skill_manual` for a specific skill's instructions.

---

## 2. Local Setup (via Files) 📂

### Option A: The .cursorrules file
Copy the content of the `SKILL.md` file you want into your project's `.cursorrules` file. This makes those instructions part of the system prompt for that project.

### Option B: Direct Reference (@)
Copy the skill folder into your project. Then, in the chat or composer, type:
- `Read @path/to/SKILL.md and follow its rules.`
