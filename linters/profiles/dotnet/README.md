# C# and Visual Basic / .NET

Use the **.NET SDK's Roslyn analyzers** with `latest-all`, nullable analysis for
C#, build-time style analysis and warnings as errors. This uses the platform's
existing analyzers before introducing another analyzer package.

## Adopt and run

Merge [Directory.Build.props](Directory.Build.props) into an SDK-style solution's
existing file; do not overwrite its build properties or imports. Pin the SDK in
`global.json`. For .NET 5+ targets the SDK analyzers are normally already enabled;
older targets and non-SDK projects need the official setup described below.

Merge this into the project's `.editorconfig` so style suggestions also become
build diagnostics:

```ini
[*.{cs,vb}]
dotnet_analyzer_diagnostic.category-Style.severity = warning
```

Run against the actual solution/project (pass its path if the directory contains
more than one):

```sh
dotnet build -warnaserror
dotnet format --verify-no-changes --severity info
dotnet test
```

`dotnet format` is a format/code-fix check; it is not a substitute for the build's
complete analyzer diagnostics. `latest-all` follows the pinned SDK's analyzer
set. A few legacy and code-metrics rules are still excluded by upstream and
must be enabled individually if needed; this is not literally every Roslyn rule.

If the repository already references `Microsoft.CodeAnalysis.NetAnalyzers`, keep
one analyzer source and resolve its version against the SDK. Do not blindly add
`EnableNETAnalyzers=true` alongside that package. Check project-level overrides
and existing `NoWarn`/`WarningsNotAsErrors`; a shared props file cannot stop later
MSBuild assignments from weakening the gate.

For **F#**, use compiler warnings as errors and the project's F# analyzers; these
C#/VB analyzer rules do not automatically analyze F#. Fantomas can provide the
formatting check.

The XML was parsed when added. The .NET SDK was unavailable; build, format and
test commands must be verified on the adopting solution.

## Primary sources

- [.NET analyzers, strict modes and style severities](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview).
- [SDK analysis properties](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props).
- [dotnet format verification mode](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format).
- [Fantomas](https://fsprojects.github.io/fantomas/).
