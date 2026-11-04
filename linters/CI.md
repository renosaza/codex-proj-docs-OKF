# Using the checks locally and in CI

Integrate selected checks with the project's existing commands and CI system. Make
one real project quality command, or a documented set of commands, run the same
checks locally and in CI; define it in the target project using that project's
package manager or build system. Do not copy imaginary scripts or silently skip
missing tools, empty source scopes, configuration errors or failed checks.

Pin compatible binaries and dependencies, use the project's lockfiles, and provide
required schemas, build metadata and environment. Choose owned source scopes and
verify generated or vendored exclusions. Keep format checks read-only in CI and
make warnings and analysis failures block. Keep tests and security checks alongside
language-specific checks when relevant. The individual profiles specify details,
including tools whose output requires an explicit failure gate.

A pre-commit hook is a convenience and can be bypassed. Enforce required checks
on the server with branch protection or equivalent repository rules, if the owner
chooses to configure them. This kit does not change hosting settings. For optional
container-based coverage of multiple languages, see the [aggregator comparison](profiles/infra/aggregators.md).
