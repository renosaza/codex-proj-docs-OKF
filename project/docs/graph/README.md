---
type: Reference
status: draft
---

# Code discovery

Template: no graph has been generated or verified for this repository. Determine the actual languages and existing tooling before selecting an indexer.

For a known symbol, start with targeted search and inspect the implementation and callers:

```sh
rg -n --glob '!*.lock' 'SYMBOL' .
rg --files
```

Replace `SYMBOL` with the real identifier and narrow the path to the relevant area. If ripgrep is unavailable, use an existing editor or repository search.

An indexer such as `codegraph` is optional. Verify the installed version's language support and CLI before documenting an executable generation command. Do not apply a Python-only generator to other languages or invent a placeholder JSON graph.

When an actual index is useful, replace this paragraph with its tool/version, included and excluded paths, unsupported languages and dynamic edges, exact rebuild command, indexed revision or content fingerprint, and bounded query command. Verify freshness before relying on missing edges; confirm important findings in code. Never load the entire graph into context by default.
