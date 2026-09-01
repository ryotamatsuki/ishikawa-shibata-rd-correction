# Equation Inventory — Stage 1

Status: `FROZEN_FOR_STAGE1`

This inventory identifies the equations needed by the correction note. It does not assign final manuscript equation numbers.

| Internal label | Source | Status | Manuscript role |
|---|---|---|---|
| `Q-OUT` | Ishikawa–Shibata Eqs. (8)–(9) | retained / reproduced | background only if needed to identify the model; do not re-derive in main text |
| `XN` | Ishikawa–Shibata Eqs. (16)–(20) | retained / independently checked | noncooperative R&D input |
| `XC` | Ishikawa–Shibata Eqs. (25)–(29) | retained / independently checked | cooperative R&D input |
| `DI` | dedicated correction definition | frozen | `D_i=x_i^n-x_i^c`; individual equality boundary `D_i=0` |
| `DA` | dedicated correction definition | frozen | `D_A=(x_1^n+x_2^n)-(x_1^c+x_2^c)`; aggregate equality boundary `D_A=0` |
| `SYM` | Stage-3 symbolic result | frozen, Stage-2 formal recheck required | symmetric crossing `b*(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)` |
| `NI` | to be derived in Stage 2 | proof obligation | cleared-denominator numerator for `D_i=0`; analytic gamma-dependence proof |
| `NA` | to be derived in Stage 2 | proof obligation | cleared-denominator numerator for `D_A=0` |
| `AGG-L0` | Stage-3 symbolic result | frozen, Stage-2 formal recheck required | at `lambda=0`, `beta_1+beta_2=1`, numerator proportional to `(beta_1-beta_2)^2[18 gamma-9+(beta_1-beta_2)^2]` |
| `IFT-I` | Stage-2 planned identity | proof obligation | local root derivative `d beta_i*/d gamma=-N_{i,gamma}/N_{i,beta_i}` on a regular asymmetric slice |
| `IFT-A` | Stage-2 planned identity | proof obligation | local aggregate-boundary derivative `d beta_1*/d gamma=-N_{A,gamma}/N_{A,beta_1}` on a regular slice |
| `CE-N` | Stage-2/3 canonical check | frozen numerical target | counterexample aggregate noncooperative R&D `3.593012699648` |
| `CE-C` | Stage-2/3 canonical check | frozen numerical target | counterexample aggregate cooperative R&D `3.629896961138` |
| `CE-D` | Stage-2/3 canonical check | frozen numerical target | counterexample `D_A=-0.036884261490` |

## Equation-use controls

1. The note must not reproduce the entire original model or all intermediate definitions from Eqs. (16)–(29).
2. Final manuscript exposition should quote or restate only the minimum retained formulas required to define `D_i` and `D_A` and make the correction self-contained.
3. `NI`, `NA`, `IFT-I`, and `IFT-A` are proof obligations, not yet canonical formulas. Stage 2 must derive and verify them before manuscript drafting.
4. Grid-based misclassification shares are deliberately excluded from the theorem equation inventory because they are illustrative, not proof inputs.
5. No equation in this inventory is a social-welfare function; aggregate R&D comparison must not be relabeled as welfare ranking.

## Numerical validation targets retained from Stage 0

For `lambda=0, beta_2=0`:

| gamma | individual trigger | aggregate boundary |
|---:|---:|---:|
| 10 | 0.481810774795 | 0.966879034253 |
| 50 | 0.496610118264 | 0.993346870078 |
| 100 | 0.498319321444 | 0.996670210259 |

These are regression/verification targets only. They do not substitute for the analytic proofs specified in `PROPOSITIONS.md`.
