# PD portfolio project proposal

## Goal

Produce a hiring-oriented Physical Design portfolio proposal for a Korean
electrical/electronics bachelor's graduate with no prior RTL-to-GDS project
and roughly four months available.

## Roles and artifacts

| Stage | Agent | Writes |
|---|---|---|
| implement | Codex | `notes/pd-portfolio/project-proposal.md` (the deliverable) and a change summary in `out-codex.md` |
| review | Claude (read-only) | verdict and required changes in `out-claude.md` only |

- `notes/pd-portfolio/project-proposal.md` is the real final artifact. Nothing
  else counts as the deliverable.
- `out-codex.md` contains only Codex's change summary (what changed at
  `path:line`, decisions, remaining work) — never the proposal itself.
- `out-claude.md` contains only the review: an explicit `VERDICT: APPROVE` or
  `VERDICT: CHANGES` line plus numbered required changes. The reviewer must not
  write the proposal.
- On `CHANGES`, Codex revises the proposal and Claude reviews again. After at
  most two iterations the result is `APPROVE` or a list of concrete unresolved
  items.

## Candidate baseline

- Open-source Ibex 32-bit RISC-V RTL
- Sky130HD platform
- OpenROAD Flow Scripts (ORFS)
- Yosys synthesis and OpenROAD physical implementation
- Baseline RTL-to-GDS run
- Controlled core-utilization and clock-period experiments
- AI/agent automation explicitly excluded

## Constraints

- One deep portfolio project, not several shallow projects.
- Must be feasible on Apple Silicon macOS using the official ORFS Docker flow.
- The candidate is a beginner; commercial EDA tools are unavailable.
- Do not claim commercial signoff or tapeout readiness; distinguish educational
  DRC/timing checks from commercial signoff.
- The result must be defensible in a new-graduate PD/PnR interview.
- No AI or agent automation inside the PD project scope.
- Avoid oversized cores, custom CPU design, and broad parameter-search
  automation.

## Required proposal contents

`notes/pd-portfolio/project-proposal.md` must contain all eight items:

1. Hiring value of the Ibex + Sky130HD + ORFS baseline for an entry-level PD role.
2. At most two alternatives, and only if they are genuinely better.
3. One final recommended project and the reason for choosing it.
4. A realistic 16-week milestone plan.
5. QoR metrics to measure and the evidence artifacts to keep.
6. Technical interview questions the candidate must be able to defend.
7. Excess scope to remove.
8. Korean resume bullet sentences an electrical/electronics bachelor's new
   graduate can use without exaggeration.

## Completion criteria

- `notes/pd-portfolio/project-proposal.md` exists, is non-empty, and is the
  final artifact.
- All eight required items above are present.
- The proposal is specific enough to implement without another architecture
  round, but not needlessly verbose.
- Scope fits four months, runs on Apple Silicon with official ORFS Docker, and
  prioritizes employability over breadth.
- AI/agent automation is excluded; no commercial signoff or tapeout-readiness
  claim appears.
- `out-codex.md` holds only the Codex change summary.
- `out-claude.md` holds an explicit verdict and stays within 300 words per the
  repository relay protocol in AGENTS.md.
