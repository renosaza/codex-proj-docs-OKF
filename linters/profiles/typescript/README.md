# JavaScript / TypeScript: ESLint + typescript-eslint + tsc

Adoption profile, reviewed on 2026-11-04. The TypeScript scope combines
`strictTypeChecked` and `stylisticTypeChecked`. ESLint and `tsc` run separately:
type-aware linting does not replace compiler diagnostics. Prettier checks formatting.

## Runtime and installation

`package.fragment.json` records the exact versions used in the smoke checks:
ESLint **10.14.0**, `@eslint/js` **10.0.1**, typescript-eslint **8.72.1**,
TypeScript **6.0.3**, and Prettier **3.9.10**. ESLint requires Node
**`^20.19.0 || ^22.13.0 || >=24`**. Tests used Node **24.22.1** on Linux.
The checked typescript-eslint documentation supports TypeScript **`>=4.8.4 <6.1.0`**;
this strict compiler fragment uses options requiring TypeScript **5.6+**.
Frameworks and additional plugins can impose narrower version ranges.

1. Merge `package.fragment.json` into the real `package.json`; preserve existing
   scripts and dependencies. Install with the repository's existing package manager
   and commit its lockfile. The fragment is not a second package or an installer.
2. Merge `eslint.config.mjs` into the configuration at the target project's root.
   Typed rules are deliberately restricted to `.ts/.tsx/.mts/.cts`. JavaScript,
   including the config itself, gets core checks without a TypeScript project service.
3. Merge `tsconfig.strict.json` compiler options into the real application/test
   configs, or extend it. Preserve the framework's module, target, JSX and resolver
   options. Every TypeScript source and test must belong to the correct TS project.
4. Add only real generated/build paths to ignores. `.vue`, `.svelte` and Angular
   templates need their own integrations in the [web profile](../web/README.md).

For an npm project, after merging and generating the lockfile:

```bash
npm ci
npm run check:lint
npm run check:types
npm run check:format
```

The scripts run `eslint . --max-warnings 0`, `tsc --noEmit`, and
`prettier --check .`. Wire each into a blocking CI job and keep existing tests.
For project references, use the repository's real build/typecheck command that
checks all referenced projects rather than only a solution config with no files.

## AI-relevant checks

- Unsafe `any` operations and misused promises are covered by the typed presets.
- `no-floating-promises` also checks thenables and rejects `void promise` as an
  escape. Handle rejection explicitly or await the operation.
- `no-unsafe-type-assertion` rejects assertions that narrow a type without evidence.
  Validate untrusted input instead of forcing it into the desired type.
- Strict boolean expressions make ambiguous truthiness explicit. Switches over
  unions must handle every member; a `default` does not make them exhaustive.
- `noInlineConfig` prevents ESLint disable/config comments from taking effect.
  `@ts-ignore`, `@ts-nocheck` and `@ts-expect-error` are rejected in TypeScript files.
  A deliberate negative type test needs a separately reviewed test policy.
- `strict` plus indexed-access and exact-optional-property checks catches undefined
  array/map lookups and conflating an absent property with an explicit `undefined`.
- Complexity **10**, nesting **4**, and parameters **5** are kit policy limits. They
  are review triggers, not proof that code is correct; avoid ceremonial abstractions
  and meaningless parameter objects just to satisfy a threshold.

## Adapting to a real runtime

For JavaScript browser or Node APIs, declare the correct `globals` only in matching
files. For example, a browser-only config must not make `window` valid in server
code. TypeScript obtains globals from its actual compiler libraries and installed
types. Do not disable `no-undef` globally as a substitute for runtime configuration.

To type-check application JavaScript, enable `allowJs` and `checkJs` in the actual
TS project and extend the typed ESLint scope to those source files. Keep tooling
config files in the untyped scope. The supplied JS scope is syntax/correctness
linting; it does not claim the same semantic coverage as checked TypeScript.

If the project service reports a file outside its TS project, correct the actual
project membership. Do not add a broad `allowDefaultProject` pattern or disable
type-aware linting to make CI pass. Existing configs can override extended options;
inspect the final resolved config during adoption.

## Optional additions

| Need | Established tool | Adoption condition |
| --- | --- | --- |
| More modern JavaScript/API conventions | [eslint-plugin-unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn) | Scope rules to the actual runtime; current upstream requires ESLint 10.4+ and ESM. |
| More bug, duplication and cognitive-complexity checks | [eslint-plugin-sonarjs](https://github.com/SonarSource/SonarJS/blob/master/packages/analysis/src/jsts/rules/README.md) | Review overlap with existing rules; use the current SonarJS repository, not the archived plugin repository. |
| Unused files, exports and dependencies | [Knip](https://knip.dev/overview/getting-started) | Configure real entry points and framework plugins before deleting reported exports. |
| A different integrated formatter/linter | [Biome](https://biomejs.dev/linter/domains/) | Its type-informed rules and engine differ; retain `tsc` and verify required rule coverage before replacing ESLint. |

These additions are researched alternatives and are not installed by this profile.

## Verification performed

The pinned tools loaded the supplied flat config and checked mixed JavaScript and
TypeScript, including `eslint.config.mjs` outside the TS project. A clean fixture
passed ESLint and `tsc`. Negative fixtures failed for a discarded promise, an unsafe
assertion, `eslint-disable`, `@ts-expect-error`, and an unchecked array access. The
shipped MJS/JSON files passed Prettier. No framework integration run is claimed.

## Primary sources

- [ESLint runtime requirements](https://eslint.org/docs/latest/use/getting-started).
- [ESLint linter options and file scopes](https://eslint.org/docs/latest/use/configure/configuration-files).
- [CLI warning budget and exit codes](https://eslint.org/docs/latest/use/command-line-interface).
- [Typed presets and their versioning](https://typescript-eslint.io/users/configs/).
- [Typed project service setup](https://typescript-eslint.io/getting-started/typed-linting/).
- [Supported dependency versions](https://typescript-eslint.io/users/dependency-versions/).
- [Unhandled promises and the void caveat](https://typescript-eslint.io/rules/no-floating-promises/).
- [Unsafe assertions](https://typescript-eslint.io/rules/no-unsafe-type-assertion/).
- [Strict boolean expressions](https://typescript-eslint.io/rules/strict-boolean-expressions/).
- [Exhaustive switches](https://typescript-eslint.io/rules/switch-exhaustiveness-check/).
- [TypeScript suppression comments](https://typescript-eslint.io/rules/ban-ts-comment/).
- [TypeScript compiler options](https://www.typescriptlang.org/tsconfig/).

The strict typed presets may change outside major releases. Pin versions and review
the diff when upgrading; never quietly accept a relaxed configuration.
