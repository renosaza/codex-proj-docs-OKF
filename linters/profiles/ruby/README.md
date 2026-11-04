# Ruby and Rails

Use **RuboCop** with its standard cops, newly introduced cops enabled and strict
complexity limits. [.rubocop.yml](.rubocop.yml) is deliberately small and inherits
the installed RuboCop version's normal rule configuration.

## Adopt and run

Add RuboCop to the project's existing development/test Gemfile group, resolve
dependencies with Bundler and commit `Gemfile.lock`. Set `TargetRubyVersion` to
the actual supported Ruby when it cannot be inferred correctly. Merge this file
into the repository's existing `.rubocop.yml`.

```sh
bundle exec rubocop --fail-level info --display-cop-names
```

The explicit fail level includes style and complexity findings, not just errors.
Do not add `--auto-gen-config` to CI: it creates suppressions. Review all existing
inherited `.rubocop_todo.yml` exclusions before claiming complete coverage.

For Rails, RSpec, performance or Minitest rules, add only the corresponding
maintained RuboCop extension that the project uses. Follow the plugin loading
syntax supported by the locked RuboCop release. Sorbet or Steep can add type
checking where the project maintains their type annotations/signatures.

`EnabledByDefault: true` is available upstream, but a universal all-cops profile
can activate contradictory style policies and preview rules. This profile keeps
the established defaults, enables pending cops, and tightens the complexity
limits explicitly. These limits are kit policy and can require small functions
to be split only where doing so improves the code.

The YAML was parsed when added. Ruby/Bundler/RuboCop were unavailable; execute
the command on the actual project before treating it as a working gate.

## Primary sources

- [RuboCop cop settings and failure levels](https://docs.rubocop.org/rubocop/latest/configuration/cop_settings.html).
- [Versioning and pending cops](https://docs.rubocop.org/rubocop/versioning.html).
- [RuboCop Performance](https://docs.rubocop.org/rubocop-performance/).
- [RuboCop Rails](https://docs.rubocop.org/rubocop-rails/).
- [Sorbet](https://sorbet.org/docs/overview) and [Steep](https://github.com/soutaro/steep).
