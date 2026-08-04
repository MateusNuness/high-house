# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

The context for this project is divided across multiple READMEs. Read each one relevant to the topic:

- **`README.md`** at the repo root — Main project context (brand foundation, general context).
- **`11_EDITORIAL_OS/README.md`** — Context for the Editorial OS subproject.
- **`11_EDITORIAL_OS/05_IMPLEMENTACAO/README.md`** — Implementation context for the Editorial OS.
- **`11_EDITORIAL_OS/05_IMPLEMENTACAO/design_system/README.md`** — Design system specifics.

If you need to understand the big picture or how a specific subproject works, always refer to these files first.

## File structure

```
/
├── README.md                          ← Main project context
└── 11_EDITORIAL_OS/
    ├── README.md                      ← Editorial OS subproject
    └── 05_IMPLEMENTACAO/
        ├── README.md                  ← Implementation details
        └── design_system/
            └── README.md              ← Design system context
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in the READMEs. Don't drift to synonyms. If the concept you need isn't in the documentation yet, that's a signal to ask or note it for future modeling.

## Flag Context Conflicts

If your output contradicts an existing rule from the READMEs, surface it explicitly rather than silently overriding.
