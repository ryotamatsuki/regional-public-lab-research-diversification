# Stage 9 / Stage 10 — Working manuscript status

Date: 2026-10-24
Canonical verdict: CONDITIONAL GO FOR DRAFT PRODUCTION; Stage 10 completion is NOT certified.

## Completed in this checkpoint
- Read workflow v2.9, including Stage 8 entry hard gate, Stage 9 and Stage 10 order.
- Confirmed latest Lean successful run 40080770116 (commit 66c22a9, 107 axiom-audited declarations).
- Preserved old, distinct public-lab direction-diversification project and root status unchanged.
- Created scoped Stage 9 provenance/reproducibility index, Stage 10 theory-first exposition architecture, reviewer proof bridge map, BibTeX, and full-length English LaTeX working draft.
- Drafted model, follower equilibrium, conditional efficiency, P1, corollary, restricted nonlinear P2, global P3+, welfare, robustness, limitations, introduction, discussion, conclusion, appendices and bibliography integration.
- Corrected P3+ saturated off-equilibrium regional gain in paper: z+x-1-x² (not interior-only formula).

## Blocking / outstanding QA
1. The canonical Stage 8 hard gate strictly requires Stage 7.5A GO and author signoff; existing Stage 8 is CONDITIONAL. This manuscript is a provisional drafting artifact, not a canonical Stage 10 GO.
2. Manuscript PDF has NOT been compiled or visually inspected in this run. Check pdflatex, BibTeX, references, math, page breaks, proof numbering, and hyperref warnings.
3. Stage 6 prior-art theorem-level nonabsorption remains conditionally accepted and not source-certified. No publication-ready originality claim.
4. Bibliographic metadata require verification, especially placeholder Zhang author given name in references.bib; no invented reference details are permitted in final.
5. Proof review required: compare every formula and primitive-to-payoff bridge against original frozen source and Lean statement; ensure generic P2 demand assumptions and proof sufficient, and exact e>0 examples not inflated into Lean global Nash proof.
6. Author intellectual contribution/signoff pending.
7. Figure/Table Gate: no charts needed in baseline; assess whether a single mechanism/timing diagram actually reduces reviewer effort. No unverified graphic is required.
8. Build reproducibility should include a LaTeX CI or explicit local PDF build with pinned dependencies, plus independent manuscript-to-theorem hostile review.

## Next authorized action
Run LaTeX build and independent full-manuscript mathematical/proof consistency audit, repair manuscript errors only (not frozen theory). Recheck Stage 7.5A and Stage 8 hard-gate prerequisites before declaring Stage 10 GO. Stage 11 adversarial manuscript audit only after Stage 10 QA.

## Stage 10 QA update (2026-10-24, after manuscript hardening)

- **LaTeX build PASS** for manuscript SHA `c71443f91506e592047058bc223998b6fe0430ff`: GitHub Actions [run 40086502295](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40086502295) compiled a 9-page PDF and passed final citation/reference checks. Companion existing PDF workflow run 40086502306 also succeeded.
- Publisher/academic records checked: Alston--Freebairn--James 2001, Balagtas--Kim 2007, Lence et al. 2007, Dixit--Norman 1978, Cardon--Pope 2003, Kinnucan--Miao 2000, Anzhou Zhang 2022. The unverified author placeholder was replaced.
- Independent four-good reconstruction reproduced farmer FOC, regional-vs-national wedge under symmetric interior adoption, global P3+ off-path local payoff including complete-adoption branch, exact welfare difference and positive-definite demand matrix eigenvalues.
- Added nonlinear P2 restricted primitive gross utility and own-minus-average adoption Jacobian, qualified reachable P1 adoption thresholds and interior-only welfare-square-completion, restored original e=3/10 rational example, and made P1 producer/CS derivation visible to reviewers.
- Initial PDF build and source consistency PASS does **not** discharge the workflow's Stage 8/7.5A author-signoff and novelty requirements. Appendix remains abbreviated, so a complete Stage 10 manuscript-quality GO is not issued. Stage 11 is being performed as an adversarial **preflight** rather than an unqualified canonical progression.

**Current status: PDF BUILD PASS; STAGE 10 CANONICAL GO NOT ESTABLISHED.**


## Follow-up completed: Stage 10 mathematical/production repairs and Stage 11 preflight inputs

- Source manuscript checkpoint: paper.tex at commit 54afd111876fb2aa45792e7f597900669b80012e, with the complete nonlinear primitive-to-wedge proof (Appendix), piecewise global P3+ branch proof (Appendix), and a rigorous distinction between a *unilateral own-effort baseline at fixed rival action* and the *mutual zero-research baseline*. Its length is 10 PDF pages as verified by GitHub Actions (manuscript PDF job 40087841120).
- The unilateral gain at xD in the P3+ family is (48z²+32z+1)/208 > 0, whereas each government's change from mutual zero research to mutual positive Nash equals (10z−1)(22z+3)/676 < 0. At z=0, these values are +1/208 and −3/676, respectively. Both come from the same primitive G_i, not different planner definitions.
- A string-substitution regression temporarily duplicated material after end-of-document; it was removed before this checkpoint. The current manuscript has exactly one document end, exactly one appendix, no duplicate LaTeX labels, and no material trailing its document terminator. CI now actively blocks recurrences.
- GitHub Actions PDF QA [40087884054](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087884054): PASS on manuscript commit and workflow guard. Both compilation and final citation/reference checks PASS.
- Independent SymPy rebuild [40087931474](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087931474): PASS, both the original four-good primitive model (including private-vs-joint payoff accounting) and a separate genuinely nonlinear N=3 six-good primitive utility with full price, adoption-Jacobian and G−W research-wedge calculation. P2 exact test returns 2/9 at a=1/4; it is a nontrivial sample check, not a universal theorem.
- Rechecked source-level contrast: Lence et al. (2006 working paper), exact pp. 5 (organizational timing), 23 (Proposition 1 fixed-development-cost threshold ranking), 27 (Proposition 3 ex-ante organization welfare), and 2007 published abstract; Alston et al. (2001) author-hosted abstract confirms producer-group cooperative comparison. This supports real institutional difference but not definitive parent-theorem nonabsorption.

**Stage 10 technical QA: PASS** for compilation, full derivation transparency, formula and scope consistency within tested modules. **Canonical pipeline progression remains blocked** by outstanding Stage 6 nonabsorption/editing significance review and original Stage 7.5A / Stage 8 author intellectual-verification signoff. Under the universal workflow, this cannot be represented as a retroactive unconditional Stage 8 GO or submission authorization.
