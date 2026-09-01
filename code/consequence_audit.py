"""C019 Stage 3 consequence audit.

Paper: Ishikawa & Shibata (2021), IREF 72, 624-642.
DOI: 10.1016/j.iref.2020.12.016

Purpose: paper-internal consequence mapping only. This script uses the paper's
published closed-form R&D solutions (Eqs. 16-20 and 25-29) as an independent
computational route, then recomputes individual and aggregate regime boundaries.
It is deterministic and uses only the Python standard library.

Dedicated-repository copy of master path:
code/C019_stage3_consequence_audit.py
"""

from __future__ import annotations

import math


def solve2(a11, a12, a21, a22, b1, b2):
    det = a11 * a22 - a12 * a21
    if abs(det) < 1e-14:
        raise ValueError("singular system")
    return ((b1 * a22 - a12 * b2) / det,
            (a11 * b2 - b1 * a21) / det)


def paper_xn(A, C, G, L, B1, B2):
    """Published Eqs. (16)-(20)."""
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
    den = (d4 - d12) * (d4 - d22) - d13 * d23
    return ((d11 * (d4 - d22) + d21 * d13) / den * (A - C),
            (d21 * (d4 - d12) + d11 * d23) / den * (A - C))


def paper_xc(A, C, G, L, B1, B2):
    """Published Eqs. (25)-(29)."""
    if math.isclose(L, 1.0):
        raise ValueError("Eq. (29) is singular at lambda=1; use a limit")

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
    den = (p4 - p12) * (p4 - p22) - p3**2
    return ((p11 * (p4 - p22) + p21 * p3) / den * (A - C),
            (p21 * (p4 - p12) + p11 * p3) / den * (A - C))


def individual_difference(B1, B2, L, G, A=100.0, C=50.0):
    xn, xc = paper_xn(A, C, G, L, B1, B2), paper_xc(A, C, G, L, B1, B2)
    return xn[0] - xc[0]


def aggregate_difference(B1, B2, L, G, A=100.0, C=50.0):
    xn, xc = paper_xn(A, C, G, L, B1, B2), paper_xc(A, C, G, L, B1, B2)
    return sum(xn) - sum(xc)


def bisect_root(func, lo=0.0, hi=1.0, tol=1e-13):
    flo, fhi = func(lo), func(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = func(mid)
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def individual_trigger(B2, L, G):
    return bisect_root(lambda B1: individual_difference(B1, B2, L, G))


def aggregate_boundary(B2, L, G):
    return bisect_root(lambda B1: aggregate_difference(B1, B2, L, G))


def symmetric_crossing(L):
    """Exact gamma-independent crossing on B1=B2, derived symbolically."""
    return (2 + L - L * L) / (L * L - 3 * L + 4)


def published_aggregate_threshold(L):
    """The paper's theta(lambda)=2*y(lambda), with y the symmetric crossing."""
    return 2 * symmetric_crossing(L)


def counterexample():
    pars = dict(A=100.0, C=50.0, G=10.0, L=0.0, B1=0.98, B2=0.0)
    xn = paper_xn(**pars)
    xc = paper_xc(**pars)
    return xn, xc, sum(xn) - sum(xc)


def grid_misclassification(L, G, n=401):
    """Area-share proxy on [0,1]^2; diagonal omission is measure zero."""
    theta = published_aggregate_threshold(L)
    disagree = total = pub_comp_corr_coop = pub_coop_corr_comp = 0
    for i in range(n):
        B1 = i / (n - 1)
        for j in range(n):
            B2 = j / (n - 1)
            if i == j:
                continue
            corr = aggregate_difference(B1, B2, L, G) > 0
            pub = B1 + B2 < theta
            total += 1
            if corr != pub:
                disagree += 1
                if pub:
                    pub_comp_corr_coop += 1
                else:
                    pub_coop_corr_comp += 1
    return (disagree / total,
            pub_comp_corr_coop / total,
            pub_coop_corr_comp / total)


def corrected_composite_difference(B1, B2, L, G):
    """Paper Eq. (47), but branch on the recomputed aggregate ranking."""
    xn = paper_xn(100.0, 50.0, G, L, B1, B2)
    xc = paper_xc(100.0, 50.0, G, L, B1, B2)
    xsn = paper_xn(100.0, 50.0, G, L, B1, B1)
    xsc = paper_xc(100.0, 50.0, G, L, B1, B1)
    if sum(xn) > sum(xc):
        return abs(sum(xn) - sum(xsn))
    return abs(sum(xc) - sum(xsc))


def main():
    print("C019 Stage 3 consequence audit")
    print("\nIndividual trigger: beta2=0, lambda=0")
    for G in (10.0, 50.0, 100.0):
        print(G, individual_trigger(0.0, 0.0, G))

    print("\nAggregate boundary beta1*: beta2=0, lambda=0")
    for G in (10.0, 50.0, 100.0):
        print(G, aggregate_boundary(0.0, 0.0, G))

    print("\nSpecial symmetric crossings (gamma independent)")
    for L in (0.0, 1/6, 1/3, 1/2, 2/3, 5/6):
        print(L, symmetric_crossing(L))

    print("\nCounterexample")
    xn, xc, diff = counterexample()
    print("xn", xn, "sum", sum(xn))
    print("xc", xc, "sum", sum(xc))
    print("aggregate difference", diff)
    assert diff < 0
    assert 0.98 < published_aggregate_threshold(0.0)

    print("\nMisclassification area-share proxies")
    for L in (0.0, 1/3):
        for G in (10.0, 50.0, 100.0):
            print("lambda", L, "gamma", G, grid_misclassification(L, G, 301))

    print("\nFig.4/Observation-6 selected-slice corrected monotonicity check")
    L, G, N = 1/3, 50.0, 1001
    for B2, direction in ((0.0, "increasing"), (1.0, "decreasing")):
        vals = [corrected_composite_difference(i/(N-1), B2, L, G) for i in range(N)]
        diffs = [vals[i+1]-vals[i] for i in range(N-1)]
        ok = all(d >= -1e-10 for d in diffs) if direction == "increasing" else all(d <= 1e-10 for d in diffs)
        print("beta2", B2, direction, ok)
        assert ok

    print("\nPASS")


if __name__ == "__main__":
    main()
