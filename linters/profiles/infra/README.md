# Infrastructure and CI

Merge only the files relevant to the target project. Pin binaries, provider
plugins and container images through its existing tool setup. Commands below
assume tools are installed and paths are replaced with the project's real paths.

| Area | Tool and strict check | Configuration or prerequisite |
| --- | --- | --- |
| Dockerfiles | `hadolint Dockerfile` | `.hadolint.yaml`: fail through `style`, ignore inline suppression pragmas. |
| GitHub Actions | `actionlint` | Run from the repository root; install ShellCheck for embedded shell checks. |
| Terraform | `terraform fmt -check -recursive`, then `terraform validate` | Initialize dependencies with `terraform init -backend=false`; commit provider lockfile. |
| OpenTofu | `tofu fmt -check -recursive`, then `tofu validate` | Initialize with `tofu init -backend=false`; use the actual target version. |
| Terraform conventions | `tflint --recursive --config "$(pwd)/.tflint.hcl" --minimum-failure-severity=notice` | `.tflint.hcl` enables the bundled Terraform plugin's `all` preset. |
| Ansible | `ansible-lint --strict` | `.ansible-lint.yaml`: `production`, no warning-only rule list; install real collection dependencies. |
| Kubernetes manifests | `kubeconform -strict -summary manifests/` | Pin the cluster schema version with `-kubernetes-version`; supply CRD schemas. |
| Helm charts | `helm lint --strict charts/my-chart` | Check real values combinations; schema-check rendered manifests too. |

The TFLint example uses a POSIX shell at the repository root. The absolute root
configuration path applies the same configuration to every inspected module. In
PowerShell, supply the actual resolved absolute path instead of POSIX substitution.
`tflint --init` installs configured external plugins; pin their versions before
adding cloud provider plugins. A bundled Terraform ruleset alone cannot validate
all provider-specific behavior. Confirm compatibility with OpenTofu features
before applying TFLint to an OpenTofu project.

The Terraform/OpenTofu `validate` commands check configuration, not deployed
infrastructure. Run `validate` for each independently initialized root module;
recursive formatting does not make validation recursive. Use `-lockfile=readonly` on CI initialization after establishing
the lockfile. Kubeconform must fail on a missing schema; do not add
`-ignore-missing-schemas` to obtain a passing run. It validates schemas, not live
cluster policy. Ansible's `production` profile includes collection/publication
requirements; adopt those consciously for playbook-only repositories.

See [optional aggregators](aggregators.md) for broad monorepo orchestration and
[security](../security/README.md) for IaC security checks.

## Sources

- [Hadolint configuration and thresholds](https://github.com/hadolint/hadolint)
- [actionlint usage and exit codes](https://github.com/rhysd/actionlint/blob/main/docs/usage.md)
- [Terraform fmt](https://developer.hashicorp.com/terraform/cli/commands/fmt) and [validate](https://developer.hashicorp.com/terraform/cli/commands/validate)
- [OpenTofu validate](https://opentofu.org/docs/cli/commands/validate/)
- [TFLint CLI](https://github.com/terraform-linters/tflint), [recursive configuration paths](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/config.md) and [Terraform presets](https://github.com/terraform-linters/tflint-ruleset-terraform/blob/main/docs/configuration.md)
- [Ansible profiles](https://docs.ansible.com/projects/lint/profiles/), [configuration](https://docs.ansible.com/projects/lint/configuring/) and [strict mode](https://docs.ansible.com/projects/lint/usage/)
- [Kubeconform](https://github.com/yannh/kubeconform)
- [Helm lint](https://helm.sh/docs/helm/helm_lint/)
