# Project documentation kit

[![skills.sh](https://skills.sh/b/renosaza/codex-proj-docs-OKF)](https://skills.sh/renosaza/codex-proj-docs-OKF)

Reusable project documentation using [Google OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), global and project instructions, and three documentation skills. No fixed human language, individual account, company, repository, technology stack or external memory service is assumed. English template text is editable source text, not a language policy.

## Install skills with skills.sh

The repository exposes three skills:

- `project-docs-init` — initialize the documentation system for a new or undocumented project.
- `project-docs-maintain` — maintain the existing documentation after implementation, decisions or handoffs.
- `project-docs-migrate` — migrate existing project knowledge into the lean AGENTS.md + OKF layout.

Preview the skills without installing anything:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF --list
```

Install interactively:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF
```

Install all three skills for Codex in the current project:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill '*' \
  --agent codex
```

Install one specific skill:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill project-docs-init \
  --agent codex
```

Use `-g` / `--global` only when you intentionally want a user-level installation available across projects:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill '*' \
  --agent codex \
  --global
```

The badge at the top is the official skills.sh install-count badge. skills.sh discovers public skills from `npx skills add` telemetry and updates the displayed install count automatically after the repository is indexed.

## Adopt the full kit

The skills CLI installs the skills only. The global and project AGENTS.md files remain explicit templates and should be merged rather than blindly overwritten.

1. Merge `global/AGENTS.md` into your Codex global `AGENTS.md` (normally `~/.codex/AGENTS.md`, or under your configured CODEX_HOME). Preserve existing relevant instructions.
2. Install the three folders under `skills/` with the skills.sh commands above. Manual copying into your agent's skills directory remains a fallback when the CLI is unavailable.
3. Merge `project/AGENTS.md` into the target repository's root AGENTS.md. Populate real purpose, boundaries and verified commands. Preserve existing restrictions.
4. For a new project, use `$project-docs-init`; adopt only useful pages from `project/docs/`. For existing documentation, use `$project-docs-migrate` instead of overwriting it with templates. Continue with `$project-docs-maintain`.

Initialization means creating the documentation system, not deploying an application.
No installer, configuration overwrite, runtime dependency or mandatory CI is included.
The full docs tree is a menu of templates; a small project needs only its index, constraints
and pages with useful knowledge. Remove unused pages and fix the index links.

## Model routing

Astra/Sol orchestrate only: research goes to Luna, changes and checks to Terra. The parent
chooses supported effort for each assignment. Terra/Luna execute directly. These instructions
use available delegation tools and explicit model selection, without custom role files.
Runtime must support the models and delegation; if unavailable, report the blocker and obtain
an explicit policy override before direct execution. AGENT_ROLE is a prompt marker when
runtime identity is unavailable, not a configuration key. Model switches require reevaluation.
Instructions are not a technical security boundary, especially with unrestricted tools.

## Knowledge format

`docs/index.md` is the bundle entrypoint. Concepts use YAML `type`; reserved index.md/log.md
are not concepts. `status` is lifecycle (draft/stable/deprecated); task_status,
decision_status and debt_status are local workflow extensions. Preserve unknown fields and
source evidence. Never invent verification or historical facts. Root AGENTS.md and skills
retain their own native formats outside docs/.

## Verified scope

The package is checked for concept metadata, internal documentation links and personal or
repository-specific leftovers. Skill structure is validated. No live routing test or
external OKF consumer certification is claimed. No token savings benchmark was performed.
