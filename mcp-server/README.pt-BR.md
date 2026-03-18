# Skills MCP Server

Leia em inglês: [README.md](README.md)

Este servidor expõe todas as skills no repositório `ia_skills` como ferramentas e recursos via MCP. Assim, qualquer cliente compatível com MCP (como Cursor ou Antigravity) consegue acessar essas skills globalmente.

## 🛠️ Ferramentas
- `list_available_skills`: Lista todas as skills no repositório.
- `get_skill_manual`: Retorna o conteúdo completo de `SKILL.md` e `README.md` de uma skill específica.

## 🏃 Como executar o servidor

Todos os comandos abaixo assumem que você está no **diretório raiz** do repositório (`ia_skills/`).

| Plataforma | Como rodar |
|----------|------------|
| **Windows (local)** | Dê duplo clique ou execute `run-server.bat`. Usa `.venv` ou `mcp-server\.venv` caso existam. |
| **Linux / macOS (Docker)** | `chmod +x run-docker.sh` e depois `./run-docker.sh`. Usa `docker compose` (ou `docker-compose`). |

O servidor atende em **http://0.0.0.0:8001**; o endpoint SSE do MCP é **http://<host>:8001/sse**.

- **Python local**: Instale as dependências com `pip install -r mcp-server/requirements.txt` (recomendado: use um venv no root do repositório ou em `mcp-server/`).
- **Docker**: Veja `docker-compose.yml` e `Dockerfile` no root do repositório.

## 🚀 Configuração

### 1. Antigravity (Gemini Code Assistant)

A configuração fica em `~/.gemini/antigravity/mcp_config.json`.

#### Opção A: Local (direto)

Use quando o servidor está na mesma máquina:

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

#### Opção B: Remoto / OrbStack (via bridge)

Se o servidor estiver em um container ou uma URL remota (como `skills-mcp.ia-skills.orb.local`), use a bridge `mcp-proxy` para compatibilidade:

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

Para usar essas skills no Cursor, vá em **Settings > Cursor Settings > Features > MCP**.

#### Opção A: Local (command)
- **Name**: `skills-mcp`
- **Type**: `command`
- **Command**: `/Users/dms/Documents/source/ia_skills/mcp-server/.venv/bin/python /Users/dms/Documents/source/ia_skills/mcp-server/main.py`

#### Opção B: Remoto (SSE)
- **Name**: `skills-mcp`
- **Type**: `SSE`
- **URL**: `http://skills-mcp.ia-skills.orb.local/sse`

---

### 3. Usando Docker

A partir do **root do repositório**, execute o script fornecido ou o docker compose diretamente:

```bash
./run-docker.sh
```

Ou manualmente:

```bash
docker compose up -d --build
```

O nome do container é `skills-mcp`; logs: `docker compose logs -f skills-mcp`. O repositório é montado no container para que mudanças nas skills reflitam sem precisar rebuildar.

## 📖 Por que usar?

Em vez de copiar `.agents/skills` ou `.cursorrules` para cada novo projeto, você pode simplesmente dizer para a IA:
*"Use a skill django-audit do meu MCP server para revisar este projeto."*

A IA vai chamar `get_skill_manual`, ler as instruções e aplicar tudo imediatamente no seu workspace atual.

