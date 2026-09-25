# IJIO submission package — Stage 5

Status: `PACKAGE_PREFLIGHT_COMPLETE_BUT_SUBMISSION_BLOCKED`.

This directory contains the IJIO-targeted source package and submission-planning records prepared up to, but not including, journal submission.

## Canonical repository assets

- `manuscript_submission.tex` — identity-neutral submission manuscript source
- `sections/` — submission-specific section overrides
- `title_page.tex` — metadata template only
- `cover_letter.md` — editor-letter draft
- `highlights.txt` — prepared highlights, pending portal requirement
- `DECLARATIONS.md` — declaration plan
- `AI_DISCLOSURE.md` — AI disclosure wording, pending author fact-check
- `reproducibility/` — reviewer-safe reproducibility source
- `PORTAL_FIELD_PLAN.md` — planned portal fields; no portal entry performed
- `SUBMISSION_FILE_INVENTORY.md`
- `POLICY_RECHECK.md`
- `CHECKSUMS.sha256`

## Generated execution artifacts

During Stage-5 preflight the following upload candidates were generated locally from the canonical sources and inspected, but are **not committed as repository binaries**:

- `manuscript_submission.pdf` — 10-page identity-neutral PDF candidate
- `source_package.zip` — editable source archive
- `reproducibility.zip` — reviewer-safe code archive
- regenerated vector `aggregate_boundary.pdf`

Their Stage-5 SHA-256 values are recorded in `CHECKSUMS.sha256`. The PDF passed two-pass LaTeX build, PDF preflight and full-page visual inspection. The reproducibility package passed deterministic execution. Binary upload candidates should be regenerated and re-hashed after the remaining portal/metadata blockers are resolved.

## Strict blockers before submission

1. exact ordinary-submission article-type label in a valid current IJIO live portal/GFA;
2. IJIO-specific submission-fee status;
3. IJIO-specific review/anonymization model;
4. verified author/affiliation/corresponding-author metadata and factual funding/COI confirmations;
5. live confirmation of highlights/graphical-abstract/CRediT requirements.

Do not submit until these items are resolved and the user explicitly authorizes a later submission stage.