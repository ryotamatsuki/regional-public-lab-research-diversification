# Stage 11 — Hostile Manuscript Re-Audit, after Stage 6 / Stage 10 Repairs

Date: 2026-10-24. Repository: ryotamatsuki/regional-public-lab-research-diversification. Branch: research/2026-10-24-ijio-response-audit. PR #2 remains Draft. Main branch unchanged.

**Canonical verdict: NO-GO TO STAGE 12 AT PRESENT.** Specifically: mathematically verified source-aligned core **PASS within stated scope**, manuscript technical and reader-bridge QA **PASS**, but independent economic novelty/field-journal editorial significance is still **CONDITIONAL / UNRESOLVED**, and author signoff / earlier canonical Stage 7.5A and Stage 8 hard gate requirements remain incomplete. This is a **revision routing decision**, not a finding that the main theorem is false or the research has no value. The present re-audit is a justified Stage 11 preflight because canonical Stage 11 entry prerequisites are not yet unconditionally certified.

## 1. Inputs, immutable theory and quality checks

Canonical model and theorem domains: checkpoints/2026-10-24/19_stage8_theory_freeze/REPORT.md (CONDITIONAL THEORY FREEZE). Formal proof source: 18_lean_formal_proofs/lean, successful Lean/mathlib build, 107 declarations axiom-audited, run https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40080770116. Scope of this green build is exactly the encoded statements, not all equilibrium partitions or nonlinear economic primitives.

Manuscript: ../20_stage9_10_manuscript/paper.tex, updated with full derivation and price-incidence appendices and regional private-versus-joint research-payoff clarification. Standalone PDF built as 10 pages, run https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087841120. Enhanced source guard and final BibTeX/reference/PDF checks all PASS in https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087884054. New QA catches duplicate document ends, appendix duplication, duplicate labels and material after end-of-document.

Independent primitive check scripts under ../21_stage11_adversarial_preflight:
- check_core_independent.py reconstructs the full four-good original model, farmer KKT, symmetric interior P1 wedge, P3+ global payoff identities, exact welfare bound and threshold. Also compares local **unilateral** versus **mutual** research payoffs from the same primitive regional objective.
- check_nonlinear_primitive.py constructs a genuine nonlinear three-region/six-good gross utility, derives each inverse price, planting Jacobian and the local-national research total derivative. At a=1/4, g=1/10, phi(q)=q³/3, K(a)=a+a²/2 and the selected symmetric x=1/10, delta=1/2, the independent exact output is **2/9**, equal to the predicted P2 value. This tests the economic price-incidence bridge, beyond the conditional general-N Lean response identity.
- Both PASS in https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087931474.

No frozen economic primitives, proposition domains or game definitions have been changed.

## 2. Reconstructed mathematics and attempted falsifiers

| Issue | Hostile test / output | Status |
|---|---|---|
| Conditional farmer efficiency | Utility-price derivatives and constrained planting KKT coincide with national welfare gradient for fixed research; concavity is explicit | PASS |
| P1 sign / equilibrium ranking | Independent symmetric total-derivative wedge equals xi(a_star-a). xD/xP comparison is separately restricted to feasible globally confirmed interior solutions | PASS in domain |
| P2 demand-class scope | Original restricted phi gross utility to Jacobian to G−W proved in Appendix; independent nonlinear 3-region rational check 2/9. General-N Lean response is conditional on Jacobian | PASS bounded; no generic-demand claim |
| P3+ local global Nash | Three follower planting branches, off-equilibrium unsimplified local payoff and saturated branch tested; unique BR in z in (zc,0]; lower endpoint excluded | PASS |
| P3+ national global welfare | Complete square on arbitrary nonnegative x and feasible a, not just follower/symmetric allocation; zero unique | PASS |
| P3+ endpoint | Each region has best responses {0,sqrt(13)/52}, yielding four pure Nash profiles at z=zc; strict lower inequality correctly retained | PASS |
| P3+ original demand geometry | B eigenvalues 19/10,11/10,1/2,1/2 strictly positive | PASS |
| e>0 interacting benchmark | Exact rational symmetric candidate, planner and welfare; nontrivial 9-status global Nash from archived exact Python, not Lean; cannot claim all asymmetric Nash uniqueness | CONDITIONAL scope explicitly bounded |
| Proof assistant vs manuscript | 107 accepted declarations, no unauthorized axiom; does not prove all economic-to-Lean bridges or full nonlinear class | PASS for honest scope |

