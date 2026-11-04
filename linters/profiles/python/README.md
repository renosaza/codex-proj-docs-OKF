# Python: Ruff + strict mypy

Adoption profile, reviewed on 2026-11-04. Ruff checks code and formatting;
mypy checks types. Merge these settings into the target project's existing
configuration. Do not leave competing Ruff or mypy configs with unclear precedence.

## Install and run

The pinned tools are Ruff **0.17.3** and mypy **2.4.1**. Their combined runtime
requirement is **Python 3.10+** (from the installed package metadata). The smoke
checks used Python **3.12.14** on Linux. This does not set the application's
minimum supported Python version: align Ruff's `target-version` and mypy's
`python_version` with the real project, including its `requires-python` metadata.

Use the project's development environment, including its real dependencies and
type stubs. Copy `requirements-lint.txt`, or add its exact versions to the project's
existing dependency manager. Lock transitive dependencies there as usual; this
two-line file is a tool version snapshot, not a complete dependency lock.

From the target project's root, after adopting `ruff.toml` and `mypy.ini`:

```bash
python -m pip install -r requirements-lint.txt
python -m ruff check --ignore-noqa .
python -m ruff format --check .
python -m mypy --config-file mypy.ini .
```

Make each nonzero exit status fail CI. For a repository needing explicit source
roots, replace `.` with all relevant source and test roots. Run the tools from
that project's root; package discovery depends on it. Run tests separately.

## What is strict

- Ruff selects **all stable rules**, including security, complexity and annotation
  checks; `preview = false` prevents accidental adoption of preview rules.
- `--ignore-noqa` makes a `noqa` comment ineffective at hiding lint failures.
- The complexity limit is **10**. This is this kit's review threshold, not an
  upstream guarantee of correctness. Prefer a clearer function over splitting
  code into artificial helpers solely to satisfy the number.
- mypy enables `strict`, rejects explicit `Any` and `Any` from untyped imports,
  checks unreachable code, and adds checks for exhaustive matches, lost awaitables,
  unsafe overrides and unqualified `type: ignore` comments.
- Unsafe automatic fixes are disabled. The CI commands do not rewrite source.

The Ruff exclusions are intentional: formatting rules that conflict with Ruff's
formatter, plus `CPY001`. Copyright headers must follow the project's actual legal
policy; agents must not invent copyright ownership to silence a linter. Google
docstring convention selects one compatible docstring style. `E501` stays enabled;
the formatter may leave a long line that must be rewritten manually.

An existing namespace-package project should declare its real `namespace-packages`.
Pytest projects may need a narrow, documented `S101` exception for assertion-bearing
test paths. Do not disable security checks throughout the repository or silently
exclude tests. Existing code may need an explicit, reviewed migration plan.

## Optional stronger type checking

For a fully typed dependency graph, mypy can additionally enable
`disallow_any_expr = True` and `disallow_any_decorated = True`. These are more
restrictive than `strict` and can expose missing third-party stubs.

[basedpyright](https://docs.basedpyright.com/latest/) is an alternative type checker
with additional `Any`/unknown-type diagnostics. Choose one primary checker according
to the framework and existing plugins; two mandatory checkers are not required by
this kit. A strict basedpyright configuration in the project's `pyproject.toml` is:

```toml
[tool.basedpyright]
typeCheckingMode = "all"
failOnWarnings = true
enableTypeIgnoreComments = false
reportIgnoreCommentWithoutRule = "error"
```

After installing and pinning basedpyright in that project's development dependencies,
run `basedpyright --warnings`. Do not create a baseline to hide new findings. This
configuration still permits qualified `pyright: ignore` comments; instructions and
review must prevent unjustified suppressions. The optional checker was researched,
not executed in this profile's smoke checks.

## Verification performed

The pinned Ruff and mypy versions were installed in an isolated environment. A
documented typed function passed Ruff, Ruff format and mypy. A mutable default with
`# noqa: B006` still failed Ruff under `--ignore-noqa`; an invalid return type failed
mypy. This verifies configuration loading and those failure paths, not an arbitrary
application or third-party plugin combination.

## Primary sources

- [Ruff configuration and discovery](https://docs.astral.sh/ruff/configuration/).
- [Ruff ALL selection and upgrades](https://docs.astral.sh/ruff/linter/).
- [Formatter conflicts and exit codes](https://docs.astral.sh/ruff/formatter/).
- [Ruff settings, including complexity and docstrings](https://docs.astral.sh/ruff/settings/).
- [Copyright notice rule](https://docs.astral.sh/ruff/rules/missing-copyright-notice/).
- [Namespace package rule](https://docs.astral.sh/ruff/rules/implicit-namespace-package/).
- [mypy configuration](https://mypy.readthedocs.io/en/stable/config_file.html).
- [mypy optional error checks](https://mypy.readthedocs.io/en/stable/error_code_list2.html).
- [basedpyright strictness and warnings](https://docs.basedpyright.com/latest/configuration/config-files/).

`ALL` and `strict` can gain checks when tools are upgraded. Review upgrades and
commit the resulting dependency lock; do not resolve new findings by weakening gates.
