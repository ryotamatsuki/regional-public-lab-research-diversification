# Stage 11 — Independent Hostile Manuscript Preflight
**Date:** 2026-10-24
**Scope:** Regional public agricultural breeding / old-new competitive variety replacement, research branch \`research/2026-10-24-ijio-response-audit\`, Draft PR #2.
**Verdict:** **NO-GO FOR UNCONDITIONAL STAGE-11 CERTIFICATION / RETURN TO GATES AND STAGE 10.** This is **not** a proof of scientific falsity or a termination of the research branch. The canonical Stage 11 entry prerequisites are not presently met because Stage 7.5A and Stage 8 have been labelled conditional, source-level novelty is unresolved and author substantive verification is pending. At the author's request, the mathematical/editorial red-team below was conducted early as a provisional Stage 11 preflight. It must not be recorded as a pipeline Stage 11 GO.

## 1. Source snapshot and validation provenance

- Manuscript: \`../20_stage9_10_manuscript/paper.tex\` with separately verified reference metadata; 9-page built PDF at commit \`c71443f91506e592047058bc223998b6fe0430ff\`, Actions run \`40086502295\` PDF and bibliography build PASS, no unresolved final references/citations. Paper continues to be edited in separate commits; successful builds must always be interpreted against their SHA.
- Frozen theory: \`../19_stage8_theory_freeze/REPORT.md\` (CONDITIONAL FREEZE, not an unconditional Stage 8 GO).
- Formal proof: \`../18_lean_formal_proofs/lean\`; successful kernel/mathlib build \`40080770116\`, 107 declarations axiom-audited, only standard permitted axioms; \`Core, Prop3Global, ExactExamples, Boundary, PrimitivesBridge, Uniqueness, Prop2N\`.
- Stage 4A/7.5A: \`../17_stage4A_75A_certification/\`; independent mathematical exact checks and preregistered portability attacks. Archived GATE_SUMMARY remains CONDITIONAL/BLOCKED as of writing; the later Lean run closes its old toolchain issue for *encoded* statements but does not silently supply author signoff or prove every unencoded proposition.
- Newly constructed arithmetic audit: \`check_core_independent.py\`, rebuilt from four-good quasilinear consumer utility, direct prices, producer receipts, consumer surplus and both governments' objectives, with symbolic checks. The author is not represented as having run these calculations.
- Literature novelty frontier: \`../16_canonical_stage6_novelty_rekill/REPORT.md\`; **CONDITIONAL GO** with one substantive source theorem absorption/editorial-distinctiveness blocker. Existing author record at checkpoint 17 still PENDING.

## 2. Hostile reconstruction: mathematically tested claims

### 2.1 Primitive-to-price-to-follower bridge — PASS
From V(q;x)=α(x)·q−q'Bq/2, q=(1−a1,a1,1−a2,a2), prices p=α−Bq and K(a)=k0a+κa²/2, independent symbolic differentiation gives exactly p_Ni−p_Oi−K'(a_i)=z+x_i−da_i−ea_j with h=1−t,j=b−c,e=b+n−2c,d=κ+2h,z=Δ+h+j−k0. Farmers' constrained KKT has the same gradients as national planner in a for fixed research. The original lemma's strict global convexity/concavity premises are needed and must remain attached to it.

### 2.2 Marginal regional/national wedge — PASS, bounded
Compute G_i=Π_i+CS/2−Rx_i²/2 and W=ΣΠ_i+CS−RΣx_i²/2 from full market primitives. Differentiate through follower \partial a/\partial x_i = H^{-1}e_i, H=[[d,e],[e,d]], evaluate a1=a2=a, x1=x2=x, and substitute the follower FOC x=Ma−z. SymPy simplifies G_i,x_i−W_x_i−[(2h−e)/(2L)]·[(h−j)/(2h−e)−a] to ZERO. This certifies the two-region linear **interior** algebra, not unrestricted nonlinear demand or global equilibrium ranking. The published P1 claim now explicitly conditions the reversal on a* being feasible, and the manuscript identifies the interior FOC used in its producer-income shortcut.

### 2.3 Theorem P3+ whole-market proof — PASS within exact analytic slice
For t=1/2, b=c=n=1/5, κ=k0=1, R=2, Δ=1/2+z, independent primitive reconstruction gives the **off-equilibrium** regional payoff difference
  F_i(x_i,a_i)=(z+x_i+1/4)a_i−5a_i²/4−x_i².
In particular at full adoption a_i=1 the correct expression is F_i=z+x_i−1−x_i². It is NOT the interior-reduced expression extended to the endpoint. This was corrected before the freeze and is already in the paper.
The demand-matrix eigenvalues are {19/10,11/10,1/2,1/2}: strictly positive. The follower response is clamp((z+x_i)/2,0,1). The interior branch gain difference equals 13/16 (x−(1+3z)/13)²; global BR proof must compare the zero, interior, and saturated branches. The zero-adoption BR is inferior for z>zc, the saturated branch is decreasing for x>=2−z, and the unique global effort is xD=(1+3z)/13. The national welfare identity
  W−W0 = z(a1+a2)−(3/4)(a1²+a2²)−(x1−a1/2)²−(x2−a2/2)²
proves unique national global zero effort/adoption for z<=0, including asymmetric and noncompetitive off-path allocations. At the decentralized Nash, WD−W0=(10z−1)(22z+3)/338<0, zc=(-4+sqrt13)/12<z<=0. At z=zc there are exactly two independent regional global best responses, hence four ordered pure Nash profiles. No mathematical counterexample found within the stated domain.

### 2.4 Strict coupling not proved as open-set theorem — LIMIT
The exact P3+ interval has e=j=0 and **zero** cross-regional first-stage effort effect; it is not analytically a strategic-substitutes R&D game. The separate e=1/100 rational candidate gives strictly negative local research cross-partial -50/39999, positive symmetric equilibrium and negative national welfare; full global BR is supported by archived exact nine-active-set Python enumerations, not a full Lean first-order proof and not uniqueness of all asymmetric equilibria. Original e=3/10 benchmark similarly relies on the archived exact nine-regime verification. Both distinctions are now explicit in manuscript.

### 2.5 Sign reversal sanity check — PASS conditional
Two archived globally verified interior scenarios share a negative local strategic cross-partial -15/391 while the R&D gap switches sign: Δ=4/5 has xD=101/647 > xP=1/8, whereas Δ=17/10 has xD=445/1294 < xP=3/8. Therefore the sign of investment distortion is not merely a consequence of relabeling strategic substitutes vs complements. This is an illustrative domain-specific result, not a general theoretical independence proof.

### 2.6 Nonlinear P2 utility class — MAJOR BUT FIXABLE exposition risk
Original Stage 10 text lacked an explicit primitive nonlinear utility and the fixed-quantity/common-curvature restrictions. Stage 10 was repaired: \`paper.tex\` now states V=Σα_is q_is−Σφ(q_is)−(β/2)Q²−(r/2)ΣQ_i²−(g/2)(Q_O²+Q_N²), each Q_i=1, and equal old/new φ; writes Lφ=K''+φ''(1−a)+φ''(a) and the Jacobian Lφ I+2g11'; identifies own-minus-average response and exact curvature formula. \`Prop2N.lean\` proves algebra **conditional** on this Jacobian, not generic nonlinear welfare incidence from primitive V. A specialist can follow the short economic sketch, but to claim Stage 10 full reviewer-verifiability GO the Appendix should provide line-by-line price/producer-CS derivation for N, and optionally a small symbolic or finite-difference regression of its primitive-to-Jacobian bridge. The asymmetric curvature counterexample (-1/16 at a=1/2) must remain visible to prevent an inflated half-share universality claim.

## 3. Prior theorem absorption: principal unresolved threat

The most dangerous independent-editor objection is NOT mathematical error but that an exact crop-breeding system delivers a known demand-investment/advertising/rent-shifting externality. The relevant published predecessors, verified to the cited access depth, include:
- Dixit and Norman (1978), \`Advertising and Welfare\`, Bell J Econ 9:1–17: privately attractive advertising need not be nationally desirable, a known family of welfare failures.
- Alston, Freebairn and James (2001), \`Beggar-Thy-Neighbor Advertising\`, AJAE 83:888–902: noncooperative promotion, cross-product producer-rent displacement, overpromotion relative to coordination.
- Kinnucan and Miao (2000), AJAE 82:672–678: distribution across related commodity markets (publisher first page/metadata only, not a verified full-text theorem).
- Balagtas and Kim (2007), AJAE 89:932–946: multi-market promotion with **competitive reallocation** of common agricultural supply.
- Lence, Marette, Hayes and Foster (2007), AJAE 89:947–963: geographic new/old differentiated agricultural markets and supply/cultivar choices.
- Cardon and Pope (2003), JARE 28:185–200: a welfare-optimal zero level of an advertising instrument appears in a different market structure.
- Zhang (2022), Manchester School 90:59–76: negative expected value of an innovation is a known possibility under an R&D race/patent model.

Application-label stripping reveals a broader model of two territorial authorities selecting costly demand/quality shifters while decentralized competitive followers reallocate a fixed resource between product variants. The generic bad-investment sign, land reallocation, competitive efficiency of adoption, and marginal consumer-price incidence are known phenomena. What remains potentially distinctive is the exact **publicly financed research / endogenous private replacement / two-region local CS share / national welfare** whole game together with global boundary proof and no entry fee or patent/licensing rent. The previously studied source propositions have not yet been shown to directly subsume this whole game, but **failure to find one identical formula is not novelty certification**. Existing Stage 6 CONDITIONAL status must remain. An editor may rationally judge this a short, application-specific instance of generic advertising externalities rather than a field-journal-worthy new theorem. This is an unresolved MAJOR blocker, not proof of an existing exact isomorphism.

## 4. Mandatory attack inventory and dispositions

| Attack | Finding | Classification |
|---|---|---|
| Known-model-in-disguise / theorem absorption | Generic outcome and all component mechanisms have parents; whole-game nonabsorption unsettled | **MAJOR BUT FIXABLE** through source-level audit or narrowed positioning; cannot rubber-stamp novelty |
| Ad hoc assumptions | National CS divided equally; no explicit intergovernmental fiscal equalization; original e=0 special slice | **MAJOR BUT FIXABLE** via transparent institutional interpretation, already partly disclosed; no claim of empirical universality |
| Unilateral/global Nash vs stationary FOC | Exact 3-branch P3+ verified; e>0 nine-regime separately audited with narrower Lean claims | PASS for exact stated scopes |
| Boundary and equilibrium multiplicity | Lower z endpoint excluded; 4 Nash profiles at zc explicitly disclosed | PASS |
| Planner definition, accounting and envelope | National W=ΣG, fixed x conditional growers optimal; nationwide joint x,a objective | PASS for baseline |
| Demand/nonlinear portability | P2 common φ required, asymmetric curvature is an explicit negative result | CONDITIONAL / proof appendix needed |
| Mathematical notation and proof mapping | P1 intermediate price/Π/CS bridge added; P3 off-path branch correct | PASS bounded; nonlinear full primitive proof requires expansion |
| Arbitrary numeric threshold/welfare scale | All welfare magnitudes theoretical; no calibration or Ehime-specific magnitude asserted | PASS |
| Editorial question-completeness | WHY/WHEN/CAN answered in restricted baseline; implementation and true empirical relevance unsolved but properly excluded from diagnostic pure theory | MAJOR publication-risk, not automatically a logical flaw |
| Reviewer arrival and streamlining | Approx. 9-page theory-first PDF, central P3 proof present, but Appendices are effectively skeletal | **MAJOR BUT FIXABLE** if positioning as full-length established-field theory article; length itself is not a formal gate |
| Formal theorem vs paper claim | 107 Lean declarations with standard allowed axioms, but not full e>0 9-branch Nash or all nonlinear economic derivations | PASS for stated bounded coverage, no whole-paper claim |
| AI/source and author accountability | Actual substantive author contribution/signoff not recorded; provenance must remain truthful | **BLOCKING GOVERNANCE** |
| Institutional/empirical interpretation | Real breeding biology, uncertain discovery, regulation, adoption inertia, dynamic diffusion outside model | Scope limitations; no unsupported policy recommendation |

No currently demonstrated fatal mathematical contradiction to the frozen P3+ claim. This is not the same as an unconditional publication-quality audit PASS.

## 5. Stage 11 routing and narrowly scoped fixes

1. **Stage 6 source-comparison reopening only**, not blind model expansion: confront the exact whole-game with the strongest published predecessor theorems (especially AFJ 2001, Balagtas--Kim 2007, Lence et al. 2007, Cardon--Pope 2003), documenting full-text access limits, exact formal mappings and what economic conclusion, if any, requires the two-stage public-breeding structure. If the mechanism is absorbed, downgrade to application/short note or stop; do not inflate generality to rescue a preferred journal.
2. **Stage 10 exposition revision**: include detailed nonlinear P2 primitive-to-wedge appendix and full proof bridge, elevate the essential P3+ global three-regime proof to a complete reader-reconstructible appendix or keep the full current main proof and add transparent proof/certificate route. Make bibliographic source comparisons substantive, not merely cite generic overlap. Rebuild PDF and run full bibliography/ref QA.
3. **Governance gate**: obtain the author's authentic review of objective and theorem scopes, AI-assisted contributions and final core proofs; never fabricate approval. Reissue Stage 7.5A formal/claim-scope gate and canonical Stage 8 state only after necessary evidence.
4. **Repeat actual Stage 11 hostile reconstruction only after Stage 10 GO prerequisites**. Stage 12 journal selection must not begin as if this hostile preflight was a GO.

**Final pipeline disposition:** \`NO-GO FOR CERTIFIED ADVANCEMENT; REVISION WITHOUT THEORY CHANGE PREFERRED\`. This does not withdraw the proved mathematical results or rewrite the frozen theory. It records that a paper technically compiling with a green Lean core still has unresolved literature, reviewer exposition and author-accountability requirements. No change to main, no PR merge, no unauthorized research extension.
