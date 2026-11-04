# Optional multi-language aggregators

Use the project's existing CI runner and native commands first. A polyglot
repository can use **Super-Linter** or **MegaLinter** to package many tools in one
container. Choose one aggregator and an explicit tool list; do not run every
competing formatter against the same files.

As checked through GitHub's repository API on 2026-11-04, Super-Linter had 10,646
stars and MegaLinter 2,640. Stars are a rough popularity signal, not evidence of
accuracy or adoption across every language. Both support standalone use;
MegaLinter also documents GitLab CI integration.

## Super-Linter

For a repository that has Bash, Dockerfiles and GitHub Actions, these documented
environment settings select a small blocking set:

```dotenv
RUN_LOCAL=true
VALIDATE_ALL_CODEBASE=true
DISABLE_ERRORS=false
VALIDATE_BASH=true
VALIDATE_DOCKERFILE_HADOLINT=true
VALIDATE_GITHUB_ACTIONS=true
BASH_SEVERITY=style
```

Use `RUN_LOCAL=true` for standalone Docker execution; use the official CI recipe
for its CI context. Keep the native strict configuration files and configure
Super-Linter's rule paths for their adopted locations. Verify the enabled tool
list and versions printed by the selected image. Keep fix mode off. Pin its
action to an immutable commit or its image to a reviewed digest in the target
project. This document does not invent an image digest.

## MegaLinter

An equivalent small `.mega-linter.yml` policy can start with:

```yaml
---
VALIDATE_ALL_CODEBASE: true
DISABLE_ERRORS: false
APPLY_FIXES: none
FAIL_IF_MISSING_LINTER_IN_FLAVOR: true
ENABLE_LINTERS:
  - BASH_SHELLCHECK
  - DOCKERFILE_HADOLINT
  - YAML_YAMLLINT
BASH_SHELLCHECK_ARGUMENTS: --severity=style --check-sourced
DOCKERFILE_HADOLINT_ARGUMENTS: --failure-threshold=style --disable-ignore-pragma
YAML_YAMLLINT_ARGUMENTS: --strict
```

Select a flavor containing these tools. Set the tools' config paths to the
adopted files. Inspect the output to confirm every requested tool actually ran
on the expected files; `DISABLE_ERRORS: false` does not enable all rules or turn
every underlying warning into an error. Avoid optional report publishing unless
it is wanted and authorized for the project. The container's pinned tool set
must be compatible with its configuration files.

## Sources

- [Super-Linter usage, tool variables and configuration paths](https://github.com/super-linter/super-linter)
- [MegaLinter configuration](https://megalinter.io/latest/configuration/)
- [MegaLinter GitLab CI installation](https://megalinter.io/latest/install-gitlab/)
- [Super-Linter repository metadata](https://api.github.com/repos/super-linter/super-linter)
- [MegaLinter repository metadata](https://api.github.com/repos/oxsecurity/megalinter)