**Important genuine exposition regression discovered and repaired.** The private gain F_i(xD)>0 is the gain from own positive research rather than zero *holding rival action fixed*, not the gain in G_i when both move from no research to research. For the P3+ symmetric family:
- unilateral gain against fixed rival: (48z²+32z+1)/208 > 0;
- each region's own gain when both research relative to mutual zero: (10z−1)(22z+3)/676 < 0;
- at z=0: +1/208 versus −3/676.
Thus mutual restraint Pareto-improves both regional government objectives despite each region choosing positive effort given the rival. Payoff interdependence remains through nationally shared consumer surplus even though effort best responses are independent at e=j=0. This is a clear equilibrium/institutional interpretation, **not** a distinct new general theorem. It is now stated and checked in manuscript and independent CI.

## 3. Theorem-absorption hostile test: sources and actual access

(a) Dixit and Norman (1978), Advertising and Welfare: private demand-shifting expenditures may be socially overdone. Hence existence of wasteful costly demand enhancement is old.

(b) Alston, Freebairn and James (2001), Beggar-Thy-Neighbor Advertising: https://digitalcommons.calpoly.edu/agb_fac/10/ (author-hosted accepted-version record and abstract, 2001 AJAE 83:888–902, doi 10.1111/0002-9092.00217). The authors compare noncooperative promotion by producer groups with joint **producer profit** maximization; related-commodity displacement and gains from coordinated cuts are known. Original author PDF retrieval returned 403 during this re-audit, so no claim of exhaustive published theorem inspection. The present model adds territorial public **quality** research, national CS shares in regional objectives, price-taking farmer land conversion and a national total-surplus benchmark. This is an institutional/game-structure difference, not automatically independent mathematical novelty.

(c) Balagtas and Kim (2007), Measuring the Effects of Generic Dairy Advertising in a Multi-Market Equilibrium, AJAE 89:932–946, doi 10.1111/j.1467-8276.2007.01037.x: common-input **competitive reallocation across goods already exists**. Different research-incentive game and counterfactual here. The final published theorem scope was not exhaustively inspected in this pass.

(d) Lence, Marette, Hayes and Foster (2007), Collective Marketing Arrangements for Geographically Differentiated Agricultural Products, AJAE 89:947–963, doi 10.1111/j.1467-8276.2007.01036.x. Verified published journal abstract: https://academic.oup.com/ajae/article-abstract/89/4/947/146334. Examined original publicly accessible 2006 working paper https://www.card.iastate.edu/files/publications/pdf/06MWP9.pdf, including PDF page 6/print p.5 (producer-organization fixed-cost timing), PDF p.24/print p.23 (Prop 1 fixed-development-cost thresholds), PDF p.28/print p.27 (Prop 3 ex-ante welfare changes for differentiated-product organizations). That paper already contains atomistic agricultural producers, old/new product activity, supply allocation and planner comparisons: these components have no novelty here. Its analyzed institutional choice is producer-organization supply control and fixed new-product development, not two decentralized territorial public-quality laboratories choosing continuous research before price-taking growers, with the current exact public Nash/global national benchmark. No direct isomorphism was found in the inspected working-paper propositions, but the 2007 final publisher version was not exhaustively proved nonabsorbing.

(e) Cardon and Pope (2003), JARE 28:185–200, agricultural advertising welfare: negative or zero-welfare advertising regimes already exist under a distinct market structure. A socially optimal zero-investment headline is **not a first-in-the-literature result**.

**Classification:**
- Competitive farm conditional efficiency: ABSORBED generic welfare/KKT.
- P1 generic price-incidence operator: ABSORBED generic envelope algebra; adoption threshold is a setup-specific parameterization.
- Corollary linking adoption/research gaps: ABSORBED algebra.
- P2 nonlinear curvature: restricted setup-specific characterization, incomplete originality proof; its equal old/new curvature is essential and a prespecified asymmetry counterexample overturns unconditional half-share neutrality.
- P3+ generic excessive investment and societal zero-research welfare sign: ABSORBED qualitative phenomenon by prior advertising/rent-seeking precedents.
- P3+ complete institutional game, exact global boundary and Pareto-improving mutual restraint **under continuous public-quality choice and endogenous efficient crop conversion**: MODEL-SPECIFIC DERIVED RESULT with an economically meaningful interpretation; **global theorem nonabsorption remains UNRESOLVED**.
- e>0 coupling: exact rational additional existence demonstration; no general open-parameter theorem.

## 4. Why this setup does deliver bounded useful economic knowledge

