# Como usar IA Skills no Cursor

O Cursor pode usar estas habilidades via **MCP (SSE ou Comando Direto)** ou localmente via **.cursorrules**.

## 1. Configuração Global (via MCP) - Recomendado 🚀

### Passo 1: Adicionar Servidor
1. Abra as Configurações do Cursor (**Settings > Cursor Settings > Features > MCP**).
2. Clique em **+ Add New MCP Server**.

![Configurações de MCP no Cursor](../images/Cursor%20Tools_MCP.png)

**Para Execução Local Python:**
- **Nome**: `ia-skills`
- **Tipo**: `command`
- **Comando**: `/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python /Users/dms/Documents/source/ia_skills/mcp-server/main.py`

**Para OrbStack/Docker (SSE):**
- **Nome**: `ia-skills`
- **Tipo**: `SSE`
- **URL**: `http://skills-mcp.ia-skills.orb.local/sse`

### Passo 2: Uso
No Chat (Cmd+L) ou Composer (Cmd+I), use o símbolo `@`:
- Digite `@ia-skills` para ver os métodos disponíveis do servidor.
- Use a ferramenta `list_available_skills` para navegar pelas habilidades do repositório.
- Use `get_skill_manual` para carregar as instruções de uma habilidade específica.

---

## 2. Configuração Local (via Arquivos) 📂

### Opção A: Arquivo .cursorrules
Copie o conteúdo do arquivo `SKILL.md` (ou `SKILL.pt-BR.md`) da habilidade desejada para o arquivo `.cursorrules` do seu projeto. Isso torna as instruções parte do prompt de sistema do Cursor.

### Opção B: Referência Direta (@)
Copie a pasta da skill para seu projeto. Então, no chat ou composer, digite:
- `Leia @caminho/para/SKILL.pt-BR.md e siga as regras dele.`
