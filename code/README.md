# Reproduction Code

## Environment

Validated during Stage 0 with Python `3.13.5`. The transferred scripts use only the Python standard library; no SymPy, NumPy, external API, random number generator, or network access is required. Execution is deterministic.

## Scripts

### `independent_reconstruction.py`

Purpose: independent Stage-2 reconstruction from model primitives. It rebuilds the output-stage equilibrium, constructs quadratic first-stage objectives, solves noncooperative and cooperative R&D FOCs, reproduces the published calibration, compares against independently transcribed published closed forms, and checks the admissible counterexample and local feasibility/curvature diagnostics.

Origin: `ryotamatsuki/economic-theory-replication-audit/code/C019_ishikawa_shibata_2021_audit.py`.

Canonical status: audit-history source remains the master repository; this dedicated copy is the publication-facing reproducibility asset after Stage 0 transition.

### `consequence_audit.py`

Purpose: Stage-3 consequence route using the paper's published closed-form R&D solutions. It recomputes individual and aggregate regime boundaries, the symmetric crossing, the strict counterexample, grid-based misclassification proxies, and selected Observation-6 branch checks.

Origin: `ryotamatsuki/economic-theory-replication-audit/code/C019_stage3_consequence_audit.py`.

Canonical status: audit-history source remains the master repository; this dedicated copy is the publication-facing reproducibility asset after Stage 0 transition.

## Canonical numerical checks

For `lambda=0, beta_2=0`:

| gamma | individual trigger | aggregate boundary `beta_1*` |
|---:|---:|---:|
| 10 | 0.481810774795 | 0.966879034253 |
| 50 | 0.496610118264 | 0.993346870078 |
| 100 | 0.498319321444 | 0.996670210259 |

Admissible counterexample `a=100,c=50,gamma=10,lambda=0,beta_1=0.98,beta_2=0`:

- aggregate noncooperative R&D: `3.593012699648`
- aggregate cooperative R&D: `3.629896961138`
- difference: `-0.036884261490`

Symmetric crossing:

`b(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)`.

## Stage-0 validation

Both computational routes reproduced the canonical values above to numerical precision. No requirements file is needed because both scripts are standard-library-only.
