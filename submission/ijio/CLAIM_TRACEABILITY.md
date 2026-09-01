# Stage-5 claim traceability

| Submission-manuscript claim | Proposition | Formal derivation / exact certificate | Code check | Stage-0 permission |
|---|---|---|---|---|
| Published equilibrium formulas used in the comparison are retained | manuscript scope statement | independent reconstruction / Stage-2 proof record | retained closed-form checks | `CLAIM_BOUNDARY.md` allowed claim 1 |
| Individual equality boundary is not gamma-invariant in general | Proposition 1 | exact regular point `(beta_1,gamma)=(1/3,44/27)` and `d beta_1*/d gamma=-9/59` | `formal_derivation.py` P1 assertions | allowed claim 2 |
| Symmetric crossing is exactly gamma-independent | Proposition 1 | exact symmetric factorization | `formal_derivation.py` symmetric factor assertions | allowed claim 3 |
| Aggregate equality is not generally a scalar constant-sum line | Proposition 2 | lambda-zero `s=1` factorization `d^2(18 gamma+d^2-9)/2` | `formal_derivation.py` aggregate factor assertion | allowed claims 4–5 |
| Corrected aggregate boundary is locally gamma-dependent | Proposition 2 | regular nonzero root at `G=2` and IFT sign certificate | `formal_derivation.py` root-bracket / derivative-reduction assertions | allowed claim 4 |
| Published fixed cutoff and corrected aggregate comparison disagree at an admissible point | Proposition 3 | exact rational counterexample | exact aggregate/gap assertions | allowed claim 6 |
| Misclassification persists on a positive-measure set | Proposition 3 | strict signs + regularity + continuity | exact strict sign and regularity certificates | allowed claim 6 |
| The note does not establish a welfare-ranking reversal | scope limitation | no welfare theorem is derived | not applicable | prohibited claims 7–8 respected |
| Broad competitiveness direction is not claimed to reverse globally | scope limitation | Stage-3 consequence boundary | not promoted to theorem | prohibited claim 6 respected |
| Observation 6 is not claimed to be overturned | scope limitation | published-calibration recomputation | consequence-audit provenance | prohibited claim 5 respected |

Result: `PASS`. No headline claim in the IJIO package exceeds the Stage-0 claim boundary or the Stage-2 exact proof record.