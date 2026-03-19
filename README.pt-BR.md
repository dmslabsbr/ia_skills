# AI Coding Skills 🚀

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Antigravity](https://img.shields.io/badge/Antigravity-Gemini-blue?style=flat) ![MCP Server](https://img.shields.io/badge/MCP-Server-4285F4?style=flat) ![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat) ![Version](https://img.shields.io/badge/version-1.0.3-blue?style=flat)

Leia em inglês: [README.md](README.md)

Coleção curada de skills para assistentes de programação (**Antigravity**, **Cursor**). Inclui fluxos de trabalho especializados e um servidor MCP global que expõe todas as skills via tools e prompts.

## 📂 Skills Disponíveis

- **[📱 Android Expert](./android-expert)**: Java/Kotlin, Material Design 3, Firebase e boas práticas para Play Store.
- **[✅ Code Review Standards](./code-review-standards)**: PEP 8, type hints, Docker, testes e checklist de qualidade.
- **[📊 ClickUp Group Progress](./clickup-group-progress)**: Acompanhar e planejar qualquer grupo/projeto no ClickUp (genérico; usuário informa o grupo).
- **[📊 ClickUp Nexus Progress](./clickup-nexus-progress)**: Acompanhar andamento e planejamento do Nexus no ClickUp.
- **[🎨 Dashboard Cloner](./dashboard-cloner)**: Análise de UI/UX a partir de screenshots; design tokens e briefs de implementação.
- **[🐍 Django Audit](./django-audit)**: Auditoria de segurança, arquitetura, performance e qualidade para apps Django.
- **[🐙 Git Platforms Expert](./git-platforms-expert)**: Fluxos GitHub/GitLab, CI/CD, commits e Git multiplataforma.
- **[🏗️ New App Bootstrap](./new-app-bootstrap)**: README, VERSION, Docker, diagrama ER, testes e scaffold do projeto.
- **[📋 Phase Execution](./phase-execution)**: Entrega em cinco fases (análise, planejamento, implementação, validação, entrega).
- **[🌍 README Bilíngue](./readme-bilingual)**: READMEs duais (EN + pt-BR) com badges e links cruzados para GitHub.
- **[📝 Technical Documentation](./technical-documentation)**: `analise.md` e `plano.md` estruturados para discussões técnicas.
- **[🔄 Update Funcoes.md](./update-funcoes-md)**: Manter `funcoes.md` atualizado quando funções forem criadas, alteradas ou removidas.

## 🛠️ Servidor MCP (skills-mcp)

O servidor expõe **tools** e **prompts** para que qualquer cliente MCP use as skills sem copiar arquivos.

| Tipo    | Exemplos |
|---------|----------|
| **Tools** | `list_available_skills`, `get_skill_manual`, `get_app_version` |
| **Prompts** | `usar-<skill>` (ex.: `usar-readme-bilingual`), `analisar-skills-disponiveis` |
| **Resource** | `skill://{skill_name}/instructions` (conteúdo do SKILL.md) |

Uma **homepage** leve em `http://<host>:8001/` exibe versão, lista de skills e log recente (atualização automática a cada 10s).

## 🚀 Como Começar

### 1. Global (MCP) – Recomendado

Rode o servidor MCP para que o assistente use as skills em qualquer projeto.

- **Windows (local)**: Na raiz do repositório, execute `run-server.bat` (servidor em `http://localhost:8001/sse`).
- **Linux / macOS (Docker)**: Na raiz do repositório, execute `./run-docker.sh` (uma vez: `chmod +x run-docker.sh`).

**Configurar o cliente:**

- **Antigravity**: [English](./mcp-server/antigravity_setup.md) \| [Português](./mcp-server/antigravity_setup.pt-BR.md)
- **Cursor**: [English](./mcp-server/cursor_setup.md) \| [Português](./mcp-server/cursor_setup.pt-BR.md)

### 2. Local (Cópia manual)

- Copie a pasta da skill para `.agents/skills/` (Antigravity) ou use em `.cursorrules` (Cursor).

Para detalhes do servidor e opções de execução, veja [README do mcp-server](./mcp-server/README.md).

## 📷 Screenshots

| Dashboard (homepage) | Servidores MCP no Cursor |
|----------------------|--------------------------|
| ![Homepage Skills MCP](images/Dashboard_mcp_server.JPG) | ![Servidores MCP no Cursor](images/Cursor_instaled_mcp_servers.JPG) |

| Uso de um prompt de skill (ex.: readme-bilingual) |
|----------------------------------------------------|
| ![Uso de um prompt de skill no chat](images/skill_use_example.JPG) |

## ☕ Apoie o projeto

Se este projeto te ajuda, considere apoiar o desenvolvimento:

- **[Buy Me a Coffee](https://buymeacoffee.com/dmslabs)**
- **Bitcoin (BTC)**: [1MAC9RBnPYT9ua1zsgvhwfRoASTBKr4QL8](https://www.blockchain.com/btc/address/1MAC9RBnPYT9ua1zsgvhwfRoASTBKr4QL8)

## Licença

[MIT](LICENSE)
