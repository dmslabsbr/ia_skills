import os
import json
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize FastMCP server
mcp = FastMCP("skills_mcp")

# Path to the skills repository
SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SkillIdentifier(BaseModel):
    skill_name: str = Field(..., description="The directory name of the skill (e.g., 'django-audit')")

@mcp.tool(
    name="list_available_skills",
    annotations={"readOnlyHint": True}
)
async def list_available_skills() -> str:
    """Lists all skills installed in the skills-claude repository."""
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
async def get_skill_manual(params: SkillIdentifier) -> str:
    """Retrieves the full instructions (SKILL.md) and documentation for a specific skill."""
    skill_dir = os.path.join(SKILLS_ROOT, params.skill_name)
    
    if not os.path.exists(skill_dir):
        return f"Error: Skill '{params.skill_name}' not found."
    
    response = {
        "name": params.skill_name,
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
    path = os.path.join(SKILLS_ROOT, skill_name, "SKILL.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "Skill not found."

if __name__ == "__main__":
    mcp.run()
