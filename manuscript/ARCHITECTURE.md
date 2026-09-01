# Manuscript Architecture — Stage 1 Working Specification

Status: `FROZEN_FOR_STAGE1`

This file is an architectural specification only. It is not manuscript prose.

## Correction object

The note corrects four linked threshold/generalization objects in Ishikawa and Shibata (2021): (i) Observation 1's generic gamma-invariance claim, (ii) Observation 4's scalar aggregate threshold, (iii) the global asymmetric interpretation of Eqs. (43)–(46), and (iv) Observation 5's fixed average-spillover cutoff classification. The published equilibrium formulas are retained. The correction concerns the threshold characterizations and the parameter-region classifications derived from them.

## Minimum publishable contribution

1. **Individual boundary.** The individual competition/cooperation boundary is not gamma-invariant in general; away from the special symmetric cancellation it varies with the R&D-cost parameter `gamma`.
2. **Aggregate boundary.** The aggregate equality set is not generally a scalar average-spillover threshold. It is a locus in `(beta_1,beta_2)` whose characterization depends on spillover asymmetry and, in general, `gamma`.
3. **Classification consequence.** The published fixed average-spillover cutoff misclassifies a positive-measure admissible parameter region.

The symmetric gamma-independent crossing is an explanation of why the published numerical analysis can suggest invariance; it is not a fourth contribution.

## Main-section architecture

| Section | Purpose | Required equations / objects | Proposition dependency | Primary-source dependency | Evidence source |
|---|---|---|---|---|---|
| 1. Introduction and correction target | identify narrow correction, preserve unaffected results, state three contributions | no derivation; only named objects | P1–P3 summaries | Obs. 1, Obs. 4–5, Eqs. (38), (43)–(46) | `EVIDENCE_MAP.md`, `CLAIM_BOUNDARY.md` |
| 2. Retained model objects | introduce only the published equilibrium formulas needed for comparison and define corrected zero sets | retained `x_i^n`, `x_i^c`, `D_i`, `D_A` | inputs to P1–P3 | Eqs. (16)–(20), (25)–(29) | `code/independent_reconstruction.py`, `code/consequence_audit.py` |
| 3. Corrected individual threshold | establish non-invariance in general and isolate exact symmetric cancellation | `D_i=0`; symmetric crossing `b*(lambda)` | P1 | Eq. (38), Obs. 1, Table 1, Fig. 1(d) | Stage-2/3 evidence frozen in Stage 0 |
| 4. Corrected aggregate threshold and classification | reject scalar straight-line characterization and show consequential misclassification | `D_A=0`; lambda=0 factorization; strict counterexample | P2, P3 | Eqs. (43)–(46), Obs. 4–5, Fig. 3 | Stage-2/3 evidence frozen in Stage 0 |
| 5. Implications and surviving results | delimit what changes and what survives | no new theorem | uses P1–P3 conclusions | Table 1, Eq. (47), Fig. 4, Introduction/Conclusion third result | `EVIDENCE_MAP.md`, `CLAIM_BOUNDARY.md` |

Optional appendix / online appendix: cleared-denominator algebra, factorization details, local regularity checks, additional numerical boundaries, and reproducibility provenance. It must not add a new model or new headline result.

## Introduction logic only

No finished introduction prose is authorized in Stage 1. The logical sequence is:

1. identify the target threshold claims in Ishikawa and Shibata (2021);
2. state that the published equilibrium formulas are retained and the correction is narrow;
3. state the corrected individual boundary, aggregate boundary, and misclassification consequence;
4. state explicitly which published results survive or require only qualification.

Avoid language such as `fundamental flaw`, `invalid paper`, `major error`, `we overturn`, or `literature missed`.

## Figure policy

Maximum two figures; working recommendation is **one main figure**.

### Figure A — preferred main figure

Corrected aggregate equality locus `D_A=0` versus the published straight line, with `lambda=0` and a small set of `gamma` values. Purpose: display the asymmetry-induced curvature and gamma sensitivity of the corrected boundary. This figure is illustrative only; Proposition 2 must rest on analytic proof.

### Figure B — optional, not currently required

Individual trigger as a function of the rival spillover parameter for several gamma values, highlighting their exact common symmetric crossing. Include only if it materially clarifies the numerical-artifact explanation after Stage 2 proof completion.

Stage 1 creates no figure files.

## Table policy

Preferred count: **0 main tables**. The three canonical trigger/boundary values can be reported compactly in text or appendix. A single small table is permitted only if the final exposition becomes clearer. No table is required for any proposition.

## Length budget

Working short Comment / Note budget:

- main text: 3,500–5,000 words;
- main propositions: 3;
- main figures: 1 preferred, 2 maximum;
- main tables: 0 preferred, 1 maximum;
- appendix: algebra, regularity and reproducibility only;
- references: minimal and correction-focused.

Assessment: feasible. The model is not re-derived, equilibrium formulas are retained, and the central correction can be organized around three propositions.

## Title options — not frozen

1. `A Comment on “R&D Competition and Cooperation with Asymmetric Spillovers in an Oligopoly Market”`
2. `Correcting R&D Competition–Cooperation Thresholds under Asymmetric Spillovers`
3. `On R&D Competition and Cooperation with Asymmetric Spillovers: Corrected Thresholds`

Final title selection is deferred to later journal strategy.

## Single-source-of-truth rule

The master audit repository remains canonical for Stage-2/3/Protocol-05 audit history. This repository is canonical for the publication-facing theorem specification and future manuscript development. Stage 1 does not edit the master repository.
