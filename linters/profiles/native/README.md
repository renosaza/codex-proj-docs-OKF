# Additional language recipes

These are ecosystem-specific starting points, not a claim that every possible
language has a universal linter. Install only tools for languages actually used,
pin compatible versions, and record the working command in the target project.
These language checks apply to relevant source changes; documentation-only work
does not require creating a new build or test target.

| Language | Established tool / gate | Adoption requirement |
| --- | --- | --- |
| Zig | `zig fmt --check .`; compiler and tests in Debug/ReleaseSafe | `zig build test` is a project-defined build step, not a universal built-in test target. Check `zig build --help`. A formatter is not a semantic linter; use the compiler and tests. |
| Elixir | Credo (`mix credo --strict`), compiler warnings as errors, Dialyxir | Install Credo/Dialyxir as development dependencies; `--strict` includes lower-priority enabled checks, not every disabled Credo check. Dialyzer requires a valid PLT and the project's types/specs. |
| Erlang | Compiler warnings as errors; `rebar3 xref`; `rebar3 dialyzer` | Configure the actual OTP version, dependencies and Dialyzer PLT. Type analysis is complementary to compilation and tests. |
| Lua | `luacheck .` plus StyLua check mode | Set the actual Lua/LuaJIT standard and explicit allowed host globals. Lua embedded in an application needs that application's environment model. |
| Luau | Official `luau-analyze` with strict mode; StyLua | Use Luau tooling, not Lua-only syntax assumptions. Configure host types for the actual application. |
| R | lintr; `R CMD check` for packages | Make lints fail: `LINTR_ERROR_ON_LINT=true Rscript -e 'lintr::lint_dir(".")'` in a POSIX shell. Some semantic checks need installed/loaded package dependencies. |
| Haskell | HLint + GHC warnings as errors | `hlint .`; set `-Wall -Wcompat -Werror` in the project's compiler policy. HLint does not replace type checking and can suggest transformations with changed edge-case semantics. |
| Julia | JET + Aqua; JuliaFormatter | Integrate `JET.test_package` and `Aqua.test_all` with the actual package/test environment. A printed `JET.report_package` result alone is not a failure gate. Match JET to Julia's compiler version. |
| Perl | Perl::Critic (`perlcritic --brutal .`), syntax check, Perl::Tidy | `--brutal` selects the strictest severity range. Tune policies for the real Perl version; syntax checks can execute compile-time blocks. |
| Clojure / ClojureScript | clj-kondo | `clj-kondo --lint src test` after selecting existing roots. Model project macros and dependencies before trusting unresolved-symbol results. |
| OCaml | Compiler warnings + Dune checks; ocamlformat | Use the project's Dune warning policy and formatting alias. Do not copy compiler warning letters across incompatible compiler versions. |
| Fortran | Compiler diagnostics (GFortran or Flang) | Configure warnings as errors for the actual language standard/build. Runtime checks and tests cover additional failures; no invented all-purpose linter is bundled. |

This review did not establish a universally adopted standalone Zig linter; the
Zig recipe therefore uses its first-party compiler and formatter. Preserve safety
checks in validation builds. A successful formatter run
cannot certify cryptography, networking behavior, unsafe pointer use or hardware
integration. `ReleaseFast` alone is not a substitute for a checked build.

Commands above require their runtimes and project dependencies. They were
researched from upstream documentation, but these language runtimes were not
available to run application-level checks in this environment. A missing tool
or missing project-specific build target is an unresolved setup issue, not a pass.

## Primary sources

- [Zig language and build documentation](https://ziglang.org/documentation/).
- [Credo strict mode](https://credo.hexdocs.pm/cli_switches.html) and [Dialyxir](https://github.com/jeremyjh/dialyxir).
- [Rebar3 analysis commands](https://rebar3.org/docs/commands/).
- [Luacheck](https://github.com/lunarmodules/luacheck), [Luau type checking](https://luau.org/typecheck) and [StyLua](https://github.com/JohnnyMorganz/StyLua).
- [lintr CI behavior](https://lintr.r-lib.org/articles/continuous-integration.html).
- [HLint](https://github.com/ndmitchell/hlint) and [GHC warnings](https://ghc.gitlab.haskell.org/ghc/doc/users_guide/using-warnings.html).
- [JET analysis](https://aviatesk.github.io/JET.jl/stable/jetanalysis/) and [Aqua](https://juliatesting.github.io/Aqua.jl/stable/).
- [Perl::Critic CLI](https://metacpan.org/pod/perlcritic).
- [clj-kondo](https://github.com/clj-kondo/clj-kondo).
- [Dune formatting](https://dune.readthedocs.io/en/stable/howto/formatting.html).
- [GFortran warnings](https://gcc.gnu.org/onlinedocs/gfortran/Error-and-Warning-Options.html).
