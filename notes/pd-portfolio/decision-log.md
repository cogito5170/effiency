# PD portfolio decision log

## 2026-10-14

- Career target: entry-level Physical Design / PnR and adjacent implementation roles.
- Candidate background: electrical/electronics bachelor's degree; no prior RTL-to-GDS project.
- Time budget: approximately four months.
- Decision: remove AI workflow automation and prioritize one defensible PD project.
- Baseline under review: Ibex + Sky130HD + OpenROAD Flow Scripts.
- Planned evidence: reproducible baseline, utilization sweep, clock-period sweep,
  timing/area/congestion/DRC analysis, and a documented failure-resolution case.
- External design review: requested from Claude through relay task
  `pd-portfolio-proposal`.
- Relay project permissions now allow `relay run`, `relay auto`,
  `relay delegate`, `relay check`, and `relay why` without repeated Claude
  Bash approval prompts.
- Automatic runner diagnosis did not pass: the current non-interactive
  environment cannot access working Claude, Codex, or agy authentication.
  No Claude project proposal has been produced yet.
