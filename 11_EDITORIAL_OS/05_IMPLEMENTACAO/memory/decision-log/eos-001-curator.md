# Registro de Decisão Arquitetural: Implementação do Curator Agent (EOS-001)

**Data:** 2026-07-30
**Autor:** Engenheiro de Arquitetura do Sistema (via prompt)

## Contexto
O Curator Agent (Fase 2 - Conhecimento e Estratégia) é o responsável por atuar como funil crítico do `raw_research`. Sua implementação documental (O Prompt/Regras) precisava ser consolidada dentro da pasta `05_IMPLEMENTACAO/agents/curator/` aplicando a diretriz de versionamento como código-fonte (`prompt_version`) e espelhando inteiramente as Fases de 01 a 10 e o Design System (`03.1`).

## Decisão
1. **Migração e Renomeação:** O arquivo embrionário (`modules/curation-guidelines.md`) foi deletado e substituído por `agents/curator/curation_rules.md`, assumindo uma estrutura yaml frontmatter para controle de versão (`prompt_version: 1.0.0`).
2. **Convergência de Conhecimento:** As regras de curadoria foram refinadas para incorporar a "Ausência do Tempo" (01), rejeitar clichês stoner e corporativos (01 a 10) e forçar a densidade e enxugamento estrutural do texto, satisfazendo a regra de "Horror ao Preenchimento" estipulada pelo Brutalismo do Design System (03.1).
3. **Comportamento de Máquina (State):** Adicionada instrução explícita de "Business Error": se 100% da pesquisa original for considerada imprópria, o agente forçará um *fail* no estado (conforme `03.2`), obrigando a refação em vez de tolerar mediocridade para dar andamento ao fluxo.

## Impacto
O agente Curator agora possui seu artefato de inicialização oficial para o runtime (LangGraph). Qualquer melhoria de prompt exigirá um novo PR alterando a `prompt_version`, permitindo que os Quality Gates auditem a regressão criativa do agente. O código (Python) do nó do Curator consumirá este markdown bruto no momento do boot.