The contribution is **not** “regional research can be excessive” but a logically complete distinction between three different objects: publicly financed quality provision, privately chosen adoption of better cultivars, and total producer-plus-consumer welfare evaluated nationally. In this two-stage game farmers' conditionally efficient response does not correct governments' preceding research externality. The marginal distortion has an observable old/new composition threshold; under equal-curvature nonlinear demand its sign or neutrality depends on quantity-weighted curvature; with a precisely specified technology there is a global locally rational yet *regionally as well as nationally Pareto-inferior* positive R&D Nash. The mutual-restraint interpretation makes the policy-relevant institutional puzzle sharper even in the transparent e=0 example. None of these proves that actual public crop breeding is inefficient, or that this is a new universal branch of game theory. The value is an independently checkable characterization of a specifically configured fiscal/agricultural institution.

The optimistic publication case is a concise applied-theory paper using existing envelopes/KKT and a sharp global counterexample to explain when decentralized public crop-quality funding should be assessed separately from successful grower adoption. The skeptical editor's case is serious: advertising/producer-organization and competitive crop-reallocation papers already cover its major ingredients, the analytic P3+ slice sets e=0, the e>0 case is an isolated exact example, and there is no policy instrument solved or empirical calibration. Neither mathematical green CI nor new notation decides this contest.

## 5. Mandatory attack register

- **Known model in disguise / absorbed economic mechanism:** MAJOR, unresolved full parent-theorem mapping; closest work now compared by agents, objective, decision rights, follow-up market and benchmark, not only abstract headlines.
- **Ad hoc institutional half-share of national CS:** MAJOR potential dependence; assumption openly recognized, tested model is not presented as empirically universal.
- **Quantifier inflation / demand generality:** controlled; P2 equal old/new curvature and symmetric interior restrictions explicit, negative T2 retained.
- **Global deviations and corners:** main exact P3+ PASS; e>0 evidence explicitly Python-not-Lean bounded.
- **Manipulated benchmark:** controlled, independent joint and unilateral G_i and W comparisons now reconstructible from source.
- **Formal theorem scope inflation:** controlled, Lean-only and full-economic-proposition mappings distinct.
- **Reviewer proof bridge:** PASS after complete P2 Appendix and P3 all-regime Appendix; substantive economic argument can be reconstructed without opening production code; CI regression keeps TeX source uncorrupted.
- **Robustness against meaningful alternatives:** T1 quartic R&D retains severe waste; T2 unequal old/new curvature overturns 1/2 neutrality; T3 quartic conversion retains P1 sign at tested point. No universal robustness claim.
- **Editorial importance/completeness:** WHY/WHEN/EXISTENCE addressed for baseline; institutional research coordination remedy, cross-region fiscal weighting and empirical magnitudes deliberately unsolved. These are publication-risk limits rather than logical inconsistencies.
- **AI provenance / author accountability:** author substantive proof, model and novelty signoff still PENDING; no AI assertion of completion.
- **Citation/page/source drift:** previously incomplete introductory parent citation improved; both published records and actual working-paper page sources identified with access limits.

No **fatal mathematical contradiction** was found in the stated frozen P1/P2/P3 scopes. This is not an unconditional claim about the entire universe of potential asymmetric nonregular equilibria or all prior published papers.

## 6. Verdict, rollback and next-stage contract

**STAGE 11: NO-GO TO UNCONDITIONAL ADVANCEMENT (REVISION).** Stage 10 technical manuscript QA and independent reconstruction now PASS, but a strict reading of pipeline v2.9 still blocks canonical Stage 11 GO because earlier Stage 7.5A/Stage 8 are conditional, authentic author review has not occurred and Stage 6 theorem-level independence/editorial significance remains unresolved. With multiple independent material blockers, reporting a Stage 11 CONDITIONAL GO (one blocker) would be inaccurate.

Precisely bounded remaining work:
1. Reopen **Stage 6** only for the strongest remaining *general parent theorem absorption* and economic editorial case, with final-source proof scopes if accessible; decide honestly whether a concise regional-public-breeding field contribution survives or should be a short note/stop. Do **not** invent a new universal proposition to force prestige.
2. Obtain authentic author intellectual contribution/proof/scope review and then apply the Stage 7.5A Formal Verification Gate and Stage 8 freeze entry requirements as written. The green Lean build can support, but not replace, actual author signoff.
3. Repeat canonical Stage 11 after all preconditions; **do not move to Stage 12 journal positioning** on this preflight result.

Maintain Draft PR #2; do not merge, rebase main or change any frozen theorem in this checkpoint.
