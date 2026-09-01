# Stage 5 Submission Package and Final Pre-Submission Audit

## Executive decision

**`STAGE5_BLOCKED` under the strict gate.**

The manuscript, figure, reproducibility package, cover-letter draft, highlights, metadata plan and visual PDF preflight are complete to the extent possible without inventing author facts. The block is not mathematical. Current public IJIO sources do not resolve three fields that the Stage-5 protocol makes mandatory before `READY_TO_SUBMIT`: the exact ordinary-submission article-type dropdown label, IJIO-specific submission-fee status, and IJIO-specific review/anonymization model. The public Editorial Manager landing page also displays a development-site warning while other current IJIO materials direct authors to that system. Verified author metadata/funding/COI declarations are additionally absent from the dedicated repository.

## PR #5 review result

No blocking Stage-4 issue. PR #5 was open, non-draft and mergeable, with no comments or unresolved review threads and no reported CI statuses. It was merged only after substantive re-review.

## PR #5 merge commit / Stage-5 starting commit

`4a195318a2f5655c3f7245e634002199d52dbdbc`

## Stage-5 branch

`stage5/submission-package-preflight`

## Primary journal

International Journal of Industrial Organization (IJIO).

## Official article type

Substantive Comment pathway: verified by the January 2026 IJIO article `Generic entry, price competition, and market segmentation in the prescription drug market – a comment`.

Live ordinary-submission dropdown label: **`ARTICLE_TYPE_UNRESOLVED`**.

## Fee status

- subscription/hybrid publication route: `ZERO_MANDATORY_APC_SUBSCRIPTION_ROUTE_VERIFIED` under current Elsevier pricing policy;
- IJIO-specific submission fee: `NOT_VERIFIED` from a current primary source.

## Review model

`NOT_VERIFIED` from a current IJIO-specific primary source. The main manuscript is therefore prepared identity-neutral, with a separate title-page template pending the official review model.

## Submission title

`A Comment on “R&D Competition and Cooperation with Asymmetric Spillovers in an Oligopoly Market”`

## Abstract / metadata

- Abstract: 120 words.
- Keywords: R&D competition; R&D cooperation; asymmetric spillovers; oligopoly; threshold characterization.
- JEL: `L13; O32`, consistent with the current AEA taxonomy and source-paper metadata.

## Author metadata

`NOT VERIFIED IN DEDICATED REPOSITORY`. No name, affiliation, corresponding-author email, ORCID, funding or competing-interest fact has been invented. Title page and cover-letter signoff retain explicit author-confirmation placeholders.

## Manuscript package

- 10-page compiled main manuscript PDF;
- editable LaTeX source package;
- one vector aggregate-boundary figure;
- title-page metadata template;
- cover-letter draft;
- five prepared highlights;
- declarations and AI-disclosure records;
- reviewer-safe reproducibility ZIP;
- portal field plan and file inventory;
- SHA-256 checksums.

## Cover letter / declarations

The cover letter is substantively complete and restrained. It states that the equilibrium solutions survive and that the note corrects threshold characterizations. Author originality/concurrent-submission, competing-interest and signoff facts remain confirmation items. Data/code wording is prepared. AI disclosure is prepared under current Elsevier policy, subject to final author fact-check/approval. Funding/COI/acknowledgments/CRediT are not invented.

## Reproducibility package

`PASS`; see `results/stage5_reproducibility_preflight.md`.

## Build / visual QC

Two-pass `pdflatex`: PASS. No fatal errors, undefined references, or overfull/underfull warnings on the final pass. PDF: 10 pages. All pages rendered and manually inspected; no clipping, overlap, broken glyph, equation overflow, or figure-label defect observed.

## Claim traceability

PASS. All headline claims trace to the three frozen propositions, Stage-2 exact derivations, deterministic code assertions and Stage-0 claim permissions. No welfare-ranking reversal, absolute novelty, empirical consequence, global lambda nesting or new-model claim was added.

## Final desk-reject simulation

- R1 target identifiable: PASS.
- R2 correction on first page: PASS.
- R3 abstract states what survives: PASS.
- R4 analytic rather than numerical: PASS.
- R5 non-cosmetic consequence: PASS.
- R6 compactness: PASS.
- R7 third-party tone: PASS.
- R8 IJIO relevance despite IREF source: `MINOR_RISK`; subject is core theoretical IO and IJIO has a comment tradition, including historical comments engaging results published outside IJIO, but cross-journal routing remains less direct than original-journal routing.
- R9 general-IO significance: `MINOR_RISK`; no new model, so editorial significance remains the main residual desk risk.
- R10 2026 IJIO precedent: `PASS_WITH_ADMIN_CAVEAT`; it verifies the substantive comment pathway but not the current portal dropdown taxonomy.

## Remaining blockers

1. Resolve the valid live IJIO ordinary-submission system/GFA and exact article-type label.
2. Verify IJIO-specific submission-fee status.
3. Verify IJIO-specific review/anonymization model and consequent file split.
4. Supply and verify author/affiliation/corresponding-author metadata.
5. Author confirms funding, competing interests, acknowledgments, originality/concurrent-submission statement and AI-disclosure factual wording.
6. Confirm portal requirements for highlights, graphical abstract and CRediT.

## Stage-5 gate

**`STAGE5_BLOCKED`**.

This follows the explicit strict rules: `READY_TO_SUBMIT` requires the official article type, fee status, review model and verified author metadata. The package itself is technically preflighted, but the submission button cannot yet be safely pressed.

## Exact next action

Do not submit. Resolve the live IJIO portal/GFA ambiguity and author metadata/declarations, then rerun a short Stage-5 delta preflight. Only after the gate becomes `READY_TO_SUBMIT` should a separate explicitly authorized Stage 6 transmit the manuscript.
