Regional public lab research diversification: audit and candidate extension
Date: 2026-10-24

Read research_audit_2026-10-24.md first.

Reproduce the exact arithmetic:
  python -m pip install sympy==1.14.0
  python verify_extension.py

This recreates results.json. model_check.py reconstructs the product-market
sufficient statistics independently from the original manuscript's primitives.

The probability/capacity-cost experiment in the proposed extension is NEW to
this audit. It is not a re-run of the original capacity-investment equilibrium.
The original market primitives are retained, but the central direct capacity
investment policy menu is a new modeling assumption.

PASS is an arithmetic/model-consistency verdict. It is NOT a novelty
certificate, external peer review, unrestricted mechanism-design theorem,
legal feasibility opinion, or promise of journal acceptance.
