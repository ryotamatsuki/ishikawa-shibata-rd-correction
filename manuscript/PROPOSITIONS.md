# Proposition Freeze — Stage 1 Working Theorem Specification

Status: `FROZEN_FOR_STAGE1`

These are working theorem specifications, not publication-ready prose. Stage 2 must complete and check the formal algebra before any statement is promoted to final manuscript language.

## Common notation and maintained scope

Use the published noncooperative and cooperative R&D equilibrium formulas retained from Ishikawa and Shibata (2021). Define

`D_i(beta_1,beta_2,lambda,gamma) = x_i^n - x_i^c`

and

`D_A(beta_1,beta_2,lambda,gamma) = (x_1^n+x_2^n) - (x_1^c+x_2^c)`.

All statements are restricted to parameter regions where the retained closed forms are well defined and the relevant interior solutions satisfy the maintained admissibility/regularity conditions. No welfare-ranking claim is embedded in these propositions.

---

## Proposition 1 — Individual R&D boundary

### Working statement

The individual competition/cooperation boundary is the zero set `D_i=0` and is **not gamma-invariant in general**. On regular asymmetric slices, the zero-set location varies with `gamma`. In contrast, on the symmetric slice `beta_1=beta_2=b`, the equality condition admits the exact crossing

`b*(lambda) = (2+lambda-lambda^2)/(lambda^2-3lambda+4)`,

which is independent of `gamma`.

### Assumptions

- retained published closed-form R&D equilibria are defined;
- parameters satisfy the paper's maintained admissible restrictions;
- for the local gamma-dependence statement, the relevant root is regular after denominators are cleared (`partial N_i / partial beta_i != 0`);
- no claim is made at singular parameter values or denominator zeros.

### Exact conclusion to be proved in Stage 2

1. After clearing nonzero denominators, write the equality condition as `N_i(beta_i,beta_j,lambda,gamma)=0`.
2. Establish analytically that the zero set is not invariant to `gamma` in general. Preferred proof route: on a simple admissible asymmetric slice such as `lambda=0, beta_j=0`, derive the exact cleared-denominator equation and show at a regular root that `partial N_i / partial gamma != 0`; the implicit-function theorem then gives `d beta_i*/d gamma != 0` locally.
3. On `beta_1=beta_2=b`, factor the equality condition and obtain the exact gamma-independent crossing above.

This establishes a general failure of the published gamma-invariance characterization while explaining the special cancellation visible at symmetry.

### Proof skeleton

1. Start from retained closed-form `x_i^n` and `x_i^c`.
2. Form `D_i` and clear denominators without changing the zero set on the regular domain.
3. Derive `N_i` on an admissible asymmetric slice.
4. Verify analytically that the gamma derivative of the equality equation is nonzero at a regular root; use the implicit-function formula `d beta_i*/d gamma = -N_{i,gamma}/N_{i,beta_i}`.
5. Use existing Stage-0 numerical values only as an independent check, not as the theorem proof.
6. Restrict to `beta_1=beta_2=b`.
7. Factor and solve to obtain `b*(lambda)`.
8. Explain that exact cancellation on the symmetric slice does not imply global gamma-invariance.

### Evidence provenance

- `CLAIM_BOUNDARY.md`, allowed claims 2–3;
- `EVIDENCE_MAP.md`, Observation 1 / Eq. (38) / Table 1 / Fig. 1(d);
- `code/independent_reconstruction.py`;
- `code/consequence_audit.py`.

### Forbidden strengthening

Do not claim global uniqueness of the trigger, global monotonicity in `gamma`, global monotonicity in `lambda`, the published inverted-U property as newly proven, or a global characterization of every branch of `D_i=0`.

---

## Proposition 2 — Aggregate R&D boundary

### Working statement

The aggregate equality boundary is the zero set `D_A=0` and is not generally characterized by a scalar line `beta_1+beta_2=theta(lambda)`. The corrected equality condition depends on spillover asymmetry and, in general, `gamma`. In particular, for `lambda=0`, substituting the published line `beta_1+beta_2=1` into the cleared numerator of `D_A` yields, up to nonzero common factors,

`(beta_1-beta_2)^2 [18 gamma - 9 + (beta_1-beta_2)^2]`.

Under the maintained `gamma>=1`, every asymmetric point on that published line fails the aggregate equality condition.

### Assumptions

- retained published closed-form R&D equilibria are defined;
- maintained `gamma>=1` for the stated lambda-zero factorization consequence;
- denominators and common factors removed from the equality condition are nonzero on the stated regular domain.

### Exact conclusion to be proved in Stage 2

