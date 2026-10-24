# Canonical Stage 7 — Welfare, Generality and Institutional Validation (reconciled post-Stage-6 closure)

**Date:** 2026-10-25 JST.
**Branch:** research/2026-10-24-ijio-response-audit; Draft PR #2.
**Authoritative input:** checkpoints/2026-10-24/25_stage6_final_absorption_closure/REPORT.md.
**Other carried evidence:** 07_integrated_propositions/THEOREMS_AND_PROOFS.md; 08_mission_finance_robustness/REPORT.md; 13_editorial_completeness_decision/REPORT.md; 17_stage4A_75A_certification/CONTRIBUTION_ROBUSTNESS_CERTIFICATE.md; 18_lean_formal_proofs; 19_stage8_theory_freeze/REPORT.md; 20_stage9_10_manuscript/paper.tex, EXPOSITION_ARCHITECTURE.md, REVIEWER_VERIFIABILITY_MAP.md; 22_stage6_10_refinement/REPORT.md; 23_stage11_reaudit/REPORT.md; 24_stage11_to_stage12_handoff/REPORT.md.
**Current research question:** Given fixed public quality efforts, competitive growers optimally split limited land across old and new varieties. Do territorial public breeding labs that choose these efforts separately yield too much or too little research relative to nationwide welfare, and can an exact globally inefficient positive-effort equilibrium occur?

## 1. Canonical stage verdict and routing

**STAGE 7: GO — WELFARE / GENERALITY / INSTITUTIONAL VALIDATION PASS, within the existing modest agriculture-specific DIAGNOSTIC applied-theory scope.** This is NOT certification of a novel general economic theorem, a policy instrument, empirical external validity, or a full-length journal article's editorial sufficiency. Proceed to **canonical Stage 7.5** for the independent full-paper-versus-compact-note economic-completeness decision. Stage 7.5 must explicitly revisit checkpoint 13's prior adverse full-article editorial assessment in light of checkpoint 25's bounded Stage 6 clearance; mathematical verification does not overrule that older objection.

This checkpoint reuses earlier independently certified calculations; **no new solver run, Lean build, outside human referee, or manuscript PDF build was performed by Stage 7 itself**. This Stage 7 decision is an economics/institutional integration and falsification-scope audit, NOT a fresh claim of formal proof. Original economics, model, benchmark, theorem order and strength unchanged; no code/LaTeX edits authorized. The user's next-stage request does not constitute author substantive intellectual proof signoff. That remains pending for Stage 7.5A/8/11.

## 2. National welfare, firm/adopter incentives and regional objectives from unchanged primitives

Two regions, quantities in region i (1-a_i, a_i) with a_i∈[0,1], additive quality improvement x_i ≥ 0 to new cultivar, competitive prices p=∇_q V(q;x), grower conversion costs K_i(a_i), real research costs C_i(x_i).

\[
\Pi_i=p_{iO}(1-a_i)+p_{iN}a_i-K_i(a_i),\quad CS=V(q;x)-p^\top q
\]
\[
G_i=\Pi_i+\frac12 CS-C_i(x_i),\quad W=\sum_i G_i
=V(q;x)-\sum_i K_i(a_i)-\sum_i C_i(x_i).
\]

**No price-transfer double counting:** producer sale receipts cancel out of sum producer receipts plus CS. Region-specific revenues may change, but nationwide total welfare accounts for real consumer valuation, conversion resources and real research costs. Quasilinear utility means there is no missing income effect inside *this particular* welfare definition, not that cash transfers are politically irrelevant.

**Competitive adoption:** for fixed x, decentralized farmer planting FOC/KKT is p_iN-p_iO-K_i'(a_i)=0 if interior, with correct inequality at a_i=0,1. Since W_a_i=p_iN-p_iO-K_i'(a_i), strict concavity on feasible a ensures conditional national efficiency for the same x including corners. This is standard welfare/KKT, NOT novelty or ex ante optimum.

