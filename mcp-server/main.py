import os
import json
import re
import html
from collections import deque
from datetime import datetime, timezone
from threading import Lock
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from starlette.requests import Request
from starlette.responses import HTMLResponse

# Initialize FastMCP server
# host and port are configured here for SSE transport
mcp = FastMCP("skills_mcp", host="0.0.0.0", port=8001)

# Path to the skills repository
SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_ROOT_RESOLVED = os.path.realpath(SKILLS_ROOT)


def _resolve_skill_dir(skill_name: str) -> str | None:
    """
    Resolve skill directory path and ensure it stays inside SKILLS_ROOT (path traversal safe).
    Returns the resolved absolute path if valid, None otherwise.
    """
    if not skill_name or skill_name.strip() != skill_name:
        return None
    # Avoid path traversal: join then resolve and ensure under SKILLS_ROOT
    candidate = os.path.join(SKILLS_ROOT, skill_name)
    resolved = os.path.realpath(candidate)
    if not resolved.startswith(SKILLS_ROOT_RESOLVED + os.sep) and resolved != SKILLS_ROOT_RESOLVED:
        return None
    return resolved


SKILL_PROMPT_PREFIX = "usar"
SKILLS_DISCOVERY_SKIP_DIRS = {".git", ".gemini", "mcp-server", "brain", ".agents", "node_modules"}

_EVENT_LOG_MAXLEN = 60
_EVENT_LOG: deque[str] = deque(maxlen=_EVENT_LOG_MAXLEN)
_EVENT_LOG_LOCK = Lock()


def _log_event(message: str) -> None:
    """Adds a lightweight in-memory log for the homepage."""
    try:
        ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
        line = f"[{ts}] {message}"
        with _EVENT_LOG_LOCK:
            _EVENT_LOG.appendleft(line)
    except Exception:
        # Never break the MCP server due to logging.
        return


def _read_text_file(path: str) -> str:
    """Reads a UTF-8 text file and returns its content."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _extract_frontmatter_fields(skill_md_content: str) -> Dict[str, str]:
    """
    Extracts YAML-like frontmatter fields (e.g. `name:` and `description:`).

    This uses a minimal parser to avoid adding dependencies.
    """
    lines = skill_md_content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return {}

    fields: Dict[str, str] = {}
    for line in lines[1:end_idx]:
        match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)\s*$", line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            fields[key] = value
    return fields


def _extract_first_heading_after_frontmatter(skill_md_content: str) -> str | None:
    """Extracts the first markdown heading after the frontmatter block."""
    lines = skill_md_content.splitlines()
    if not lines or lines[0].strip() != "---":
        for line in lines:
            if line.startswith("# "):
                return line[2:].strip() or None
        return None

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None

    for line in lines[end_idx + 1 :]:
        if line.startswith("# "):
            return line[2:].strip() or None
    return None


def _discover_skills_with_metadata() -> List[Dict[str, str]]:
    """Discovers skill directories (containing SKILL.md) and extracts metadata."""
    skills: List[Dict[str, str]] = []
    try:
        items = os.listdir(SKILLS_ROOT)
    except OSError:
        return skills

    for item in items:
        if item in SKILLS_DISCOVERY_SKIP_DIRS:
            continue
        item_path = os.path.join(SKILLS_ROOT, item)
        if not os.path.isdir(item_path):
            continue

        skill_md_path = os.path.join(item_path, "SKILL.md")
        if not os.path.exists(skill_md_path):
            continue

        try:
            content = _read_text_file(skill_md_path)
        except OSError:
            continue

        fields = _extract_frontmatter_fields(content)
        skill_name = fields.get("name", item)
        description = fields.get("description", "").strip()
        heading = _extract_first_heading_after_frontmatter(content) or ""

        skills.append(
            {
                "skill_dir_name": item,
                "skill_name": skill_name,
                "description": description,
                "heading": heading,
            }
        )

    return skills


_SKILLS_METADATA_CACHE: List[Dict[str, str]] = _discover_skills_with_metadata()


def _build_skill_prompt(skill_dir_name: str, skill_name: str, description: str, heading: str) -> str:
    """Builds a consistent 'use this skill' prompt for humans and LLMs."""
    description_line = description or "Sem descrição adicional no SKILL.md."
    heading_line = f"Título: {heading}." if heading else ""

    return f"""Você pode usar a skill `{skill_dir_name}` via MCP.

