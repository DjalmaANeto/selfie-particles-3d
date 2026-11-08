# Skill de Criação de Cards (Multi-LLM Guide)

## O que é?
O **Criacao de Cards** é um guia agnóstico de LLM desenvolvido para padronizar rigorosamente a criação de cartões no Trello para os projetos da Mult, utilizando como referência o modelo de Franco da Rocha, letras maiúsculas, cores/etiquetas por município e checklists estruturados.

## Como implementar em outras LLMs (Copilot, Gemini, Claude Code)

### 1. GitHub Copilot (`.github/copilot-instructions.md`)
Adicione as regras de padronização visual, títulos em maiúsculas e etiquetas por município no arquivo de instruções do Copilot. O Copilot garantirá que sugestões de criação de cards ou issues sigam o padrão Mult.

### 2. Claude Code (`CLAUDE.md` ou system prompt)
Insira as diretrizes do modelo de Franco da Rocha e formatação de títulos no arquivo `CLAUDE.md`. O Claude seguirá estritamente as regras de consistência ao gerar artefatos de gerenciamento de projetos.

### 3. Gemini CLI (`.gemini/skills/criacao-cards/SKILL.md`)
Esta skill já está nativamente instalada neste repositório. Quando ativada, ela aplica as regras de governança para a criação de cartões.