**Research-stage divergence:** national reduced-form envelope W_x_i=a_i-Rx_i; local objective does not internalize the same induced producer-price and nationally shared CS reallocations. Because W=G_1+G_2, local minus national marginal research payoff equals minus the opposing region's induced marginal payoff, a generic incidence identity. In the existing linear symmetric interior economy:
\[
G_{i,x_i}-W_{x_i}=\xi(a_\star-a),\qquad
\xi=(2h-e)/(2L)>0,\quad a_\star=(h-j)/(2h-e).
\]
Thus excess/shortfall has a conditional composition threshold when a_star ∈(0,1). Do NOT say every equilibrium sign follows from this first-order condition: actual stage-1 Nash/planner comparison requires both feasible global solutions, strict curvature and an interior planner on the *same* branch.

**Model-specific, not general:** the restricted old/new equal-curvature nonquadratic demand class has wedge proportional to Hphi(1-a)-Hphi(a), Hphi(q)=q phi''(q). The half-share neutrality in that class is destroyed under asymmetric old/new demand curvature (T2 yields -1/16). Therefore 1/2 is no universal adoption policy target.

**Global strict loss:** exact P3+ analytic slice t=1/2, b=c=n=1/5, k0=kappa=1, R=2, Delta=1/2+z, e=j=0, zc=(-4+sqrt(13))/12 < z ≤0. The unique global local research BR xD=(1+3z)/13>0 induces aD=(1+16z)/26>0 and unique national global planner xP=aP=0; welfare loss:
\[
W_D-W_0=(10z-1)(22z+3)/338<0.
\]
All 3 follower regimes were proven for unilateral global best responses. Crucially P3+ nationwide planner proof holds in the **unreduced joint strategy space**, all feasible x_i≥0, a_i∈[0,1], not merely one equilibrium path:
\[
W-W_0=z\sum_i a_i+\sum_i x_i a_i-\sum_i a_i^2-\sum_i x_i^2
\le z\sum_i a_i-\tfrac34\sum_i a_i^2\le 0,
\]
since x_i a_i ≤ x_i²+a_i²/4. Equality only at x=a=0. Thus negative national welfare is not solely cancelling accounting transfers: nonzero real R&D and cultivation costs can dominate the real utility improvement in this example. This is an existence result without measured real-world frequency or magnitude.

**Mutual-restraint nuance:** In P3+ at z=0, holding the other lab fixed, an individual gains +1/208 by its unilateral positive optimal effort relative to choosing x_i=0. But each locality is -3/676 worse off at the mutual positive-effort Nash than at mutual zero effort; their opposition to unilateral retrenchment coexists with Pareto-improving joint restraint. This is familiar public-choice coordination logic, not a novel generic prisoner's-dilemma theorem. At z=zc exactly FOUR pure research equilibria; uniqueness requires z>zc. The analytic P3+ slice e=0 has **no cross-effort best-response dependence**. A distinct e=1/100 exact Nash example (9 active-set arithmetic outside Lean) supports genuine strategic coupling but does not give uniqueness of all asymmetric equilibria.

## 3. Institutional empirical anchor, and exact defense/failure of primitives

**Public R&D organizations are genuine, regionally decentralized:** OECD, *Innovation, Agricultural Productivity and Sustainability in Japan* (2019), section on prefectural agricultural research organisations:
https://www.oecd.org/en/publications/innovation-agricultural-productivity-and-sustainability-in-japan_92b8dff7-en/full-report/component-9.html
It explicitly states that Japanese prefectures maintain research centers oriented to local conditions and develop regional cereal varieties (rice, wheat, soybean), complementing national labs that develop enabling breeding techniques/genetic resources. This supports geographic public lab identity, not equal-CS weighting.

**Actual public variety research and downstream uptake:** MAFF/AFFRC, varietal breeding policy and national strategy (current site as accessed 2026-10-25):
https://www.affrc.maff.go.jp/docs/hinsyu/hinsyu_kaihatu.html
and MAFF producer/stakeholder introduction support for newly bred varieties and technologies:
https://www.maff.go.jp/j/seisan/gizyutu/hukyu/h_zirei/brand/brand.html
These are distinct research/diffusion processes, compatible with a stylized quality-then-adoption timing, but do not demonstrate that public authorities optimize the paper's exact payoffs.

**Concrete provincial applied relevance:** Ehime Prefecture fruit research center (official):
https://www.pref.ehime.jp/soshiki/94/
and orange production practice/new locally bred varieties (official):
https://www.pref.ehime.jp/page/1361.html
Indicate named cultivars e.g. Ehime-kashi 28 and 48 and trials to improve local grower income and adoption. This supports discussion as one representative institutional application, NOT calibration, a two-region empirical game, or evidence that current xD is excessive.

