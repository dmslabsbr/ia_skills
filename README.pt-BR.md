# AI Coding Skills 🚀

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Claude Code](https://img.shields.io/badge/Claude-Code-d97757?style=flat) ![MCP Server](https://img.shields.io/badge/MCP-Server-4285F4?style=flat) ![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat)

Leia em inglês: [README.md](README.md)

Uma coleção curada de skills especializadas, projetadas para turbinar assistentes modernos de codificação (como Antigravity, Cursor e Claude Code). Este repositório fornece fluxos de trabalho avançados, prompts de sistema e um servidor Model Context Protocol (MCP) global para expandir instantaneamente a capacidade técnica do seu agente em qualquer projeto.

## 📂 Skills Disponíveis

- **[📱 Android Expert](./android-expert)**: Melhores práticas para desenvolvimento Android com Java/Kotlin, Material Design, Firebase e publicação na Google Play Store.
- **[✅ Code Review Standards](./code-review-standards)**: Revisões de qualidade, segurança e padrões de projeto englobando PEP 8, type hints, Docker e testes integrados.
- **[🎨 Dashboard Cloner](./dashboard-cloner)**: Análise profunda de UI/UX a partir de referências visuais para extrair design tokens, layouts e comportamento responsivo.
- **[🐍 Django Audit](./django-audit)**: Auditoria técnica profunda para aplicações Django com foco em segurança, arquitetura, performance e qualidade de código.
- **[🐙 Git Platforms Expert](./git-platforms-expert)**: Fluxos de trabalho no GitHub/GitLab, estratégias de branch, pipelines CI/CD e geração de mensagens de commit semânticas e padronizadas.
- **[🏗️ New App Bootstrap](./new-app-bootstrap)**: Estruturação inicial (scaffolding) rápida para novas aplicações incluindo setup de testes, diagramas ER e Docker.
- **[📋 Phase Execution](./phase-execution)**: Metodologia de entrega de projetos estruturada em 5 fases (análise, planejamento, implementação, validação, entrega) embasadas por checklists de qualidade.
- **[🌍 README Bilíngue](./readme-bilingual)**: Criação e manutenção automatizada de documentação dual-language amigável para a página inicial do GitHub.
- **[📝 Technical Documentation](./technical-documentation)**: Criação e padronização da documentação base do ciclo de vida em arquivos analise.md e plano.md.
- **[🔄 Update Funcoes.md](./update-funcoes-md)**: Rastreamento automatizado da criação, alteração ou exclusão de funções diretamente num diário do projeto em funcoes.md.

## 🚀 Instalação e Uso

### 1. Servidor MCP Global (Recomendado)
A maneira mais poderosa de usar este repositório é rodando o servidor MCP incluso. Isso garante às suas IAs acesso instantâneo e global a todas as skills.

**Via Docker:**
```bash
docker-compose up -d --build
```
*Em seguida, adicione o cliente SSE na sua IDE (Cursor/Antigravity) apontando para `http://localhost:8001/sse`.*

### 2. Configuração Local (Links Simbólicos)
Se preferir adicionar skills individualmente por projeto:
```bash
mkdir -p .agents/skills
ln -s /caminho/para/ia_skills/django-audit $(pwd)/.agents/skills/django-audit
```

### 3. Regras no Cursor
Para uso rápido no Cursor, basta mencionar o arquivo da skill no seu prompt (ex: `@django-audit/SKILL.md`) ou colar o conteúdo no seu arquivo `.cursorrules`.

## 🤝 Contribuindo
Sinta-se à vontade para adicionar novas skills ou melhorar as existentes. Certifique-se de que suas contribuições incluam os formatos `SKILL.md` (Inglês) e `SKILL.pt-BR.md` (Português).
