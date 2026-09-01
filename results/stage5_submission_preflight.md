# Stage 5 Submission Package and Final Pre-Submission Audit

## Executive decision

**`STAGE5_BLOCKED` under the strict gate, with only one remaining blocker.**

The manuscript, figure, reproducibility package, cover letter, highlights, title page, declarations, metadata plan and visual PDF preflight are complete. Stable author metadata and authenticated IJIO workflow facts were recovered from the author's prior Shy (2002) IJIO submission package dated 2026-08-31. On 2026-09-01, the author separately confirmed the present manuscript's funding, competing-interest, acknowledgments, originality/no-concurrent-submission and AI-disclosure facts.

Resolved:

- IJIO author-facing Article Type: `Research Paper`; no `Comment` option exposed;
- operational double-anonymized workflow: anonymous manuscript plus separate title page;
- initial LaTeX source not required until revision;
- Highlights available as an optional upload type;
- stable author identity/contact metadata;
- funding: no external funding;
- competing interests: none;
- acknowledgments: none;
- manuscript is original except for properly cited material;
- manuscript is not under consideration elsewhere;
- current Stage-5 AI disclosure approved by the author.

The only remaining strict-gate blocker is IJIO-specific submission-fee status.

## PR #5 review result

No blocking Stage-4 issue. PR #5 was merged after substantive re-review.

## PR #5 merge commit / Stage-5 starting commit

`4a195318a2f5655c3f7245e634002199d52dbdbc`

## Stage-5 branch

`stage5/submission-package-preflight`

## Primary journal

International Journal of Industrial Organization (IJIO).

## Official article type / Comment routing

Substantive function: third-party Comment.

Authenticated ordinary-submission Article Type observed in the author's prior IJIO submission flow on 2026-08-31: **`Research Paper`**. No `Comment` option was exposed. Enter the present manuscript under `Research Paper`, with its title and cover letter identifying it explicitly as a Comment.

## Fee status

- subscription/hybrid publication route: `ZERO_MANDATORY_APC_SUBSCRIPTION_ROUTE_VERIFIED` under current Elsevier pricing policy;
- IJIO-specific submission fee: `NOT_VERIFIED` from a current IJIO-specific primary source or the prior authenticated-project record.

Current non-primary journal-fee listings describe IJIO submission as free, but the strict protocol requires authoritative IJIO-specific confirmation before upgrading the gate.

## Review model

**Double-anonymized operational workflow confirmed from the authenticated 2026-08-31 IJIO package.** The main manuscript is anonymous and the title page is separate.

## Submission title

`A Comment on “R&D Competition and Cooperation with Asymmetric Spillovers in an Oligopoly Market”`

## Abstract / metadata

- Abstract: 120 words.
- Keywords: R&D competition; R&D cooperation; asymmetric spillovers; oligopoly; threshold characterization.
- JEL: `L13; O32`.

## Verified author metadata

- Author: Ryota Matsuki
- Single author / corresponding author
- Affiliation: Independent Researcher
- Location: Matsuyama, Ehime, Japan
- Postal code: 790-0853
- Email: ryota.matsuki@gmail.com
- Phone: +81-90-9552-5110
- ORCID: 0009-0005-2329-531X

A street-level address is not inferred; provide one only if the authenticated IJIO system requires it.

## Current-manuscript author attestations

Confirmed by the author on 2026-09-01:

- No external funding.
- No competing interests.
- No acknowledgments.
- Original except for properly cited material.
- Not under consideration by another journal.
- Current Stage-5 AI-disclosure wording is accurate and approved.

Canonical confirmation record: `submission/ijio/CURRENT_MANUSCRIPT_AUTHOR_CONFIRMATION.md`.

## Manuscript package

- 10-page compiled anonymous main manuscript PDF;
- editable LaTeX source package;
- one vector aggregate-boundary figure;
- populated separate title-page source;
- finalized cover-letter text and verified signature/contact metadata;
- five prepared optional highlights;
- finalized manuscript-specific declarations and AI-disclosure records;
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
- R10 IJIO comment pathway/routing: PASS; authenticated workflow resolves routing through `Research Paper`.

## Remaining blocker

1. Verify IJIO-specific submission-fee status from an authoritative IJIO/Elsevier submission source or the authenticated current submission flow.

## Stage-5 gate

**`STAGE5_BLOCKED`** solely because the user-specified strict gate requires submission-fee status to be resolved before `READY_TO_SUBMIT`.

No mathematical, manuscript, author-metadata, declaration, anonymization, article-type, reproducibility or package blocker remains.

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

Do not submit. Resolve IJIO-specific submission-fee status. Then rerun the short final Stage-5 delta preflight, regenerate/re-hash upload binaries if needed, and move to `READY_TO_SUBMIT` only if that final fee check passes. Actual transmission still requires separate explicit authorization.
