# Stage 1 Manuscript Architecture and Proposition Freeze

## Executive decision

**Decision: `STAGE1_PASS`.**

The correction has been reduced to three publication functions and three bounded propositions. Each proposition has an analytic proof path; none is intended to rest solely on numerical evidence. The note remains a narrow third-party correction/comment: the published equilibrium formulas are retained, no welfare reversal is claimed, no model extension is required, and no manuscript prose has been drafted.

Starting main commit: `e4ebad8dffb9755ff94ebdceedb173b4dd0d06b8`.

Working branch: `stage1/manuscript-architecture`.

## Correction object

Frozen target:

1. Observation 1's generic gamma-invariance claim;
2. Observation 4's scalar aggregate threshold;
3. the global asymmetric interpretation of Eqs. (43)–(46);
4. Observation 5's fixed average-spillover cutoff classification.

Control sentence:

> The published equilibrium formulas are retained. The correction concerns the threshold characterizations and the parameter-region classifications derived from them.

## Minimum contribution

Exactly three contributions are frozen:

1. The individual competition/cooperation boundary is not gamma-invariant in general; the exact gamma-independent crossing is a special symmetric cancellation.
2. The aggregate equality set is not generally a scalar average-spillover threshold; its corrected characterization depends on spillover asymmetry and, in general, gamma.
3. The fixed average-spillover cutoff consequently misclassifies a positive-measure admissible parameter region.

The symmetric cancellation is explanatory value, not a fourth contribution.

## Frozen propositions

### Proposition 1 — Individual R&D boundary

Working conclusion: `D_i=x_i^n-x_i^c=0` is not gamma-invariant in general. Stage 2 will prove local gamma variation analytically on a regular asymmetric slice after clearing denominators and applying an implicit-function or equivalent exact argument. On `beta_1=beta_2=b`, the exact crossing is

`b*(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)`,

which is gamma-independent.

### Proposition 2 — Aggregate R&D boundary

Working conclusion: `D_A=0` is not generally equivalent to `beta_1+beta_2=theta(lambda)`. At `lambda=0` and on the published line `beta_1+beta_2=1`, the cleared numerator is proportional to

`(beta_1-beta_2)^2[18 gamma-9+(beta_1-beta_2)^2]`.

For maintained `gamma>=1`, no asymmetric point on that line satisfies aggregate equality. Stage 2 must additionally prove local gamma variation of the corrected aggregate zero set analytically on a regular asymmetric slice.

### Proposition 3 — Positive-measure classification error

At `a=100,c=50,gamma=10,lambda=0,beta_1=0.98,beta_2=0`, the published cutoff predicts aggregate competitive-R&D dominance, but retained equilibrium formulas give aggregate noncooperative R&D `3.593012699648`, cooperative R&D `3.629896961138`, and `D_A=-0.036884261490`. Stage-2 admissibility/regularity evidence plus strict inequality and continuity yield an open disagreement region and therefore positive measure.

## Proposition skeptical review

| Proposition | Exact claim | Proof type | Assumptions | What it does NOT prove | Editorial value |
|---|---|---|---|---|---|
| P1 | individual boundary not gamma-invariant in general; exact symmetric gamma-independent crossing | cleared-denominator algebra + regular-root implicit-function argument + exact symmetric factorization | retained closed forms, regular root, nonzero denominators | global uniqueness, monotonicity, inverted-U, global branch map | high: directly corrects Observation 1 and explains numerical appearance |
| P2 | aggregate scalar line fails generally; asymmetric points on published lambda-zero line fail equality; corrected locus varies with gamma locally | exact factorization + sign argument + local implicit-function argument | retained closed forms, `gamma>=1` for factorization consequence, regularity | global closed-form boundary, global monotonicity, convexity, lambda nesting | high: replaces published classification geometry |
| P3 | fixed cutoff reverses qualitative classification at an admissible point and on an open neighborhood | exact/high-precision substitution + admissibility + continuity | interior regular point, nonzero denominators | welfare reversal, economic magnitude, downstream impact | medium-high: establishes non-cosmetic consequence |