Descrição: {description_line}
{heading_line}

Instruções de uso (para o agente/LLM e para o usuário humano):
1. Chame a tool `get_skill_manual` com `skill_name="{skill_dir_name}"` para obter as instruções completas (SKILL.md e README.md, quando existir).
2. Aplique as regras de saída exatamente como definido no manual (formato, seções e restrições).
3. Se o pedido do usuário for ambíguo ou envolver risco/ações destrutivas, faça 1-2 perguntas antes de executar.
4. Responda na mesma língua do usuário (quando o manual mencionar “Language Note”, siga esse requisito).
"""


def _register_skill_prompts() -> None:
    """Registers a prompt for each discovered skill at startup."""
    for skill in _SKILLS_METADATA_CACHE:
        skill_dir_name = skill["skill_dir_name"]
        skill_name = skill["skill_name"]
        description = skill["description"]
        heading = skill["heading"]

        prompt_name = f"{SKILL_PROMPT_PREFIX}-{skill_dir_name}"
        prompt_text = _build_skill_prompt(
            skill_dir_name=skill_dir_name,
            skill_name=skill_name,
            description=description,
            heading=heading,
        )

        # Use a factory to avoid late binding issues inside loops.
        def _make_handler(text: str, short_description: str):
            def _handler() -> str:
                return text

            # The Cursor UI typically reads function docstrings as the short description.
            _handler.__doc__ = short_description
            return _handler

        short_description = description or heading or f"Use a skill `{skill_dir_name}` via MCP."
        mcp.prompt(prompt_name)(_make_handler(prompt_text, short_description))


# --- PROMPTS (Atalhos de comando) ---

@mcp.prompt("analisar-skills-disponiveis")
def analisar_skills() -> str:
    """Cria um guia rápido das habilidades instaladas e sugere as melhores para o projeto."""
    return """Por favor, execute os seguintes passos:
1. Use a ferramenta 'list_available_skills' para ver o que temos no repositório.
2. Com base no código que estamos editando neste projeto do Cursor, identifique quais 2 ou 3 skills seriam mais úteis agora.
3. Para essas selecionadas, use 'get_skill_manual' para ler o SKILL.md delas.
4. Faça um resumo curto de como cada uma pode me ajudar neste arquivo específico."""


_register_skill_prompts()

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
    _log_event("tool:list_available_skills")
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
    _log_event(f"tool:get_skill_manual skill={skill_name}")
    
    skill_dir = _resolve_skill_dir(skill_name)
    if skill_dir is None or not os.path.isdir(skill_dir):
        return f"Error: Skill '{skill_name}' not found."
    
    response = {
        "name": skill_name,
        "content": {}
    }
    
    # Read SKILL.md
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if os.path.exists(skill_md_path):
        with open(skill_md_path, "r", encoding="utf-8") as f:
            response["content"]["SKILL.md"] = f.read()
            
    # Read README.md if exists
    readme_path = os.path.join(skill_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            response["content"]["README.md"] = f.read()

    return json.dumps(response, indent=2)

@mcp.resource("skill://{skill_name}/instructions")
def skill_instructions(skill_name: str) -> str:
    """Provides direct resource access to a skill's SKILL.md content."""
    print(f"[MCP] 📖 Resource accessed: skill_instructions | requested skill: {skill_name}", flush=True)
    _log_event(f"resource:skill_instructions skill={skill_name}")
    
    skill_dir = _resolve_skill_dir(skill_name)
    if skill_dir is None or not os.path.isdir(skill_dir):
        return "Skill not found."
    path = os.path.join(skill_dir, "SKILL.md")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "Skill not found."


