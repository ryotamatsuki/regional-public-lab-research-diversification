# Canonical Stage 7.5A — Quantifier / Portability / Lean Proof-Core Reconciliation

**Date:** 2026-10-25 JST
**Project:** Regional Public Breeding and Variety Replacement
**Branch:** `research/2026-10-24-ijio-response-audit`; Draft PR #2.
**Inputs:** Stage 6 checkpoint 25 (bounded application-specific GO), Stage 7 checkpoint 26 (welfare/institutions GO), Stage 7.5 checkpoint 27 (compact applied-theory GO), historical Stage 7.5A checkpoint 17 (pre-registered attacks and pending author review), actual Stage 8 proof audit checkpoint 19, manuscript `20_stage9_10_manuscript/paper.tex`, manuscript independent Stage 11 checkpoint 23.

## 1. Gate verdict

**CANONICAL STAGE 7.5A: CONDITIONAL GO — exactly one outstanding hard blocker: the author's substantive intellectual/proof/claim-scope verification.**

Substantive quantified theorem scope, actual preregistered portability results, economic-to-formal bridge classification and proof-critical formal-verification gate are **PASS with explicitly limited coverage**. **FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE ONLY** (not full paper/full economic model). The previous checkpoint-17 judgment `FORMALIZATION APPLICABLE — NOT TESTED` was true *at its original date* but is superseded by later Lean build and this source-identity audit; do not erase or misrepresent the historical record.

The workflow expressly requires a real author intellectual contribution record with substantive author judgment **before unconditional Stage 7.5A GO**. Checkpoint-17 record exists but remains PENDING; no user request to proceed, assistant review or green CI is itself the author's substantive proof endorsement. Therefore no unconditional GO and no unconditional Stage 8 theory freeze are declared. After genuine documented author review, reconfirm unchanged source / statement scope and issue final Stage 7.5A GO (if the review endorses the exact claims), then Stage 8.

**NO new mathematical results, new central theorem, revised model, paper revisions or author approval recorded in this checkpoint.** Draft PR stays draft, main unchanged.

## 2. Current formal proof audit: actual toolchain, same source, theorem mapping

### A. Reproducibility and proof-assistant success

- GitHub Actions: https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40080770116
- Run `40080770116`, completed **SUCCESS**, commit `66c22a9db4b2f7dfe4a8d675e4588a36aaa4b772` on 2026-10-24, with both `Build Lean 4/mathlib proof cores and audit axioms` and setup steps successful.
- `lean-toolchain`: `leanprover/lean4:v4.35.0`. `lakefile.lean`: mathlib git reference `v4.35.0`. CI uses `leanprover/lean-action@v1` with `build:true, axiom-audit:true`. Existing Stage-8 CI summary reports 107 audited declarations and only `propext`, `Classical.choice`, `Quot.sound` permitted.
- **Content-identity check against actual green-run commit:** `PublicBreedingLean.lean`, `Core.lean`, `Prop3Global.lean`, `Uniqueness.lean`, `Boundary.lean`, `PrimitivesBridge.lean`, `Prop2N.lean`, `ExactExamples.lean`, `lean-toolchain`, `lakefile.lean` all have the same Git blob SHA at green-run commit and present branch. Consequently historical green-build evidence is applicable to current source. This is **not** a fresh build performed in this checkpoint.
- Inspected the current sources for `sorry`, `admit`, explicit `axiom`, `constant`, `opaque`, invented project-specific axioms and vacuous conclusion definitions: none identified. No theorem was found to assume the desired P3+ global BR or zero-optimum conclusion as a hypothesis.
- Dependency versions are tagged; `lake update` runs in CI. The repository listing did not expose a committed `lake-manifest.json`, so fully immutable transitive dependency snapshots are not asserted. This is reproducibility housekeeping, not evidence that recorded successful code was unproved.

**Axiom/placeholder verdict:** PASS within successfully compiled target declarations, subject to the ordinary reliance on Lean/mathlib and CI toolchain. FORMAL GATE CLOSED AS PROOF-CRITICAL-CORE PASS.

### B. Paper theorem ↔ actual formal theorem ↔ not-encoded scope

