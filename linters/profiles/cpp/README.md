# C, C++, Objective-C and CUDA

Use **clang-tidy** for compiler-aware diagnostics and the Clang Static Analyzer.
[.clang-tidy](.clang-tidy) enables strict, general C/C++ rule families and makes
their warnings fatal. **Cppcheck** is an optional complementary analyzer;
clang-format handles formatting.

## Adopt and run

Merge the configuration at the source root. Pin LLVM tools to a version that
understands the project's compiler, language standard and target. Supply a real
`compile_commands.json`, including include paths, defines and generated headers.

For a CMake project using a generator that supports compilation databases:

```sh
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build
clang-tidy --verify-config
run-clang-tidy -p build
```

`run-clang-tidy` is LLVM's companion script; distributions may provide it with
a version suffix or a `.py` suffix. It runs on the database, not just files named
in a hand-maintained list. Generate required headers before analyzing. For other
build systems, export the real database instead of fabricating compiler flags.

An optional second pass, after installing a pinned Cppcheck version:

```sh
cppcheck --project=build/compile_commands.json --enable=all --error-exitcode=1
```

Configure the actual platform, library models and source scope. Fix missing
includes before trusting the result. `--inconclusive` may be added for an
explicitly reviewed deeper pass; its extra findings can be false positives.

## Adaptation boundaries

This is intentionally demanding: modernization, ownership, bounds and naming
rules may require a documented project policy. Do not adopt project-specific
rule families such as `google-*`, `llvm-*` or `fuchsia-*` indiscriminately.
`HeaderFilterRegex: '.*'` includes every non-system header; narrow it to owned
headers if the compilation database contains vendored code, without excluding
handwritten application code. For C, select the applicable families; C++ rules
do not create C++ semantics in C sources.

For Objective-C, add the applicable `objc-*` checks after checking the SDK's
toolchain. CUDA requires Clang-compatible CUDA flags and toolkit paths; an NVCC
database may need adaptation. Compiler warnings (`-Wall -Wextra -Werror`, then
reviewed stricter flags), sanitizers and tests remain separate checks.

The YAML was parsed when added. LLVM, Cppcheck and a real compilation database
were unavailable; parser success is not a completed static analysis run.

## Primary sources

- [clang-tidy configuration, compile database and CUDA](https://clang.llvm.org/extra/clang-tidy/).
- [Available check families](https://clang.llvm.org/extra/clang-tidy/checks/list.html).
- [CMake compilation database](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html).
- [Cppcheck manual](https://cppcheck.sourceforge.io/manual.html).
