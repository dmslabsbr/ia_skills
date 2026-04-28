---
name: ia-skills
description: A curated collection of specialized AI coding skills and a global MCP server. Use when you need expert assistance for specific domains (Android, Django, Git) or when managing AI agent workflows.
version: 1.0.3
author: dmslabs
---

# IA Skills

A comprehensive repository of specialized workflows, prompts, and tools designed for modern AI coding assistants like **Antigravity** and **Cursor**. This project serves as a central hub for various "skills" that can be activated to provide expert assistance across multiple technical domains.

## Overview

IA Skills (AI Coding Skills) provides a unified interface to a diverse set of expert knowledge bases and automation scripts. It includes a global **MCP Server** (`skills-mcp`) that exposes these skills as tools and prompts, making them instantly accessible across different projects and AI clients without manual configuration.

## When to use

- **Specialized Development**: When working on specific platforms or frameworks (e.g., Android Expert, Django Audit, Python development).
- **Workflow Standardization**: When you need to follow consistent processes like code reviews, phase-based execution, or technical documentation.
- **Task Automation**: When automating repetitive repository maintenance tasks like updating `funcoes.md`, versioning, or generating bilingual READMEs.
- **Skill Discovery**: When you want to explore and implement expert behaviors and best practices in your AI assistant's workflow.

## Instructions

1. **Discovery**: Use the `list_available_skills` tool to retrieve a complete list of all installed skills within this repository.
2. **Skill Details**: For any specific skill (e.g., `django-audit`), use the `get_skill_manual(skill_name)` tool to read its detailed instructions and operational requirements.
3. **Execution**: Trigger skills by using their specific keywords in your chat or by explicitly asking the agent to use a certain skill (e.g., "Use readme-bilingual to update documentation").
4. **Setup & Maintenance**: Refer to the root `README.md` and the `mcp-server/` directory for installation guides (Docker, local scripts) and configuration for various AI clients.
5. **Version Management**: Check the `VERSION` file or use `get_app_version` to ensure you are using the latest release of the skills collection.

## Available Skills (Highlights)

- **[📱 Android Expert](./android-expert)**: Java/Kotlin expertise, Material Design 3, and Play Store standards.
- **[🐍 Django Audit](./django-audit)**: Deep audits for security, architecture, and performance.
- **[🌍 README Bilingual](./readme-bilingual)**: Automated English and Portuguese documentation with cross-links.
- **[📋 Phase Execution](./phase-execution)**: A structured 5-phase delivery process for complex tasks.
- **[🐙 Git Platforms Expert](./git-platforms-expert)**: Advanced GitHub/GitLab workflows and CI/CD integration.
- **[🏗️ New App Bootstrap](./new-app-bootstrap)**: Rapid project scaffolding with tests, Docker, and documentation.

## Output Format

When interacting with these skills:
- Maintain a professional, direct, and expert tone.
- Provide links to relevant subdirectories for further reading.
- Clearly state which tools or prompts are being utilized to solve the user's request.

## Notes & Guardrails

- **MCP Connectivity**: Ensure the `skills-mcp` server is running and connected to your AI client to enable real-time tool access.
- **Skill Consistency**: When adding or updating skills, ensure the `SKILL.md` follows the progressive disclosure pattern (metadata + instructions).
- **Safety**: Always verify system commands or scripts within specialized folders before execution.
