# Codex output

- Added the Port-managed first vertical slice in `infra/port/`: provider constraints,
  `AI Job` blueprint, `Run AI Relay` action, GitHub workflow input mapping, outputs,
  and credential-safe setup instructions.
- Added `docs/ai-workload-control-plane.md` defining the control-plane boundaries and
  objective criteria required before claiming a distributed system.
- Reused `.github/workflows/cloud-relay.yml`; no duplicate runner or custom UI was added.
- Added a bounded OpenAI Responses API adapter for the `codex` route in
  `relay/cloud_job.py`; local CLI sessions are not reused or misrepresented.
- GitHub injects `OPENAI_API_KEY` and `OPENAI_MODEL` into the isolated container;
  the Port form now exposes only the implemented live route.
- Added live-adapter tests and Phase 2 setup/security documentation.
- Verification: all 100 Python tests pass; Terraform formatting passes. Terraform
  provider validation is blocked in the current sandbox during plugin startup.

Decision: Port owns self-service UX and policy, Terraform owns repeatable configuration,
and GitOps is reserved for long-lived desired state. Transient jobs remain events rather
than commits in a Git-backed queue.

Remaining: connect a Port account/GitHub integration and apply Terraform. Add Argo CD
only after a Kubernetes workload exists; add a provider API only with explicit budget,
timeout, and secret-store boundaries.
