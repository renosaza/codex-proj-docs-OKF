# Cross-stack security checks

Use established local scanners in addition to language linting. Pin tool
versions and record the rule/database version used by CI. Security scanners
can miss defects and report false positives; their success does not establish
that a change is secure.

## Secrets: Gitleaks

Merge `.gitleaks.toml` to retain the shipped rule set. Scan both committed history
and the current working tree so uncommitted AI-generated secrets are checked.

```sh
gitleaks git --redact --ignore-gitleaks-allow --exit-code=1 .
gitleaks dir --redact --ignore-gitleaks-allow --exit-code=1 .
```

Use a full Git checkout for a complete history scan. The commands redact
findings from console output and do not honor inline `gitleaks:allow` comments.
Project allowlists and `.gitleaksignore` still require review; do not create a
baseline from current findings to turn a failing change green.

Source: [Gitleaks usage, configuration and exit codes](https://github.com/gitleaks/gitleaks).

## Source patterns: Semgrep Community Edition

Vendor a reviewed subset of [official Semgrep rules](https://github.com/semgrep/semgrep-rules)
at an exact commit under the target project's `tooling/semgrep-rules/`. Preserve
applicable licenses and verify those rules against the pinned Semgrep version.
Then run the local rules explicitly:

```sh
semgrep scan --config tooling/semgrep-rules/ --error --strict --disable-nosem --metrics=off .
```

`--error` blocks findings, `--strict` blocks scan/configuration errors at the
documented warning level, and `--disable-nosem` prevents inline suppressions from
hiding findings. No `--config auto`, remote rules URL, account login or upload
step is required. Choose rules for the actual languages and threat model; this
pack does not ship an empty ruleset and label it a security check.

Source: [Semgrep CLI, errors, suppressions and metrics](https://docs.semgrep.dev/cli-reference).

## Dependencies, images and IaC: Trivy

```sh
trivy fs --scanners vuln,misconfig,secret --exit-code 1 .
trivy config --exit-code 1 infrastructure/
```

These are separate applicable checks; do not run the second command when that
directory does not exist. The explicit exit code is essential: do not rely on
report generation alone. Keep all severities blocking for the strict profile
and do not use `--ignore-unfixed` to hide known findings. Maintain reviewed
exceptions explicitly when a dependency has no usable fix.

Trivy downloads vulnerability databases and check bundles unless an offline
workflow is configured. Keep those artifacts fresh under the project's update
policy; a pinned binary alone does not make vulnerability results immutable.
These commands use local scanning and do not request a source-code upload.

Sources: [Trivy misconfiguration scanning](https://trivy.dev/docs/latest/scanner/misconfiguration/),
[Trivy failure exit codes](https://trivy.dev/docs/latest/configuration/others/).
