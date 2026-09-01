# Stage 5 Reproducibility Preflight

Date: 2026-09-01.

Decision: `PASS`.

Environment:
- Python 3.13.5
- SymPy 1.14.0
- NumPy 2.3.5
- Matplotlib 3.10.8
- no network access used by verification scripts
- no stochastic simulation

Execution marker: `STAGE5_REPRODUCIBILITY_PASS`.

Verified outputs:
- P1 local root derivative: `-9/59`;
- P1 symmetric crossing: `(2+lambda-lambda^2)/(lambda^2-3lambda+4)`;
- P2 isolated root bracket: `4097/5000 < alpha < 1639/2000`;
- P3 exact aggregates: `360160/100239` and `69400/19119`;
- P3 exact gap: `-23562520/638823147`.

Figure regeneration succeeded as a vector PDF from deterministic Python/Matplotlib code.

Reviewer-safety QC:
- no GitHub username;
- no author identity;
- no absolute local paths;
- no network calls;
- dependency versions listed;
- expected terminal marker documented.