Assessment:

- No proposition is intentionally stronger than the Stage-0 evidence boundary.
- P1 and P2 are not numerical-only because their frozen proof paths require exact zero-set algebra.
- P3 uses a numerical parameter point but the publication claim is topological/qualitative: strict disagreement plus continuity gives positive measure.
- P2 is not an obvious restatement of original Proposition 2: the correction supplies the actual failure of the scalar boundary and the asymmetry factorization.

## Proof architecture

### P1

Retained closed forms → form `D_i` → clear denominators → derive exact asymmetric slice equation → verify regular gamma-dependent root analytically → implicit-function derivative nonzero → restrict to symmetry → exact factorization → symmetric crossing.

### P2

Retained closed forms → form `D_A` → clear denominators → set `lambda=0` → transform to `s=beta_1+beta_2`, `d=beta_1-beta_2` → substitute `s=1` → factor → positivity for `gamma>=1,d!=0` → separately show local gamma variation of corrected zero set on a regular asymmetric slice.

### P3

Published cutoff classification → substitute stated admissible point into retained closed forms → strict corrected sign → record local denominator nondegeneracy/admissibility → continuity of rational equilibrium objects → open disagreement neighborhood → positive measure.

Proof architecture status: **complete as an architecture; formal derivations remain Stage-2 obligations.**

## Lemma policy

Main-text lemma count: **0**.

Long algebra and regularity checks should go to an appendix. Introduce a lemma only if Stage 2 demonstrates that readability materially requires one; doing so would require an architecture update before drafting.

## Section architecture

Five main sections are frozen:

1. Introduction and correction target.
2. Model objects retained from Ishikawa and Shibata.
3. Corrected individual threshold.
4. Corrected aggregate threshold and classification.
5. Implications and surviving results.

Optional appendix: algebra, regularity, additional numerical verification, reproducibility provenance.

No completed introduction, abstract, conclusion or manuscript body has been written.

## Equation inventory

Canonical retained inputs: published `x_i^n`, `x_i^c`; correction definitions `D_i`, `D_A`; frozen symmetric crossing; frozen lambda-zero aggregate factorization; counterexample values.

Stage-2-only proof targets: exact cleared numerators `N_i`, `N_A` and local root-derivative identities. See `manuscript/EQUATION_INVENTORY.md`.

## Original-paper correction map

Central correction objects:

- Eq. (38) / Observation 1;
- Eqs. (43)–(44) / Observation 4;
- Eqs. (45)–(46) / Observation 5.

Interpretation-dependent objects: Table 1, Fig. 1(d), Fig. 3, Eq. (47)/Fig. 4, and the third headline result in Introduction/Conclusion.

Explicitly preserved: Eqs. (8)–(9), Eqs. (16)–(20), Eqs. (25)–(29), original Propositions 1–2 under the C019 dependency map, and Observation 6 at the published calibration.

## Figure / table policy

- Preferred main figures: **1**.
- Maximum main figures: **2**.
- Preferred main tables: **0**.
- Maximum main tables: **1**.

Preferred Figure A: corrected aggregate locus against published straight line at `lambda=0` for a small set of gamma values. It is illustration, not proof.

Optional Figure B: individual triggers for several gamma values showing the exact symmetric intersection; include only if it materially improves explanation after proof completion.

No figure or table files are created in Stage 1.

## Length budget

- Main text: 3,500–5,000 words.
- Propositions: 3.
- Figures: 1 preferred, 2 maximum.
- Tables: 0 preferred, 1 maximum.
- Appendix: algebra and reproducibility only.
- References: minimal.

Assessment: **feasible for a short Comment / Note** without re-deriving the full model.

## Referee kill test

