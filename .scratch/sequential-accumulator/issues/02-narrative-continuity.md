# 02 — Narrative Continuity in Editorial

**What to build:** Updates `IEditorialAgent`, `EditorialWorkflow`, and `EditorialAgent` to receive and format `previous_posters`. The agent writes captions aware of the previous posters in the collection.

**Blocked by:** 01 — Accumulator Core & Orchestration

**Status:** done

- [x] `IEditorialAgent` run signature accepts an optional `previous_posters` list.
- [x] `EditorialWorkflow` extracts `previous_posters` from the state and passes it to the `EditorialAgent`.
- [x] `EditorialAgent` LLM prompt uses the history to generate text that maintains continuity.
- [x] The generated poster text reflects awareness of the narrative established in prior loops.