@mcp.custom_route("/", methods=["GET"])
async def home_page(request: Request) -> HTMLResponse:
    """Public lightweight homepage showing key skills and recent MCP activity."""
    client_host = getattr(getattr(request, "client", None), "host", None) or "unknown"
    skills = _SKILLS_METADATA_CACHE
    total_skills = len(skills)
    last_events = list(_EVENT_LOG)[:12]

    def _short(text: str, limit: int = 90) -> str:
        text = text or ""
        if len(text) <= limit:
            return text
        return text[: limit - 1] + "…"

    skills_items = "".join(
        f"<li><code>{html.escape(s['skill_dir_name'])}</code> - {html.escape(_short(s.get('description') or s.get('heading') or '', 120))}</li>"
        for s in skills[:10]
    )

    events_items = "".join(f"<li>{html.escape(e)}</li>" for e in last_events)

    html_body = f"""
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>skills-mcp</title>
  <style>
    :root{{--bg:#0b1020;--card:#121a33;--text:#e8ecff;--muted:#aeb7e6;--accent:#67e8f9;}}
    body{{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial; background:linear-gradient(180deg,#070a14 0%, var(--bg) 100%); color:var(--text);}}
    .wrap{{max-width:980px; margin:0 auto; padding:28px 16px;}}
    .hero{{background:radial-gradient(900px 200px at 10% 0%, rgba(103,232,249,.18), transparent 60%), linear-gradient(180deg, rgba(18,26,51,.9), rgba(18,26,51,.65)); border:1px solid rgba(103,232,249,.22); border-radius:16px; padding:18px 18px 14px;}}
    h1{{margin:0 0 6px; font-size:20px; letter-spacing:.2px;}}
    .sub{{color:var(--muted); margin:0 0 12px; font-size:13px;}}
    .grid{{display:grid; gap:12px; grid-template-columns: 1.25fr .75fr; margin-top:14px;}}
    @media (max-width: 860px) {{ .grid{{grid-template-columns:1fr;}} }}
    .card{{background:rgba(18,26,51,.55); border:1px solid rgba(255,255,255,.06); border-radius:14px; padding:14px;}}
    code{{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;}}
    a{{color:var(--accent); text-decoration:none;}}
    a:hover{{text-decoration:underline;}}
    ul{{margin:10px 0 0; padding:0; list-style:none;}}
    li{{padding:6px 0; border-bottom:1px dashed rgba(255,255,255,.08); font-size:13px;}}
    li:last-child{{border-bottom:none;}}
    .pill{{display:inline-block; padding:6px 10px; border-radius:999px; border:1px solid rgba(103,232,249,.25); color:var(--accent); font-size:12px;}}
    .small{{color:var(--muted); font-size:12px;}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <h1>skills-mcp</h1>
      <p class="sub">Página pública (leve) para visualizar skills e o log recente do servidor MCP.</p>
      <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
        <span class="pill">{total_skills} skills detectadas</span>
        <span class="small">Cliente: {html.escape(str(client_host))}</span>
      </div>
      <div style="margin-top:10px" class="small">
        Repo: <a href="https://github.com/dmslabsbr/ia_skills" target="_blank" rel="noreferrer">github.com/dmslabsbr/ia_skills</a>
        · MCP SSE: <code>/sse</code> (porta <code>8001</code>)
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <div><b>Skills (amostra)</b> <span class="small">- últimos metadados carregados no boot</span></div>
        <ul>
          {skills_items if skills_items else "<li>Nenhuma skill encontrada (verifique SKILL.md na raiz).</li>"}
        </ul>
        <div class="small" style="margin-top:10px">
          Use a tool <code>list_available_skills</code> para a lista completa.
        </div>
      </div>

      <div class="card">
        <div><b>Log recente</b> <span class="small">- chamadas de tools/resources</span></div>
        <ul>
          {events_items if events_items else "<li>Sem eventos recentes.</li>"}
        </ul>
        <div class="small" style="margin-top:10px">
          Atualiza a cada requisição (página simples para baixo consumo).
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

    return HTMLResponse(content=html_body)


if __name__ == "__main__":
    # mcp.run()
    mcp.run(transport="sse")