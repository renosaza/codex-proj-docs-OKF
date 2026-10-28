# Project documentation kit

[![skills.sh installs](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Frenosaza%2Fcodex-proj-docs-OKF%2Fmain%2F.github%2Fbadges%2Fskills-sh.json&style=for-the-badge)](https://skills.sh/renosaza/codex-proj-docs-okf)

Reusable project documentation using [Google OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), global and project instructions, three documentation skills, and one optional coding skill. No fixed human language, individual account, company, repository, technology stack or external memory service is assumed. English template text is editable source text, not a language policy.

## Install skills with skills.sh

The repository exposes three project documentation skills and one optional coding skill:

- `project-docs-init` — initialize the documentation system for a new or undocumented project.
- `project-docs-maintain` — maintain the existing documentation after implementation, decisions or handoffs.
- `project-docs-migrate` — migrate existing project knowledge into the lean AGENTS.md + OKF layout.
- `ub-mode` — opt-in coding workflow for small changes, behavior-first tests, root-cause fixes, and available quality gates.

Preview the skills without installing anything:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF --list
```

Install interactively:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF
```

Install all four skills for Codex in the current project:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill '*' \
  --agent codex
```

Install one specific documentation skill:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill project-docs-init \
  --agent codex
```

Install the optional coding skill separately:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill ub-mode \
  --agent codex
```

In Codex, request `$ub-mode` for a coding task to apply it. The skill does not apply its code gates to documentation-only work. Its companion quality tools are separate projects; the skill does not install them or change project configuration.

Use `-g` / `--global` only when you intentionally want a user-level installation available across projects:

```bash
npx skills@latest add renosaza/codex-proj-docs-OKF \
  --skill '*' \
  --agent codex \
  --global
```

The badge at the top mirrors the repository's `total installs` value from skills.sh. A scheduled GitHub Action refreshes the badge data every six hours. This avoids depending on the official skills.sh badge endpoint while it returns `resource not found` for this indexed repository.

## Adopt the full kit

The skills CLI installs the skills only. The global and project AGENTS.md files remain explicit templates and should be merged rather than blindly overwritten.

1. Merge `global/AGENTS.md` into your Codex global `AGENTS.md` (normally `~/.codex/AGENTS.md`, or under your configured CODEX_HOME). Preserve existing relevant instructions.
2. Install the four folders under `skills/` with the skills.sh commands above. Manual copying into your agent's skills directory remains a fallback when the CLI is unavailable.
3. Merge `project/AGENTS.md` into the target repository's root AGENTS.md. Populate real purpose, boundaries and verified commands. Preserve existing restrictions.
4. For a new project, use `$project-docs-init`; adopt only useful pages from `project/docs/`. For existing documentation, use `$project-docs-migrate` instead of overwriting it with templates. Continue with `$project-docs-maintain`. Request `$ub-mode` separately when you want its coding workflow.

Initialization means creating the documentation system, not deploying an application.
No installer, configuration overwrite, runtime dependency or mandatory CI is included.
The full docs tree is a menu of templates; a small project needs only its index, constraints
and pages with useful knowledge. Remove unused pages and fix the index links.

## ub-mode source

`ub-mode` is an independently worded adaptation of engineering principles from
[unclebob/ub-mode at commit 57a8bdd](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/SKILL.md).
The skill does not reproduce upstream text. The Crapper, Dryer, and Mutator tools are independent projects and
are not bundled with or installed by this skill.

## Model routing

`gpt-6-astra` / `gpt-6.1-sol` orchestrate only; delegated research, changes and checks run
on `gpt-6-luna`. The parent chooses supported effort for each assignment. Luna executes directly. These instructions
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
