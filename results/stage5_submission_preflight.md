# Stage 5 Submission Package and Final Pre-Submission Audit

## Executive decision

**`STAGE5_BLOCKED` under the strict gate, with materially reduced blockers after cross-project metadata recovery.**

The manuscript, figure, reproducibility package, cover-letter draft, highlights, metadata plan and visual PDF preflight are complete. Stable author metadata and several IJIO workflow fields that were previously unresolved have now been recovered from the author's authenticated Shy (2002) IJIO submission package dated 2026-08-31.

Resolved from that authenticated evidence:

- IJIO author-facing Article Type: `Research Paper`; no `Comment` option exposed;
- operational double-anonymized workflow: anonymous manuscript plus separate title page;
- initial LaTeX source not required until revision;
- Highlights available as an optional upload type;
- stable author identity/contact metadata (Ryota Matsuki; Independent Researcher; Matsuyama, Ehime, Japan; 790-0853; email; phone; ORCID).

The remaining block is not mathematical. The strict gate still requires IJIO-specific submission-fee status and manuscript-specific author attestations/declarations before `READY_TO_SUBMIT`.

## PR #5 review result

No blocking Stage-4 issue. PR #5 was open, non-draft and mergeable, with no comments or unresolved review threads and no reported CI statuses. It was merged only after substantive re-review.

## PR #5 merge commit / Stage-5 starting commit

`4a195318a2f5655c3f7245e634002199d52dbdbc`

## Stage-5 branch

`stage5/submission-package-preflight`

## Primary journal

International Journal of Industrial Organization (IJIO).

## Official article type / Comment routing

Substantive Comment pathway: verified by the January 2026 IJIO article `Generic entry, price competition, and market segmentation in the prescription drug market – a comment`.

Authenticated ordinary-submission Article Type observed in the author's prior IJIO submission flow on 2026-08-31: **`Research Paper`**. No `Comment` option was exposed. The present manuscript should therefore be entered under `Research Paper`, with its title and cover letter identifying it explicitly as a Comment.

## Fee status

- subscription/hybrid publication route: `ZERO_MANDATORY_APC_SUBSCRIPTION_ROUTE_VERIFIED` under current Elsevier pricing policy;
- IJIO-specific submission fee: `NOT_VERIFIED` from either the current public IJIO materials located in this audit or the prior authenticated-project records.

## Review model

**Double-anonymized operational workflow confirmed from the authenticated 2026-08-31 IJIO package.** The main manuscript is identity-neutral and the title page is separate.

## Submission title

`A Comment on “R&D Competition and Cooperation with Asymmetric Spillovers in an Oligopoly Market”`

## Abstract / metadata

- Abstract: 120 words.
- Keywords: R&D competition; R&D cooperation; asymmetric spillovers; oligopoly; threshold characterization.
- JEL: `L13; O32`.

## Verified stable author metadata

Recovered from `ryotamatsuki/stable-pricing-switching-costs/submission/submission_metadata.md` and the completed author-confirmation record:

- Author: Ryota Matsuki
- Single author / corresponding author
- Affiliation: Independent Researcher
- Location: Matsuyama, Ehime, Japan
- Postal code: 790-0853
- Email: ryota.matsuki@gmail.com
- Phone: +81-90-9552-5110
- ORCID: 0009-0005-2329-531X

A street-level address was not supplied in the prior package and is not inferred. Add one only if an authenticated IJIO page actually requires it.

## Manuscript-specific attestations not automatically reused

The prior Shy package recorded no external funding, no competing interests, no acknowledgments, originality/no concurrent submission, and approval of that manuscript's AI disclosure. Those are manuscript-specific factual attestations. They are useful as prior provenance but remain confirmation items for the Ishikawa--Shibata manuscript rather than being silently copied.

## Manuscript package

- 10-page compiled anonymous main manuscript PDF;
- editable LaTeX source package;
- one vector aggregate-boundary figure;
- populated separate title-page source, with manuscript-specific declarations still marked for confirmation;
- cover-letter draft with verified signature/contact metadata;
- five prepared highlights;
- declarations and AI-disclosure records;
- reviewer-safe reproducibility package;
- portal field plan and file inventory;
- SHA-256 checksums.

## Reproducibility package

`PASS`; see `results/stage5_reproducibility_preflight.md`.

## Build / visual QC

Two-pass `pdflatex`: PASS. No fatal errors, undefined references, or serious box warnings. PDF: 10 pages. All pages rendered and manually inspected; no clipping, overlap, broken glyph, equation overflow, or figure-label defect observed.

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
- R8 IJIO relevance despite IREF source: `MINOR_RISK`.
- R9 general-IO significance: `MINOR_RISK`.
- R10 2026 IJIO precedent: PASS; authenticated workflow separately resolves routing through `Research Paper`.

## Remaining blockers

1. Verify IJIO-specific submission-fee status.
2. Confirm funding status for this manuscript.
3. Confirm competing interests for this manuscript.
4. Confirm acknowledgments for this manuscript.
5. Confirm originality and no concurrent submission for this manuscript.
6. Final author factual approval of the present AI-disclosure wording.
7. Complete any later authenticated system-only fields; obtain a street address only if IJIO explicitly requires it.

## Stage-5 gate

**`STAGE5_BLOCKED`**.

This remains the correct strict-gate classification because `READY_TO_SUBMIT` requires fee status and complete factual declarations. The earlier blockers for article type, review model and stable author metadata are resolved.

## Cross-project evidence

Source repository: `ryotamatsuki/stable-pricing-switching-costs`.

Primary records:

- `submission/submission_metadata.md`
- `submission/author_confirmation_required.md`
- `submission/upload_manifest.md`
- `submission/README_stage8.md`
- `submission/title_page.tex`

These document an authenticated IJIO submission workflow observed on 2026-08-31 and explicit stable author metadata.

## Exact next action

Do not submit. Confirm the manuscript-specific declarations and resolve the IJIO submission-fee status. Then rerun a short Stage-5 delta preflight, regenerate the title-page/cover-letter binaries and package hashes if needed, and move to `READY_TO_SUBMIT` only if all strict-gate items pass.
