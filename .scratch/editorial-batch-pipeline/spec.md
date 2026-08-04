Status: ready-for-agent

## Problem Statement

Atualmente, o pipeline de agentes da High House (através do `run_production.py`) processa um único briefing por vez e gera como saída código HTML e uma URL de imagem isolados. A marca, no entanto, não opera na lógica de posts unitários para feed, mas sim lançando **Revistas/Coleções** (lotes). Além disso, o resultado precisa ser o Pôster finalizado (a imagem em PNG 1080x1350) acompanhado da sua legenda, e não apenas código-fonte disperso.

## Solution

Adicionar uma Camada de Orquestração de Coleção e um Motor de Renderização ao framework EOS. O sistema passará a aceitar um `CollectionBrief` (que contém uma lista de `EditorialBriefs`), processando os pôsteres em lote (batch processing). Um novo `Renderer` nativo (utilizando Playwright) será responsável por compilar o HTML/CSS gerado junto com a imagem fotográfica, salvando o resultado como PNGs estáticos em formato de retrato (4:5) na pasta correspondente, ao lado de suas respectivas legendas geradas (.txt).

## User Stories

1. As a founder/operator, I want to initiate a batch generation process passing a `CollectionBrief`, so that the system generates the entire Collection (multiple Posters) automatically.
2. As a founder/operator, I want the system to output final, static PNG images formatted as 1080x1350px, so that I can directly publish them to the Instagram grid without manual assembly.
3. As a founder/operator, I want the system to generate and save the caption text alongside each PNG, so that I have the complete publication package (image + text) ready in one place.
4. As a founder/operator, I want the output to be automatically organized in directories named after the collection (e.g., `collections/001_manifesto/poster_01.png`), so that my editorial archive remains strictly structured and easily navigable.

## Implementation Decisions

- **Collection Orchestration:** A new domain contract `CollectionBrief` will be created to hold an array of `EditorialBrief`. 
- **Collection Workflow:** A new orchestrator module (`collection_orchestrator.py`) will iterate through the `CollectionBrief` and trigger the existing `EditorialWorkflow` sequentially for each chapter.
- **Rendering Engine:** A new infrastructure module (`renderer.py`) will integrate `playwright` (native Python library) to take a snapshot of the `RenderedCode` HTML.
- **Native Playwright:** The `playwright` package will be added as a dependency via `pyproject.toml` instead of relying on an external MCP server, ensuring a robust local batch pipeline.
- **Output Organization:** The final artifacts (PNG and TXT) will be saved to the filesystem under `05_IMPLEMENTACAO/collections/<collection_name>/`. The Coder Node/Human Approval Node logic will be updated to orchestrate this final dump.
- **Strict Scope of Collection 001:** The first collection will strictly execute 3 predefined chapters (Visual Impact, Contrast, Object of Desire) with no automatic expansion by the AI.

## Testing Decisions

- **What makes a good test:** The test must verify the end-to-end batch process. It should provide a mock `CollectionBrief` and assert that the output directory contains the expected number of PNG files and corresponding TXT caption files.
- **Modules to be tested:** `collection_orchestrator.py`, `renderer.py`.
- **Prior Art:** Existing unit tests or integration tests for `run_production.py` and `EditorialWorkflow` can serve as a base to ensure the mock memory and agents are properly instantiated during the test.

## Out of Scope

- Implementing the AI agent expansion logic for Collections > 001. (We are locking Collection 001 to 3 predefined posters).
- Connecting to a remote Playwright MCP Server.
- Direct API integration with Instagram for automatic publishing.

## Further Notes

- The terms "Poster", "Collection", "CollectionBrief", and "Renderer" have been formally documented in `CONTEXT.md` as part of the domain glossary to ensure alignment moving forward.
