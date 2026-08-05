Status: ready-for-agent

## Problem Statement

The High House Editorial Operating System (EOS) is experiencing architectural friction in three key areas, primarily due to "shallow modules" and leaky boundaries:
1. **Sequential Accumulator state leaks**: The history of previous posters is managed as a generic `list[dict]` in the `GlobalState`. This forces the workflow orchestrator to assemble dictionaries and the Agents (Editorial and Art Director) to manually iterate and parse them to construct their contrast and narrative prompts.
2. **Shallow LLM Adapter**: The `StructuredLLMAdapter` merely wraps LangChain's invocation but forces individual agents to still construct `SystemMessage` and `HumanMessage` objects, duplicating LangChain infrastructure code across all agents.
3. **Leaky Orchestrator**: The `CollectionOrchestrator` handles workflow execution but also manages side-effects like launching a headless browser (Playwright) to render PNGs and writing text files to disk, violating the Single Responsibility Principle.

## Solution

Deepen the architecture by introducing focused domain modules that encapsulate these responsibilities, shrinking the interfaces exposed to the rest of the application:
1. Introduce a `CollectionHistory` deep module in the `GlobalState` to absorb prompt formatting for narrative continuity and aesthetic contrast.
2. Deepen the `StructuredLLMAdapter` to accept raw strings (`system_prompt`, `human_prompt`) and the output schema, keeping LangChain primitives strictly inside the adapter.
3. Extract a `PublicationExporter` module to handle the headless rendering and file I/O, allowing the orchestrator to delegate side-effects cleanly.

## User Stories

1. As a System Maintainer, I want the poster history encapsulated in a `CollectionHistory` object, so that I can change how contrast and narrative contexts are formatted without touching the Agent implementations.
2. As an Agent Developer, I want to ask `history.get_contrast_context()` or `history.get_narrative_context()`, so that my agent only receives the specific information it needs without parsing raw dictionaries.
3. As an Agent Developer, I want to pass raw strings and a Pydantic schema to the `StructuredLLMAdapter`, so that my agent code doesn't need to import or assemble LangChain `SystemMessage` or `HumanMessage` objects.
4. As a System Maintainer, I want to consolidate file exporting into a `PublicationExporter` module, so that the `CollectionOrchestrator` is purely responsible for managing the batch generation loop.
5. As a QA Engineer, I want the file I/O and Playwright logic separated into `PublicationExporter`, so that I can substitute an in-memory exporter during automated tests and avoid writing files to disk.

## Implementation Decisions

- **CollectionHistory**: A new domain module (`src/eos/domain/collection_history.py`) will be created. It will expose `get_narrative_context()` and `get_contrast_context()`.
- **GlobalState update**: The `previous_posters` array in `GlobalState` will be replaced by `history: CollectionHistory`.
- **Agent simplification**: `ArtDirectorAgent` and `EditorialAgent` will be updated to consume the `CollectionHistory` methods instead of parsing `list[dict]`.
- **Deep LLM Adapter Interface**: `StructuredLLMAdapter.invoke()` will change its signature from `invoke(messages, schema, fallback)` to `invoke(system_prompt: str, human_prompt: str, schema: Type[T], fallback_obj: T)`.
- **Agent LLM calls**: All agents using `StructuredLLMAdapter` will be updated to match the new signature, removing `langchain_core.messages` imports.
- **PublicationExporter**: A new infrastructure module (`src/eos/infrastructure/publication_exporter.py`) will handle `render_to_png` and saving captions. It will be instantiated in `CollectionOrchestrator` and called at the end of the batch loop.

## Testing Decisions

- Tests should only test the external behavior of the batch pipeline at the highest seam possible.
- **Seams**: The primary test seam for the workflow is the `CollectionOrchestrator.process_collection` method.
- **Module testing**: We will use `tests/workflows/test_collection_orchestrator.py` to verify the orchestrator runs end-to-end without failing. We will mock the `PublicationExporter` to avoid disk I/O and Playwright initialization during unit testing.
- **Prior art**: The existing mock agents (`tests/fixtures/mock_*.py`) will be used to run the orchestrator loop without hitting the real LLM.

## Out of Scope

- Modifying the core behavior, fallback logic, or prompts of the agents (aside from refactoring how they receive the history context).
- Changes to the Playwright renderer logic itself (it will just be moved, not rewritten).
- Changing the LangGraph `EditorialWorkflow` node definitions beyond passing the new `history` object and invoking the new adapter signature.

## Further Notes

- These changes align with the project's Domain Language in `CONTEXT.md` (e.g., `CollectionHistory` and `StructuredLLMAdapter`).
