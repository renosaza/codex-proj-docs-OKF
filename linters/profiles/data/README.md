# Configuration, documentation and API formats

Adopt only the relevant templates and pin tools in the target project's
existing dependency setup. Check source files with actual schemas when a
format has an application-specific contract; syntax or formatting alone does
not check whether the keys mean anything.

| Format | Tool and check | Adoption detail |
| --- | --- | --- |
| YAML | `yamllint --strict .` | Merge `.yamllint.yaml`; warnings must fail. Quote GitHub Actions' `on` key if the YAML truthiness rule flags it. |
| Markdown | `markdownlint-cli2` | Merge `.markdownlint-cli2.jsonc`; default rules, no inline disabling, dependencies excluded. |
| TOML | `taplo check` and `taplo fmt --check` | Add schema validation for files with a known contract. |
| JSON / YAML schemas | `check-jsonschema --schemafile schemas/config.schema.json config.json` | Example paths: supply a real, reviewed schema and the corresponding files. |
| OpenAPI / AsyncAPI | `spectral lint --fail-severity hint --fail-on-unmatched-globs api/openapi.yaml` | Merge `.spectral.yaml`; all reported severities block. |
| Protobuf | `buf lint` | Merge `buf.yaml`; `STANDARD` plus documentation checks, no comment ignores. |

With Taplo, use `taplo check --schema schemas/config.schema.json config.toml`
for a pinned local schema. Automatic schema catalogs are convenient locally;
vendor schemas when CI reproducibility matters. Neither an empty glob nor an
unrecognized schema should be accepted as coverage of a requested check.

The Buf profile intentionally leaves streaming RPCs available: the separate
`UNARY_RPC` category is a transport restriction, not a universal quality rule.
Add breaking-change checks against the project's real published schema when
the API has consumers. Review any existing module-level Buf lint overrides.

For other formats, use the corresponding established tool when relevant:
[GraphQL ESLint](https://the-guild.dev/graphql/eslint),
[Redocly CLI](https://redocly.com/docs/cli) for OpenAPI workflows,
[xmllint](https://gnome.pages.gitlab.gnome.org/libxml2/xmllint.html) with the real
XML schema, and [EditorConfig Checker](https://github.com/editorconfig-checker/editorconfig-checker)
for cross-editor whitespace contracts. These are catalog options, not installed
or enabled by copying this folder.

## Sources

- [yamllint configuration and strict exit behavior](https://yamllint.readthedocs.io/en/stable/configuration.html)
- [yamllint rules](https://yamllint.readthedocs.io/en/stable/rules.html)
- [markdownlint-cli2 configuration](https://github.com/DavidAnson/markdownlint-cli2)
- [Taplo validation](https://taplo.tamasfe.dev/cli/usage/validation.html) and [format checking](https://taplo.tamasfe.dev/cli/usage/formatting.html)
- [check-jsonschema usage](https://check-jsonschema.readthedocs.io/en/stable/usage.html)
- [Spectral rulesets](https://github.com/stoplightio/spectral) and [CLI failure levels](https://github.com/stoplightio/spectral/blob/develop/docs/guides/2-cli.md)
- [Buf lint configuration](https://buf.build/docs/lint/usage/)
