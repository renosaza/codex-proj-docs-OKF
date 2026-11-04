# Rust

Use the official **Clippy** analyzer with `all`, `pedantic`, selected restriction
lints and compiler warnings as errors; use rustfmt for formatting.

## Adopt and run

Merge [Cargo-lints.toml](Cargo-lints.toml) into the package's `Cargo.toml`.
Manifest lint configuration requires Rust/Cargo 1.74 or newer. In a workspace,
use `[workspace.lints.rust]` and `[workspace.lints.clippy]` at the workspace root
instead, and add the following to **each member** that should inherit it:

```toml
[lints]
workspace = true
```

Pin the supported compiler and components in the project's existing toolchain
file. Install the components for that toolchain, then check from the workspace:

```sh
rustup component add clippy rustfmt
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace --all-targets
```

Check supported feature combinations and targets separately. Add `--all-features`
only if that combination is valid; mutually exclusive features must not be
combined merely to make the command look exhaustive. For libraries, retain
documentation tests with `cargo test --workspace --doc` as well.

## Strictness and limits

The profile rejects unchecked `unwrap`/`expect`, placeholder macros, debug macros
and undocumented unsafe blocks. Tests can return `Result` and use `?`; exceptions
must be narrow and reviewed. `unsafe_op_in_unsafe_fn` requires explicit unsafe
blocks but does not prove memory safety. `pedantic` deliberately has false
positives; valid exceptions require a reason rather than a blanket disable.

Never enable the whole `restriction` or `nursery` group. Upstream recommends
selecting relevant rules individually. `cargo audit` or `cargo deny` can add
dependency/security checks, but they do not replace Clippy or tests.

The TOML fragment was parsed when added. Rust/Clippy execution and a workspace
inheritance check must be performed in the adopting repository.

## Primary sources

- [Clippy configuration and manifest support](https://doc.rust-lang.org/clippy/configuration.html).
- [Lint group semantics and caveats](https://doc.rust-lang.org/clippy/lints.html).
- [Cargo lint inheritance](https://doc.rust-lang.org/cargo/reference/manifest.html#the-lints-section).
- [Clippy usage and warnings as errors](https://doc.rust-lang.org/clippy/usage.html).
