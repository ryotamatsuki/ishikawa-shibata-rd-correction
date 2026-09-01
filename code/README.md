# Reproduction and Formal-Verification Code

## Environments

### Stage-0 reproduction routes

Validated with Python `3.13.5`. `independent_reconstruction.py` and `consequence_audit.py` use only the Python standard library. They are deterministic and require no network access.

### Stage-2 formal derivation

Validated with Python `3.13.5` and SymPy `1.14.0`. Dependency is pinned in repository-root `requirements.txt`. The script is deterministic and requires no network access.

## Scripts

### `independent_reconstruction.py`

Purpose: independent reconstruction from model primitives. It rebuilds the output-stage equilibrium, constructs quadratic first-stage objectives, solves noncooperative and cooperative R&D FOCs, reproduces the published calibration, compares against independently transcribed published closed forms, and checks the admissible counterexample and local feasibility/curvature diagnostics.

Origin: `ryotamatsuki/economic-theory-replication-audit/code/C019_ishikawa_shibata_2021_audit.py`.

### `consequence_audit.py`

Purpose: consequence route using the paper's published closed-form R&D solutions. It recomputes individual and aggregate regime boundaries, the symmetric crossing, the strict counterexample, grid-based misclassification proxies, and selected Observation-6 branch checks.

Origin: `ryotamatsuki/economic-theory-replication-audit/code/C019_stage3_consequence_audit.py`.

### `formal_derivation.py`

Purpose: exact Stage-2 symbolic verification of the three frozen correction propositions. It:

- derives the cleared individual equality polynomial on `lambda=0,beta_2=0`;
- verifies an exact regular root and `d beta*/d gamma=-9/59`;
- verifies the exact symmetric crossing factorization;
- derives the aggregate `(s,d)` factorization on the published line;
- isolates a unique regular aggregate root at `G=2` and proves its local gamma dependence;
- evaluates the Proposition-3 counterexample with exact rational arithmetic;
- checks exact positivity/curvature certificates at the proof-support points.

Expected terminal marker: `STAGE2_FORMAL_DERIVATION_PASS`.

Canonical proof record: `manuscript/FORMAL_DERIVATIONS.md`.

## Canonical numerical checks

For `lambda=0, beta_2=0`:

| gamma | individual trigger | aggregate boundary `beta_1*` |
|---:|---:|---:|
| 10 | 0.481810774795 | 0.966879034253 |
| 50 | 0.496610118264 | 0.993346870078 |
| 100 | 0.498319321444 | 0.996670210259 |

Counterexample `a=100,c=50,gamma=10,lambda=0,beta_1=0.98,beta_2=0`:

- aggregate noncooperative R&D: `3.593012699648`
- aggregate cooperative R&D: `3.629896961138`
- difference: `-0.036884261490`

Stage 2 upgrades the counterexample sign to the exact rational identity

`D_A=-23562520/638823147<0`.

Symmetric crossing:

`b(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)`.
