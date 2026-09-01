# Ishikawa–Shibata R&D Correction

## Target paper

Nana Ishikawa and Takashi Shibata (2021), “R&D competition and cooperation with asymmetric spillovers in an oligopoly market,” *International Review of Economics & Finance* 72, 624–642. DOI: `10.1016/j.iref.2020.12.016`.

## Project status

- Project type: third-party mathematical correction / comment project
- Origin: `C019` in `ryotamatsuki/economic-theory-replication-audit`
- Publication-gate status: `CORRECTION_CANDIDATE`
- Dedicated-repository status: `Stage 0 — Evidence Freeze`

## Confirmed correction

1. The published output-stage equilibrium and closed-form noncooperative/cooperative R&D solutions used in the audit remain valid.
2. The individual competition/cooperation boundary is the zero set `D_i=x_i^n-x_i^c=0` and generically depends on `gamma`; the symmetric crossing `b(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)` is a special gamma-independent cancellation.
3. The aggregate boundary is `D_A=(x_1^n+x_2^n)-(x_1^c+x_2^c)=0` and generically depends on `gamma` and spillover asymmetry; it is not generally a scalar line `beta_1+beta_2=theta(lambda)`.
4. The fixed average-spillover rule used in Observation 5 misclassifies a positive-measure admissible region.

## What is not being claimed

This project does not claim that the entire paper or its published closed-form equilibrium formulas are wrong; does not establish a welfare-ranking reversal, an empirical-estimate change, or a downstream-literature effect; does not overturn Proposition 1, Proposition 2, or Observation 6; and does not assert absolute novelty. See `CLAIM_BOUNDARY.md`.

## Reproducibility

Publication-facing reproduction assets are under `code/`. Stage 0 transfers the audited scripts with provenance preserved and validates the canonical numerical checks before manuscript drafting.

## Repository structure

- `PROJECT_STATUS.md` — stage and gate status
- `PROVENANCE.md` — source and repository lineage
- `EVIDENCE_MAP.md` — claim-to-evidence map
- `CLAIM_BOUNDARY.md` — allowed, qualified, and prohibited claims
- `NOVELTY_LOG.md` — publication-facing novelty record
- `code/` — reproducibility assets
- `results/` — controlled stage results
- `manuscript/` — manuscript workspace; no manuscript exists at Stage 0
- `submission/` — submission workspace; no submission materials exist at Stage 0

## Provenance

Master audit history remains canonical in `ryotamatsuki/economic-theory-replication-audit`; publication-facing derivations, manuscript assets, figures/tables, submission files, and journal-correspondence metadata become canonical in this repository after Stage 0 transition.

## Current next step

Complete `Stage 0 — Evidence Freeze`; if it passes, proceed to `Stage 1 — Manuscript Architecture and Proposition Freeze`.
