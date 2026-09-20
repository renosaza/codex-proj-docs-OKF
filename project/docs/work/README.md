---
type: Reference
status: draft
---

# Work

Template: identify the authoritative task source from the repository's actual workflow. If GitLab or GitHub issues own task state, link that tracker here and keep only needed handoff knowledge locally.

Use [task cards](../_templates/task.md) for independent outcomes that need tracking or handoff. Several checks of one small fix do not require several tasks. Group genuinely independent outcomes in an [epic](../_templates/epic.md) when useful. Empty task and epic folders contain no invented work.

One owner integrates each task. Before parallel edits, agree ownership of overlapping files; run relevant integrated checks after combining results. Split non-atomic work into bounded subtasks, follow the active global model-routing policy for delegation.

For `done`, include observed results, actual checks and the tested revision in Result. A command that has not run is a plan, not evidence. On pause or transfer, add Resume: done, next step, blocker, branch/revision, last check. Replace obsolete handoff text rather than accumulating a journal.

Use plain ASCII metadata values and stable IDs. `depends_on` is a bracket list; `parent`, `related_decision`, `supersedes`, `superseded_by` are scalar IDs or `null`. External IDs start with `external:` and need a full source link in the body. `README.md` files are folder guides, not cards.

Use `task_status` for the record workflow state; `status` is reserved for OKF document lifecycle (`draft`, `stable`, `deprecated`).
