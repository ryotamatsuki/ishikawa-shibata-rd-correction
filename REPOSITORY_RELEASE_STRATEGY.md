# Repository Release Strategy

Status: `FROZEN_STAGE4`.

## Current state

Repository `ryotamatsuki/ishikawa-shibata-rd-correction` is private. Stage 4 does **not** change repository visibility.

The repository contains publication-facing derivations, deterministic reproduction/formal-verification scripts, manuscript source, figure source, internal referee records and publication governance. Master audit history remains in `ryotamatsuki/economic-theory-replication-audit`.

## Primary-journal review-model uncertainty

The current public IJIO pages accessed during Stage 4 did not expose a reliable journal-specific statement of single- versus double-anonymous review. Therefore anonymity must not be inferred.

Decision: **keep the canonical GitHub repository private through Stage-5 package construction until the live IJIO portal/GFA confirms the review model.**

## Recommended route

`ROUTE C + ANONYMIZED REVIEW SNAPSHOT IF NEEDED`.

1. Keep canonical GitHub repository private at initial package-preparation stage.
2. If IJIO uses or permits author-identifying review, provide an appropriate code/repository link or supplementary archive consistent with the live submission instructions.
3. If reviewer anonymity requires removal of author identity, prepare a clean anonymized review snapshot containing only publication-facing scripts, dependency file, minimal README and reproduction instructions. Do not expose Git history, usernames, internal audit correspondence or identifying project-management records to reviewers.
4. At acceptance/publication stage, make a citable public archival release of the publication-facing reproducibility package, subject to publisher policy and author approval.
5. Consider Zenodo or another DOI-minting archive for the final public release so the code snapshot is versioned independently of the mutable GitHub main branch.

## Code/data availability logic

No empirical dataset is analyzed. The paper's central claims are analytic. Deterministic Python/SymPy scripts verify the exact algebra and numerical certificates; the aggregate-boundary figure is generated deterministically from code.

Stage-5 working data/code statement should distinguish:

- **Data:** no external empirical dataset was used.
- **Code:** deterministic verification/reproduction code is available in the project package and will be made available to reviewers/published readers in a manner compatible with journal anonymity and repository policy.

Do not claim a public URL until one actually exists.

## Preprint strategy

Elsevier's general sharing policy permits authors to share preprints. Stage 4 does not create or post a preprint. Because the project is a correction of a named paper, a public preprint could improve discoverability, but the decision should be made in Stage 5 after the live IJIO article-type/review requirements are known.

## Archival strategy

Preferred final route after acceptance, or earlier if IJIO policy clearly permits and anonymity is not compromised:

1. tag/freeze publication version in GitHub;
2. archive publication-facing subset on Zenodo or equivalent;
3. obtain DOI;
4. update manuscript/code-availability statement with the immutable DOI;
5. retain master audit repo as provenance history, not as the manuscript-facing archive.

## Exact Stage-5 actions

1. confirm IJIO review model and repository-link policy in live portal/GFA;
2. build anonymized code snapshot if required;
3. decide supplementary ZIP vs private reviewer link vs public archive;
4. write final data/code availability statement;
5. do **not** change canonical repo visibility until the author explicitly approves the release action.

Stage-4 repository decision: **PRIVATE NOW; PUBLIC/ARCHIVAL RELEASE DEFERRED AND CONTROLLED.**