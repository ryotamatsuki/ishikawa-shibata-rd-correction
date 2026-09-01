"""C019 full mathematical audit: Ishikawa & Shibata (2021).

The implementation is a deterministic, standard-library-only reconstruction of
the two-stage game. It builds the output equilibrium and the first-stage
objectives directly from primitives using affine/quadratic coefficient
arithmetic; it then solves the first-order systems and independently evaluates
the paper's published closed forms (Eq. 16 and Eq. 25).

Target:
    Nana Ishikawa and Takashi Shibata (2021),
    "R&D competition and cooperation with asymmetric spillovers in an
    oligopoly market", International Review of Economics & Finance 72,
    624-642, DOI 10.1016/j.iref.2020.12.016.

No random numbers or external packages are used.

Dedicated-repository copy of master path:
code/C019_ishikawa_shibata_2021_audit.py
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Tuple


@dataclass(frozen=True)
class Affine:
    """c + l1*x1 + l2*x2."""

    c: float
    l1: float = 0.0
    l2: float = 0.0

    def __add__(self, other: "Affine") -> "Affine":
        return Affine(self.c + other.c, self.l1 + other.l1, self.l2 + other.l2)

    def __sub__(self, other: "Affine") -> "Affine":
        return Affine(self.c - other.c, self.l1 - other.l1, self.l2 - other.l2)

    def scale(self, k: float) -> "Affine":
        return Affine(k * self.c, k * self.l1, k * self.l2)

    def value(self, x1: float, x2: float) -> float:
        return self.c + self.l1 * x1 + self.l2 * x2

    def product(self, other: "Affine") -> "Quadratic":
        return Quadratic(
            self.c * other.c,
            self.c * other.l1 + self.l1 * other.c,
            self.c * other.l2 + self.l2 * other.c,
            2.0 * self.l1 * other.l1,
            self.l1 * other.l2 + self.l2 * other.l1,
            2.0 * self.l2 * other.l2,
        )


@dataclass(frozen=True)
class Quadratic:
    """c + l1*x1 + l2*x2 + h11*x1^2/2 + h12*x1*x2 + h22*x2^2/2."""

    c: float
    l1: float = 0.0
    l2: float = 0.0
    h11: float = 0.0
    h12: float = 0.0
    h22: float = 0.0

    def __add__(self, other: "Quadratic") -> "Quadratic":
        return Quadratic(self.c + other.c, self.l1 + other.l1, self.l2 + other.l2,
                         self.h11 + other.h11, self.h12 + other.h12, self.h22 + other.h22)

    def __sub__(self, other: "Quadratic") -> "Quadratic":
        return Quadratic(self.c - other.c, self.l1 - other.l1, self.l2 - other.l2,
                         self.h11 - other.h11, self.h12 - other.h12, self.h22 - other.h22)

    def scale(self, k: float) -> "Quadratic":
        return Quadratic(k * self.c, k * self.l1, k * self.l2,
                         k * self.h11, k * self.h12, k * self.h22)

    def value(self, x1: float, x2: float) -> float:
        return (self.c + self.l1 * x1 + self.l2 * x2 + 0.5 * self.h11 * x1 * x1
                + self.h12 * x1 * x2 + 0.5 * self.h22 * x2 * x2)

    def gradient(self, x1: float, x2: float) -> Tuple[float, float]:
        return (self.l1 + self.h11 * x1 + self.h12 * x2,
                self.l2 + self.h12 * x1 + self.h22 * x2)


def solve2(a11: float, a12: float, a21: float, a22: float,
           b1: float, b2: float) -> Tuple[float, float]:
    determinant = a11 * a22 - a12 * a21
    if math.isclose(determinant, 0.0, abs_tol=1e-14):
        raise ValueError("Singular 2x2 system")
    return ((b1 * a22 - a12 * b2) / determinant,
            (a11 * b2 - b1 * a21) / determinant)


def output_equilibrium(A: float, C: float, L: float, B1: float, B2: float) -> Tuple[Affine, Affine]:
    denominator = (3.0 - L) * (1.0 + L)
    common = (1.0 + L) * (A - C) / denominator
    q1 = Affine(common, (2.0 - B1 + B1 * L) / denominator,
                (2.0 * B2 - 1.0 + L) / denominator)
    q2 = Affine(common, (2.0 * B1 - 1.0 + L) / denominator,
                (2.0 - B2 + B2 * L) / denominator)
    return q1, q2


def first_stage_objectives(A: float, C: float, G: float, L: float, B1: float, B2: float):
    q1, q2 = output_equilibrium(A, C, L, B1, B2)
    price = Affine(A) - q1 - q2
    mc1 = Affine(C, -1.0, -B2)
    mc2 = Affine(C, -B1, -1.0)
    gross1 = (price - mc1).product(q1)
    gross2 = (price - mc2).product(q2)
    f1 = gross1 - gross2.scale(L) - Quadratic(0.0, h11=G)
    f2 = gross2 - gross1.scale(L) - Quadratic(0.0, h22=G)
    return f1, f2, q1, q2


def primitive_xn(A: float, C: float, G: float, L: float, B1: float, B2: float):
    f1, f2, _, _ = first_stage_objectives(A, C, G, L, B1, B2)
    return solve2(f1.h11, f1.h12, f2.h12, f2.h22, -f1.l1, -f2.l2)


def primitive_xc(A: float, C: float, G: float, L: float, B1: float, B2: float):
    f1, f2, _, _ = first_stage_objectives(A, C, G, L, B1, B2)
    joint = f1 + f2
    return solve2(joint.h11, joint.h12, joint.h12, joint.h22, -joint.l1, -joint.l2)


def paper_xn(A: float, C: float, G: float, L: float, B1: float, B2: float):
    def d1(B):
        return 2 * (2 - B) + L * (1 - 3 * B - 2 * L + (1 + B) * L**2)

    def d2(B):
        return 2 * ((2 - B + B * L) * (2 - B - L)
                    - L * (2 * B - 1 + L) * (2 * B - 1 - B * L))

    def d3(Bi, Bj):
        return ((2 - Bi - L) * (2 * Bj - 1 + L)
                + (2 - Bi + Bi * L) * (2 * Bj - 1 - Bj * L)
                - L * ((2 - Bj - L) * (2 * Bi - 1 + L)
                       + (2 - Bj + Bj * L) * (2 * Bi - 1 - Bi * L)))

    d4 = G * (3 - L) ** 2 * (1 + L)
    d11, d21 = d1(B1), d1(B2)
    d12, d22 = d2(B1), d2(B2)
    d13, d23 = d3(B1, B2), d3(B2, B1)
    denominator = (d4 - d12) * (d4 - d22) - d13 * d23
    return ((d11 * (d4 - d22) + d21 * d13) / denominator * (A - C),
            (d21 * (d4 - d12) + d11 * d23) / denominator * (A - C))


def paper_xc(A: float, C: float, G: float, L: float, B1: float, B2: float):
    if math.isclose(L, 1.0):
        raise ValueError("Eq. (29) is singular at lambda=1; use a limit instead.")

    def p1(B):
        return 2 * (1 + L) * (1 - L) * (1 + B)

    def p2(B):
        return 2 * ((2 - B + B * L) * (2 - B - L)
                    + (2 * B - 1 + L) * (2 * B - 1 - B * L))

    def cross(Bi, Bj):
        return ((2 - Bi - L) * (2 * Bj - 1 + L)
                + (2 - Bi + Bi * L) * (2 * Bj - 1 - Bj * L))

    p3 = cross(B1, B2) + cross(B2, B1)
    p4 = G * (3 - L) ** 2 * (1 + L) / (1 - L)
    p11, p21 = p1(B1), p1(B2)
    p12, p22 = p2(B1), p2(B2)
    denominator = (p4 - p12) * (p4 - p22) - p3**2
    return ((p11 * (p4 - p22) + p21 * p3) / denominator * (A - C),
            (p21 * (p4 - p12) + p11 * p3) / denominator * (A - C))


def individual_difference(B1: float, B2: float, L: float, G: float,
                          A: float = 100.0, C: float = 50.0) -> float:
    xn = primitive_xn(A, C, G, L, B1, B2)
    xc = primitive_xc(A, C, G, L, B1, B2)
    return xn[0] - xc[0]


def aggregate_difference(B1: float, B2: float, L: float, G: float,
                         A: float = 100.0, C: float = 50.0) -> float:
    xn = primitive_xn(A, C, G, L, B1, B2)
    xc = primitive_xc(A, C, G, L, B1, B2)
    return sum(xn) - sum(xc)


def bisect_root(func: Callable[[float], float], lo: float, hi: float,
                tol: float = 1e-12, max_iter: int = 300) -> float:
    flo = float(func(lo)); fhi = float(func(hi))
    if flo == 0.0: return lo
    if fhi == 0.0: return hi
    if flo * fhi > 0:
        raise ValueError(f"Root is not bracketed: f({lo})={flo}, f({hi})={fhi}")
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fmid = float(func(mid))
        if abs(fmid) < tol or (hi - lo) / 2.0 < tol:
            return mid
        if flo * fmid <= 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2.0


def check_close_pair(lhs, rhs, tol=1e-10):
    return all(math.isclose(float(x), float(y), rel_tol=tol, abs_tol=tol)
               for x, y in zip(lhs, rhs))


def feasibility_checks(A: float, C: float, G: float, L: float, B1: float, B2: float):
    f1, f2, q1_aff, q2_aff = first_stage_objectives(A, C, G, L, B1, B2)
    xn = primitive_xn(A, C, G, L, B1, B2)
    xc = primitive_xc(A, C, G, L, B1, B2)
    qn = (q1_aff.value(*xn), q2_aff.value(*xn))
    qc = (q1_aff.value(*xc), q2_aff.value(*xc))
    mc_n = (C - xn[0] - B2 * xn[1], C - xn[1] - B1 * xn[0])
    mc_c = (C - xc[0] - B2 * xc[1], C - xc[1] - B1 * xc[0])
    own_second = (f1.h11, f2.h22)
    noncoop_jac_det = f1.h11 * f2.h22 - f1.h12 * f2.h12
    joint = f1 + f2
    coop_hessian_det = joint.h11 * joint.h22 - joint.h12**2
    return xn, xc, qn, qc, mc_n, mc_c, own_second, noncoop_jac_det, joint.h11, coop_hessian_det, f1, f2


if __name__ == "__main__":
    print("C019 — Ishikawa & Shibata (2021) full-audit replication")

    A, C, G, L, B1, B2 = 100.0, 50.0, 50.0, 0.0, 0.5, 0.0
    q1_aff, q2_aff = output_equilibrium(A, C, L, B1, B2)
    qtest = (q1_aff.value(0.7, 1.1), q2_aff.value(0.7, 1.1))
    residuals = ((A - C + 0.7 + B2 * 1.1) - 2.0 * qtest[0] - (1.0 - L) * qtest[1],
                 (A - C + 1.1 + B1 * 0.7) - 2.0 * qtest[1] - (1.0 - L) * qtest[0])
    assert max(abs(v) for v in residuals) < 1e-10
    print("Primitive output-stage FOCs reproduce published Eqs. (8)-(9): PASS")

    tau_g50 = bisect_root(lambda b1: individual_difference(b1, 0.0, 0.0, 50.0), 0.0, 1.0)
    print(f"Table-1 check, lambda=0, beta_j=0, gamma=50: tau={tau_g50:.12f}")
    assert round(tau_g50, 4) == 0.4966

    print("\nObservation 1 gamma-sensitivity, lambda=0, beta_j=0:")
    tau_values = {}
    for G in (10.0, 50.0, 100.0):
        root = bisect_root(lambda b1, G=G: individual_difference(b1, 0.0, 0.0, G), 0.0, 1.0)
        tau_values[G] = root
        print(f"  gamma={G:6.1f} -> tau={root:.12f}")
    assert abs(tau_values[10.0] - tau_values[50.0]) > 1e-3
    assert abs(tau_values[50.0] - tau_values[100.0]) > 1e-3

    B1, B2, L = 0.49, 0.0, 0.0
    d10 = individual_difference(B1, B2, L, 10.0)
    d50 = individual_difference(B1, B2, L, 50.0)
    print(f"  beta1=.49, beta2=0, lambda=0: x1^n-x1^c={d10:.12f} at gamma=10; {d50:.12f} at gamma=50")
    assert d10 < 0 < d50

    print("\nSpecial-slice check, lambda=0, beta_j=1/2:")
    for G in (10.0, 50.0, 100.0):
        root = bisect_root(lambda b1, G=G: individual_difference(b1, 0.5, 0.0, G), 0.0, 1.0)
        print(f"  gamma={G:6.1f} -> tau={root:.12f}")
        assert math.isclose(root, 0.5, abs_tol=1e-10)

    print("\nObservation 4 aggregate boundary, lambda=0, beta2=0:")
    theta_edge = {}
    for G in (10.0, 50.0, 100.0):
        root_b1 = bisect_root(lambda b1, G=G: aggregate_difference(b1, 0.0, 0.0, G), 0.0, 1.0)
        theta_edge[G] = root_b1
        print(f"  gamma={G:6.1f} -> boundary beta1+beta2={root_b1:.12f}")
    assert abs(theta_edge[10.0] - theta_edge[50.0]) > 1e-3

    A, C, G, L, B1, B2 = 100.0, 50.0, 10.0, 0.0, 0.98, 0.0
    xn, xc, qn, qc, mc_n, mc_c, own_second, noncoop_jac_det, h11, coop_hessian_det, f1, f2 = feasibility_checks(A, C, G, L, B1, B2)
    aggregate_gap = sum(xn) - sum(xc)
    print("\nConsequence counterexample to Eq. (45)/Observation 5:")
    print(f"  x^n={xn}, aggregate={sum(xn):.12f}")
    print(f"  x^c={xc}, aggregate={sum(xc):.12f}")
    print(f"  x^n-x^c={aggregate_gap:.12f}")
    assert (B1 + B2) / 2.0 < 0.5
    assert aggregate_gap < 0.0

    xn_paper = paper_xn(A, C, G, L, B1, B2)
    xc_paper = paper_xc(A, C, G, L, B1, B2)
    assert check_close_pair(xn, xn_paper)
    assert check_close_pair(xc, xc_paper)
    print("Independent closed-form verification: PASS")

    assert all(v > 0.0 for v in xn + xc + qn + qc + mc_n + mc_c)
    f_n = (f1.value(*xn), f2.value(*xn))
    f_c = (f1.value(*xc), f2.value(*xc))
    assert all(v > 0.0 for v in f_n + f_c)
    assert all(v < 0.0 for v in own_second)
    assert noncoop_jac_det > 0.0
    assert h11 < 0.0 and coop_hessian_det > 0.0
    print("Feasibility / positivity / local stability-optimality checks: PASS")

    print("\nAUDIT RESULT:")
    print("  Observation 1 gamma-invariance: NOT REPRODUCED")
    print("  Observation 4 gamma-invariance / straight aggregate boundary: NOT REPRODUCED")
    print("  Eq. (45)/Observation 5 classification at admissible point: REVERSED")
    print("  Mathematical classification supported by this script: ERROR_CONFIRMED")
