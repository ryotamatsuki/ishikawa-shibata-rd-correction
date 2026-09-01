# Stage 3 Manuscript Drafting and Internal Referee Review

## Executive decision

`STAGE3_PASS`.

The Stage-2 exact proof package has been converted into a five-section correction manuscript with three propositions, one illustrative figure, four short algebraic appendix sections, deterministic reproducibility language, and two rounds of skeptical internal referee review. Round 2 concludes `READY_FOR_JOURNAL_STRATEGY`.

## Starting state

- PR #3 reviewed with no blocking issue.
- PR #3 merge commit / Stage-3 starting main: `80f6c4587db1548f7d88e055a554ee8cfec9518c`.
- Stage-3 branch: `stage3/manuscript-draft-referee`.

## Working title

`Correcting R&D Competition--Cooperation Thresholds under Asymmetric Spillovers`

## Manuscript structure and length

Five main sections: Introduction/correction target; retained model objects; corrected individual threshold; corrected aggregate threshold/classification; changes and surviving results.

Appendix A--D: individual polynomial; symmetric factorization; aggregate factorization/local root; exact regularity certificate.

Revised main text: approximately 3,520 words before the short appendix; approximately 3,680 including appendix. Three propositions, one main figure, zero tables.

## Proposition status

- P1 exact individual non-invariance + exact symmetric crossing: PASS.
- P2 exact aggregate asymmetry correction + local gamma dependence: PASS.
- P3 exact rational reversal + positive-measure continuity result: PASS.

All proofs trace to `manuscript/FORMAL_DERIVATIONS.md` and `code/formal_derivation.py`.

## Figure and reproducibility

`figures/aggregate_boundary.pdf` overlays the published line with corrected `D_A=0` loci for gamma 10, 50 and 100 at lambda 0. It is explicitly illustrative. Figure source: `code/figure_aggregate_boundary.py`.

The manuscript states that proposition-level algebra is verified by deterministic Python/SymPy code; the repository URL remains a submission-stage placeholder while private.

## Internal referee review

Round 1: `MINOR_INTERNAL_REVISION`. Main issues were excessive compression, implicit P1 quantifier logic, insufficient separation of P2's two arguments, terse P3 continuity explanation, and weak change/survival mapping.

Revision expanded explanation without new mathematics, retained three propositions/one figure/zero tables, and strengthened the mapping to affected and surviving original objects.

Round 2: `READY_FOR_JOURNAL_STRATEGY`. All ten mandatory kill questions survive.

## Claim-boundary QC

PASS: equilibrium formulas preserved; P1 gamma dependence analytic; symmetric cancellation not generalized; P2 asymmetry/gamma arguments separate; P3 exact rational sign and regular-neighborhood continuity; no welfare reversal; Observation 6 not overturned; no broad global competitiveness reversal; no absolute novelty; no new model/mechanism; no global lambda nesting.

## Build status

PASS. `pdflatex` two-pass internal build completed with no fatal errors, undefined references, serious overfull boxes, or missing bibliography. Internal PDF target: `manuscript/manuscript_draft.pdf`, 10 pages. Render verification passed 10/10 pages with no observed clipping, overlap, broken glyph, or figure-label failure.

## Stage 3 gate

Decision: **`STAGE3_PASS`**.

## Remaining editorial risks

- significance may be judged moderate because equilibrium formulas survive;
- journal/article type and final title convention unresolved;
- repository remains private;
- author/affiliation metadata omitted;
- no external human referee review.

## Recommended next stage

After Stage-3 PR review/merge, proceed to `Dedicated Stage 4 — Journal Strategy and Submission-Readiness Review`.
