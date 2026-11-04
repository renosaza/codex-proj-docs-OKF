# Go

Use **golangci-lint v2**, which runs established analyzers including Staticcheck,
govet, errcheck, gosec and revive in one invocation. The supplied
[.golangci.yml](.golangci.yml) adds resource lifetime, context, error handling,
complexity and suppression checks. Formatting uses gofumpt and goimports.

## Adopt and run

Merge the configuration into the Go module root. Pin a compatible golangci-lint
v2 release in the project's existing tool installer or CI. Its Go compiler must
support the Go version used by the project; a newer `go` executable alone does
not upgrade a previously built golangci-lint binary.

```sh
golangci-lint version
golangci-lint config verify
golangci-lint run ./...
go test ./...
```

`run` checks both linters and configured formatters without editing files.
For a deliberate local fix, use `golangci-lint fmt`, inspect the diff, then rerun
the checks. Each module and supported build-tag/OS combination needs its own
check where the package graph differs. Run the race detector separately on a
supported platform when concurrency is relevant.

## Strictness and limits

The profile enables 34 named linters, all govet analyzers, all Staticcheck checks,
and reporting for discarded errors. It does not hide repeated findings or exempt
all test files. Only files matching Go's formal generated-code marker are skipped.
The agent must not add that marker to handwritten code to avoid diagnostics.

The list is explicit because enabling every available linter mixes mutually
incompatible or project-specific style policies. Additional rules are added
deliberately after running them on the project. Complexity thresholds are kit
policy, not an upstream guarantee of correctness. A suppression still needs a
specific rule, a reason and review; `nolintlint` cannot judge that reason.

The YAML parsed and passed the official current v2 JSON Schema on 2026-11-04.
No Go project or golangci-lint runtime was available for an execution test.
`config verify` against the pinned tool and a real module run are still required
on adoption; schema validation does not execute the analyzers.

## Primary sources

- [Configuration schema and v2 structure](https://golangci-lint.run/docs/configuration/file/).
- [Analyzer settings](https://golangci-lint.run/docs/linters/configuration/).
- [CLI and formatter behavior](https://golangci-lint.run/docs/configuration/cli/).
- [Installation and version compatibility](https://golangci-lint.run/docs/welcome/install/local/).
- [Official JSON Schema](https://github.com/golangci/golangci-lint/blob/main/jsonschema/golangci.jsonschema.json).
