# How to use IA Skills in Antigravity

Antigravity (the Gemini-based coding agent) can consume these skills either globally via **MCP** or locally by **copying folders**.

## 1. Global Setup (via MCP) - Recommended 🚀

This is the most efficient way. You set it up once, and the assistant can pull any skill to any project.

### Step 1: Configuration
Edit your Antigravity config file at `~/.gemini/antigravity/mcp_config.json`.

![MCP Config Example](../images/Antigravity%20mcp_config.png)

**If you are running the server locally:**
```json
{
  "mcpServers": {
    "ia-skills": {
      "command": "/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python",
      "args": [
        "/Users/dms/Documents/source/ia_skills/mcp-server/main.py"
      ]
    }
  }
}
```

![Antigravity Config Location](../images/Antigravity%20settings.png)

**If you are using the OrbStack/Docker URL (via Bridge):**
```json
{
  "mcpServers": {
    "ia-skills": {
      "command": "/Users/dms/Documents/skills-claude/mcp-server/.venv/bin/mcp-proxy",
      "args": [
        "http://skills-mcp.ia-skills.orb.local/sse"
      ]
    }
  }
}
```

### Step 2: Usage
Once configured, you can simply ask Antigravity:
- *"List my available skills."*
- *"Use the django-audit skill to analyze this file."*
- *"What skills do I have for project management?"*

![Manage MCP Servers](../images/Antigravity%20Manage%20MCP%20servers.png)

---

## 2. Local Setup (Manual Copy) 📂

Use this if you want specific skills to live inside a project repository or if you are working offline.

### Step 1: Copy the Folder
Copy the desired skill folder (e.g., `django-audit`) into your project under the `.agents/skills/` directory.

### Step 2: Usage
Antigravity automatically scans the `.agents/` folder. You can reference specific instructions directly or ask:
- *"Read the instructions in .agents/skills/django-audit/SKILL.md and apply them."*
