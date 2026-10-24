# Canonical Stage 10 — Integrated Manuscript Construction and QA

**Date:** 2026-10-25 JST
**Project:** Regional Public Breeding and Variety Replacement: Decentralized Research Incentives and National Welfare
**Theoretical authority:** Stage 8 Theory Freeze v2, \`checkpoints/2026-10-25/30_canonical_stage8_theory_freeze_v2/REPORT.md\`.
**Source inputs:** Stage 9 verified frozen-source manifest and \`checkpoints/2026-10-24/20_stage9_10_manuscript/\` provisional draft.

## Decision

**STAGE 10: GO — COMPLETE INTEGRATED ENGLISH WORKING MANUSCRIPT (THEORY-FIRST, COMPACT AGRICULTURAL APPLIED THEORY).**

This is an editorial and construction gate, **not** independent Stage 11 hostile-referee review, journal selection, submission readiness, validation of new general economic theory, or a claim the article has been externally reviewed.

**Authoritative Stage 10 production path:** \`checkpoints/2026-10-25/32_stage10_manuscript/\`. Older frozen Stage 9 original manuscripts are intentionally **unchanged** because Stage 9 pins their Git blob IDs; the revised Stage 10 file is a *new* production artifact, not the same file as the older \`20_stage9_10_manuscript/paper.tex\`.

## Revised manuscript and provenance

- \`32_stage10_manuscript/paper.tex\`: 10-page A4 journal-neutral LaTeX theory-first English article, with anonymous title page, proof-critical equations in main text and detailed appendices. Git blob SHA \`89cce290e148b3ed9311783068461d699b8383e2\`.
- \`32_stage10_manuscript/references.bib\`: existing closest agriculture/advertising research plus independently cross-checked public-university apple innovation comparator (Akhundjanov et al. 2020, *Economic Modelling* 86:88–100, DOI 10.1016/j.econmod.2019.06.004), and OECD (2019) *Innovation, Agricultural Productivity and Sustainability in Japan*, DOI 10.1787/92b8dff7-en. Git blob \`d8f633c4084a1264fa80649b5a46b702d3fe6064\`.
- \`32_stage10_manuscript/EXPOSITION_ARCHITECTURE.md\`: theory-first ordering, reader-arrival and figure/table gate; **no unnecessary illustrative tables or plots**.
- \`32_stage10_manuscript/REVIEWER_VERIFIABILITY_MAP.md\`: five result/proof bridges and exact formal versus SymPy coverage.
- \`32_stage10_manuscript/verify_manuscript.py\`: fully automated locked-object comparison to Stage 8-frozen provisional \`paper.tex\`. **Lemma/proposition/corollary statements byte-identical**, 30 displayed math environments unchanged except for a single purely notational correction \`H(1-a)-H(a)\` → \`H_\phi(1-a)-H_\phi(a)\` in the *P2 signed-curvature display*. Label and BibTeX-key checks also run.
- \`.github/workflows/public-breeding-stage10.yml\`: triggered by new Stage 10 manuscript path, performs frozen theorem/computation mapping regression, citation/label check, LaTeX/BibTeX PDF build, final unresolved-reference log check, PDF signature/size check, 30-day PDF artifact upload.

**Editorial changes actually implemented:**
1. Replaced repetitive novelty-defensive opening with a brief question, game, results, closest-parent contrast and limited claim paragraph. Public agricultural laboratories are documented with OECD official source, and university-bred cultivar commercialization is clearly acknowledged as prior research.
2. Added explicit information/timing observation sentence to the stage-1/stage-2 game without changing its known structure.
3. Added an economically useful P1 interpretation of \`G_i,x_i-W_x_i=-G_j,x_i\`, explaining why adoption composition reverses the regional externality, while refusing to treat this local derivative as an unconditional equilibrium ranking.
4. Consolidated routine references to Lean source into main/appendix proof crosswalk, keeping the crucial P1 price/producer-income/CS incidence and P3 full three-branch deviation/payoff bridges in the article itself.
5. Preserved P2 restrictions, P3 z-cutoff and endpoint multiplicity, distinct e=0 analytic family and e>0 exact coupled rational case, mutual vs unilateral payoff distinction, and non-implementation/non-empirical policy limitations.
6. A4 paper and \`hidelinks\` hyperlink rendering only: the mathematics, cost domain, Nash concept, lemma/propositions, benchmark national W and numerical claims were unchanged.

## Figure/Table Architecture Gate and specialist reconstruction

**PASS: ZERO exhibits needed.** Section 2 defines timing, players, products, national prices, G_i, W and all planting constraints; Section 3 contains P1 exact price-incidence bridge, conditional effort differences and restricted nonlinear P2; Section 4 contains P3 all three piecewise global BR regimes and real national W square-completion; Section 5 separates bounded portability and e>0 exact rational checks; appendices show primitive-to-Jacobian and full boundary proof.
These are sufficient for a competent referee to follow the paper's theorem chain without running an external solver, while the proof files allow exact computational verification. No figure/table would add distinct economic knowledge at this length.

**Reviewer-verifiability accounting:** L1 requires constrained competitive KKT. P1 is a *conditional symmetric interior* result, with effort/planner globality separately hypothesized. P2 is equal-old/new curvature only, Jacobian algebra Lean verified conditionally and economic bridge given in appendix. P3+ is an exact global e=j=0 research interval with negative W, z=zc excluded because four Nash. e>0 exact 9-active-set Nash verification is SymPy, not a complete Lean global theorem. No paper sentence may upgrade these scopes at Stage 11.

## Executed CI and PDF visual audit

**Authoritative final run:** [GitHub Actions 40117492851](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40117492851) **SUCCESS** at commit \`9602d049fa512a21e2ae2d185d4a5bc57bdf7748\`. Stage 10 static check logs confirm:
- Lemma, proposition and corollary statements unchanged vs frozen version;
- 30 displayed math blocks, **only one notation-only correction**;
- 32 distinct valid labels, five distinct cited bibliography keys resolved;
- LaTeX/BibTeX compiles, final \`paper.log\` passed the unresolved-citation/ref and LaTeX error grep test;
- PDF signature valid and nonempty;
- workflow artifact \`public-breeding-stage10-revised-manuscript-pdf\`, artifact ID \`12570555190\`, ZIP about 238KB, PDF \`243247\` bytes.

**Additional actual container inspection:** Downloaded final GitHub workflow artifact into active task container, extracted \`paper.pdf\` (11-page previous draft is NOT authoritative), checked \`pdfinfo\` for **10 pages, A4 595.3×841.9pt**, rendered *all 10* pages to PNG using the PDF skill and inspected the contact sheet. No visually obvious math overflow, failed typesetting, broken reference border or orphan one-reference last page. Prior 11-page US-letter build had an isolated one-reference page and prominent hyperlink boxes; these were corrected by A4 sizing and \`hidelinks\` without content changes. Visual review is at contact-sheet scale, not a substitute for a specialized print-proof inspection at Stage14.

**Failed/superseded attempts, explicitly retained:**
- First editorial insert accidentally triggered JS replacement interpolation on \`$'\` in math prose and triplicated the \`paper.tex\` source. CI caught multiple \`\\end{document}\`. Restored source from clean GitHub commit, and used callback-based literal replacement to recover a single ~31.7KB paper.
- Intermediate PDF QA attempt failed **after** successful LaTeX/BibTeX because \`pdfinfo\` was missing on GitHub runner host; replaced that nonportable verification with Python PDF-signature/size check. No mathematical or LaTeX failure.
- The successful first 11-page version was subsequently layout-corrected to final 10-page A4 and **recompiled**. The last successful run ID above supersedes all early failed/cancelled CI runs.

No error has been erased from historical GitHub Actions.

## Novelty, institutional, proof and source limitations

- Core economic novelty is **the complete institutional public-breeding application**: territorial public research effort with downstream efficient private old/new fixed-land replacement and a composition-sensitive territorial/national incidence; exact global welfare-harmful regionally positive public R&D family. Generic overpromotion, competitive allocation efficiency, price-incidence and optimal social zero are old mechanisms. Stage 6 absorbs the general claims and keeps the modest institutional application.
- Public lab institution and grower adoption are grounded to official OECD and peer-reviewed university apple innovation literature. Regional \`CS/2\`, certain quality benefits, no royalties, no private R&D, static planting and calibrated welfare are deliberate theoretical abstractions, not real government mandates or quantified policy findings.
- Lean covers original **proof-critical core only**. P2 economic primitive-to-Jacobian bridge is in manuscript and a separate exact instance; e>0 all nine constrained planting active-set and BR is checked in exact SymPy, not fully formally encoded. Neither a full Lean proof of the economics paper nor full absence of identical paywalled parent theorems is asserted.
- Journal-specific word count, article type, AI disclosure requirements, fees and acceptance quality are OUTSIDE Stage 10 and remain to be validated by later workflow stages; references were checked on the selected new institutional citations, not exhaustively against every proprietary archival publisher PDF.

## Handoff

**Stage 10 PASS / GO**, with no outstanding known construction or figure/table architecture blocker. Production manuscript \`32_stage10_manuscript/paper.tex\` and final 10-page PDF artifact are the appropriate source for **canonical Stage 11 independent hostile referee reconstruction**, not the older provisional \`20_stage9_10_manuscript/paper.tex\`. Stage 11 should test whether the economics is too close to advertising theory after the now concise contribution framing, isolate any proof or paper-facing inconsistency despite automated passes, and either GO or return focused authorable changes without inventing new mechanisms.

Do **not** merge Draft PR #2, alter \`main\`, or submit before Stage 11 and subsequent formal Stage 12/14. Frozen theory unchanged; Stage 9 manifests and older artifacts preserved intact.

**One-line status: Stage 10 GO; English manuscript integrated, source-math invariant and PDF successfully built; Stage 11 referee test next.**