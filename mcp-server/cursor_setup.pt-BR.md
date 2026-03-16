# Como usar IA Skills no Cursor

O Cursor pode usar estas habilidades via **MCP (SSE ou Comando Direto)** ou localmente via **.cursorrules**.

## 1. Configuração Global (via MCP) - Recomendado 🚀

### Passo 1: Adicionar Servidor

A configuração do servidor MCP pode ser feita **pela interface** ou **pelo arquivo `mcp.json`**.

#### Opção A: Arquivo de configuração (`mcp.json`)

Crie ou edite o arquivo de configuração MCP:

- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **macOS / Linux**: `~/.cursor\mcp.json`

Exemplo para servidor remoto (HTTP/SSE):

```json
{
  "mcpServers": {
    "is-skills-mcp-server": {
      "url": "http://10.234.10.87:8001/sse"
    }
  }
}
```

Substitua a URL pelo endereço do seu servidor (host e porta onde o MCP está rodando). Reinicie o Cursor ou recarregue a janela após alterar o `mcp.json`.

#### Opção B: Interface de configurações do Cursor

1. Abra as Configurações do Cursor (**Settings > Cursor Settings > Features > MCP**).
2. Clique em **+ Add New MCP Server**.

![Configurações de MCP no Cursor](../images/Cursor%20Tools_MCP.png)

**Para execução local em Python:**
- **Nome**: `ia-skills` (ou outro de sua preferência)
- **Tipo**: `command`
- **Comando**: `python caminho/para/ia_skills/mcp-server/main.py` (use o Python do venv e o caminho completo)

**Para servidor remoto / Docker (SSE):**
- **Nome**: `is-skills-mcp-server` (ou outro nome)
- **Tipo**: `SSE`
- **URL**: `http://<host>:8001/sse` (ex.: `http://10.234.10.87:8001/sse` ou `http://skills-mcp.ia-skills.orb.local/sse`)

### Passo 2: Uso

No Chat (Cmd+L) ou Composer (Cmd+I), use o símbolo `@`:
- Digite `@is-skills-mcp-server` (ou o nome que você configurou) para ver as ferramentas disponíveis.
- Use a ferramenta `list_available_skills` para navegar pelas habilidades do repositório.
- Use `get_skill_manual` para carregar as instruções de uma habilidade específica.

---

## 2. Configuração Local (via Arquivos) 📂

### Opção A: Arquivo .cursorrules
Copie o conteúdo do arquivo `SKILL.md` (ou `SKILL.pt-BR.md`) da habilidade desejada para o arquivo `.cursorrules` do seu projeto. Isso torna as instruções parte do prompt de sistema do Cursor.

### Opção B: Referência Direta (@)
Copie a pasta da skill para seu projeto. Então, no chat ou composer, digite:
- `Leia @caminho/para/SKILL.pt-BR.md e siga as regras dele.`
