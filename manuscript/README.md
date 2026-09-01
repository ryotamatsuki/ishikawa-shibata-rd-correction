# Manuscript Workspace

Stage 3 has produced an internal publication-facing correction manuscript. It is not yet a journal-specific submission package.

## Manuscript package

- `main.tex` — modular top-level LaTeX source
- `sections/01_introduction.tex` through `sections/05_implications.tex` — five main sections
- `sections/appendix_A.tex` through `sections/appendix_D.tex` — exact algebra/regularity appendix
- `references.bib` — bibliography source
- `FORMAL_DERIVATIONS.md` — Stage-2 canonical exact proof record
- `../figures/aggregate_boundary.pdf` — one illustrative corrected-boundary figure
- internal build target: `manuscript_draft.pdf`

## Frozen scope

- propositions: 3
- main figures: 1
- main tables: 0
- main text: approximately 3,520 words
- appendix sections: 4
- equilibrium formulas preserved
- no welfare-ranking reversal, absolute novelty, global lambda nesting, model extension, or downstream-literature claim

## Internal referee status

Round 1: `MINOR_INTERNAL_REVISION`.

Round 2 after mandatory revision: `READY_FOR_JOURNAL_STRATEGY`.

The manuscript remains controlled by `CLAIM_BOUNDARY.md` and the exact proof package in `FORMAL_DERIVATIONS.md` / `code/formal_derivation.py`.

## Not yet resolved

- journal/article type
- final journal-specific title and format
- author/affiliation metadata
- repository disclosure/public-release plan
- cover letter and submission files

Next stage after Stage-3 PR review/merge: `Dedicated Stage 4 — Journal Strategy and Submission-Readiness Review`.
