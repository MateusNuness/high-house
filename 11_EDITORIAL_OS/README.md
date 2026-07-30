# High House — Editorial Operating System (EOS)

O **Editorial Operating System (EOS)** é a camada de inteligência autônoma da High House, estruturada não como um mero gerador de imagens ou textos, mas como uma **agência autônoma baseada na construção sequencial de marca a longo prazo**.

## 🏗️ O Pipeline de 12 Agentes

Todo o fluxo de conteúdo obedece estritamente a este pipeline, impedindo que o Design se inicie antes da Narrativa e que a Publicação ocorra sem o crivo da Marca.

1. **Briefing** (Gatilho)
2. ⬇️ **Research Agent** (Pesquisa repertório)
3. ⬇️ **Curator Agent** (Seleciona e filtra anti-patterns)
4. ⬇️ **Editorial Agent** (Cria a narrativa do capítulo)
5. ⬇️ **Art Director Agent** (Define direção criativa e visual)
6. ⬇️ **Designer Agent** (Estrutura a hierarquia do layout)
7. ⬇️ **Image Agent** (Decide técnica: Foto Real vs IA vs HTML)
8. ⬇️ **Coder Agent** (Implementa HTML/CSS/SVG)
9. ⬇️ **Vision Agent** [Auditoria 1/3] (Renderiza e avalia layout/técnica)
10. ⬇️ **Critic Agent** [Auditoria 2/3] (Avalia originalidade frente ao mercado)
11. ⬇️ **Brand Guardian Agent** [Auditoria 3/3] (Juiz supremo da identidade da marca)
12. ⬇️ **Memory Agent** (Arquiva o processo concluído para a perpetuidade)
13. ⬇️ **Metrics Agent** (Injeta os resultados e hipóteses no motor empírico)
14. **Publish**

## 📂 Estrutura do Sistema

A documentação e implementação seguem um fluxo estrito e agnóstico de tecnologia, guiando a inteligência antes da codificação real:

1. **`01_SYSTEM_ARCHITECTURE.md`** - *Como o sistema funciona?* (Filosofia, Pipeline, Domínios)
2. **`02_MASTER_IMPLEMENTATION_PLAN.md`** - *Como vamos construir o sistema?* (Roadmap, Backlog, Fases)
3. **`03_BRAND_DESIGN_FOUNDATION.md`** - *Qual é o DNA puro da marca?* (Propósito estético permanente)
4. **`03.1_DESIGN_SYSTEM_SPECIFICATION.md`** - *Como uma IA deve pensar antes de desenhar?* (Manual de Direção de Arte / RFC Estética)
5. **`04_AGENT_SPECIFICATIONS.md`** - *Quem toma cada decisão?* (Especificação rigorosa dos 12 Agentes)
6. **`05_IMPLEMENTACAO/`** - *Onde mora o código.* (Contém `agents/`, `design_system/`, `memory/`, `html/`, `css/`, etc. Esta é a única pasta que pode mudar de tecnologia no futuro sem quebrar o EOS).

## 📐 Padrão Arquitetural Obrigatório

Todos os documentos contidos nesta pasta (`11_EDITORIAL_OS`) **DEVEM** obedecer estritamente às seguintes regras de engenharia de sistema:

1. **Fonte Única da Verdade (SSOT):** O conhecimento não deve ser duplicado. Se uma regra visual ou identidade da marca já existe em `03.1_DESIGN_SYSTEM_SPECIFICATION.md` ou na raiz do projeto (`01` a `10`), ela **nunca** deve ser reescrita em planos de implementação ou orquestração. Documentos de gestão devem apenas conter referências para a Fonte da Verdade.
2. **Ordem Inegociável:** O código nasce da documentação. O design não pode ocorrer sem especificação (`03.1`), a injeção não pode ocorrer sem o contrato do agente (`04`), e o código (`05`) não pode existir sem os dois anteriores. 
3. **Planos Orquestram, Não Definem:** Documentos como `02_MASTER_IMPLEMENTATION_PLAN.md` existem para gerenciar *como* e *quando* construir o sistema. Eles não podem carregar restrições de negócio, cores, fontes ou comportamentos de IA internamente em suas tarefas.
4. **Estado Inicial vs Estado Atual:** Documentações arquiteturais devem ser escritas visando longevidade. Use "Estado Inicial da Implementação" (um fato histórico inalterável) em vez de "Estado Atual" (que envelhece e requer manutenção constante).
5. **Entregáveis (Artefatos):** Toda tarefa ou mudança no sistema gera um **Artefato** material (código/documento), exige uma **Validação** objetiva, e produz uma **Memória gerada** (logs de decisão na pasta `memory`).
