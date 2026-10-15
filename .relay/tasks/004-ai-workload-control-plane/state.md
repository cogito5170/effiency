# State

## Current slice

Port self-service form → GitHub Actions Cloud Relay dry-run, with Port configuration
managed by Terraform.

## Decisions

- Product name: AI Workload Control Plane.
- Port before Backstage to deliver a usable mobile interface within four months.
- Runtime jobs remain event-driven; GitOps is reserved for long-lived platform state.
- Argo CD is deferred until a Kubernetes runtime and deployable workload exist.

## Next

Configure `OPENAI_API_KEY` and `OPENAI_MODEL` in GitHub Actions, push the workflow,
apply the updated Port action, then invoke one `codex` advisory run from Port.

## Phase 2 implementation

- Added one tool-free OpenAI Responses API adapter for the `codex` cloud route.
- Added a 90-second timeout, 1,200-output-token ceiling, provider request metadata,
  usage accounting, and secret-free artifacts.
- Restricted the cloud UI to the only implemented live route; local Claude/Agy
  sessions are not presented as remotely available.
- Preserved `--dry-run` for validation without a model call.

