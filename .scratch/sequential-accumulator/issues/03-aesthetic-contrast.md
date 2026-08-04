# 03 — Aesthetic Contrast in Art Direction

**What to build:** Updates `IArtDirectorAgent`, `EditorialWorkflow`, and `ArtDirectorAgent` to receive and format `previous_posters`. The agent plans visual designs that contrast with preceding posters.

**Blocked by:** 01 — Accumulator Core & Orchestration

**Status:** done

- [x] `IArtDirectorAgent` run signature accepts an optional `previous_posters` list.
- [x] `EditorialWorkflow` extracts `previous_posters` from the state and passes it to the `ArtDirectorAgent`.
- [x] `ArtDirectorAgent` LLM prompt uses the history to suggest aesthetic contrast (e.g. brutalist vs clean) compared to earlier posters.
- [x] The generated visual direction reflects a deliberate contrast relative to prior loops.
