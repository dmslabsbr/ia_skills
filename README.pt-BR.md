# AI Coding Skills 🚀 (Português)

Bem-vindo à coleção de skills especializadas para assistentes de codificação de IA modernos. Estas skills foram desenvolvidas para estender as capacidades de ferramentas como **Antigravity**, **Cursor** e **Claude Code**, fornecendo-lhes conhecimento de nível especialista e fluxos de trabalho estruturados.

## 🛠️ Ferramentas Integradas

Este repositório está otimizado para:

- **Antigravity**: Estas skills seguem a especificação oficial `SKILL.md`. O Antigravity pode descobrir e usar automaticamente estas skills para realizar tarefas complexas com alta precisão.
- **Cursor**: Você pode usar estes arquivos como referência em suas sessões de "Chat" ou "Composer", ou integrá-los ao seu `.cursorrules` para definir comportamentos persistentes no projeto.
- **Claude Code**: Use estes arquivos como contexto ou copie o conteúdo para suas instruções de projeto para guiar o comportamento do Claude durante tarefas técnicas profundas.

---

## 📂 Skills Disponíveis

### 🐍 Django Audit
**Auditoria técnica completa para aplicações Django.**
- **Foco**: Segurança (vulnerabilidades), Arquitetura (boas práticas), Performance (N+1 queries) e Qualidade de Código.
- **Entrega**: Relatórios detalhados com níveis de severidade e planos de correção acionáveis.
- **Localização**: [`/django-audit`](./django-audit)

### 🎨 Dashboard Cloner
**Análise profunda de UI/UX a partir de referências visuais.**
- **Foco**: Extração de design tokens, estruturas de layout, tipografia e comportamento responsivo.
- **Entrega**: Análise estruturada em JSONC e um Developer Brief (briefing para o desenvolvedor) de alta fidelidade.
- **Localização**: [`/dashboard-cloner`](./dashboard-cloner)

---

## 🚀 Como Usar

### No Antigravity
O Antigravity detecta automaticamente as skills no workspace. Basta pedir à IA para realizar uma ação relacionada à skill (ex: *"Faça uma auditoria de segurança no meu app Django"*), e ela usará os padrões definidos.

### No Cursor
1. Pressione `Cmd+K` ou `Cmd+L`.
2. Referencie o arquivo da skill usando `@SKILL.md` (ex: `@django-audit/SKILL.md`).
3. Instrua o Cursor: *"Use as instruções deste arquivo para analisar meu código."*

### No Claude Code
Adicione a skill ao seu contexto ou prompt de projeto:
```bash
claude "Analise meu projeto Django usando os padrões em /path/to/django-audit/SKILL.md"
```

---

## 🌐 Suporte a Idiomas

Todas as skills estão disponíveis em **Inglês** e **Português (pt-BR)**. A IA responderá automaticamente no idioma que você utilizar.

- Documentação: `README.md` / `README.pt-BR.md`
- Definições da Skill: `SKILL.md` / `SKILL.pt-BR.md`

---

*Curado com ❤️ para a comunidade de coding de IA.*
