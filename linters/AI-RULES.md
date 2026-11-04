# Rules for AI-assisted changes

- Inspect the real manifests, runtime versions, language versions, source scopes,
  monorepo packages and existing scripts before choosing checks. Merge applicable
  profiles with existing settings; install only needed, compatible tools and pin
  exact versions in the project's established dependency and lockfile workflow.
- Run the project's actual formatter check, linter, type checker or compiler and
  relevant existing tests for changed code. Treat warnings as failures where the
  tool supports it. Check that each requested tool runs against the intended files.
- Fix the underlying issue. Do not add `noqa`, `eslint-disable`, `nolint`,
  `ts-ignore`, unsafe casts, skipped tests, broad exclusions or baselines merely to
  obtain a green check. Never mask failures with `|| true`, `continue-on-error` or
  a missing-tool-is-success fallback. Preserve accepted narrow exceptions; new ones
  need a concrete justification and the authority required by the project.
- Use compatible, relevant rules rather than blindly enabling mutually conflicting
  presets. Avoid splitting code into meaningless helpers or other ceremony just to
  satisfy a complexity limit. Keep behavior, security and existing safeguards intact.
- Report the exact commands, tool versions and exit status observed, plus checks not
  run and why. Do not describe syntax parsing as a successful analyzer run.

Instructions alone do not enforce a gate: an agent with authority to change checks
can change the gate itself. Review configuration and changes, run project tests and
use protected server-side checks where appropriate. Linters find patterns, not proof
of correctness or safety.
