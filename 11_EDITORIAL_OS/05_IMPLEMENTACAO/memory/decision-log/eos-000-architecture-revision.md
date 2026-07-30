# Registro de Decisão Arquitetural: Revisão do Master Plan (EOS-000)

**Data:** 2026-07-30
**Autor:** Engenheiro de Arquitetura do Sistema (via prompt)

## Contexto
Durante a auditoria de preparação para o início da fase de implementação, identificou-se uma violação do princípio "Código nasce da documentação" no `02_MASTER_IMPLEMENTATION_PLAN.md`. O roadmap original misturava a elaboração de especificações no documento `04_AGENT_SPECIFICATIONS.md` com as tarefas de geração de artefatos de código, além de apresentar inversão cronológica nas dependências entre Agentes (Fases).

## Decisão
1. **Remoção de Redundâncias:** A elaboração do `04_AGENT_SPECIFICATIONS.md` foi separada da implementação. Todas as tarefas do Backlog Mestre foram retificadas para focar exclusivamente na injeção de contexto na pasta `05_IMPLEMENTACAO`.
2. **Reestruturação das Fases:** O roadmap foi reestruturado para respeitar o pipeline lógico:
   - *Fase 1 (Infraestrutura):* Memory Agent.
   - *Fase 2 (Estratégia):* Research, Curator e Editorial.
   - *Fase 3 (Governança):* Brand Guardian.
   - *Fase 4 (Materialização):* Art Director, Tokens CSS, Templates HTML, Image e Coder/Vision.
   - *Fase 5 (Evolução):* Critic/Metrics.
3. **Inclusão de Agentes:** Adicionados EOS-010 (Memory Agent) e EOS-011 (Coder/Vision Agent) ao Backlog Mestre.

## Impacto
O Master Plan agora dita as regras de materialização na ordem precisa em que o sistema cognitivo evolui da ideia bruta para a materialização final, respeitando a premissa de que infraestrutura e conteúdo antecedem o design estrutural.
