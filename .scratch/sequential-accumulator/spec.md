Status: ready-for-agent

## Problem Statement

Atualmente, o `CollectionOrchestrator` e o `EditorialWorkflow` processam `EditorialBriefs` (pôsteres) de forma completamente isolada. A marca High House lança coleções narrativas (Capítulos) onde cada peça visual (Pôster) precisa dialogar com as demais para criar contraste e fluidez no grid do Instagram (ex: Pôster 1 é denso e brutalista, Pôster 2 deve ser mais leve e contrastante). Sem que os agentes do LangGraph saibam o que foi gerado no pôster anterior, perde-se a coesão narrativa sequencial da Coleção.

## Solution

Implementar um "Acumulador Sequencial" no `CollectionOrchestrator`. O orquestrador continuará a processar o workflow de um Pôster por vez (para proteger a capacidade do CoderAgent), mas acumulará um histórico (contexto) dos pôsteres concluídos com sucesso. Esse histórico (`previous_posters`) será injetado no estado inicial do LangGraph do próximo pôster, permitindo que os agentes narrativos (`EditorialAgent` e `ArtDirectorAgent`) leiam as decisões anteriores e ajustem suas propostas para manter o contraste estético e a continuidade textual.

## User Stories

1. As a founder/operator, I want the `EditorialAgent` to be aware of the caption written in Poster 1 when generating Poster 2, so that the textual narrative flows seamlessly across the Chapter.
2. As a founder/operator, I want the `ArtDirectorAgent` to know the aesthetic mood of the previous poster, so that it can deliberately create visual contrast (e.g. alternating between dark/heavy and light/clean designs) in the same Collection.
3. As a system architect, I want the generation of posters to remain computationally isolated (one LangGraph execution per poster) rather than batched into a single prompt, so that the `CoderAgent` and `ImageAgent` do not suffer from output truncation or hallucination from massive context payloads.
4. As a founder/operator, I want the generated Collection outputs (PNGs and TXTs) to inherently reflect this aesthetic sequence, so that they look cohesive when posted side-by-side on the Instagram grid.

## Implementation Decisions

- **Domain State Modification**: O `GlobalState` no arquivo `state.py` receberá um novo campo `previous_posters: list[dict]`.
- **Orchestrator Loop**: O `CollectionOrchestrator` em `collection_orchestrator.py` instanciará uma lista vazia `previous_posters` e a passará no estado inicial do `app.invoke`. Ao final de um pôster bem-sucedido, extrairá o resumo (tópico do brief, direção, caption) e adicionará à lista.
- **Interfaces Modifications**: As assinaturas de `run()` em `IEditorialAgent` e `IArtDirectorAgent` (em `interfaces.py`) serão atualizadas para aceitar opcionalmente o parâmetro `previous_posters: list[dict] | None = None`. O CoderAgent e ImageAgent não receberão esse contexto para se manterem focados na execução bruta.
- **Workflow Dependency Injection**: Os nós `_editorial_node` e `_art_director_node` no `EditorialWorkflow` extrairão `state.get("previous_posters")` e o repassarão para os respectivos agentes.
- **Agent Prompts**: As implementações físicas do `EditorialAgent` e `ArtDirectorAgent` (em `src/eos/application/agents/`) formatarão o array `previous_posters` em texto legível para orientar o LLM a seguir a continuidade e o contraste na Coleção.

## Testing Decisions

- **What makes a good test**: The highest seam available is the `process_collection` method inside `CollectionOrchestrator`. A good test will execute a mock `CollectionBrief` with 3 chapters/posters. It must assert that on the 2nd and 3rd iterations of `app.invoke`, the `previous_posters` list injected into the state is correctly populated with the summarized artifacts from the preceding loops.
- **Modules to be tested**: `CollectionOrchestrator` (batching logic), `EditorialWorkflow` (state passing).
- **Prior art**: Existing tests for `run_production.py` or orchestrator mock tests can be leveraged. Mocking the LangGraph invoke avoids triggering the actual DeepSeek endpoints.

## Out of Scope

- Atualizar o `CoderAgent`, `ImageAgent` e `BrandGuardianAgent` para consumirem o histórico. O papel de gerar contraste sequencial pertence puramente ao Planejamento (Editorial e Direção de Arte). Os nós de execução não precisam desse ruído.
- Criação autônoma de Capítulos pela IA. A estrutura de 3 sub-briefings continuará sendo fornecida explicitamente na raiz pelo fundador (via `run_collection.py`).

## Further Notes

- O `CONTEXT.md` já foi atualizado para desvincular o conceito de Capítulo e Pôster, estabelecendo formalmente que 1 Capítulo desdobra-se em N Pôsteres para publicação sequencial.
