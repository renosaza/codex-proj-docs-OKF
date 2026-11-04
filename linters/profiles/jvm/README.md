# JVM: Java, Kotlin and Scala

These checks need the real build classpath and compiler version. Merge them into
the existing Maven/Gradle/sbt configuration; an isolated source scan is not
equivalent to analyzing the built application.

| Language | Primary tools | Strict policy |
| --- | --- | --- |
| Java | Error Prone + NullAway; SpotBugs; Checkstyle | Compiler warnings as errors; NullAway `ERROR` on owned packages; SpotBugs maximum effort and low threshold; Checkstyle violations fail the build. |
| Kotlin / Android | detekt + ktlint; Android Lint for Android | Build on the default detekt rules, no ignored failures/baseline additions, type resolution where supported; ktlint in check mode; Android Lint warnings treated as errors. |
| Scala | Scalafix + Scalafmt + compiler warnings | SemanticDB/classpath for semantic rules, Scalafix check mode, compiler warning policy for the actual Scala version. |

## Java

Error Prone checks Java during compilation; NullAway adds nullness checks. Set
`-Xep:NullAway:ERROR` and configure the actual owned package scope (or the
documented null-marked mode). Java's `-Werror` makes warnings fatal. Do not use
`-XepAllErrorsAsWarnings` to force a successful build. Review optional Error
Prone checks individually and preserve the compiler/JDK compatibility requirements.

For SpotBugs configure `effort=Max`, a `Low` report/failure threshold and a
failing `check` task/goal. Generating only an HTML report does not block a build.
Checkstyle enforces a selected style ruleset; it is not a replacement for
semantic analysis. Wire all selected checks into the project's normal `check`
or `verify` lifecycle and verify that a deliberately bad fixture fails it.

## Kotlin / Android

For the stable detekt 1.23.x Gradle plugin, set `buildUponDefaultConfig = true`
and `ignoreFailures = false`, using the project's compatible pinned version.
Prefer its typed `detektMain`/`detektTest` tasks when the plugin provides them:

```sh
./gradlew detektMain detektTest
ktlint
```

Use the repository's ktlint Gradle task instead of the CLI when already installed.
Android variants and Kotlin Multiplatform have different tasks/source sets;
inspect `./gradlew tasks --all` and include every supported target. Android Lint
is an additional platform check. For Android's lint configuration use
`abortOnError = true` and `warningsAsErrors = true`.

At the source review date, detekt 2.0 documentation still describes alpha
releases. Do not copy its `--fail-on-severity` or `--analysis-mode` flags into a
1.23.x setup. `--all-rules` also activates unstable rules; it is an optional
review pass, not an automatically compatible preset.

## Scala

After installing compatible Scalafix/Scalafmt sbt plugins and selecting rules:

```sh
sbt "scalafixAll --check" scalafmtCheckAll
```

Semantic Scalafix rules need SemanticDB and a successful compile. Select the
compiler warning flags for the actual Scala 2/3 version; flags are not
interchangeable. Do not use a fixer command as the CI check or leave an empty
Scalafix ruleset and claim that code has been analyzed.

These are integration recipes, not a tested universal JVM build. No JDK,
Gradle/Maven/sbt project or Android SDK was available for execution here.

## Primary sources

- [Error Prone flags](https://errorprone.info/docs/flags) and [installation](https://errorprone.info/docs/installation).
- [NullAway configuration](https://github.com/uber/NullAway/wiki/Configuration).
- [SpotBugs Maven check configuration](https://spotbugs.github.io/spotbugs-maven-plugin/check-mojo.html).
- [Checkstyle](https://checkstyle.org/).
- [detekt 1.23.8 Gradle tasks](https://detekt.dev/docs/1.23.8/gettingstarted/gradle/) and [2.0 migration status](https://detekt.dev/changelog-2.0.0/).
- [ktlint CLI](https://ktlint.github.io/ktlint/latest/install/cli/).
- [Android Lint configuration](https://developer.android.com/studio/write/lint).
- [Scalafix installation](https://scalacenter.github.io/scalafix/docs/users/installation.html) and [Scalafmt installation](https://scalameta.org/scalafmt/docs/installation.html).