**Crucial disanalogies / tests that did NOT pass as empirical realism:**
1. Local government behavioral objective G_i=local producer income+CS/2-own C is a **transparent stylized fiscal/welfare rule**, NOT directly confirmed Japanese prefectural decision criterion. The CS half share, consumer residence, taxation, tax-displacement incidence and local employment are not empirically measured. If policy weights change, thresholds move or vanish. Project checkpoint 08 showed this algebraically, with finite exact KKT audits, and it is retained outside main 3 claims.
2. Assumed direct quality increment from public expenditure is deterministic continuous f(x)=x; actual variety R&D is uncertain, takes time, and may affect yields, disease resistance, adaptation, resource needs and genetic spillovers as well as perceived quality.
3. Fixed one-unit land and instantaneous smooth old/new substitution are useful for tractability but cannot represent irreversible long-lived orchard replanting, annual acreage fluctuations, input land opportunity costs or heterogeneous farms automatically.
4. Private price taking is plausible as a stylized price-mediated sector and useful to locate incentive distortions, but actual territorial branding, producer groups, exclusive rights and local product differentiation can confer bargaining/market power.
5. Seed protection/licensing can alter private adoption and finance: official MAFF plant variety rights FAQs https://www.maff.go.jp/j/kanbo/tizai/brand/syubyo_top/faq.html and model license templates https://www.maff.go.jp/j/shokusan/syubyouhou/hinagata.html. The frozen model is a special no-royalty/no-private-IP-rent benchmark; checkpoint 08 explicitly modeled an exogenous per-adoption royalty as an alternative and found resulting wedges altered. NO CLAIM that all real new cultivars are freely usable or identical to x.
6. The exact P3+ analytic family has e=j=0, so substantive first-stage strategic *substitutability* is shown only by a separate coupled instance, not the theorem interval.
7. All model comparative statics require demand cross-derivatives and real financing costs that the paper does not estimate. No actual region, crop, price or public spending result can be inferred directly.

**Institutional verdict:** Baseline **credible as a transparent stylized diagnostic**, not a realistic structural quantitative model of any actual prefectural scheme. The bounded agricultural purpose survives with those limitations explicit. No empirical foundation was invented for CS/2 or for any parameter values.

## 4. Welfare policy claim ladder (diagnosis / national SHOULD / implementable COULD)

**DIAGNOSIS — PASS:** On specified regular interior states, observed equilibrium adoption aD and estimable demand substitution can, *conditionally on validity of the model*, indicate whether the nationwide marginal research welfare gradient is positive or negative at the decentralized equilibrium:
  G_i,x=0 implies W_x_i=-xi(a_star-a_D).
This is a *local gradient* at the decentralized equilibrium, **not** a global prescription or empirical treatment effect. Archived checkpoint 13 derives the formula, but it is generic restatement of the benchmark's welfare wedge, not a fourth novelty theorem.

**NORMATIVE — PASS as within-model:** The national planner accounts for all consumers/producers and chooses research x to maximize the same W; strict P3+ globally prefers xP=aP=0 within the exact parameter family. Cannot infer actual research funding should go to zero.

**IMPLEMENTATION — NOT MODELED:** No legal/procedural mechanism enforces joint abstention, central funding, Pigouvian transfers, budget-neutral matching grants, contracts, public lab merger or intellectual-property bargaining. A reduced-form planner allocation is **not an implementable coordination rule**. Fiscal incidence, information about price slopes, credible commitments and rights must be modeled separately before an applied reform recommendation. That extension is NOT ESSENTIAL for a deliberately **diagnostic** pure-theory research question and is NOT silently added here.

## 5. Portability/generality classification from original preregistered attacks

See 17_stage4A_75A_certification/CONTRIBUTION_ROBUSTNESS_CERTIFICATE.md. Reuse actual independent model re-solutions; this Stage performs no post-hoc specification tuning:
- **L1**: portable across strictly concave gross-utility and convex cost constrained competitive allocation at each fixed research vector.
- **P1**: conditionally portable local incidence; in preregistered T3 a quartic K preserves signed local wedge +7/151 at an exactly constructed interior state, not every global equilibrium ranking.
- **P2**: conditionally portable strictly within equal-old/new separable-curvature demand family. In preregistered T2 unequal curvature, midpoint neutrality FAILS, wedge -1/16.
- **P3+ analytic unique equilibrium / welfare signs**: exact MODEL-SPECIFIC parameter interval; in T1 quartic R&D C=x²+x⁴, the qualitative strictly positive local Nash / global national zero phenomenon survives at one re-solved benchmark; separate nonzero e positive strategic coupling example exists. This is *not* a general theorem in nonquadratic costs or arbitrary e.

