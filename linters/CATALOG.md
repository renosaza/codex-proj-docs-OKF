# Profile catalog

Select tools that match the actual project. **Template** means this kit includes
one or more configuration files or fragments to merge; **recipe** means the named
stack needs its own configuration. Neither label means every tool listed is
installed or tested against your project. See each profile for versions, checks,
limitations and primary sources. L = linter/static analyzer; T = type checker or
compiler; F = formatter; S = security scanner; A = aggregator.

| Language or format | Main upstream tools (category) | Kit support |
| --- | --- | --- |
| Python | [Ruff](https://docs.astral.sh/ruff/) (L, F), [mypy](https://mypy.readthedocs.io/) (T) | [Template](profiles/python/README.md) |
| JavaScript, TypeScript | [ESLint](https://eslint.org/), [typescript-eslint](https://typescript-eslint.io/) (L), [TypeScript](https://www.typescriptlang.org/) (T), [Prettier](https://prettier.io/) (F) | [Template](profiles/typescript/README.md) |
| HTML, CSS | [HTML-validate](https://html-validate.org/), [Stylelint](https://stylelint.io/) (L) | [Template](profiles/web/README.md) |
| React, React Native, Vue, Svelte, Angular, SCSS | Framework-specific integrations, e.g. [eslint-plugin-vue](https://eslint.vuejs.org/) (L) | [Recipes](profiles/web/README.md) |
| Go | [golangci-lint](https://golangci-lint.run/) (L, F) | [Template](profiles/go/README.md) |
| Rust | [Clippy](https://doc.rust-lang.org/clippy/) (L), rustc (T), rustfmt (F) | [Template fragment](profiles/rust/README.md) |
| C, C++, Objective-C, CUDA | [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) (L), clang-format (F) | [Template](profiles/cpp/README.md); target-specific adaptation |
| C#, Visual Basic | [.NET analyzers](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview) (L), SDK compiler (T), dotnet format (F) | [Template](profiles/dotnet/README.md) |
| F# | Compiler (T), [Fantomas](https://fsprojects.github.io/fantomas/) (F) | [Recipe](profiles/dotnet/README.md) |
| Java | [Error Prone](https://errorprone.info/), [SpotBugs](https://spotbugs.github.io/), [Checkstyle](https://checkstyle.org/) (L) | [Recipe](profiles/jvm/README.md) |
| Kotlin, Android | [detekt](https://detekt.dev/), [Android Lint](https://developer.android.com/studio/write/lint) (L), [ktlint](https://ktlint.github.io/) (L, F) | [Recipe](profiles/jvm/README.md) |
| Scala | [Scalafix](https://scalacenter.github.io/scalafix/) (L), [Scalafmt](https://scalameta.org/scalafmt/) (F) | [Recipe](profiles/jvm/README.md) |
| PHP | [PHPStan](https://phpstan.org/) (L, T), [PHP_CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) (L, F) | [Template](profiles/php/README.md) |
| Ruby, Rails | [RuboCop](https://docs.rubocop.org/rubocop/) (L, F), [Sorbet](https://sorbet.org/) (T) | [Template](profiles/ruby/README.md) |
| Dart, Flutter | [Dart analyzer](https://dart.dev/tools/dart-analyze) (L, T), Dart formatter (F) | [Template](profiles/mobile/README.md) |
| Swift | [SwiftLint](https://github.com/realm/SwiftLint) (L), [swift-format](https://github.com/swiftlang/swift-format) (F) | [Recipe](profiles/mobile/README.md) |
| Bash, POSIX sh, dash, ksh | [ShellCheck](https://www.shellcheck.net/) (L), [shfmt](https://github.com/mvdan/sh) (F) | [Template](profiles/shell/README.md) |
| PowerShell | [PSScriptAnalyzer](https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/overview) (L) | [Template and failure gate](profiles/shell/README.md) |
| 1C BSL, OneScript | [BSL Language Server](https://1c-syntax.github.io/bsl-language-server/) (L) | [Template and report gate](profiles/bsl/README.md) |
| SQL | [SQLFluff](https://www.sqlfluff.com/) (L, F) | [Template](profiles/sql/README.md) |
| Dockerfile, GitHub Actions, Terraform/OpenTofu, Ansible, Kubernetes, Helm | [Hadolint](https://github.com/hadolint/hadolint), [actionlint](https://github.com/rhysd/actionlint), [TFLint](https://github.com/terraform-linters/tflint), [ansible-lint](https://docs.ansible.com/projects/lint/), [kubeconform](https://github.com/yannh/kubeconform) (L) | [Templates and recipes](profiles/infra/README.md) |
| YAML, Markdown, TOML, JSON, OpenAPI, AsyncAPI, Protobuf, GraphQL, XML | [yamllint](https://yamllint.readthedocs.io/), [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2), [Taplo](https://taplo.tamasfe.dev/), [Spectral](https://github.com/stoplightio/spectral), [Buf](https://buf.build/docs/lint/) (L) | [Templates and recipes](profiles/data/README.md) |
| Zig, Elixir, Erlang, Lua, Luau, R, Haskell, Julia, Perl, Clojure, ClojureScript, OCaml, Fortran | Compiler checks and ecosystem tools, e.g. [Credo](https://credo.hexdocs.pm/), [clj-kondo](https://github.com/clj-kondo/clj-kondo) (L, T, F) | [Recipes](profiles/native/README.md) |
| Cross-stack secrets, code patterns, dependencies, IaC | [Gitleaks](https://github.com/gitleaks/gitleaks), [Semgrep](https://semgrep.dev/), [Trivy](https://trivy.dev/) (S) | [Template and recipes](profiles/security/README.md) |
| Optional multi-language CI | [Super-Linter](https://github.com/super-linter/super-linter), [MegaLinter](https://megalinter.io/) (A) | [Comparison and recipes](profiles/infra/aggregators.md) |

[SonarQube Server](https://github.com/SonarSource/sonarqube) is an optional
server-based analysis and quality-gate platform for teams that already use or
choose to set it up. Its [quality gates](https://docs.sonarsource.com/sonarqube-server/2026.1/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates)
can block CI and pull requests. Check language and edition support, project setup
and scanner configuration for the target deployment; this kit does not install it.

These tools are established choices, not a universal popularity ranking. As one
imperfect signal of public interest, GitHub repository metadata on 2026-11-04 showed
[Ruff: 50,423 stars](https://api.github.com/repos/astral-sh/ruff),
[ESLint: 27,604](https://api.github.com/repos/eslint/eslint),
[ShellCheck: 40,279](https://api.github.com/repos/koalaman/shellcheck) and
[golangci-lint: 19,500](https://api.github.com/repos/golangci/golangci-lint).
Stars are neither usage counts nor evidence of quality, coverage or suitability.