| Paper result | Audited formal theorem objects | What is certified | Not certified by Lean alone |
|---|---|---|---|
| Fixed-x conditional farmer efficiency | `Core.conditional_adoption_global`, `Core.kkt_direction` | Exact concave quadratic KKT ⇒ global constrained allocation, corners and asymmetric alternatives included | That actual farmers follow the residual/KKT, and general real-market price-taking assumptions |
| P1 signed wedge, effort ranking, adoption gap | `Core.p1_wedge_factorization`, `p1_effort_gap_from_focs`, `adoption_gap_corollary`, `p1_welfare_gap` | Correct rational identity/factorization assuming derived equilibrium equations; conditional square completion | Universal government Nash existence/uniqueness, original price-and-CS derivative bridge, off-branch global effort ranking |
| P2 nonlinear equal-curvature demand class | `Prop2N.p2_n_region_response`, `p2_n_region_curvature_incidence`; `Core.p2_half_share_neutral`, `p2_asymmetric_curvature_counterexample` | N-region rank-one Jacobian response algebra and signed curvature identity GIVEN Jacobian equations, half-share identity/falsifier | Derivation of Jacobian/economic incidence from arbitrary smooth national gross utility; general N full economic model formalization |
| P3+ competitive planting and BR | `Prop3Global.plant_lower/middle/upper`, `local_global_best_response`, `Uniqueness.p3_unique_global_best_response` | Entire nonnegative unilateral effort domain and all zero/partial/full adoption branches in exact original e=j=0 subfamily; unique positive BR for zCut<z≤0 | Generic e>0 BR, all agricultural technology profiles |
| P3+ model primitive bridge | `PrimitivesBridge.cs_from_four_goods`, `full_regional_off_equilibrium_reduction`, `local_objective_matches_full_market`, `full_national_off_equilibrium_reduction`, `farm_price_foc_reduced` | Four-good quadratic welfare and pricing expressions from the exact P3+ special-family primitives; local payoff reduction does NOT extrapolate interior-only FOC to corners | A Lean model of all P1/P2 primitives simultaneously; empirical institutions |
| P3+ planner unique zero and exact strict loss | `Prop3Global.national_square_identity`, `national_global_zero`, `national_at_local_strictly_negative`, `Uniqueness.p3_national_global_zero_unique` | Nonpositive real national welfare on free x,a feasible domain, global planner uniqueness and strict equilibrium loss in exact family | Empirically relevant size or sign of research in any actual prefecture |
| Excluded endpoint multiplicity | `Boundary.cutoff_exact_best_response_set`, `cutoff_four_nash_actions`, `cutoff_positive_effort` | At z=zCut exactly 0 and sqrt13/52 unilateral BRs; independent responses produce exactly 4 pure profiles | Multiple Nash for parameters outside cutoff slice |
| e=0.01 and e=0.3 coupled examples | `ExactExamples.interacting_farmer_foc`, `interacting_negative_welfare_exact`, `interacting_strategic_substitutes`, `national_zero_with_nonnegative_cross`, original analogues | Exact rational candidate FOC, cross-effect sign and nonpositive national welfare | Complete 9-regime global research BR proof or absence of all asymmetric equilibria; these are external exact Python evidence ONLY |

**Critical interpretation**: `Prop2N.lean` takes correct Jacobian equations `hown/hother` as hypotheses; claiming this file formalizes the entire nonlinear-demand derivation would be false. The manuscript has an explicit unformalized primitive-to-Jacobian economic proof and prior independent primitive calculation (N=3 exact check), but only the abstract rank-one algebra is Lean certified. Conversely P3+ has a stronger explicit economic-to-formal bridge via `PrimitivesBridge.lean`.

## 3. Formal quantifier / portability certificate (updated)

