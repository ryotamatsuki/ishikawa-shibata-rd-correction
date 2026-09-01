# Stage 4 Journal Strategy and Submission-Readiness Review

## Executive decision

**`READY_FOR_SUBMISSION_PACKAGE`**.

The Stage-3 manuscript is mathematically and editorially suitable for progression to a journal-specific submission package. Current 2026-09-01 policy/precedent research identifies the International Journal of Industrial Organization (IJIO) as the strongest primary target.

## PR #4 review and merge

- Stage-3 PR: `#4 — Stage 3: draft correction manuscript and complete internal referee review`
- review result: no blocking issue; open/non-draft/mergeable, no unresolved comments or review threads; Round-2 status `READY_FOR_JOURNAL_STRATEGY`; Stage-0 claim boundary maintained.
- self-approval through GitHub was not possible because GitHub does not allow authors to approve their own PR; this was not treated as a substantive blocker.
- merge commit / Stage-4 starting commit: `2a77c087b4e2acc6186cf732b26cb165b3acc81d`.
- Stage-4 branch: `stage4/journal-strategy-readiness`.

## Candidate journals

| Rank | Journal | Score | Key conclusion |
|---:|---|---:|---|
| 1 | International Journal of Industrial Organization | **92/100** | Primary: exact theoretical-IO audience + Jan-2026 third-party theory Comment precedent + no-APC subscription route |
| 2 | Review of Industrial Organization | **86/100** | Backup 1: strong IO fit + verified no-APC subscription route; current comment portal taxonomy less certain |
| 3 | International Review of Economics & Finance | **77/100** | Backup 2: original journal + genuine third-party comment precedent, but currently fully gold OA and therefore cost-disadvantaged |
| 4 | Journal of Economics | **72/100** | Strong mathematical fallback + no-APC subscription route + historical theoretical Comment precedent |
| 5 | Economics Letters | **40/100** | Reject strategy: official scope says comments are unsuitable and normal length is ~2,000 words |

## Primary journal

**International Journal of Industrial Organization.**

Current official scope directly covers theoretical IO, strategic behavior, market structure and technological change. A January 2026 IJIO article explicitly titled `... – a comment` revises a theoretical condition in a prior IJIO paper, providing a very close editorial precedent for the present third-party mathematical correction.

## Primary article type

Working type: **`Comment`**.

This is based on current IJIO publication precedent, not on an invented label. The exact live submission-portal dropdown name was not exposed by accessible public GFA material and must be confirmed in Stage 5.

## Submission working title

`Correcting R&D Competition--Cooperation Thresholds under Asymmetric Spillovers`.

## Cost status

### IJIO

- current publishing model: subscription journal;
- mandatory publication APC under chosen subscription route: **none** under current Elsevier pricing policy;
- optional OA APC: not required;
- submission fee: **not primary-source verified for IJIO**. Elsevier says fee-charging economics journals flag fees in GFA/submission; Stage 5 must confirm the live portal. No current publisher source located in Stage 4 states an IJIO fee.

### IREF

Elsevier currently lists IREF among fully gold open-access economics/finance journals. Therefore the project should assume a mandatory APC unless a waiver/agreement applies. Exact current journal-specific amount was not authoritatively verified and is not invented here.

## Policy verification status

Verified from current journal/publisher primary sources where available:

- IJIO aims/scope and subscription status;
- current IJIO third-party theory-Comment precedent;
- Elsevier subscription-route no-APC policy;
- Elsevier current 2026 generative-AI policy;
- Elsevier data/sharing policy;
- IREF scope, fully gold-OA classification and third-party comment precedent;
- Economics Letters no-comment and ~2,000-word policies;
- RIO hybrid/no-APC subscription route, manuscript/AI/data requirements;
- Journal of Economics hybrid/no-APC subscription route and manuscript requirements.

Items marked `NOT VERIFIED` rather than guessed: exact IJIO portal article-type label, IJIO review-anonymization model, IJIO submission fee, and some auxiliary portal requirements such as highlights/graphical abstract.

## Manuscript fit

The current manuscript has three exact propositions, five main sections, one illustrative figure, no main table, four short appendices and ~3,520 main-text words. No material IJIO length conflict was identified. The note is substantially closer to the Jan-2026 IJIO theoretical Comment precedent than to Economics Letters' letter format.

No new mathematical proposition or experiment is required.

## Editorial-necessity result

E1--E8: **all STRONG**.

Core rationale: correct equilibrium formulas do not rescue incorrect published threshold/generalization statements. The correction is analytic rather than numerical, maps to explicit source-paper objects, and gives a strict classification reversal that persists on an open positive-measure admissible region.

## Desk-reject simulation

No fatal desk-reject issue. Main residual risk is **MODERATE editorial-significance/narrowness risk** because the underlying equilibrium solutions survive. Appropriate mitigation is the existing exact zero-set correction + positive-measure consequence + explicit statement of surviving results. Adding welfare analysis, a new model or downstream claims is not recommended.

## Contact strategy

`DIRECT_SUBMISSION`.

No pre-submission editor inquiry and no original-author contact are recommended as prerequisites. Stage 4 sent no contact and made no journal submission.

## Repository strategy

`PRIVATE NOW; CONTROLLED REVIEW SNAPSHOT; PUBLIC ARCHIVAL RELEASE LATER`.

Keep the canonical repo private until IJIO's live review/anonymization rules are confirmed. If anonymity requires it, create an anonymized publication-facing code snapshot for reviewers. At acceptance/publication, subject to author approval and policy, create a citable public archival release (preferably DOI-bearing, e.g. Zenodo) and update code-availability text. Stage 4 did not alter repository visibility.

## AI disclosure strategy

Current Elsevier policy requires disclosure because generative-AI assistance in this project exceeded basic copy editing and also entered manuscript/code workflow. `AI_DISCLOSURE_DRAFT.md` records a Stage-5 author-confirmation draft. AI is not treated as an author or evidence source; mathematical evidence remains explicit algebra and deterministic verification code.

## Remaining submission gaps

Administrative/formatting only:

1. confirm live IJIO portal article-type label;
2. confirm submission fee status;
3. confirm review/anonymization model;
4. confirm highlights/graphical-abstract/CRediT requirements;
5. add factual author/affiliation/corresponding-author metadata;
6. add keywords/JEL codes;
7. finalize funding/conflict/data/code/AI declarations;
8. implement reviewer-safe repository/supplement route;
9. draft cover letter;
10. build final submission PDF/source package and run preflight.

No substantive proof blocker remains.

## Stage 4 gate

Primary target fixed: PASS.
Article path fixed/narrowly resolved: PASS (`Comment`; portal label confirmation only).
Backups ranked: PASS.
Zero-cost publication route for primary: PASS.
Current policies documented: PASS.
Manuscript fit: PASS.
Claim boundary: PASS.
Editorial risk audit: PASS.
Repository strategy: PASS.
AI disclosure strategy: PASS.
No new proof obligation: PASS.
No actual journal submission: PASS.

**Decision: `READY_FOR_SUBMISSION_PACKAGE`.**

## Recommended Stage 5

Proceed, after review/merge of the Stage-4 PR, to **Dedicated Stage 5 — Submission Package and Final Pre-Submission Audit** for IJIO. Stage 5 should perform the live-portal confirmations above, add factual metadata/declarations, prepare cover letter and any required highlights, generate the final manuscript/source package, complete anonymity/repository handling, and stop immediately before the irreversible journal-submission action unless the user separately instructs submission.