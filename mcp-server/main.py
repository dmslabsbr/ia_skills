import os
import json
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize FastMCP server
# host and port are configured here for SSE transport
mcp = FastMCP("skills_mcp", host="0.0.0.0", port=8001)

# Path to the skills repository
SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- PROMPTS (Atalhos de comando) ---

@mcp.prompt("analisar-skills-disponiveis")
def analisar_skills() -> str:
    """Cria um guia rápido das habilidades instaladas e sugere as melhores para o projeto."""
    return """Por favor, execute os seguintes passos:
1. Use a ferramenta 'list_available_skills' para ver o que temos no repositório.
2. Com base no código que estamos editando neste projeto do Cursor, identifique quais 2 ou 3 skills seriam mais úteis agora.
3. Para essas selecionadas, use 'get_skill_manual' para ler o SKILL.md delas.
4. Faça um resumo curto de como cada uma pode me ajudar neste arquivo específico."""

# --- TOOLS (Ações dinâmicas) ---


#class SkillIdentifier(BaseModel):
#    skill_name: str = Field(..., description="The directory name of the skill (e.g., 'django-audit')")
#

@mcp.tool(
    name="list_available_skills",
    annotations={"readOnlyHint": True}
)
async def list_available_skills() -> str:
    """Lists all skills installed in the skills-claude repository."""
    print("[MCP] 🛠️  Tool called: list_available_skills", flush=True)
    skills = []
    # Skip directories like .git, mcp-server, etc.
    skip_dirs = {".git", ".gemini", "mcp-server", "brain", ".agents", "node_modules"}
    
    for item in os.listdir(SKILLS_ROOT):
        item_path = os.path.join(SKILLS_ROOT, item)
        if os.path.isdir(item_path) and item not in skip_dirs:
            skill_file = os.path.join(item_path, "SKILL.md")
            if os.path.exists(skill_file):
                skills.append(item)
    
    return json.dumps({"skills": sorted(skills)}, indent=2)

@mcp.tool(
    name="get_skill_manual",
    annotations={"readOnlyHint": True}
)
async def get_skill_manual(
    skill_name: str = Field(..., description="Skill folder name (ex: 'django-audit') to retrieve the SKILL manual")
) -> str:
    """Retrieves the full instructions (SKILL.md) and documentation for a specific skill."""
    print(f"[MCP] 🛠️  Tool called: get_skill_manual | requested skill: {skill_name}", flush=True)
    
    skill_dir = os.path.join(SKILLS_ROOT, skill_name)
    
    if not os.path.exists(skill_dir):
        return f"Error: Skill '{skill_name}' not found."
    
    response = {
        "name": skill_name,
        "content": {}
    }
    
    # Read SKILL.md
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if os.path.exists(skill_md_path):
        with open(skill_md_path, "r") as f:
            response["content"]["SKILL.md"] = f.read()
            
    # Read README.md if exists
    readme_path = os.path.join(skill_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            response["content"]["README.md"] = f.read()

    return json.dumps(response, indent=2)

@mcp.resource("skill://{skill_name}/instructions")
def skill_instructions(skill_name: str) -> str:
    """Provides direct resource access to a skill's SKILL.md content."""
    print(f"[MCP] 📖 Resource accessed: skill_instructions | requested skill: {skill_name}", flush=True)
    
    path = os.path.join(SKILLS_ROOT, skill_name, "SKILL.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "Skill not found."

if __name__ == "__main__":
    mcp.run()
