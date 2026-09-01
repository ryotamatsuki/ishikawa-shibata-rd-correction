# Stage 2 — Formal Derivation and Proof Completion

## Executive decision

`STAGE2_PASS`.

All six proof obligations frozen in Stage 1 are closed with exact symbolic algebra, exact rational verification, or exact root-isolation arguments. No model extension, new economic mechanism, welfare claim, downstream-literature claim, or manuscript prose was introduced.

## Starting state

- Dedicated repository starting main commit: `c899973479b71084a6db032cf9ce9cb3c4e905ae`
- Working branch: `stage2/formal-derivation-proof`
- Stage 1 status: `STAGE1_PASS`
- Frozen propositions: 3

## Proposition 1 — individual boundary

### Generic gamma-invariance fails analytically

On the exact asymmetric slice `lambda=0,beta_2=0`, the cleared equality polynomial is

`Q_I(B,G) = -27(2B-1)G^2 +18(2B^3-7B^2+12B-5)G -4(10B^3-35B^2+45B-18)`.

At the exact admissible regular root

`B=1/3, G=44/27`,

- `Q_I=0`,
- `Q_G=-4/3`,
- `Q_B=-236/27`,
- cleared denominator `=808640/19683 !=0`.

Hence by the implicit-function theorem

`dB*/dG=-9/59 !=0`.

This closes the analytic non-invariance obligation without relying on numerical threshold comparisons.

### Symmetric crossing

On `beta_1=beta_2=b`, the numerator of `D_1` factors exactly as

`-gamma(a-c)(lambda-3)^2 [b(lambda^2-3lambda+4)+lambda^2-lambda-2]`.

Thus on the regular domain

`b*(lambda)=(2+lambda-lambda^2)/(lambda^2-3lambda+4)`.

The gamma cancellation is exact and confined to this symmetric crossing.

## Proposition 2 — aggregate boundary

### Asymmetry dependence

At `lambda=0`, with `s=beta_1+beta_2` and `d=beta_1-beta_2`, the cleared aggregate equality polynomial satisfies on the published line `s=1`

`Q_A = d^2(18gamma+d^2-9)/2`.

For maintained `gamma>=1`, the second factor is strictly positive. After cancellation of this nonzero common factor, the exact aggregate difference on the published line is

`32 gamma d^2(a-c) / {[-6gamma+d^2+3][36gamma^2-20gamma d^2-36gamma+d^4+6d^2+9]}`.

Therefore every regular asymmetric point `d!=0` on the published line fails aggregate equality. The published straight line is not the general asymmetric equality locus.

### Gamma dependence of the corrected aggregate locus

On `lambda=0,beta_2=0`, the cleared aggregate equation is

`Q_A(B,G)=20B^4+18B^3G-106B^3-108B^2G+216B^2-27BG^2+171BG-198B+27G^2-90G+72`.

At `G=2`, this becomes

`Q_A(B,2)=2B(10B^3-35B^2+18)`.

The cubic factor is strictly decreasing on `(0,1)` and has a unique root `alpha` in

`4097/5000 < alpha < 1639/2000`,

or `alpha≈0.81945409098`.

The closed-form denominator is nonzero on this interval. Exact reduction modulo the root polynomial gives

- `Q_G(alpha,2)=-(9/5)(25alpha^2-35alpha+8)>0`,
- `Q_B(alpha,2)=2(35alpha^2-54)<0`.

Hence `d alpha*/dG=-Q_G/Q_B>0`. The corrected aggregate equality locus therefore depends locally on gamma at a regular asymmetric interior point.

## Proposition 3 — exact misclassification and positive measure

At

`a=100,c=50,gamma=10,lambda=0,beta_1=49/50,beta_2=0`,

the published fixed-cutoff rule classifies the point as competitive-R&D dominant because average spillover is `49/100<1/2`.

Exact retained equilibria are

- `x^n=(110500/100239,83220/33413)`,
- `x^c=(44500/19119,8300/6373)`.

Therefore

- aggregate noncooperative `=360160/100239`,
- aggregate cooperative `=69400/19119`,
- `D_A=-23562520/638823147<0`.

The sign reversal is exact. Outputs and marginal costs are positive; noncooperative and cooperative curvature conditions have the correct strict signs; all rational closed-form denominators are nonzero.

Because both the published cutoff inequality and the corrected `D_A<0` inequality are strict and the rational equilibrium functions are continuous on a regular neighborhood, the disagreement persists on an open neighborhood. Hence the misclassified parameter set has positive Lebesgue measure.

## Proof-obligation closure

| Stage-1 obligation | Evidence | Status |
|---|---|---|
| exact analytic individual gamma dependence | exact IFT point, derivative `-9/59` | CLOSED |
| symmetric crossing factorization | exact symbolic factorization | CLOSED |
| lambda-zero aggregate factorization | exact `(s,d)` factorization and canceled expression | CLOSED |
| analytic aggregate gamma dependence | unique regular root at `G=2` plus exact IFT signs | CLOSED |
| counterexample strict sign | exact rational `D_A<0` | CLOSED |
| denominator nondegeneracy / continuity | exact nonzero denominators and strict regularity | CLOSED |

## Verification code

`code/formal_derivation.py` uses SymPy exact arithmetic and assertions for the identities and regularity certificates above.

Validated locally with:

- Python 3.13.5
- SymPy 1.14.0

Expected terminal marker:

`STAGE2_FORMAL_DERIVATION_PASS`

## Scope controls checked

- equilibrium formulas preserved
- no global uniqueness claim
- no global gamma monotonicity claim
- no global lambda-nesting theorem
- no welfare-ranking reversal
- no downstream-literature consequence claim
- no absolute novelty claim
- no new model or mechanism
- no manuscript/abstract/introduction/conclusion drafting

## Stage 2 gate

PASS criteria:

1. all three frozen propositions have exact proof paths completed — PASS;
2. P1/P2 do not rely only on numerical evidence — PASS;
3. P3 strict sign is exact rational — PASS;
4. local regularity and continuity are explicit — PASS;
5. Stage-0 claim boundary remains respected — PASS;
6. no model extension needed — PASS.

Decision: **`STAGE2_PASS`**.

## Recommended next stage

After review and merge of the Stage-2 PR, proceed to **Dedicated Stage 3 — Manuscript Drafting and Internal Referee Review**. At that stage the three verified propositions may be converted into publication-ready exposition, while preserving the Stage-0 claim boundary and Stage-2 exact proof record.