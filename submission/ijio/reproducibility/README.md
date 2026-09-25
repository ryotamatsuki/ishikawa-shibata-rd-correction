# Reviewer-safe reproducibility package

This directory contains no GitHub username, author identity, absolute personal path, network dependency, or stochastic simulation.

Stage-5 preflight environment:
- Python 3.13.5
- SymPy 1.14.0
- NumPy 2.3.5
- Matplotlib 3.10.8

Run:

```bash
python formal_derivation.py
python figure_aggregate_boundary.py
```

Expected first terminal marker from the symbolic check:

`STAGE5_REPRODUCIBILITY_PASS`

The symbolic script verifies the individual-boundary IFT certificate, the exact symmetric crossing, the aggregate-line factorization and local gamma-dependence certificate, and the exact rational counterexample. The figure script regenerates the aggregate-boundary vector PDF. No external empirical dataset is used.
