---
type: Reference
status: draft
---

# Documentation style

Keep a small set of accurate, linked Markdown pages. Update affected knowledge with the code change. One fact has one authoritative home; link to it instead of copying it. Follow the project's language policy.

- Start with the purpose and useful next action. State scope, status, prerequisites or source evidence where their absence could mislead; do not add empty metadata to every page.
- Separate verified current behavior, accepted constraints, proposed changes and historical decisions. Mark uncertainty explicitly. Code alone does not authorize dropping an accepted constraint.
- Use descriptive headings, short paragraphs and real relative links. Add a table only when it makes parallel information easier to compare.
- For an operational guide, give prerequisites, ordered steps, expected result and relevant failure recovery. State which commands were actually checked; never present a template as a tested procedure.
- Keep confirmed decisions in their existing records; link from current architecture. Remove stale duplicates after preserving required history and resolving conflicting sources.
- Read the index, then only relevant pages. Do not paste transcripts, complete tool output or generated code graphs into project memory.

The docs directory is an Open Knowledge Format (OKF) v0.2 bundle. Enter through [index.md](index.md). Preserve concept frontmatter and use `status` only for OKF lifecycle; task, decision and debt state use `task_status`, `decision_status` and `debt_status`. Optional trust metadata must reflect actual evidence.