Original archival checkpoint 08 further shows changing public objective weighting, effective financing share or per-adoption royalty can shift/eliminate the adoption threshold. These are genuine economic boundary failures and should be summarized rather than buried.

**Final generality verdict:** The *economic question* generalizes conceptually to territorial public applied-quality R&D with downstream capacity reallocation, but current mathematical theorem does NOT automatically extend to oligopoly/Cournot/Bertrand production or arbitrary public grant competition. Agriculture is the valid primary application. Do not do a superficial broad-IO retitling at Stage 7.

## 6. Kill tests, adversarial alternative and editorial relevance

1. **Is welfare loss merely redistribution?** NO. W=V-sum real K-sum real C and P3+ full-space inequality certifies strictly negative W change.
2. **Is the conditional adoption efficiency and research divergence just algebra?** Generic envelope is indeed old; P1 is a particular incidence sign characterization, not new generic welfare economics.
3. **Are quality investment and fixed land public labs just agricultural labels on known advertising models?** Major general-model threat closed as application-specific only by Stage 6/Checkpoint 25. Do not assert original general theorem. Public labs' local CS weighting, crop switching and full national objective change the evaluated institution, not mathematically new incidence calculus.
4. **Can the half-adoption threshold be used as a universal rule?** NO. Depends on product substitutability symmetry, identical curvature and particular local finance weighting; fails T2 and altered mission/royalty cases.
5. **Does the exact P3+ support genuinely interactive research competition generally?** NO. It is analytically independent BR across regions (e=j=0); merely separate existence with nonzero e established.
6. **Can a 10-page full article make a strong contribution?** Not determined by Stage 7. Original checkpoint 13 judged three-proposition broad full-length *general theory* article NO-GO and modest compact agricultural note plausible. Stage 6 now permits limited application-specific route; canonical Stage 7.5 independently decides whether that supports current article length/format after exact standalone/editor-value checklist. Do NOT bypass this skepticism on a good mathematical welfare certificate.
7. **New policy instrument required?** NO for diagnostic theory, YES if manuscript promises implementable grant advice; current Discussion disclaims implementation. All relevant material omissions classified explicitly below.

## 7. Contribution completeness and bounded alternative

- Why can growers adopt efficiently yet public breeders overspend? **ANSWERED** by conditional social KKT and regional-national externality, within exact assumptions.
- When does decentralized funding overshoot/undershoot? **ANSWERED ONLY FOR RESTRICTED symmetric interior linear and P2 restricted demand**; corners not implied.
- Is strictly welfare-harmful positive noncooperative research possible? **ANSWERED BY GLOBAL EXACT P3+ INTERVAL** and separately tested interacting candidate, with no general quantifier.
- Institutional CS weighting/actual tax burden? **BOUNDED LIMITATION** made explicit; not defensible to state empirical fiscal optimality.
- Real spending size, farmer/consumer effects and price slope estimates? **BOUNDED LIMITATION** of diagnostic non-calibrated theory, potentially serious journal editor concern.
- Economic mechanism and theorem novelty vs parent literature? **CLOSED FOR MODEST APPLICATION/INTERPRETATION CLAIM** by Stage 6. Stronger general new theorem claim would reopen Stage 6.
- Executable transfers, fiscal agreements, legal IP arrangements? **FUTURE PAPER**. If stronger policy claims, classification becomes ESSENTIAL and require rollback.
- Long-lived crop conversion/dynamic varietal cohorts, uncertainty, R&D spillovers, private breeding, general manufacturing/Cournot adaptation? **FUTURE PAPER**.
- AI provenance and genuine author proof and normative/scope verification? **SEPARATE NEXT-STAGE GOVERNANCE HARD GATE**, not manufactured by this Stage.

