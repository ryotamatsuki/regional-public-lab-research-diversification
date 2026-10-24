# Stage 05: IJIO-response audit

This directory contains a **non-destructive research checkpoint**. Earlier checkpoints and the main branch remain unchanged.

- `REPORT.md` — R1–R10: general price-incidence decomposition; exact conditional fixed-adoption neutrality; counterexample; symmetric signed theorems; adversarial novelty analysis; verification scope; journal fit and next gates.
- `verify_ijio.py` — independent Python 3 script using NumPy/SciPy/SymPy (does not import stage04 model); symbolic, linear, non-linear and rational-certificate checks.
- `RUN_RESULTS.json` — compact numerical record from an **independent local audit program**, with rounded displayed outputs and explicitly distinguished verification limits.

### Run locally

```bash
python -m pip install numpy scipy sympy
python checkpoints/2026-10-24/05_ijio_response/verify_ijio.py
```

The script should terminate without assertion failures and print JSON containing a two-region algebraic wedge, the three linear benchmarks, 24 nonlinear finite-difference comparisons, and the exact rational national-zero-effort certificate.

### Scope and nonclaims

The analytical arbitrary-V incidence formula is proved in the report. **Novelty is not established** by writing an envelope calculation in general notation. The script checks symmetric benchmarks, not a completely general nonlinear asymmetry theorem. The new script itself has not been executed by GitHub Actions in the remote repository. Independent local computations used for `RUN_RESULTS.json` were completed with a separate, longer audit program; exact identity and baseline numbers were checked there. Historical exhaustive global Nash branch enumeration remains in `../04_varietal_replacement/verify_breeding.py`.

**Decision:** IJIO criterion partially overcome; research status REVISE, with a qualified JARE/CJAE/ARER path only after close prior-art equivalence and a nontrivial policy proposition. No merger of this draft checkpoint should be read as journal acceptance or certification.
