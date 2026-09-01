# Stage 0 Evidence Freeze

## Executive result

`STAGE0_PASS`.

C019's confirmed audit evidence has been transferred into the dedicated correction-paper repository with claims, novelty wording, consequence labels, provenance, reproducibility assets, and single-source-of-truth responsibilities frozen. No manuscript or submission materials were drafted.

## Source repository state

Dedicated repository: `ryotamatsuki/ishikawa-shibata-rd-correction`.

- visibility: private
- default branch: `main`
- repository was initially empty (`size=0`), so a minimal bootstrap README commit was required before a feature branch could exist
- bootstrap commit: `baf2a6140d28f00745db5f38ea3a28b06c918733`
- Stage 0 branch: `stage0/evidence-freeze`

Master audit repository: `ryotamatsuki/economic-theory-replication-audit`.

- Stage-0 transition starting commit: `85bb39f5310816d452bc8ca333180f06129e7984`
- C019 starting status: `CORRECTION_CANDIDATE`

## Master audit provenance

Canonical audit-history sources remain in the master repository:

- `CANDIDATE_REGISTRY.md`
- `cases/C019_ishikawa_shibata_2021.md`
- `results/C019_stage3_consequence_audit.md`
- `results/C019_protocol05_publication_gate.md`
- `code/C019_ishikawa_shibata_2021_audit.py`
- `code/C019_stage3_consequence_audit.py`
- `PRIOR_DISCLOSURE_LOG.md`

## Canonical claims frozen

A. Published output-stage and closed-form R&D equilibria used in the audit survive.

B. `D_i=x_i^n-x_i^c=0` generically depends on `gamma`; only the symmetric crossing `b(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)` is exactly gamma-independent.

C. `D_A=(x_1^n+x_2^n)-(x_1^c+x_2^c)=0` is generically gamma- and asymmetry-dependent and cannot generally be reduced to `beta_1+beta_2=theta(lambda)`.

D. Observation 5's fixed cutoff strictly misclassifies an admissible point, and continuity gives a positive-measure disagreement region.

## Claim boundaries frozen

`CLAIM_BOUNDARY.md` records allowed, qualified, and prohibited claims. In particular, this project does not claim paper-wide invalidity, equilibrium-formula failure, welfare-ranking reversal, empirical-estimate change, downstream-literature impact, global lambda nesting, or absolute novelty.

## Novelty status

`N-A — NO_PRIOR_DISCLOSURE_FOUND_UNDER_PUBLICATION_GRADE_SEARCH`.

Permissible statement only:

> No prior disclosure covering the same correction was found under the documented search protocol as of 2026-09-01.

## Consequence status

- `PARAMETER_REGION_CHANGED`
- `INTERPRETATION_CHANGED`
- severity: `LEVEL 3 — qualitative classification changes for admissible parameters`
- publication-value classification: `MEDIUM-HIGH`

Not assigned: `EQUILIBRIUM_CHANGED`, `WELFARE_RANKING_CHANGED`, `EMPIRICAL_ESTIMATE_CHANGED`.

## Reproducibility assets transferred

- `code/independent_reconstruction.py`
- `code/consequence_audit.py`
- `code/README.md`

The two routes remain conceptually independent: the first reconstructs from primitives; the second evaluates the published closed forms.

## Reproduction validation

Validated with Python 3.13.5, standard library only.

For `lambda=0,beta_2=0`:

| gamma | individual trigger | aggregate boundary |
|---:|---:|---:|
| 10 | 0.481810774795 | 0.966879034253 |
| 50 | 0.496610118264 | 0.993346870078 |
| 100 | 0.498319321444 | 0.996670210259 |

Counterexample `a=100,c=50,gamma=10,lambda=0,beta_1=0.98,beta_2=0`:

- aggregate noncooperative: `3.593012699648`
- aggregate cooperative: `3.629896961138`
- difference: `-0.036884261490`

Both the primitive reconstruction route and the published-closed-form route reproduce these values to numerical precision.

## Evidence map created

`EVIDENCE_MAP.md` maps Observation 1, Eq. (38), Table 1, Fig. 1(d), Observation 4, Eqs. (43)–(44), Fig. 3, Observation 5, Eqs. (45)–(46), Eq. (47), Fig. 4, and the third Introduction/Conclusion result to their audit evidence, verification status, consequence, and potential manuscript use.

## Single-source-of-truth allocation

Master repository remains canonical for candidate identity/status and Stage 2/3/Protocol-05 audit history. The dedicated repository becomes canonical for publication-facing derivations, manuscript, manuscript figures/tables, submission files, and journal-correspondence metadata after transition.

## Remaining uncertainties

- Novelty remains a documented-search result, not proof of absolute novelty.
- No Protocol-04 downstream citation-dependency audit has been performed.
- No global lambda-nesting theorem has been established.
- Journal selection has not been performed.

No `UNPLANNED_NEW_RESULT` was adopted into the Stage-0 claim set.

## Stage 0 gate

PASS criteria satisfied:

- dedicated repository initialized
- project identity fixed
- canonical claims fixed
- prohibited claims fixed
- novelty wording fixed
- reproducibility code transferred
- canonical values reproduced
- provenance recorded
- evidence map created
- single-source-of-truth allocation documented
- manuscript not drafted
- submission files not created
- master repository transition branch prepared

Decision: **`STAGE0_PASS`**.

## Recommended Stage 1 action

Proceed only after Stage-0 PRs are reviewed/merged. Next stage: `Stage 1 — Manuscript Architecture and Proposition Freeze`, limited to correction-note structure, proposition allocation, proof architecture, and manuscript scope control.