| Kill | Assessment | Reason / architecture response |
|---|---|---|
| 1. Only small changes outside gamma=50? | `SURVIVES` | strict qualitative regime reversal and positive-measure disagreement; not merely numerical drift |
| 2. Equilibrium formulas are correct, so low value? | `SURVIVES` | note explicitly preserves them; publication value is correction of published general threshold/classification statements |
| 3. One counterexample only? | `SURVIVES` | P2 provides analytic factorization; P3 adds continuity-based positive-measure result |
| 4. Original Proposition 2 already mentions gamma? | `SURVIVES` | architecture treats that as a consistency point; the original proposition does not provide the corrected zero set or repair Observations 4–5 |
| 5. Fig. 3 line only bends slightly? | `SURVIVES` | at lambda=0 every asymmetric point on the asserted equality line fails equality under `gamma>=1`; issue is structural, not graphic styling |
| 6. Cutoff error economically negligible? | `SURVIVES_WITH_SCOPE_CONTROL` | no magnitude claim; qualitative classification is wrong on an open admissible set, which is sufficient for a correction note |
| 7. Numerical note only? | `SURVIVES` | P1/P2 require analytic zero-set and factorization proofs; numerics are verification/illustration |
| 8. Broad economic conclusion survives, so correction unnecessary? | `SURVIVES` | architecture explicitly says broad direction is qualified, not reversed; published fixed thresholds remain general claims that require correction |

No fatal kill condition. No architecture change is required before Stage 2.

## Editorial-value test

Scores: 1 = weak, 2 = adequate, 3 = strong.

| Dimension | Score | Reason |
|---|---:|---|
| Correction clarity | 3 | exact affected observations/equations isolated |
| Analytic content | 3 | two zero-set corrections with exact factorization / planned exact regular-root proof |
| Consequence | 3 | qualitative classification reversal on positive-measure admissible set |
| Brevity | 3 | three propositions, five sections, no model extension |
| Independence from model extension | 3 | uses retained published equilibria only |
| Reproducibility | 3 | two independent deterministic code routes already frozen |
| Editorial necessity | 2 | broad directional conclusion survives, but general published threshold statements require correction |

Total: **20/21**. No dimension scores 1.

## Unresolved proof obligations

1. Derive exact cleared-denominator `N_i` and prove analytic gamma dependence at a regular asymmetric root; numerical trigger movement alone is insufficient.
2. Independently re-derive the symmetric crossing factorization in a publication-grade symbolic workflow.
3. Independently re-derive the lambda-zero aggregate factorization and document removed nonzero factors/domain restrictions.
4. Prove local gamma dependence of the aggregate zero set analytically; the presence of gamma in the residual on the published line is not by itself enough.
5. Express/check the Proposition-3 strict sign with exact rational arithmetic or sufficiently controlled symbolic/high-precision arithmetic.
6. State local denominator nondegeneracy and continuity conditions explicitly.

These are formal-proof tasks, not evidence failures. None requires new economics or a model extension.

## Stage 1 gate

Gate checks:

- correction object narrow and exact: PASS;
- contributions <=3: PASS (3);
- propositions <=3: PASS (3);
- every proposition has analytic proof path: PASS;
- no proposition intended to rely only on numerics: PASS;
- positive-measure continuity path: PASS;
- equilibrium formulas explicitly preserved: PASS;
- no welfare overclaim: PASS;
- no absolute novelty claim: PASS;
- no model extension: PASS;
- minimal section structure: PASS (5 main sections);
- affected original objects mapped: PASS;
- proof obligations listed: PASS;
- referee kill test has no fatal issue: PASS;
- editorial-value test has no score 1: PASS;
- manuscript prose not drafted: PASS.

Decision: **`STAGE1_PASS`**.

No `UNPLANNED_NEW_RESULT` is promoted to the frozen proposition set. The planned implicit-function identities are proof methods/obligations, not new economic claims.

## Recommended Stage 2

Proceed to `Stage 2 — Formal Derivation and Proof Completion` on a new dedicated-repository branch after Stage-1 PR review/merge. Stage 2 should use symbolic/exact algebra to close the six proof obligations, produce independently checkable derivation artifacts, and preserve the three-proposition scope. It should still defer full manuscript drafting until the formal proof gate passes.
