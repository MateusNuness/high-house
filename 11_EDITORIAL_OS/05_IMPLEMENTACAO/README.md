# High House - Editorial OS Implementation

Este repositório contém a execução em código (LangGraph/LangChain) dos agentes definidos na especificação da High House.

## Status do Pipeline
- **EOS-009**: Implementação do Research Agent [CONCLUÍDO]
  - `MarkdownContextLoader` extraindo o contexto diretamente do `04_AGENT_SPECIFICATIONS.md` (Princípio DRY/SSOT garantido).
  - Contrato estrito `ResearchReport` alinhado ao MVP.
  - Testes de aderência culturais (`test_research_agent.py`) e fixtures configurados.
  - LLM Router configurado para rotear o papel de "research".
