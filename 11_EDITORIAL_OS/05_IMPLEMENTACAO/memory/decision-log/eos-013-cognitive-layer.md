# Decision Log: EOS-013 — Criação da Camada Cognitiva antes da implementação dos agentes

**Date:** 2026-07-30  
**Context:** Etapa pré-código (Pausa estratégica).  
**Status:** Approved by Architecture Gate.

## A Decisão

Após o provisionamento físico do motor base do LangGraph (EOS-012), optou-se por **interromper a codificação de agentes reais em Python** para forçar a criação da "Camada Cognitiva" do sistema em Markdown.

## Motivação

Se a infraestrutura gerasse classes Pydantic e grafos imediatamente, os agentes operariam como IAs genéricas de "chat", trocando strings aleatórias. A IA não saberia *como a marca High House pensa*. 
Foi diagnosticado o risco crítico de "desacoplamento cognitivo": o código estava rápido demais, e a "alma" da marca ainda estava abstrata demais.

## Ações Executadas

1. **`04.2_COGNITIVE_WORKFLOWS.md`:** Criado para definir o modelo mental.
   - Decisão-chave: Agentes não trocam mensagens, eles produzem e analisam **Artefatos Versionáveis** (ex: `ResearchReport`, `VisualProposal`).
   - Decisão-chave: O Brand Guardian perdeu temporariamente o poder de *Veto Silencioso*. Na fase inicial da marca, qualquer rejeição do Guardian escalará para um *Human-in-the-loop* avaliar o reporte técnico.
   - Definido o fluxo MVP cognitivo: "Xarpi Carioca".
2. **`04.1_AGENT_OPERATIONAL_CONTRACTS.md`:** Criado para estruturar o Input/Output exato. Define quais chaves existirão nos futuros Pydantic Models, transformando intenção filosófica em tipos de dados.
3. **`04_AGENT_SPECIFICATIONS.md`:** Revisado para remover últimos vestígios da palavra "Premium" na avaliação do Guardian, alinhando com a evolução para "Design Cultural Underground".
