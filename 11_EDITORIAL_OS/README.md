# High House — Editorial Operating System (EOS)

O **Editorial Operating System (EOS)** é a camada de inteligência autônoma da High House, estruturada não como um mero gerador de imagens ou textos, mas como uma **agência autônoma baseada na construção sequencial de marca a longo prazo**.

- [x] Agentes Funcionais
- [x] Integração Visual Bruta (HTML/CSS)
- [x] Batch Pipeline & Playwright Renderer (Lançamento de Coleções)
- [ ] Conexão com o Memory Server (Postgres)

## 🏗️ O Pipeline de 12 Agentes (Visão Arquitetural)

*Nota: A lista abaixo representa o **End-State** projetado da arquitetura. O estado atual da implementação (MVP Iterativo) opera com 9 agentes ativos na esteira. Os agentes marcados como `[Projetado]` terão sua lógica materializada em fases futuras.*

1. **Briefing** (Gatilho)
2. ⬇️ **Research Agent** (Pesquisa repertório) `[Implementado]`
3. ⬇️ **Curator Agent** (Seleciona e filtra anti-patterns) `[Projetado]`
4. ⬇️ **Editorial Agent** (Cria a narrativa do capítulo) `[Implementado]`
5. ⬇️ **Art Director Agent** (Define direção criativa e visual) `[Implementado]`
6. ⬇️ **Designer Agent** (Estrutura a hierarquia do layout) `[Implementado]`
7. ⬇️ **Image Agent** (Gera a fotografia base) `[Implementado]`
8. ⬇️ **Coder Agent** (Implementa HTML/CSS) `[Implementado]`
9. ⬇️ **Vision Agent** [Auditoria 1/3] (Auditoria técnica e estética) `[Implementado]`
10. ⬇️ **Critic Agent** [Auditoria 2/3] (Originalidade frente ao mercado) `[Projetado]`
11. ⬇️ **Brand Guardian Agent** [Auditoria 3/3] (Juiz supremo da identidade da marca) `[Implementado]`
12. ⬇️ **Memory Agent** (Arquiva o processo) `[Implementado]`
13. ⬇️ **Metrics Agent** (Hipóteses no motor empírico) `[Projetado]`
14. **Publish**

## 📂 Estrutura do Sistema

A documentação e implementação seguem um fluxo estrito e agnóstico de tecnologia, guiando a inteligência antes da codificação real:

1. **`01_SYSTEM_ARCHITECTURE.md`** - *Como o sistema funciona?* (Filosofia, Pipeline, Domínios)
2. **`02_MASTER_IMPLEMENTATION_PLAN.md`** - *Como vamos construir o sistema?* (Roadmap, Backlog, Fases)
3. **`03_BRAND_DESIGN_FOUNDATION.md`** - *Qual é o DNA puro da marca?* (Propósito estético permanente)
4. **`03.1_DESIGN_SYSTEM_SPECIFICATION.md`** - *Como uma IA deve pensar antes de desenhar?* (Manual de Direção de Arte / RFC Estética)
5. **`03.2_AGENT_RUNTIME_SPECIFICATION.md`** - *Como os agentes operam tecnicamente?* (State Schema, Grafos, Checkpoints e Infraestrutura)
6. **`04_AGENT_SPECIFICATIONS.md`** - *Qual é o contrato cognitivo de cada agente?* (Hierarquia, responsabilidades, limites e especificações dos 12 Agentes)
7. **`05_IMPLEMENTACAO/`** - *Onde mora o código.* (Contém `agents/`, `design_system/`, `memory/`, etc. Esta é a única pasta que pode mudar de tecnologia no futuro sem quebrar o EOS).
8. **`06_GOVERNANCE/`** - *Auditorias e integridade.* (Contém os artefatos de aprovação de Fonte de Verdade e decisões não-técnicas).

## 📐 Padrão Arquitetural Obrigatório

Todos os documentos contidos nesta pasta (`11_EDITORIAL_OS`) **DEVEM** obedecer estritamente às seguintes regras de engenharia de sistema:

1. **Fonte Única da Verdade (SSOT):** O conhecimento não deve ser duplicado. Se uma regra visual ou identidade da marca já existe em `03.1_DESIGN_SYSTEM_SPECIFICATION.md` ou na raiz do projeto (`01` a `10`), ela **nunca** deve ser reescrita em planos de implementação ou orquestração. Documentos de gestão devem apenas conter referências para a Fonte da Verdade.
2. **Ordem Inegociável:** O código nasce da documentação. O design não pode ocorrer sem especificação (`03.1`), a injeção não pode ocorrer sem o contrato do agente (`04`), e o código (`05`) não pode existir sem os dois anteriores. 
3. **Planos Orquestram, Não Definem:** Documentos como `02_MASTER_IMPLEMENTATION_PLAN.md` existem para gerenciar *como* e *quando* construir o sistema. Eles não podem carregar restrições de negócio, cores, fontes ou comportamentos de IA internamente em suas tarefas.
4. **Estado Inicial vs Estado Atual:** Documentações arquiteturais devem ser escritas visando longevidade. Use "Estado Inicial da Implementação" (um fato histórico inalterável) em vez de "Estado Atual" (que envelhece e requer manutenção constante).
5. **Entregáveis (Artefatos):** Toda tarefa ou mudança no sistema gera um **Artefato** material (código/documento), exige uma **Validação** objetiva, e produz uma **Memória gerada** (logs de decisão na pasta `memory`).

---
*Última atualização: Implementação do núcleo do Acumulador Sequencial concluída, permitindo ao orquestrador de coleção acumular o histórico de pôsteres gerados e injetá-lo no estado inicial do LangGraph.*
