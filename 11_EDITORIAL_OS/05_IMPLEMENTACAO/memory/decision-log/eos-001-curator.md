# Registro de Decisão Arquitetural: Implementação do Curator Agent (EOS-001)

**Data:** 2026-07-30
**Autor:** Engenheiro de Arquitetura do Sistema (via prompt)

## Contexto
O Curator Agent (Fase 2 - Conhecimento e Estratégia) é responsável por atuar como funil crítico do "Raw Research Package", garantindo que a High House não publique conteúdos rasos, corporativos ou baseados em "marketing digital". Sua implementação deve materializar as especificações definidas em `04_AGENT_SPECIFICATIONS.md` e espelhar o DNA estabelecido nos documentos fundacionais (01, 03.1 e `brand-essence.md`).

## Decisão
As diretrizes de curadoria (`curation-guidelines.md`) foram refatoradas e estritamente atreladas a três regras fundamentais de exclusão:
1. **O Teste do Óbvio:** Rejeição imediata de didatismo exagerado, modismos de redes sociais (TikTok/Instagram) e linguagens genéricas.
2. **A Regra da Densidade:** O conteúdo aprovado deve ser estruturalmente denso para harmonizar com a tipografia colossal e o "Horror ao Preenchimento" estipulado no Design System (`03.1_DESIGN_SYSTEM_SPECIFICATION.md`). Sem redundâncias, apenas tensão pura.
3. **Anti-patterns (Blindagem Cultural):** Foi cravada a proibição de uso de linguagem corporativa e de clichês canábicos (ex: "vibe stoner", "larica"), forçando o conteúdo para a contemplação e o *flow* ("Ausência do Tempo").

## Impacto
O Curator Agent agora possui um "Curation Guideline" em código que reflete 100% da identidade atual da marca, servindo como o artefato oficial para injetar prompt e contexto limitador neste agente, bloqueando vazamentos semânticos antes mesmo de alcançarem o Editorial Agent.
