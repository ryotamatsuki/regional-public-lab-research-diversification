# Canonical Stage 8 — Theory Freeze v2 (author-attested, proof-scope-controlled)

**Date:** 2026-10-25 JST
**Project:** Regional Public Breeding and Variety Replacement: Decentralized Research Incentives and National Welfare
**Canonical workflow:** \`research-paper-workflow/THEORY_PAPER_RESEARCH_PIPELINE.md\` v2.9, Stage 8
**Working branch:** \`research/2026-10-24-ijio-response-audit\` (Draft PR #2)
**Status:** **STAGE 8 GO — CANONICAL THEORY FREEZE, bounded agriculture-specific diagnostic applied theory**.
This freeze supersedes the CONDITIONAL *entry status* in 2026-10-24 checkpoint 19, but retains that checkpoint and its earlier findings as provenance. It does not confer Stage 9/10/11 or submission GO.

## 1. Formal entry gate and author provenance

All hard entries for canonical Stage 8 have been satisfied **in recorded, explicitly limited scopes**:

- **Stage 4A GO**: \`checkpoints/2026-10-24/17_stage4A_75A_certification/STAGE4A_MATH_CERTIFICATES.md\`. Global positive-effort Nash proof, off-path planting case split, exact national W square completion, boundary and independent utility bridge in original technical evidence.
- **Stage 6 GO** (only modest institution-specific contribution): \`25_stage6_final_absorption_closure/REPORT.md\`, generic incidence/advertising rent-shifting novelty downgraded.
- **Stage 7 GO**: \`checkpoints/2026-10-25/26_canonical_stage7_welfare_institution/REPORT.md\` — welfare is real-resource accounting; actual institutions are modeled as a transparent diagnostic rather than calibrated policy.
- **Stage 7.5 GO**: \`checkpoints/2026-10-25/27_canonical_stage7_5_economic_completeness/REPORT.md\` — ONE compact agriculture-specific applied-theory story, not a claimed novel general IO result.
- **Stage 7.5A GO**: \`checkpoints/2026-10-25/29_stage7_5A_final_gate_closure/REPORT.md\`. Quantifier/portability and source-to-proof statement checks passed in checkpoint 28; sole outstanding author gate satisfied by the author's direct attestation.
- **FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE ONLY**: actual GitHub Actions [run 40080770116](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40080770116), \`success\`, Lean 4.35.0 + mathlib 4.35.0, earlier audit reports 107 audited declarations and standard axioms only. Lean files presently have the SAME blobs as that run. This is a past successful run, not a newly executed build. Relevant economically unformalized scopes are listed below.
- **AUTHOR completion attested by user, not invented by AI**. Exact current-turn statement \`著者確認が完了で、次のステージ行って\` (2026-10-25 JST) is quoted and documented in \`17_stage4A_75A_certification/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md\`, with six-point review subject from checkpoint 28. No independent human referee report, item-by-item proof notes, or checking method was provided. Self-attested author completion is not a claim of private proof method, and does not replace mathematical evidence.

This is a **complete theory freeze for the narrow current article**, not an assertion of complete source-literature priority or unconditional empirical validity.

## 2. Frozen research question, contribution and publication route

**Question:** When can territorial public agricultural breeding labs choose excessive or insufficient quality research relative to nationwide total welfare, even if growers efficiently replace established cultivars with improved cultivars conditional on that publicly chosen quality? Does a nonempty parameter interval have strictly positive local research Nash effort while unique national optimal public research is zero?

**ONE central paper-facing contribution:** Solve the two-stage regional public quality-investment and competitive old/new fixed-land adoption model sufficiently to (i) isolate the research-stage national/regional divergence despite efficient follower allocation; (ii) derive a model-specific, composition-sensitive signed investment wedge with precisely stated scope; and (iii) construct a globally validated, strictly welfare-negative decentralized investment equilibrium without fixed research entry fees or downstream monopoly. Restricted nonlinear curvature is conditional scope/robustness, not a new general theory. The work is an **agricultural applied theory / public agricultural research financing diagnosis**. It is *not* a general new strategic R&D, industrial organization, price-incidence or rent-seeking theorem.

**Editorial route frozen:** compact single-question agricultural field Research Article (or a genuinely eligible short insight format after Stage12), retain substantive P1 and P3+ and proof-critical appendices. BAE or another credible agricultural outlet may be examined at Stage12 but is NOT selected here and cannot relax mathematical scope to fit its prestige.

## 3. Frozen game/strategy/information/technological environment

**Players/stages:** (1) two territorial publicly financed research laboratories/governments simultaneously choose quality increments \`x_i ∈ [0,∞)\` to their own NEW cultivar; simultaneous moves with public knowledge of primitives and decisions for the follower stage. (2) atomistic price-taking growers in each region choose old vs new planted-area fraction \`a_i∈[0,1]\`, so land and total regional crop output normalized to 1: \`q=(1-a1,a1,1-a2,a2)\`. Four differentiated agricultural products face ONE national consumer market. Competitive inverse prices satisfy \`p=∇_q V(q;x)\`; no Cournot/Bertrand quantity-setting downstream firms, government commitment bargains, inter-regional transfers or private breeding investments. Two-stage subgame-perfect / Nash research equilibrium with unique follower response when the specified concavity applies.

**Preferences:** national quasilinear gross utility \`V(q;x)=α(x)'q - (1/2) q'Bq\` in baseline, B symmetric positive definite. Additive new-cultivar quality \`α_iN=A+Δ+x_i\`; old \`α_iO=A\`. Quadratic conversion \`K_i(a_i)=k0 a_i+(κ/2)a_i²\` with \`κ>0\`. Real public research \`C_i(x_i)=(R/2)x_i²\`, \`R>0\`. Baseline B diagonal 1, within-regional old/new cross term t and across-regional old-old b, old-new c, new-new n, subject to positive definiteness.

**National/regional account:** \`Π_i=p_iO(1-a_i)+p_iN a_i-K_i(a_i)\`; \`CS=V-p'q\`. Local \`G_i=Π_i + CS/2 - C_i\`; nationwide \`W=G1+G2=V - ΣK_i -ΣC_i\`. **CS/2 is a modeling assumption about regional welfare shares, not evidence on Japanese fiscal rules.** Nominal market producer payments cancel from national W; national losses in P3+ are changes in real valuation and cost, not just income transfers.

**Frozen parameter/computation notation:**
\`h=1-t\`, \`j=b-c\`, \`e=b+n-2c\`, \`d=κ+2h\`, \`M=d+e\`, \`L=d-e\`, \`D=d²-e²\`, \`z=Δ+h+j-k0\`, \`J=2h-e>0\` in the admissible baseline and \`ξ=J/(2L)>0\`, \`aStar=(h-j)/J\`; B positive definite, hence required follower Hessian eigenvalues positive under the stated model restrictions. Interior competitive adoption \`H a=z*1+x\` with \`H=[[d,e],[e,d]]\`, and at symmetric interior \`a=(z+x)/M\`. At adoption boundaries solve constrained KKT, **never substitute the interior formula globally**.

**Exact solution restrictions:** symmetric planner \`xP=z/(RM-1)\` and \`aP=R*xP\`, and symmetric regional candidate \`xD=[(1-ξ)z+ξ M aStar]/(RM-1+ξ)\`, \`aD=(z+xD)/M\`, are **INTERIOR CANDIDATES**. They are actual equilibrium/optimum comparisons only with all positivity, feasibility, strictly convex/concave national restrictions (e.g. \`R>1/min(L,M)\` where used), and complete global unilateral-deviation certification. These equations do not establish all-parameter existence or uniqueness of regional equilibrium.

**P2 separate restricted demand family:** N≥2 identical regional growers with unit land, \`V=Σ α_is(x_i) q_is - Σ φ(q_is) - (β/2)Q² - (r/2)ΣQ_i² -(g/2)(Q_O²+Q_N²)\` with common \`φ\` for OLD/NEW products, \`φ''>0\`, \`β,r,g≥0\`, \`f'(x)>0\`, symmetric interior a and invertible adoption Jacobian \`Lφ I +2g 11'\`, \`Lφ=K''+φ''(1-a)+φ''(a)>0\`; regional CS share 1/N. NOT arbitrary nonlinear inverse demand.

## 4. Frozen result register: exact quantifiers, proof and portability

| ID | Theorem statement within explicit restriction | Mathematical status | Formal coverage | Portability |
| --- | --- | --- | --- | --- |
| L1 | For ANY given x, price-taking farmer constrained KKT and planner conditional W(a;x) KKT coincide; global conditional efficiency under strict concavity | **PROVED** within original concavity/price-taking scope | PROOF-CRITICAL CORE via \`Core.conditional_adoption_global\`; external economic KKT bridge | PORTABLE to concave competitive constrained allocations, not x efficiency |
| P1A | For ANY symmetric interior two-region baseline state, \`G_i,xi - W_xi = ξ(aStar-a)\` with \`ξ>0\`; threshold \`aStar\` generates reversal only if feasible in (0,1) | **PROVED** conditional on exact baseline model | Core factorization Lean; original demand/price-incidence derivation manuscript/SymPy | CONDITIONALLY PORTABLE |
| P1B/C | IF actual decentralized symmetric Nash and symmetric planner solutions are both feasible, global and interior with stipulated positivity, \`xD-xP=[ξ M/(RM-1+ξ)](aStar-aP)\` and \`W(xP,xP)-W(xD,xD)=(R-1/M)(xD-xP)²\` | **CONDITIONAL** analytic identities, proved under hypotheses | Lean FO-condition identities, not a proof of globality for every parameter | MODEL-SPECIFIC |
| Corollary | Same equilibrium restrictions: \`aD-aP=(xD-xP)/M\` | **CONDITIONAL** proved | Lean \`Core.adoption_gap_corollary\` | MODEL-SPECIFIC |
| P2 | For ANY symmetric interior point in restricted common-φ nonlinear demand class, \`G_i,xi-W_xi=[f'(x)(N-1)/(N Lφ)]*[Hφ(1-a)-Hφ(a)]\`, \`Hφ(q)=q φ''(q)\` | **PROVED WITH RESTRICTED ASSUMPTIONS** (paper model-Jacobian bridge; exact independent 3-region example); no arbitrary-demand theorem | Lean general-N Jacobian algebra **GIVEN** hown/hother; full economic P2 bridge is manuscript argument, not full Lean | CONDITIONALLY PORTABLE |
| P3+ | For EACH \`z∈(zCut,0]\` **IN EXACT PARAMETER FAMILY**, unique pure research Nash \`(xD,xD)\`, \`xD=(1+3z)/13>0\`; \`aD=(1+16z)/26>0\`; unique full-domain national social \`xP=aP=0\`; \`WD-W0=((10z-1)*(22z+3))/338<0\` | **PROVED exact full-domain global family** | Proof-critical-core Lean including 3 follower regimes, \`PrimitivesBridge\`, BR uniqueness and planner global uniqueness | MODEL-SPECIFIC |
| P3 endpoint | At \`z=zCut\`, exactly two local best responses \`0, sqrt(13)/52\`; exactly FOUR ordered research Nash profiles; lower endpoint not covered by uniqueness | **PROVED exact boundary**, retained adverse finding | Lean \`Boundary.lean\` | MODEL-SPECIFIC |
| P3 interaction | Exists separate e=1/100 and e=3/10 rational examples, xD positive, national optimum zero and strict W loss; nonzero first-stage cross-effect where claimed | **PROVED insofar as archival exact rational nine-KKT-active-set unilateral BR + national welfare evidence**; broader e-neighborhood/global uniqueness NOT PROVED | Lean \`ExactExamples\` certifies only candidate FOC/welfare algebra, **not** 9-regime Nash or uniqueness of all asymmetric equilibria | MODEL-SPECIFIC numerical exact examples |
| Economic application | Territorial public quality research first, fixed land privately and competitively switched later | **SUPPORTED INTERPRETATION**, not mathematically universal institutional theorem | Economic sources/argument only | INSTITUTION-SPECIFIC |

**P3+ exact parameter slice:** \`t=1/2\`, \`b=c=n=1/5\`, \`k0=κ=1\`, \`R=2\`, \`A=10\`, \`Δ=1/2+z\`, \`e=j=0\`, \`zCut=(-4+sqrt(13))/12\`. For each z with \`zCut<z≤0\`, region's \`x≥0\` constrained planting \`plant(z,x)=0\` if \`x≤-z\`, \`(z+x)/2\` if \`-z<x<2-z\`, \`1\` if \`x≥2-z\`. Off-path regional gain \`(z+x+1/4)a-(5/4)a²-x²\`. When substitution is valid:
- no-adoption \`F=-x²\` (never better than positive optimal gain),
- interior \`F=(z+x)/8 +3(z+x)²/16-x²\` (unique top \`xD=(1+3z)/13\`),
- fully adopted \`F=z+x-1-x²\` (large x never dominates).
National global welfare difference for *all* feasible x≥0 and a∈[0,1]²: \`W-W0 = z Σa + Σ x a -Σ a²-Σ x² = z Σa -(3/4)Σa²-Σ(x-a/2)² ≤0\`, unique equality at zeros. P3+ is not merely first-order optimality on equilibrium continuation, and no fixed fee is present.

**Unilateral vs mutual effort:** At symmetric P3+ Nash, one region's unilateral move to zero with rival effort held fixed is individually worse, but both regions prefer mutual zero effort to their mutual positive-effort equilibrium in the stipulated model. For z=0, unilateral positive research gain relative to own zero with other fixed is \`1/208\`, while mutual Nash vs mutual zero local welfare change is \`-3/676\`; no conflation. Analytic P3+ e=j=0 means **no strategic BR cross-response** despite shared welfare incidence; nonzero e proof is a separate example, not generic theorem.

## 5. Proof, source, axiom and independent evaluation artifacts

**Authoritative original theorem/proof:** \`checkpoints/2026-10-24/07_integrated_propositions/THEOREMS_AND_PROOFS.md\` (Git blob \`eca097f7a025dfd5efbe4ffbf8bebe41e33dcbb7\`). Stage 4A certificate blob \`dce97ea68caf162458ca0c7040b34ffe8cfdbb00\`. Stage 7.5A certificate blob \`6a679f3e4c08f9a104f6de45900b650cbdd08cfd\`. Stage7.5A final closure blob \`8ac4cb2f917bb246d63d0e6ff0d27d14e1eecb30\`. Original robustness certificate blob \`fbd8153c892d92c39df7e60592d4a198c1b5b242\`. Author record (self-attestation + evidence limits) blob \`4bfbaa86b0d96854d2295f72087213c6793ef810\`.

**Formal project:** \`checkpoints/2026-10-24/18_lean_formal_proofs/lean/\`. Lean top-level module \`PublicBreedingLean.lean\` blob \`e67810e718936e6e3658c4dd581b634d685e9a3a\`, and verified full tree:
- \`Core.lean\` blob \`6b780732e94bedcb7118188e2ee40d669717cd91\`;
- \`Prop3Global.lean\` \`616bdac943f020349622960a04a20c746644ba7c\`;
- \`Uniqueness.lean\` \`2b98e1421ec49c9f852c3de79075d4388966256e\`;
- \`Boundary.lean\` \`39563b1f101a3807a81a7b9b276c2713789f9bf4\`;
- \`PrimitivesBridge.lean\` \`9c283290f2284d7dc6230c287c07a27fade3aa71\`;
- \`Prop2N.lean\` \`aead43f0cdbb3558c318ec3a683dc7469294cb8e\`;
- \`ExactExamples.lean\` \`043053dacc802ecba607192aa1d4a9370ab5c617\`.
- \`lean-toolchain\` = \`leanprover/lean4:v4.35.0\`, blob \`a6aff065db2882c535684f8c5bcd4f16e9a23915\`; \`lakefile.lean\` mathlib \`v4.35.0\`, blob \`a7d45789cb48500f939f5d9a2a922b8362fbeb5d\`.
- Historical green build run \`40080770116\` commit \`66c22a9db4b2f7dfe4a8d675e4588a36aaa4b772\`: SUCCESS (compiled proof core, axiom audit). 107 declarations audited, no sorry/project axioms and only standard \`propext\`, \`Classical.choice\`, \`Quot.sound\` allowlisted according to checkpoint 19. Do not imply a new run occurred on this freeze-report commit.
- \`lakefile\` uses mathlib tag; \`lake update\` is called by CI; transitive dependencies not asserted byte-locked absent a committed manifest. Revisit if reproducibility policy requires exact revision pin.

**Previously independently verified external code:** Stage 4A preregistered diagnostic scripts under checkpoint 17, original exact nine-adoption-regime research BR check under checkpoints 04/15, \`21_stage11_adversarial_preflight/check_core_independent.py\` and \`check_nonlinear_primitive.py\`, GitHub Actions [run 40087931474](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40087931474) SUCCESS. Model economic derivation outside Lean includes generic P1 price/CS incidence and arbitrary nonlinear class P2 primitive-to-Jacobian proof. **Do not inflate \`Prop2N\` into complete Lean certification of those external assumptions.**

**Working manuscript source, NOT part of immutable theory proof:** \`checkpoints/2026-10-24/20_stage9_10_manuscript/paper.tex\`, blob \`373e56eee6aef3c9010968d7b1d53b2ac520d081\`. Earlier pdf/QA run \`40088099590\` succeeded in archival report; this Stage 8 has **not** performed a new PDF build or independent line-for-line copyedit. Stage9/10 will reconcile this existing provisional draft with the **now unconditional** Stage8 theory freeze.

## 6. Benchmarks / counterexample and portability regression register

**Benchmark definition:**
1. Conditional farmer optimum \`a(x)\` at fixed given publicly selected x is NOT first-stage optimal public R&D.
2. Symmetric interior regional Nash \`xD\`: simultaneous stage-1 individually global best response against rival action, downstream follower KKT solved for every unilateral action; not any local FOC candidate automatically.
3. National planner: maximizes \`W=V-ΣK-ΣC\` over the **existing model's technology and feasible x,a**, not an asserted feasible political contract; P3+ global inequality is on larger joint feasible set, so a nationwide first-best *within baseline technologies* is proved.
4. Mutually coordinated no-research \`(0,0)\`: baseline comparison that may be jointly welfare-improving despite no unilateral zero effort incentive. Always separate its payoff calculation from own unilateral gain.
5. Nonlinear-demand P2 planner shares \`1/N\`: welfare interpretation depends on that regional allocation rule. Real local fiscal/consumer incidence is not estimated.

**Negative / boundary register (all preserved, not paper-rescuing variants):**
- T1 preregistered: real research cost altered to \`C=x²+x⁴\`. Re-solved model at z=0 retains unique positive local optimum satisfying \`32x³+13x-1=0\` and national unique zero, negative W. **One bounded positive portability test**, not a general nonquadratic theorem.
- T2 preregistered: old/new own-demand curvature differs, \`φO''=1\`, \`φN''=2\`; at a=1/2 wedge \`-1/16\` despite neutrality in restricted equal-curvature P2. **Negative genuine counterexample**, prohibits universal half adoption.
- T3 preregistered: quartic grower conversion \`K=a+a²/2+a⁴/4\`; at a=1/4 exact wedge \`7/151>0\` after KKT re-solution; bounded local sign preservation, not general full-game proof.
- P3+ cutoff \`z=zCut\`: exactly four pure research profiles, **not unique**. Excluded lower boundary absolutely frozen.
- Finance/behavior/royalty: varying local objective weights \`λ,ω\`, effective fiscal incidence \`τ\` or positive per-adoption licensing royalties shifts/erases \`aStar\`. See checkpoint 08; NONE are incorporated into canonical baseline.
- P3+ analytic \`e=j=0\` yields independent public research BR; \`e>0\` strict interaction is supported by *separate* exact example only, not analytic open nonzero-e family or uniqueness of all asymmetric Nash.
- Missing P2 original-to-Lean full economic Jacobian proof, actual farm-side market power, uncertain innovation, IP rights, irreversibility, empirical calibration are stated omissions, not assertions of robustness.

**Stop rule:** no post-hoc new demands, region count, R&D player, policy subsidy instrument, asymmetric model or altered policy objective to boost reputation or rescue failure. New economic result requires formal rollback to Stage 3/4/4A/6 etc and Stage7.5A formal verification if affected.

## 7. Predecessor literature, institutions, AI/provenance and prohibited claims

**Closest predecessors, not to be erased:** Alston, Freebairn & James (2001) on beggar-thy-neighbor advertising; Balagtas & Kim (2007) on common input reallocation/optimal advertising; Lence et al. (2007) on collective product development and existing competitive adoption; Kinnucan & Miao (2000) related-product incidence (full source paywall); Akhundjanov et al. (2020) public-university apple licensing; Cardon & Pope (2003), generic/socially wasteful promotion; strategic quality R&D policy (Jinji & Toshimitsu etc). Point-by-point exact provenance and reading-depth limitations in checkpoint 25. **Original generic overinvestment/rent transfer, resource-reallocation, conditional farmer efficiency or demand-curvature envelope identity are NOT claimed novel.**

**Institutional meaning:** public prefectural agricultural experimentation and local varietal development are documented by OECD/MAFF official sources and particular prefectural research organizations. Institutional match **does not verify** exact G_i=Π_i+CS/2-C_i objective, deterministic research quality, real local tax burdens, average consumers, crop life cycle or nation-wide welfare impact. Treat as model/diagnostic implications, not observed numbers or budget advice.

**Material AI/source provenance:** Manuscript text, audits, source comparisons, math/computational scripts and formal proof files were developed with AI-assisted research and code workflows with GitHub provenance. Human author has expressly attested that the Stage 7.5A intellectual review is completed; **no independent source describing how that review was undertaken is supplied**. Lean, Python/SymPy, source-level referee tests and the author's attestation play different assurance roles. The eventual journal's AI-use policy, accurate use disclosure, authorship accountability, data/code statements and contribution declaration require specific preparation at submission; this freeze does **not** represent a final journal disclosure. Never claim an external editor independently evaluated the paper.

**Unsupported stronger claims forbidden:**
- "New general theorem on public R&D competition", first ever welfare-harmful innovation, universal overfunding, or general demand neutrality at a=1/2.
- "All actual regional breeding budgets should be cut", empirical welfare magnitudes or observed regional financing inefficiency.
- "Full paper is formally proved in Lean", complete generic P2 economic bridge Lean checked, or e>0 full nine-regime Nash Lean certified.
- "Positive Nash effort with strictly strategic substitution for all z in analytic e=0 interval"; \`e=0\` has no cross-effort BR effect.
- "Unique Nash at z=zCut", "all asymmetric Nash unique for e>0", "every parameter combination has a global interior Nash."
- "The national planner's allocation is implemented by a particular transfer, mandate, matching grant or budget-balanced agreement."
- "The current manuscript is already peer-review-ready" or "a specific journal is guaranteed to publish the result for free."

## 8. Family/dependency register, deferred and rejected options

**ADOPTED CORE**: Lemma L1; P1 (A sign/B conditional rank) and derivative corollary; exact global P3+; P2 restricted robustness/curvature classification (could be shorter in main text). Baseline public regional welfare and fixed-land allocation. Two separate e>0 EXACT example checks as supportive but not theorem expansion. The P3+ proof relies on classical consumer price-incidence theory, but does not introduce a separate novel generic parent theorem.

**DIAGNOSTIC-ONLY**: T1–T3, alternative λ/ω/τ/royalty policies in checkpoint 08, alternate nonquadratic real costs, stage-4A hostile boundary tests. Preserve successful AND failed alternatives, no claim added.

**DEFERRED FUTURE PAPER**: endogenous enforceable/fiscally balanced grant coordination, irreversible heterogeneous orchard vintages, uncertain quality research, innovation dynamics/knowledge spillovers, private breeder competition, explicit licensing and empirical structural welfare estimation. No authorized new theory work.

**REJECTED CURRENT GENERALIZATION**: cosmetic "public R&D for all industries" retitling or Cournot/Bertrand oligopoly reduction without re-solving and new contribution kill audit; also unsupported pure strategic R&D general theorem or indiscriminate institution-free policy recommendation.

## 9. Sequential game equilibrium and result taxonomy

- Stage-1 leader effort domain nonnegative unbounded real x_i; research payoff coercive under exact quadratic costs in frozen cases, but global optimality must still be proved not inferred from coercivity.
- Stage-2 independent grower shares restricted to [0,1] and priced nationally; interior FOC and two corners must be included for *every relevant leader deviation*, even if the selected equilibrium interior.
- Original P3+ prove case split all three response branches and strict unique BR in open z interval. zCut excluded endpoint exactly 4 profiles; no tie-breaking imposed.
- Asymmetric R&D effort deviations are included in unilateral best-response inequalities; full two-leader all-asymmetric equilibrium uniqueness is proven ONLY for e=j=0 separable research responses. No such uniqueness claim for e>0.
- e>0 global BR evidence uses original exact Python 3×3 adoption active-set enumeration, piecewise switching vertices and upper tails. Numerical solver failure, invalid branch/NaN are not counted as proof of nonexistence; original exact validations were reported PASS for named rational instances.
- Follower conditional efficiency proof uses constrained KKT, strict concavity and a continuous feasible compact planting square, not an interior extrapolation.
- Positive research plus negative national welfare is PROVED in exact P3+; quantitative external welfare magnitude **NOT MEASURED**.
- Evidence classes above disambiguate **PROVED / CONDITIONAL / EXACT NUMERIC-SUPPORTED OUTSIDE LEAN / REJECTED / NOT CLAIMED**. No extrapolation to unknown equilibria.

## 10. Change control, manuscript reuse and next canonical step

**Frozen mathematical object**: no mutation to \`paper.tex\`, \`THEOREMS_AND_PROOFS.md\`, Lean source, proofs, equations, model assumptions, existing CI or branch main in this checkpoint. Freeze is documentary, not a git tag, a merge or a permission policy. It freezes the *intended* theorem objects and the evidence versions enumerated above.

**Allowed without reopening theory gates:** concise English/exposition editing preserving math, reordering proof presentation without changing logic/quantifiers, polishing typesetting, fixing actual citation metadata, providing verified institutional source references, appendix formatting, computational reproduction hygiene, journal style/Word conversion, honest AI disclosure, and journal-specific submission form requirements.

**Requires reopening earlier theoretical checkpoints:** changing actors/government objectives, information/timing, private market conduct, demand/cost class, IP rights, fiscal incidence, proofs, admissible z bound, P3+ strategic claims, benchmark feasible set, or falsely strengthening generality from existing formula. Re-run every affected Stage 4/4A/6/7.5A/formal gate before re-freeze.

**Next in canonical order:** Stage 9 reproducibility/provenance reconciliation on the EXISTING draft and independent verification scripts, followed by Stage 10 final manuscript QA, then canonical Stage 11 adversarial paper/referee test, and formal Stage 12 venue/fees suitability. Old stage 9/10 manuscripts and Stage11 preflights are **pre-existing provisional artifacts**, not automatic gate passes merely because Stage8 is now GO.

**Final authoritative status: STAGE 8 GO / THEORY FROZEN v2, fully bounded institutional agricultural applied theory; author self-attestation recorded, proof-critical Lean PASS; manuscript/submission certification remains OPEN.**