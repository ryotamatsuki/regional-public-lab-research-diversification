# Canonical Stage 9 — Repository, Provenance and Reproducibility Setup

**Date:** 2026-10-25 JST  
**Project:** Regional Public Breeding and Variety Replacement  
**Branch:** \`research/2026-10-24-ijio-response-audit\`, Draft PR #2.  
**Theoretical authority:** \`checkpoints/2026-10-25/30_canonical_stage8_theory_freeze_v2/REPORT.md\`.  
**Verdict:** **STAGE 9 GO — SOURCE/REGRESSION REPRODUCIBILITY SETUP CERTIFIED WITH EXPLICIT ENVIRONMENT LIMITATIONS**, not Stage 10 publication-ready and not new mathematical certification.

## 1. Stage 9 implementation (actual repository changes)

**New scoped production files**, all under this checkpoint:
- \`frozen_source_manifest.json\`: 25 authoritative Git blob IDs for Stage 8 frozen original mathematical and manuscript sources, the author attestation and certificates, seven top-level/child Lean modules, formal package metadata, and 6 runnable exact verification scripts. Fails on deletion or byte change instead of silently testing a different theorem version.
- \`verify_all.py\`: self-contained orchestrator validating Git-blob integrity using the real Git header with NUL separator, one LaTeX document/appendix, unique reference labels and BibTeX citation keys, unilateral-versus-mutual payoff bridge, plus six previously existing independent or preregistered exact SymPy scripts. Python runner may be invoked from any directory and resolves paths relative to \`__file__\`.
- \`requirements.txt\`: Python 3.11 in CI, \`sympy==1.13.3\`, \`mpmath==1.3.0\`.
- \`Makefile\`: \`deps\`, \`verify\`, \`formal\`, \`pdf\`, \`all\` targets with absolute source paths relative to this checkpoint.
- \`.github/workflows/public-breeding-stage9.yml\`: CI on this branch and checkpoint changes; installs exact pinned Python dependencies; runs source integrity and all six tests; no credentials or external data needed after dependency installation.

**No new economic game, new theorem, model coefficients, Lean proof, manuscript argument or empirical estimate** were added. Historical Stage 9 report at \`20_stage9_10_manuscript/STAGE9_REPRODUCIBILITY.md\` was provisional before Stage 8 GO; the present checkpoint supersedes its conditional routing, not its history.

**Important code hygiene incident discovered and corrected:** The archived \`14_full_paper_reopen_p3_analytic_open_set/verify_analytic_wasteful_rd.py\` compared \`s.factor(s.diff(F,x))\` by Python *structural equality* to an expanded rational expression. SymPy 1.13.3 returns an algebraically identical factored representation, so the old assertion failed while the exact difference simplified to zero. Corrected **only** the test line to \`assert s.simplify(s.diff(F,x)-(1+3*z-13*x)/8)==0\`, with zero change to demand, Nash model, polynomial identity, paper theorem or mathematical conclusion. The new Git blob \`6070ecb9c7386c36830abd76cdafe70013d8a13d\` replaces the old verifier blob in the frozen-source manifest; older archived original script remains retrievable from history. This is a *source/equality test correction*, not new theory and not evidence that all similarly archived scripts passed unchanged.

## 2. Actual CI evidence and independent re-runs

**New Stage 9 single-workflow run:**
- [run 40115835689](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40115835689) — **SUCCESS** at commit \`6c4c6ee3bc3373665680aabc9724b39f16927b7e\`, includes explicit \`sympy==1.13.3\` and \`mpmath==1.3.0\` pins.
- Prior full six-check run [40115767343](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40115767343) — **SUCCESS**; log explicitly shows 25 blob matches, 32 unique LaTeX labels, 6 BibTeX keys referenced, all six scripts and strict coupled Nash global check.
- First expanded six-test run [40115653477](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40115653477) — **FAIL**, archived, diagnostic evidence of the structural-equality test mistake; fixed and rerun, NOT erased.

Specific reproduced assertions:
1. Four-good utility/prices, competitive planting KKT, P1 research wedge, payoff off-path (including full adoption), P3+ exact nationwide welfare and cutoff, positive definiteness;
2. A distinct genuine nonlinear 3-region/six-good exact primitive model: incidence wedge \`2/9\`;
3. Pre-registered T1 quartic public research cost: positive local research, national zero; T2 unequal old/new curvature: \`-1/16\` at equal adoption; T3 quartic grower conversion: \`7/151\`;
4. Exactly two first-stage best responses at \`z=zCut\`, four pure research profiles at the excluded cutoff;
5. Analytic P3+ closed-form research effort, interval and national welfare identity (after shape-equality test repair);
6. Coupled \`e=1/100\` original model: **nine potential grower active-set statuses**, 7 nonempty research intervals, 9 global best-response candidates compared exactly, global symmetric local \`xD=9751/130096\`, \`aD=1051/32524\`, cross research derivative \`-50/39999\`, negative national welfare \`-1933000423/211562115200\`. This is an **exact global unilateral best-response audit** and a verified symmetric Nash, NOT proof that all asymmetric equilibrium profiles are absent or that every e>0 model exhibits the phenomenon.

**Existing separate Lean and PDF CI runs, source-fidelity checked in Stage 8:**
- [Lean build 40080770116](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40080770116) **SUCCESS**, Lean 4.35.0 and mathlib v4.35.0, 107 declarations axiom-audited per Stage 8 archive, valid only for encoded proof-critical core. Original Lean blobs unchanged.
- [Stage 11 independent core 40087931474](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087931474) **SUCCESS** on frozen scripts; Stage 9 explicitly reran both of those scripts in its own CI.
- [Draft PDF 40088099434](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40088099434) and [PDF QA 40088099590](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40088099590) **SUCCESS** on an earlier frozen manuscript blob matching the present Stage 8 source. They are historical runs; no fresh PDF compilation was done in this Stage 9 CI. PDF is an ephemeral workflow artifact (retention limits), not a permanently pinned downloadable file.

**Formal coverage limitations deliberately preserved:** \`Prop2N.lean\` proves conditional N-region Jacobian response algebra, not the full arbitrary nonlinear economic demand model; exact \`e>0\` 9-status global BR is SymPy and is NOT Lean formalization. No automatic claim of an entirely Lean-verified economic paper.

## 3. How an independent reviewer reproduces the code results

From a clean checkout of the branch \`research/2026-10-24-ijio-response-audit\`, with Python 3.11 and pip:

\`\`\`bash
python -m pip install -r checkpoints/2026-10-25/31_stage9_reproducibility/requirements.txt
python checkpoints/2026-10-25/31_stage9_reproducibility/verify_all.py
\`\`\`

Optional Makefile entrypoint:
\`\`\`bash
make -f checkpoints/2026-10-25/31_stage9_reproducibility/Makefile verify
make -f checkpoints/2026-10-25/31_stage9_reproducibility/Makefile formal
make -f checkpoints/2026-10-25/31_stage9_reproducibility/Makefile pdf
\`\`\`

\`verify\` is genuinely demonstrated successful on GitHub Actions. \`formal\` requires a working Lean/Lake toolchain with network/cached mathlib and is evidenced by the **separate** successful Lean workflow; \`pdf\` requires an external LaTeX distribution (\`latexmk\`, natbib etc.) and is evidenced by the **separate** manuscript workflow. **The Makefile \`all\` target itself has not been run end-to-end**, so no such claim is made.

## 4. Freeze object/provenance and boundaries

Research source includes Stage 8 v2 model, Stage 4A original theorem certificate, Stage 7.5A robustness/quantifier/formal source map, author self-attestation, current 10-page working LaTeX manuscript, \`references.bib\`, exact scripts, Lean code and independent scripts. Each original frozen artifact is pinned in \`frozen_source_manifest.json\`. Root \`README.md\` and \`PROJECT_STATUS.md\` concern an older, **distinct public-lab research-diversification direction project**. The frozen public-breeding work is scoped to checkpoint directories on the draft PR branch; avoid accidentally invoking unrelated root manuscripts or overwriting that project.

**Benchmark register:** farmer conditional adoption at fixed x; region Nash with follower KKT under all unilateral deviation branches; national unconstrained-vs-existing-technology joint welfare benchmark; mutual zero-effort (different from a unilateral cutback); e>0 exact symmetric Nash supporting example (not all-profile uniqueness). Precise accounts and restrictions in Stage 8 v2.

**Negative results/regression register:** T2 asymmetric curvature nonneutral \`-1/16\` at adoption one half; P3+ lower bound exactly 4 Nash; P3+ \`e=j=0\` no cross research BR; finite e>0 check not generalized; objective weights/fiscal shares/royalty shift threshold. These are not to be dropped in later exposition to claim universal effect.

**Current environment limitations:** Python dependencies explicitly version-pinned but \`pip\` wheels are not hash-locked; GitHub setup actions use version tags rather than immutable action commits; Lean toolchain and mathlib tagged but a transitive \`lake-manifest.json\` is not committed; LaTeX GitHub Action image/environment not permanently pinned; no real-world data or raw empirical dataset (none needed for theoretical paper). These are documented reproducibility risks rather than false mathematical claims or blockers to the code-only Stage 9 GO.

**No data/figures:** No empirical dataset is asserted; charts are not necessary to establish the frozen theorem. Do not create a decorative numerical chart and call it an empirically validated research figure. Manuscript bibliographic key existence checks are technical, **not full scholarly metadata fact verification**.

## 5. Stage exit and next handoff

**Stage 9 GO for evidence-backed reproducibility and repository production setup.** The source integrity register and six-script CI run are newly executed, while formal and PDF pipelines have separately successful historical proofs. The documented limits do not stop a theoretical manuscript production route, and no theory extension is authorized.

**Next canonical Stage 10:** use existing \`20_stage9_10_manuscript/paper.tex\` and its bibliography to perform final text, proof clarity, publication style/appropriate length and full PDF QA from the now-canonical Stage 8 theory freeze. Check discussion/abstract do not exaggerate general novelty; verify proof bridge and reference metadata, AI-use disclosure and publisher-format suitability. Stage 10 must not claim automatically to have passed because an earlier working PDF built. Stage 11 hostile manuscript review and Stage 12 fee/journal fit remain after Stage 10.

**Change control:** No changes to original economic model, theorem statements, Lean sources, original paper.tex, references.bib, branch main, Draft PR status, or author record. One inherited verification script's symbolic assertion was corrected **as stated above** without changing the verified economic result, and the source-hash manifest follows that single correction. Current report and runner are production/checkpoint artifacts.

**Final status: STAGE 9 GO — frozen source verified and six mathematical/sensitivity regressions reproducible; Stage 10 and actual submission remain OPEN.**