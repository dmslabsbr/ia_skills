# How to use IA Skills in Cursor

Cursor can use these skills via **MCP (SSE or Direct Command)** or locally via **.cursorrules**.

## 1. Global Setup (via MCP) - Recommended 🚀

### Step 1: Add Server
1. Open Cursor Settings (**Settings > Cursor Settings > Features > MCP**).
2. Click **+ Add New MCP Server**.

![Cursor MCP Settings](../images/Cursor%20Tools_MCP.png)

**For Local Python Execution:**
- **Name**: `ia-skills`
- **Type**: `command`
- **Command**: `/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python /Users/dms/Documents/source/ia_skills/mcp-server/main.py`

**For OrbStack/Docker (SSE):**
- **Name**: `ia-skills`
- **Type**: `SSE`
- **URL**: `http://skills-mcp.ia-skills.orb.local/sse`

### Step 2: Usage
In Chat (Cmd+L) or Composer (Cmd+I), use the `@` symbol:
- Type `@ia-skills` to see available tools from the server.
- Use the `list_available_skills` tool to browse the repository skills.
- Use `get_skill_manual` for a specific skill's instructions.

---

## 2. Local Setup (via Files) 📂

### Option A: The .cursorrules file
Copy the content of the `SKILL.md` file you want into your project's `.cursorrules` file. This makes those instructions part of the system prompt for that project.

### Option B: Direct Reference (@)
Copy the skill folder into your project. Then, in the chat or composer, type:
- `Read @path/to/SKILL.md and follow its rules.`
