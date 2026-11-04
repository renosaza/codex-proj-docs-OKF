# Dart / Flutter and Swift

## Dart and Flutter

Use the SDK analyzer with **Very Good Analysis**, an established strict preset.
Merge [analysis_options.yaml](analysis_options.yaml) into the package root,
preserving useful existing rules. The three strict type modes reject implicit
downcasts and missing type information in additional situations.

Install the preset once, then lock a version compatible with the actual SDK:

```sh
dart pub add dev:very_good_analysis
dart analyze --fatal-infos
dart format --output=none --set-exit-if-changed .
dart test
```

For Flutter, use `flutter pub add dev:very_good_analysis` for installation and
the project's `flutter analyze`/`flutter test` commands; ensure informational
diagnostics are fatal in its analyzer command. Keep the Dart formatting check.
Use the project's actual source roots if formatting `.` would include vendored
or generated code. If existing `flutter_lints` supplies framework-specific rules,
review the effective rules before replacing its include.

The preset intentionally omits rules that contradict other rules or the Dart
formatter. Enabling literally every lint is not a coherent style policy. Record
the resolved package/SDK versions and reject new blanket `ignore_for_file`
directives added to bypass checks.

## Swift / Apple platforms

Use **SwiftLint** with warnings made fatal, selected opt-in semantic rules and
the matching Swift/Xcode toolchain. Merge this minimum into `.swiftlint.yml`:

```yaml
strict: true
allow_zero_lintable_files: false
opt_in_rules:
  - force_unwrapping
```

```sh
swiftlint lint --strict
swift format lint --strict --recursive .
```

The `swift format` subcommand requires a toolchain that provides it; the
standalone official `swift-format lint --strict --recursive .` is the alternative.
Select one formatter and align any overlapping SwiftLint style rules. For deeper
SwiftLint analyzer rules, configure `analyzer_rules` and pass a clean build's
compiler log to `swiftlint analyze`; ordinary `lint` does not run those rules.
Run the project's SPM or Xcode build and tests with warnings as errors too.

Kotlin and Android-specific checks are covered by the [JVM profile](../jvm/README.md).
The Dart YAML was parsed when added. No Dart, Flutter, Swift or Xcode runtime was
available to execute these checks in this environment.

## Primary sources

- [Very Good Analysis usage and deliberate exclusions](https://pub.dev/packages/very_good_analysis).
- [Dart strict analysis modes](https://dart.dev/tools/analysis).
- [Dart fatal diagnostics](https://dart.dev/tools/dart-analyze) and [format check](https://dart.dev/tools/dart-format).
- [SwiftLint configuration and analyzer rules](https://github.com/realm/SwiftLint).
- [Official swift-format lint mode](https://github.com/swiftlang/swift-format).