**Compare three presentation/research routes without changing the underlying economics:**
- A: Broad general-economics/RIO interpretation, full generic R&D policy theorem: **REJECT**, not proven, strong prior-art absorption.
- B: Existing agricultural diagnostic theory framed as a concise stand-alone field paper or Research Insight-style note: **PREFERRED** for Stage 7.5 editorial test. Retains full proofs/appendix and P3+, but does not multiply claim count.
- C: Add endogenous balanced-budget central grant/coordination mechanism: economically interesting but generic Pigouvian absorption risk; **UNAUTHORIZED FUTURE QUESTION**, requires Stage 3/4/4A/6 replay if selected; not necessary to diagnose welfare wedge.

## 8. Result-to-exposition architecture for manuscript Stage 10 (one essential story)

| Content | Suggested vehicle | Placement | Why |
| --- | --- | --- | --- |
| Regional public R&D → competitive varietal replacement timing, exact public objective W | one short model paragraph/equations; schematic optional | Model section | Reader sees institution, fixed land, CS/2 assumption |
| Conditional grower adoption efficiency | short Lemma with KKT proof | model/follower subsection | Shows distortion is upstream public R&D; familiar, not headline novelty |
| P1 signed region-national wedge and a_star | ONE main proposition, brief cross-equilibrium qualification | main results | Main tractable diagnostic result |
| Observed decentralized adoption policy gradient | concise corollary or 2-line discussion, **not separate novelty theorem** | immediately after P1 | Economically legible diagnostic without policy overclaim |
| Corollary xD-xP and aD-aP | combined 2-line algebra within main | main/appendix | Supports interpretation but dependent on P1 |
| Restricted nonlinear P2 | short secondary proposition or compact boxed equation | main/robustness; full proof appendix | Demand-shape scope is important but not separate generic contribution |
| P3+ exact global existence/welfare proof | one main proposition with compact key branch inequality and global welfare inequality; detailed branch partition appendix | main results/appendix | Strongest payoff-globality and distinctive institution case |
| Quartic C, unequal curvature, quartic K tests | short paragraph; details in existing supplementary certificates | robustness | Honest positive/negative portability without result inflation |
| e=0.01 coupled exact Nash | concise one paragraph/table note, with Python-non-Lean scope | robustness or appendix | Addresses sterile e=0 BR critique but does not prove uniqueness |
| National planner vs actual mechanism | one explicit sentence, no policy advocacy | discussion | Stop recommendation inflation |
| 2026 source evidence (OECD, MAFF, prefectural centers) | modest citations in motivation, no new factual estimates | introduction/discussion | Strengthens application relevance without claiming a model calibration |
| All numeric exact calculations, Lean proof-assistant boundaries, full primitive P2 algebra | lean proof crosswalk and appendices | Appendix/supplement | Keeps reviewer bridge while reducing reader cost |

No figures are *needed*. Optional one simple investment/adoption timing diagram can reduce effort; do not commission decorative charts or actual welfare plots unsupported by calibration. Reader arrival targets from checkpoint 20 remain appropriate. Article length/venue is a **Stage 7.5 & later Stage 12** matter.

## 9. Provenance, evidence, stop rules and next contract

This integration included **new primary institutional web evidence** found on 2026-10-25; results cited above. No new mathematical claims or cost/benefit magnitudes generated. Original proofs and Stage 4A/Stage 7.5A exact enumerations were read from preserved GitHub sources, not rerun and not newly described as independent Stage-7 verification. The relevant GitHub Actions green Lean build and original mathematical scope remain documented at checkpoint 19; green Lean cannot validate journal value or unencoded primitives.

**Stage 7 GO** on the exactly delimited application-institutional welfare/diagnostic theory and result architecture. Stage 7.5 now must confront the serious compact-note versus full-article objection from checkpoint 13, evaluate whether the surviving *one economic insight* is full-paper worthy on source-grounded economics, close or condition any ESSENTIAL completeness issue, and nominate required scope/exposition changes without altering the frozen model. If it finds insufficient incremental contribution beyond generic incidence, it must issue NO-GO despite Stage 6 and Stage 7 GO.

Only after Stage 7.5 comes Stage 7.5A, and the pre-freeze author+formal requirements must still be reconciled. Do NOT say Stage 8 is unconditionally frozen, Stage 11 is passed, or Stage 12 selection is authorized. Main untouched; PR #2 remains draft.
