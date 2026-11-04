# Web markup, CSS and framework checks

Adoption profile, reviewed on 2026-11-04. Add these checks only for technologies
present in the target project, alongside its JavaScript/TypeScript checks.

## CSS and complete HTML documents

Merge `package.fragment.json` into the real manifest and merge the corresponding
configuration files. Its scripts are intended for **authored plain CSS and full HTML
documents**. Scope globs and ignore lists to real source paths so generated output
and dependencies are not linted as first-party source. Do not silently exclude
application markup that needs a framework-specific parser.

Pinned and executed versions:

| Tool | Version | Runtime requirement from installed metadata |
| --- | --- | --- |
| Stylelint | 18.0.0 | Node `^22.22.2 || ^24.15.0 || >=26.0.0` |
| stylelint-config-standard | 41.0.0 | Same Node range; Stylelint `^18.0.0` |
| HTML-validate | 11.18.0 | Node `^22.22.0 || >=24.8.0` |

The combined profile was tested on Node **24.22.1**. Do not assume the lower Node
requirement of ESLint also satisfies these packages. Install with the project's
existing package manager and commit its lockfile.

```bash
npm run check:css
npm run check:html
```

Stylelint extends its standard config, treats warnings as failures, ignores
`stylelint-disable` comments, and rejects `!important` and ID selectors. Those last
two constraints are an explicit CSS-maintenance policy, not universal correctness
rules; evaluate them against the project's existing CSS architecture. For SCSS use
[stylelint-config-standard-scss](https://github.com/stylelint-scss/stylelint-config-standard-scss)
and its supported syntax. Tailwind and other custom syntaxes need their actual
integration rather than globally disabling unknown-at-rule checks.

HTML-validate enables recommended rules and checks that need a complete document;
its Prettier compatibility preset removes formatter conflicts. Do not apply the
full-document preset directly to partial component templates. Use the appropriate
framework parser or validate rendered HTML. Static a11y checks cover only the
patterns they recognize; keyboard behavior and accessible interaction still need
application tests and manual inspection.

## Framework integrations

The following are researched adoption routes, **not preconfigured or executed
framework profiles**. Use the versions compatible with the target framework and
adapt its existing config before adding these typed rules.

| Stack | Main route | Strict additions / type checking |
| --- | --- | --- |
| React / React Native | [Official eslint-plugin-react-hooks](https://react.dev/reference/eslint-plugin-react-hooks), `recommended` | Keep all hook/compiler diagnostics blocking. For web JSX add [jsx-a11y `flatConfigs.strict`](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y); map custom components so the rules see their real semantics. |
| Vue | [eslint-plugin-vue](https://eslint.vuejs.org/user-guide/), `flat/recommended` | Preserve `vue-eslint-parser`; put the TS parser in `parserOptions.parser`. Run [vue-tsc](https://vuejs.org/guide/typescript/overview) for SFC type checks. |
| Svelte / SvelteKit | [Official eslint-plugin-svelte](https://sveltejs.github.io/eslint-plugin-svelte/user-guide/), `recommended` | Follow the actual Svelte/SvelteKit version's parser/config setup and run its Svelte-aware type checker. The upstream `all` preset is explicitly not recommended. |
| Angular | [angular-eslint](https://github.com/angular-eslint/angular-eslint/blob/main/docs/CONFIGURING_ESLINT.md) | Combine TS, template-recommended and template-accessibility configs; process inline templates. Enable [strictTemplates and strictInjectionParameters](https://angular.dev/reference/configs/angular-compiler-options) in the actual compiler config. |

Do not install all four frameworks' plugins into an unrelated project. A simple
`.ts` glob cannot validate a Vue/Svelte template or an Angular inline template.

## Verification performed

The pinned Stylelint and HTML-validate packages loaded the supplied configs. Clean
CSS and a complete HTML fixture passed. Unknown CSS properties and
`!important` failed even behind a disable comment; duplicate HTML IDs failed.
The shipped MJS/JSON files passed Prettier. These checks did not exercise SCSS,
Tailwind, JSX, Vue, Svelte or Angular integration.

## Primary sources

- [Stylelint setup](https://stylelint.io/user-guide/get-started/).
- [Standard CSS config](https://github.com/stylelint/stylelint-config-standard).
- [Stylelint options, disable comments and warning budget](https://stylelint.io/user-guide/options/).
- [Stylelint configuration](https://stylelint.io/user-guide/configure/).
- [No-important rule](https://stylelint.io/user-guide/rules/declaration-no-important/).
- [ID-selector limit](https://stylelint.io/user-guide/rules/selector-max-id/).
- [HTML-validate presets](https://html-validate.org/rules/presets.html).
- [HTML-validate CLI and warning budget](https://html-validate.org/usage/cli.html).

Framework-specific primary sources are linked in the table above.
