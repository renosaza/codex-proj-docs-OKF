# 1C BSL and OneScript

Use **BSL Language Server** against the exported source and metadata, not a
binary `.cf`/`.dt` file. Merge `.bsl-language-server.json` into the project and
place `check_report.py` in its tooling directory. The template enables all
diagnostics and does not skip modules based on vendor support status. Keep the
actual target platform and configuration compatibility settings in the project.
Change diagnostic language if needed; Russian here is a template default.

`mode: ALL` is intentionally demanding. Review applicability to ordinary vs
managed applications and extensions before adopting it. Any exception must be
narrow, explained and reviewed; an agent must not suppress a finding just to
finish a task. Existing `BSLLS:...-off` comments still need review.

## A report is not a passing CI check

The analyzer's successful analysis path returns zero even when it has written
diagnostics. The included Python standard-library gate requires a non-empty
`fileinfos` array, validates file entries and diagnostic fields, and fails on
every severity. Missing files, malformed JSON and empty scans fail too. It does
not prove that every intended source file was included; configure and review
the source scope and compare the reported file count with the export.

Use a fresh output directory so a failed run cannot reuse an old clean report.
For POSIX CI, after adopting the config and helper:

```sh
set -eu
: "${BSL_LS_JAR:?Set the path to the reviewed BSL Language Server jar}"
report_dir="$(mktemp -d)"
java -jar "$BSL_LS_JAR" analyze \
  --srcDir src \
  --configuration .bsl-language-server.json \
  --reporter json \
  --outputDir "$report_dir"
python3 tooling/check_report.py "$report_dir/bsl-json.json"
```

Retain or delete the temporary report according to the CI job's artifact policy.
On Windows the same Java arguments and gate work with `python`; create a new
output directory per run and check `$LASTEXITCODE` immediately after Java and
Python, because PowerShell does not automatically stop on a native nonzero exit.
Pin the jar release/checksum and use the Java version required by that release.

Run the gate's own contract checks from this kit:

```sh
python3 -m unittest discover -s linters/profiles/bsl -p 'test_*.py'
```

These tests validate the report gate, not the 1C configuration. Platform syntax
checks, module tests and Vanessa scenarios still cover behavior unavailable to
a static linter.

## Sources

- [Analyzer CLI](https://1c-syntax.github.io/bsl-language-server/en/)
- [Configuration and ALL mode](https://1c-syntax.github.io/bsl-language-server/en/features/ConfigurationFile/)
- [JSON report contract](https://1c-syntax.github.io/bsl-language-server/en/reporters/json/)
- [Analyzer exit behavior in source](https://github.com/1c-syntax/bsl-language-server/blob/develop/src/main/java/com/github/_1c_syntax/bsl/languageserver/cli/AnalyzeCommand.java)
- [JSON reporter includes each analyzed file](https://github.com/1c-syntax/bsl-language-server/blob/develop/src/main/java/com/github/_1c_syntax/bsl/languageserver/reporters/JsonReporter.java)
- [Release-specific runtime requirements](https://1c-syntax.github.io/bsl-language-server/en/systemRequirements/)
