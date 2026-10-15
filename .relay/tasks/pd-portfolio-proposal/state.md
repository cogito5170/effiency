# State

## Done

- User chose a PD portfolio project and removed AI workflow automation from scope.
- Codex drafted an Ibex + Sky130HD + ORFS concept with utilization and clock
  period experiments (concept only, in `notes/pd-portfolio/decision-log.md`).
- Runner check on 2026-10-14 now passes: claude, codex, and agy all respond.

## Earlier review attempts — invalid

- Two `relay run --only review` runs on 2026-10-14 both returned
  `VERDICT: CHANGES`. These reviews are void: they were caused by an artifact
  role definition error, not by authentication or a Claude connection problem.
  Only the review stage ran, so no proposal existed, and the read-only reviewer
  reviewed its own `out-claude.md`. Kept here as a record, not as findings.

## Decision

- Artifact roles are now fixed in `brief.md`: Codex (implement) writes
  `notes/pd-portfolio/project-proposal.md`, Claude (review) writes only the
  verdict in `out-claude.md`.
- `notes/pd-portfolio/project-proposal.md` is kept untracked until review so the
  reviewer receives its full content as a new file.

## Completed — 2026-10-14

- `relay run pd-portfolio-proposal --only implement review --max-iterations 2
  --review-max-turns 4` finished in one iteration.
- implement (codex, 97.5s) wrote `notes/pd-portfolio/project-proposal.md:1-157`
  and the change summary in `out-codex.md`.
- review (claude, 4.6s, 1 turn) returned `VERDICT: APPROVE` in `out-claude.md`:
  all eight required items present, 16-week scope, Apple Silicon ORFS Docker
  feasible, AI automation excluded, no signoff or tapeout claim.
- Verified: proposal non-empty (157 lines), sections 1-8 present, educational
  checks explicitly separated from commercial signoff at
  `notes/pd-portfolio/project-proposal.md:19,116,145`.
- Task closed. Final artifact: `notes/pd-portfolio/project-proposal.md`.

## Open items (execution, not proposal)

- Korean resume bullets at `notes/pd-portfolio/project-proposal.md:140-143`
  contain bracketed placeholders; fill them only with measured QoR numbers
  after the real ORFS runs.
- Docker/ORFS environment on the Mac is still unverified against the plan's
  week 1-2 setup steps.
