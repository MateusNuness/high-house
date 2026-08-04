# 01 — Accumulator Core & Orchestration

**What to build:** Modifies `GlobalState` and `CollectionOrchestrator` to accumulate and inject `previous_posters`. Adds the core test for `process_collection` to ensure the history array builds correctly across loop iterations.

**Blocked by:** None — can start immediately.

**Status:** completed

- [x] `GlobalState` type in `state.py` is updated to include `previous_posters: list[dict]`.
- [x] `CollectionOrchestrator` loop maintains a `previous_posters` list and appends poster summaries after each iteration.
- [x] `previous_posters` array is passed into the LangGraph state initial payload.
- [x] Unit tests for `process_collection` assert that the array correctly accumulates across a multi-poster mock collection.