1. After clearing denominators, write `D_A=0` as `N_A(beta_1,beta_2,lambda,gamma)=0`.
2. At `lambda=0`, set `s=beta_1+beta_2` and `d=beta_1-beta_2`, substitute `s=1`, and verify the frozen factorization.
3. Since `18 gamma-9+d^2 > 0` for `gamma>=1`, show that `d!=0` implies `N_A!=0` on the published line. Therefore the published straight line cannot be the general asymmetric equality locus.
4. To support the separate statement that the corrected boundary varies with `gamma` rather than merely that the residual on the published line contains `gamma`, Stage 2 must derive a regular local slice (preferred: `lambda=0, beta_2=0`) and verify `d beta_1*/d gamma != 0` via the implicit-function theorem or an equivalent exact algebraic argument.

### Proof skeleton

1. Form `D_A` from retained closed forms.
2. Clear denominators and define `N_A`.
3. Set `lambda=0`; transform to `(s,d)` coordinates.
4. Substitute `s=1` and factor.
5. Use `gamma>=1` and `d!=0` to reject aggregate equality along every asymmetric point of the published line.
6. Establish local gamma dependence of the corrected zero set on a regular asymmetric slice analytically.
7. State only the warranted conclusion: the published scalar average-spillover characterization fails generally; do not assert a global closed-form replacement unless Stage 2 actually derives one.

### Evidence provenance

- `CLAIM_BOUNDARY.md`, allowed claims 4–5;
- `EVIDENCE_MAP.md`, Observation 4 / Eqs. (43)–(44) / Fig. 3;
- Stage-3 frozen factorization;
- `code/consequence_audit.py` for independent numerical boundary checks.

### Forbidden strengthening

Do not claim global monotonicity of the corrected boundary, a globally unique graph `beta_1=g(beta_2)`, global convexity/concavity, or a global lambda-nesting theorem.

---

## Proposition 3 — Positive-measure classification error

### Working statement

At

`a=100, c=50, gamma=10, lambda=0, beta_1=0.98, beta_2=0`,

the published fixed average-spillover rule classifies the point as aggregate competitive-R&D dominant because `(beta_1+beta_2)/2=0.49<0.5`, whereas the retained closed-form equilibria imply

- `x_1^n+x_2^n = 3.593012699648`,
- `x_1^c+x_2^c = 3.629896961138`,
- `D_A = -0.036884261490`.

The classification therefore reverses at an admissible interior point. Because the difference is strict and the equilibrium objects are continuous on a regular neighborhood of that point, the disagreement persists on an open neighborhood and hence on a set of positive measure.

### Assumptions

- the stated parameter point is admissible and interior under the frozen Stage-2 feasibility/curvature checks;
- denominators of the retained closed forms remain nonzero in a neighborhood of the point;
- the published classification rule is interpreted exactly as in Observation 5 / Eqs. (45)–(46), not as a welfare ranking.

### Exact conclusion to be proved in Stage 2

1. Re-evaluate the retained exact/rational closed forms at the stated point and verify the strict sign `D_A<0`.
2. Record the published cutoff prediction at the same point.
3. Verify local denominator nondegeneracy explicitly.
4. Invoke continuity of the rational equilibrium functions on that regular neighborhood.
5. Conclude that an open set retains the sign disagreement; therefore the misclassified set has positive measure.

### Proof skeleton

1. State parameter point and published cutoff classification.
2. Substitute into retained closed forms.
3. Show strict corrected sign.
4. Confirm admissibility and local regularity.
5. Apply continuity.
6. Conclude open disagreement region and positive measure.

Grid-area calculations are not part of the proposition proof and may appear only as optional illustration.

### Evidence provenance

- `CLAIM_BOUNDARY.md`, allowed claim 6;
- `EVIDENCE_MAP.md`, Observation 5 / Eqs. (45)–(46);
- `code/independent_reconstruction.py` feasibility and closed-form cross-check;
- `code/consequence_audit.py` counterexample route.

### Forbidden strengthening

Do not translate this result into `WELFARE_RANKING_CHANGED`, do not claim the disagreement region is economically large without a separate metric, and do not claim downstream empirical or citation effects.

---

## Lemma policy

**Frozen main-text lemma count: 0.**

The note should remain compact. Algebraic identities and local denominator/continuity checks are supporting proof steps, not separate economic lemmas. Stage 2 may place long factorizations in an appendix. A formal lemma may be introduced only if proof readability materially deteriorates; doing so requires an explicit architecture update before manuscript drafting.

## Stage-2 proof obligations

1. Derive an exact cleared-denominator `N_i` sufficient for an analytic non-invariance proof and verify a regular `gamma`-dependent root using an implicit-function or equivalent algebraic argument.
2. Re-derive and independently verify the frozen symmetric factorization for Proposition 1.
3. Re-derive and independently verify the lambda-zero aggregate factorization for Proposition 2.
4. Establish analytic local gamma dependence of the aggregate zero set on at least one regular asymmetric slice.
5. Express the Proposition-3 counterexample with enough exact/rational or high-precision symbolic support that the strict sign is not a floating-point artifact.
6. Record denominator nondegeneracy and continuity conditions used by Proposition 3.

No unresolved item requires a model extension.
