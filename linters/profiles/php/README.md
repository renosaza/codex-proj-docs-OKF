# PHP

Use **PHPStan at `max` + phpstan-strict-rules**. The supplied
[phpstan.neon](phpstan.neon) also checks property initialization, uncertain array
offsets and less certain union types. This is semantic/type analysis, not a
formatter. PHP_CodeSniffer or PHP-CS-Fixer can enforce the existing style policy.

## Adopt and run

Install development dependencies in the target project's Composer environment
and commit its lockfile:

```sh
composer require --dev phpstan/phpstan phpstan/phpstan-strict-rules
```

Merge the config into the project root. The include path assumes `vendor/` is
there. If `phpstan/extension-installer` already loads strict-rules automatically,
avoid loading it twice. Install the appropriate PHPStan framework extension for
Laravel, Symfony, Doctrine or another framework actually in use.

Use real source/test directories, adjusting `src tests` if the layout differs:

```sh
vendor/bin/phpstan analyse --configuration=phpstan.neon --no-progress src tests
```

At the source review date, `max` resolves to level 10. It can become stricter on
an upgrade, so dependency upgrades require a real analysis run. Commit compatible
versions, not a fresh dependency resolution inside every CI execution. Tests and
PHP's runtime `declare(strict_types=1)` remain separate concerns.

Do not generate a baseline automatically to make a failed check pass. Existing
baseline entries and narrow ignores must have a reviewed justification; unmatched
ignores are reported. Psalm is another established analyzer; it is an alternative
or deliberate extra pass, not a required duplicate installation.

The settings were checked against PHPStan's official references. PHP and Composer
were unavailable; this NEON file has not been parsed by PHPStan or tested on an
application in this environment.

## Primary sources

- [Rule levels and stricter options](https://phpstan.org/user-guide/rule-levels).
- [Configuration reference](https://phpstan.org/config-reference).
- [Official strict-rules extension and loading](https://github.com/phpstan/phpstan-strict-rules).
- [PHP_CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer).
- [Psalm](https://psalm.dev/docs/).
