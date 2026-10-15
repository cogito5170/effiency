# AI Workload Control Plane — Port vertical slice

## Goal

Expose the existing Cloud Relay workflow as a governed Port self-service action,
with the Port model and action managed by Terraform.

## Constraints

- Port is the user-facing control plane; GitHub Actions remains an implementation detail.
- Do not put Port, GitHub, or model credentials in Git or Terraform variables files.
- Do not describe the system as distributed until queue, durable state, leases, retries,
  and multiple workers exist.
- GitOps governs long-lived platform configuration, not transient jobs used as a Git queue.

## Done

- Terraform defines an AI Job blueprint and Run AI Relay action.
- Action inputs match `.github/workflows/cloud-relay.yml`.
- Setup and security boundaries are documented.
- Terraform formatting/static validation is run when the CLI is available.

