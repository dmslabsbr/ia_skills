# Como usar IA Skills no Antigravity

O Antigravity (agente baseado no Gemini) pode consumir estas habilidades globalmente via **MCP** ou localmente via **cópia de pastas**.

## 1. Configuração Global (via MCP) - Recomendado 🚀

Esta é a forma mais eficiente. Você configura uma vez e o assistente pode puxar qualquer skill para qualquer projeto.

### Passo 1: Configuração
Edite seu arquivo de configuração do Antigravity em `~/.gemini/antigravity/mcp_config.json`.

![Exemplo de Configuração JSON](../images/Antigravity%20mcp_config.png)

**Se estiver rodando o servidor localmente:**
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

![Localização das Configurações](../images/Antigravity%20settings.png)


**Se estiver usando a URL do OrbStack/Docker (via Bridge):**
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

### Passo 2: Uso
Uma vez configurado, você pode simplesmente perguntar ao Antigravity:
- *"Liste minhas skills disponíveis."*
- *"Use a skill django-audit para analisar este arquivo."*
- *"Quais skills eu tenho para gerenciamento de projeto?"*

![Gerenciar Servidores MCP](../images/Antigravity%20Manage%20MCP%20servers.png)

---

## 2. Configuração Local (Cópia Manual) 📂

Use isto se quiser que skills específicas vivam dentro do repositório do projeto ou se estiver offline.

### Passo 1: Copiar a Pasta
Copie a pasta da skill desejada (ex: `django-audit`) para dentro do seu projeto no diretório `.agents/skills/`.

### Passo 2: Uso
O Antigravity escaneia automaticamente a pasta `.agents/`. Você pode referenciar as instruções diretamente ou pedir:
- *"Leia as instruções em .agents/skills/django-audit/SKILL.md e aplique-as."*
