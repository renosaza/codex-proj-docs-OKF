# Strict quality profiles

This is a selectable collection of configuration templates and adoption recipes for
AI-assisted and human development. Start with the [catalog](CATALOG.md), then read
the chosen profile before merging it. A supplied file is a starting point, not a
complete, universally runnable project configuration. Profiles state what was
actually tested and what still needs verification.

1. Inspect manifests, runtime versions, source ownership, monorepo packages and
   existing quality commands. Select only applicable profiles.
2. Merge relevant settings with the project's real configuration, preserve its
   runtime and framework requirements, and pin compatible tool versions using its
   existing dependency manager and lockfile. A configuration fragment is not an installer.
3. Run the real format check, linter, type check or compiler, and relevant tests.
   Set up blocking checks in the project's existing local and CI workflow. See
   [AI rules](AI-RULES.md) and [CI guidance](CI.md).
4. Record actual commands, tool versions, exit statuses and checks not run. Verify
   that each intended source scope was actually analyzed.

Strict compatible rules expose more issues, but enabling every available rule can
introduce contradictions or irrelevant constraints. Fix real issues and review
applicability instead of weakening gates to obtain a green result. Static analysis
cannot establish semantic correctness, security or accessibility by itself; tests
and human review remain necessary. No profile changes branch protection or installs
itself. Documentation-only work does not require inventing code checks.

## Validation snapshot: 2026-11-04

- Python, TypeScript, CSS and HTML profiles passed 17 positive and negative
  runtime/configuration smoke checks. Tested versions and exact scope are in the
  [Python](profiles/python/README.md), [TypeScript](profiles/typescript/README.md)
  and [web](profiles/web/README.md) profiles.
- The [BSL report gate](profiles/bsl/README.md) passed four unittest methods and
  strict mypy checking. The BSL Language Server jar was not run.
- The [Go configuration](profiles/go/README.md) passed the official v2 JSON Schema
  check; golangci-lint itself was not run.
- Other profiles were researched against documentation; selected JSON, YAML,
  TOML, XML and INI configurations received syntax checks. Their language analyzers
  and application integrations were not run. Syntax checks alone do not validate
  tool behavior.