| ID | Exact quantified assertion and economic restrictions | Mechanism invariant | Pre-specified attack(s), result | Final classification / licensed wording |
|---|---|---|---|---|
| L1 | For ALL fixed x and feasible a∈[0,1]^2 under price taking, same real cost to farmer/planner and concave welfare, competitive KKT globally solves conditional W(a;x) | competitive adoption = conditional social allocation | Common stage-4A constrained KKT; no claim that x is efficient | **PORTABLE** within competitive-concave-constrained class; NOT R&D efficiency |
| P1A | For ALL symmetric interior states of the specific TWO-region linear/four-good game, when denominators valid, local-national x_i marginal wedge ξ(aStar−a). Strict sign switch occurs IF ξ>0 and aStar∈(0,1) | endogenous new/old allocation × induced cross-region price income incidence | T3 pre-registered quartic K fully re-solved, exact signed wedge 7/151 | **CONDITIONALLY PORTABLE** sign/incidence in defined classes; NOT generic arbitrary demand or all equilibrium corners. The prior checkpoint-17 discussion of N≥2 must NOT enlarge the precise four-good P1 theorem automatically |
| P1B/C & dependent corollary | IF both symmetric stage-1 Nash and planner are globally optimal and interior on same branch, with required strict Hessian/denominators, THEN exact xD−xP, aD−aP, squared welfare-gap identities | price-mediated quality-funding wedge with endogenous a | Exact verified algebra, no unconditional global BR for all parameter values | **MODEL-SPECIFIC** conditional research/planting comparison |
| P2 | For ALL symmetric interior points in particular N≥2 equal-old/new separable φ demand with f'>0 and Lφ>0, incidence sign ∝ Hφ(1−a)−Hφ(a) | same-generation response cancels after region-minus-national CS weighting; product-quantity weighted slopes | T2 pre-specified asymmetric φO/φN: a=1/2 but wedge −1/16, so blanket half-share neutrality FAILS | **CONDITIONALLY PORTABLE** only equal-curvature demand class; no universal 50% recommendation |
| P3+ exact analytical family | For ALL z∈((−4+sqrt13)/12,0] with EXACT t=.5,b=c=n=.2,k0=κ=1,R=2, continuous nonnegative x and fixed a∈[0,1], there EXISTS one unique pure research Nash (xD,xD), xD=(1+3z)/13>0, aD=(1+16z)/26>0; national unique global xP=aP=0; WD<W0 | upstream public locally profitable quality increases can lower national welfare via efficient competitive land reallocation | All 3 branches globally proved; T1 pre-specified quartic public cost separately sustains qualitative harmful positive Nash; excluded endpoint exactly four pure equilibria | **MODEL-SPECIFIC** analytic existence interval, NOT unique all-e Nash/generic social-wasteful R&D |
| e>0 interacting evidence | EXISTS specified rational parameter example e=.01 with strictly negative cross-effort derivative and one symmetric candidate independently 9-KKT-global-BR verified; all-e/all-asymmetric uniqueness NOT claimed | survives genuine (nonzero) effort strategic interaction in one example | independently exact pre-existing 9-case active-set method and numeric-rational identities | **MODEL-SPECIFIC** supporting existence only; global BR from Python, not Lean |
| Application itself | Territorial publicly funded quality research before private fixed-resource varietal conversion under model's explicit CS/2 regional accounting | distinctive sequence of public local financing and efficient private adoption | Institutional evidence OECD/MAFF, negative objective-weight/finance variants recorded in checkpoint 08 | **INSTITUTION-SPECIFIC** applied theory, not evidence of a new general theorem or empirically optimal province/crop policy |

### Updated tests, including negative results

- **T1** (quartic public cost): F(x)=x/8−13x²/16−x⁴ for z=0 middle adoption; first-order condition 32x³+13x−1=0 has a unique strictly positive global BR within tested regime; national planner zero and strictly lower W at Nash. Supporting paper `17.../CONTRIBUTION_ROBUSTNESS_CERTIFICATE.md`.
- **T2** (unequal old/new curvature): φO''=1, φN''=2, symmetric half-share a=1/2 yields exact wedge **−1/16 ≠0**. This is a genuine **failure of broad midpoint neutrality**, not a problem within the restricted P2 theorem.
- **T3** (quartic orchard conversion K): at exactly verified a=1/4, K''=19/16 and baseline cross-demand parameters, marginal wedge **7/151 >0**.
- In this turn, independently re-evaluated with SymPy: T1 polynomial derivative identity discrepancy 0; T2 result −1/16; T3 result 7/151; P3+ symmetric national-welfare polynomial equals (10z−1)(22z+3)/338 identically (residual 0). **These checks are supporting algebra only, not replacements for archived global deviation proofs**.
- **Negative boundaries retained:** at z=zCut exactly four pure Nash; at unequal old/new curvature midpoint no longer neutral; arbitrary local CS weighting/finance/royalty alter incidence; analytic e=j=0 does NOT provide strict strategic-substitute BR cross derivative.

**Portability stop rule:** No post-hoc alternative modification, no new theorem candidate, no "general robustness" inference. No pair of failed alternatives is concealed; broad transferability claims not made. No need to inject new assumptions to raise outlet prestige.

## 4. Paper abstract/introduction/discussion scope crosscheck

