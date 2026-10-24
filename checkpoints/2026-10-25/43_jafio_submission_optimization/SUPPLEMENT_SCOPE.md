# Anonymous Reproducibility Supplement — Scope and QA

Date: 2026-10-25 JST. Build script: `make_blinded_supplement.py`; output: `JAFIO_Blinded_Reproducibility.zip`. This is a new packaging of existing frozen verification materials, not a new economic result or a full-paper formal-proof certificate.

## Exact contents

- Nine self-contained Python programs: the six exact programs called by the Stage 9 runner, independent Stage 11 primitive reconstruction, and the two checkpoint-12 programs for the secondary interacting rational case.
- Existing Lean root module, seven proof modules, `lakefile.lean`, and `lean-toolchain`.
- Anonymous README, Python subprocess runner, pinned `sympy==1.13.3` requirements, and SHA-256 manifest.

Python programs are flattened into a `python/` directory only after source inspection found their imports and mathematical calculations self-contained; no repository-relative imports or external data reads are needed. Their bytes, and all Lean source/configuration bytes, are copied unchanged. The runner is a new standard-library orchestration script. SHA-256 entries identify every nonmanifest member. ZIP entries have fixed neutral timestamps and permissions; no filesystem ownership fields are added.

The archive excludes `.git`, GitHub history, internal audit reports, personal-author contribution records, workflow reports, publication strategy, citation-access audits and identifying repository links. The builder scans every text member for the project owner's name/login, employer/region name, personal repository metadata, workspace paths and private-record tokens. The sole GitHub URL admitted is the generic mathlib dependency URL in `lakefile.lean`. Anonymity checks reduce direct metadata leakage; they cannot prevent recognition from manuscript subject matter or public pre-existing research.

## Licensed assurance and limitations

The exact Python programs cover primitive-to-price and planting gradients, the symmetric interior P1 wedge, one exact nonlinear incidence instance, bounded cost variations and unequal-curvature midpoint counterexample, P3+ global analytic identities/boundary, and global unilateral best responses in the two specified interacting rational cases. They do not establish all-demand robustness, all-parameter equilibria or uniqueness among all asymmetric interacting equilibria.

The Lean sources check the encoded proof-critical core: conditional quadratic/KKT and first-order identities, the analytic P3+ global family with market-to-payoff bridge and excluded endpoint, and specified interacting candidate/planner identities. General-N nonlinear-demand coverage is conditional Jacobian algebra; neither the full nonlinear economic derivation nor interacting nine-regime Nash globality is fully Lean-formalized. The manuscript proofs remain the reader-facing economic arguments.

Lean 4.35.0 and mathlib v4.35.0 are specified. `lake update` requires network access. This packaging does not add a locked transitive dependency manifest or bundle third-party caches. The combined CI separately rebuilds the unchanged Lean project and audits axioms; successful extracted Python reproduction must not be reported as a Lean kernel build.

The README discloses substantive ChatGPT assistance in writing and verification-code/formal-source development. Computational checks do not certify human rederivation, originality or journal-policy eligibility.

## Test

`python make_blinded_supplement.py --test` creates the archive, extracts it to a fresh temporary directory, verifies every manifest hash and runs the standalone Python runner from that extracted directory. Output is recorded in `SUPPLEMENT_QA_RESULTS.txt`. The combined JAFIO workflow repeats this build/test and uploads the ZIP with the review PDF and LaTeX source package. The final CI run URL/SHA belongs in `REPORT.md`; local success is not substituted for final-commit CI.
