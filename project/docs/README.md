---
type: Reference
status: draft
---

# Project knowledge

This is an unpopulated template, not a description of this repository. Replace prompts with verified project facts before adopting it. Delete pages that have no useful content. Do not create fictional decisions, debt, tasks or graph data to fill folders.

Start from the OKF [index](index.md), then read only the area relevant to the task:

- [Constraints](constraints.md): active project prohibitions; read before planning or delegation.
- [Writing conventions](style.md): concise, sourced documentation.
- [Architecture](architecture/README.md): boundaries and invariants that code alone does not explain.
- [Decisions](architecture/decisions/README.md): accepted choices and reconsideration conditions.
- [Debt](debt/README.md): tolerated compromises and removal conditions.
- [Work](work/README.md): authoritative task source and optional local cards.
- [Code discovery](graph/README.md): search or a verified, compatible index.
- [Human guides](guides/README.md): setup, deployment and troubleshooting.
- [Record templates](_templates/): copy only when an actual record is needed.

Code establishes current behavior; accepted requirements and decisions establish intended constraints. Investigate discrepancies instead of silently preferring one. Preserve source links and flag uncertain migrated claims. Store concise outcomes, not chat transcripts or hidden reasoning.

After a change, update only affected knowledge. For a pause, use the task's optional Resume section; for a small completed change with no durable new knowledge, do not create a card. Do not duplicate tasks already owned by a tracker.

Use the project's existing checks for links, YAML metadata and workflow records when available.
Otherwise inspect changed metadata and references directly. No validator, runtime, language,
CI gate or board generator is required by this template. Checks do not establish truth.