Actual manuscript `20_stage9_10_manuscript/paper.tex` on current branch read and compared:
- Abstract specifies **regional** breeder, **competitive** constrained land, two-stage quality effort and planting, and **explicit parameter family** rather than universal budget result: PASS.
- Introduction explicitly acknowledges Dixit/Norman, AFJ, Cardon/Pope, Balagtas/Kim, Lence, prior rent shifting and incomplete absolute source nonabsorption: PASS. After final Stage-6 closure this caveat may be made concise as an editorial revision later, but it does not misstate proof.
- P1 theorem says **symmetric interior**, permits sign reversal only when aStar feasible and ξ>0; xD/xP formulas additionally require interior feasibility / globality: PASS.
- P2 exact utility and stated theorem limit equality of old/new φ, symmetric interior and market-curvature Jacobian; does NOT claim any arbitrary nonlinear demand is neutral at half adoption: PASS.
- P3+ theorem strict lower cutoff, unique pure Nash in exact e=j=0 slice and unique national optimum, all 3 active sets and excluded 4-Nash boundary; distinction between unilateral and mutual payoff changes: PASS.
- e=.01 and e=.3 examples explicitly separate candidate arithmetic from non-Lean global 9-regime BR and do not assert uniqueness of all asymmetric Nash: PASS.
- National planner is a mathematical benchmark, NOT an automatically implementable central grant policy: PASS.
- The title uses "regional public breeding" without an unsupported IO/general R&D mechanism claim: PASS.
- **Minor wording future caution**: do not upgrade the paper's "derivation in appendix" to "Lean proof of every N-region economic primitive"; do not turn one quartic cost check into generalized robustness; avoid calling P3+ e=0 a strict strategic R&D substitution theorem.
- **Not examined in this stage:** new typeset PDF review, full peer-editor fit, new empirical estimates, or submission fee rules. Those are subsequent stages.

**No quantified theorem/discussion mismatch requiring changed economic primitives or new proof was identified** in this completed review. This is an internal adversarial source comparison, not a claim to replace outside referee judgement.

## 5. Planner and welfare benchmark

National objective W = sum local producer income + total CS − real research costs = gross utility V(q;x) − real grower conversion cost K(a) − real public R&D costs C(x). P3+ uniquely maximizes W at x=a=0 on full feasible x≥0, a∈[0,1]², a **larger** set than equilibrium-follower planting. Thus calling this the within-model national social optimum is licensed. No national patent, wage tax, intergovernmental commitment contract or empirical optimum is established. "First best" must be restricted to the model's given technologies if used at all.

## 6. AUTHENTIC AUTHOR INTELLECTUAL REVIEW — only unresolved hard blocker

The author's record already exists at:
`checkpoints/2026-10-24/17_stage4A_75A_certification/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`.
It explicitly remains `AWAITING AUTHOR'S ACTUAL REVIEW`. The audit has not witnessed or obtained the author's **substantive** statement on:

1. L1/P1: approves difference between conditionally efficient grower adoption and inefficient public research; understands interior/global assumptions and why 50% is not general.
2. P2: approves the essential equal-old/new curvature restriction and acknowledges T2's exact midpoint failure.
3. P3+: checks the three global planting cases and national square-completion; acknowledges the exact z domain and four equilibria at lower boundary.
4. Strategic interaction/welfare: acknowledges e=j=0 has no cross-effort BR, separate e>0 is numeric-exact case with no all-asymmetric uniqueness, and unilateral profitability differs from mutual zero-lab coordination.
5. Novelty/institutional assumptions: endorses restricted agricultural application/interpretation, CS/2 as stylized assumption, no novel generic overpromotion theorem, no operational grant implementation claim.
6. Evidence/attribution: notes what was verified in Lean versus paper argument/Python, and confirms the author has personally substantively considered the proofs, not merely agreed to an AI summary.

**DO NOT mark these approved in the absence of the author's own actual review.** Existing checkpoint 17 remains unchanged rather than falsifying a "signed" date. No AI inference about prior user's "next stage" instruction is acceptable proof approval.

A concise author-facing review form/checklist may be provided separately. A later authentic approval must refer to the exact version/claims, and substantive objection must reopen the affected theory/gate rather than rubber stamp.

## 7. Change control and next action

- **Stage 6 bounded novelty GO, Stage 7 economic/institutional GO, Stage 7.5 compact applied-theory GO** carried intact.
- **This Stage 7.5A:** quantifier, portability, statement-fidelity and FORMAL PROOF-CRITICAL CORE **PASS**. Overall **CONDITIONAL GO solely pending actual author's substantive intellectual review**. Do not misstate as unconditional Stage 7.5A GO or formally advance to Stage 8 just from this certificate.
- The previous "no Lean" blocker is NOW CLOSED through historical CI and byte-equivalent current source. Do not require a fresh duplicate symbolic audit unless source changes.
- Once author genuinely reviews and affirms the exact qualified claims, record that approval, recheck the same Git blob identity and **complete Stage 7.5A GO**, then perform Stage 8 canonical freeze. After that, revisit Stage 10/11 and formal Stage 12 journal choice in workflow order.
- No model changes, source patches, new economic headline, unauthorized journal submission, CI changes, PR merge, or author record alteration performed.
