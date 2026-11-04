# Shell and PowerShell

Adopt the configuration for the shells actually used by the target project.
Pin installed tool versions in that project's existing dependency or CI setup.

## Bash, POSIX sh, dash and ksh

Use **ShellCheck** for correctness and **shfmt** for formatting. Merge
`.shellcheckrc` into the project root. It enables optional ShellCheck checks and
allows analysis of sourced files. Supply all maintained scripts to the command;
the file paths below are examples, not a discovery algorithm.

```sh
shellcheck --severity=style --check-sourced scripts/build.sh scripts/test.sh
shfmt -d scripts
```

Every ShellCheck severity is blocking, including `style`; `--check-sourced`
also checks diagnostics inside sourced files. Preserve correct shebangs and
make dynamic source paths explicit. Do not add `shellcheck disable` comments
to make an AI patch pass. Review existing suppressions separately: ShellCheck
still respects them. ShellCheck does not lint arbitrary zsh, fish or Windows
batch syntax. Use each unsupported shell's own syntax checker and tests.

Sources: [ShellCheck options and rc files](https://github.com/koalaman/shellcheck/blob/master/shellcheck.1.md),
[shfmt manual](https://github.com/mvdan/sh/blob/master/cmd/shfmt/shfmt.1.scd).

## PowerShell

Use **PSScriptAnalyzer**. Keep the settings file and `Invoke-Lint.ps1` together,
for example under `tooling/powershell/`, or pass `-Settings` explicitly.

```powershell
pwsh -NoProfile -File tooling/powershell/Invoke-Lint.ps1 -Path scripts
```

The wrapper fails on errors, warnings and information diagnostics, including
suppressed findings. Missing tools, invalid input and empty source directories
also fail. `-EnableExit` alone is insufficient for this policy: Microsoft's
documented exit behavior counts error records rather than every severity.
The settings enable all built-in rule names and two configurable formatting
checks; compatibility rules need the project's actual PowerShell target data.

Install a reviewed, pinned PSScriptAnalyzer version in the existing tool setup.
Do not use `-Fix` in the CI check. Native parser/runtime tests remain necessary.

Sources: [Invoke-ScriptAnalyzer](https://learn.microsoft.com/en-us/powershell/module/psscriptanalyzer/invoke-scriptanalyzer),
[settings](https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/using-scriptanalyzer),
[indentation rule](https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/useconsistentindentation).
