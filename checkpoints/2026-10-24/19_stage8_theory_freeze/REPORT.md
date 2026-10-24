# Stage 8 — Theory Freeze v1 (2026-10-24)

## Gate verdict: CONDITIONAL THEORY FREEZE / WRITING-READY, NOT UNQUALIFIED CERTIFICATION

This checkpoint freezes the **substantive theory as it stands** for full-paper drafting. No modifications to original economic primitives, equilibrium definition, original propositions or archived proofs are authorized by this checkpoint. The user explicitly directed Stage 8 after checking final Lean build. The author has not separately signed a substantive verification record; Stage 6 novelty remains conditionally accepted at the user's direction. These two limits must not be described as PASS.

### 1. Verified latest build

GitHub Actions run https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40080770116, commit 66c22a9db4b2f7dfe4a8d675e4588a36aaa4b772: SUCCESS. Lean 4.35.0, mathlib v4.35.0, 107 declarations audited; only propext, Classical.choice, Quot.sound allowlisted. The top-level imports all Core, Prop3Global, ExactExamples, Boundary, PrimitivesBridge, Uniqueness, Prop2N. No "sorry"/unapproved axiom dependency in audited declarations. **Kernel PASS only for statements actually encoded, not for the whole source paper.**

### 2. Frozen economic structure

Two regional public breeding labs choose nonnegative continuous quality R&D efforts x_i simultaneously (stage 1). Competitive price-taking farmers choose new variety planting share a_i∈[0,1] on fixed land (stage 2), with four differentiated old/new varieties and national market inverse prices from quasilinear consumer utility. Region i maximizes local producer surplus plus one-half of national consumer surplus minus own real convex public R&D cost R x_i²/2. National planner maximizes the sum of regional objectives. Research and adoption are different decision variables, but follower a responds to x. Baseline linear/quadratic model definitions:

h=1-t; j=b-c; e=b+n-2c; M=κ+2h+e; L=κ+2h-e; z=Δ+h+j-k₀; ξ=(2h-e)/(2L); a★=(h-j)/(2h-e).
Symmetric interior follower a=(z+x)/M.
Symmetric planner xP=z/(RM-1), aP=Rz/(RM-1).
Symmetric decentralized candidate xD=[(1-ξ)z+ξ M a★]/(RM-1+ξ), aD=(z+xD)/M.
All formulae require the stated positive denominators, relevant Hessian/concavity, interior feasibility, and global Nash/planner verification; never extrapolate these formulas to corners without KKT case analysis.

### 3. Frozen theorem order and precise scope

- Lemma 1 (conditional adoption efficiency): for given research efforts, farmer price-taking planting KKT conditions coincide with the conditional national welfare KKT, including planting corners, provided common concave national surplus and identical real conversion cost. This does **not** imply socially efficient x.
- Proposition 1 (research incentive incidence): on specified symmetric interior linear demand states, regional-national marginal research wedge ξ(a★-a); threshold sign only if positive prefactor assumptions hold. Global research ranking requires separately established equilibria and positivity/concavity.
- Corollary 1 (endogenous adoption follows research): for symmetric interior solutions, aD-aP=(xD-xP)/M, and xD-xP=[ξ M/(RM-1+ξ)](a★-aP). Same-sign conclusion only if ξ>0, M>0, RM-1+ξ>0; it is not a new independent market failure.
- Proposition 2 (nonlinear curvature): restricted old/new identical-curvature separable-demand family, Hessian invertibility, and symmetric interior farmer response; sign depends on H(1-a)-H(a), H(q)=q φ''(q), with appropriate positive multipliers. General N response difference algebra is Lean-verified under explicitly assumed Jacobian equations, **not** arbitrary utility or asymmetry. At a=1/2 neutrality depends on equal old/new curvature; preregistered asymmetric test yielded nonzero wedge -1/16.
- Proposition 3 / P3+ (severe national waste): in the explicit e=j=0 exact parameter family t=1/2,b=c=n=1/5, κ=k₀=1,R=2, A=10, Δ=1/2+z, zc=(-4+sqrt13)/12 < z ≤0: unique local global BR xD=(1+3z)/13>0; planting aD=(1+16z)/26>0; unique nationwide global social optimum xP=aP=0; welfare loss (10z-1)(22z+3)/338<0. Local BR proven over all three follower planting regimes and national optimum over arbitrary nonnegative x and feasible a. At z=zc, each regional BR is {0,sqrt13/52}, giving four pure Nash profiles, so the lower bound MUST remain strict.
- Distinct e>0=0.01 interacting example: original model candidate symmetric Nash xD=9751/130096, aD=1051/32524, national optimum zero, welfare loss -1933000423/211562115200, strict strategic-substitute derivative -50/39999. Exact original Python 9-regime global BR verification; Lean certifies rational candidate arithmetic and planner bound, **NOT** 9-regime Nash globality or uniqueness of all asymmetric equilibria.
- Distinct original Δ=0.34,e=0.3 example: xD=389/6470, aD=141/6470, welfare loss -2569157/418609000. The 9-regime Nash audit remains a non-Lean exact computation. Do not conflate its parameter set with P3+ analytic slice.

### 4. Independent proof and portability audit

Stage 4A mathematical adversarial check GO within enumerated theorem scope. Stage 7.5A preregistered meaningful alternatives: quartic public R&D costs retain harmful local positive Nash; old/new asymmetric curvature defeats half-share neutrality; quartic orchard conversion retains P1 incidence sign at tested point. Excluded P3+ endpoint yields multiple Nash. No universal generalization from one or two alternative tests. The latest formal proof core removes the old Stage7.5A "no Lean toolchain" blocker, but **does not retrospectively assert full Stage7.5A author signoff**. See checkpoint 17's contribution review record.

### 5. Frozen novelty and editorial scope

The research contribution is a bounded characterization of endogenous quality R&D and competitive variety replacement under territorial public lab objectives and nationwide price incidence. Generic beggar-thy-neighbor advertising, public R&D under/overinvestment, rent dissipation, negative social innovation and geographic differentiation are known; do not assert those broad categories are new. Closest published parent literature was compared in prior checkpoints; Stage 6 remains provisional/conditional as explicitly instructed. Theorems' hypotheses, game structure, follower adoption and comparison benchmark all matter to originality, not headline sign alone.

**No submission-ready GO.** Full-length manuscript drafting is permissible using this frozen baseline with transparent limitations, proof appendices, and bibliography checks. No unproved empirical claim, no automatic policy prescription, no journal acceptance likelihood guarantee.

### 6. Open gates and change control

1. Author's actual substantive model/proof/scope review: PENDING; only author can sign. Preserve checkpoint 17 author record unchanged.
2. Stage 6 source novelty remains provisionally accepted and must be reconfirmed before final submission; do not silently upgrade.
3. Formal proof of all original e>0 9-regime regional Nash globality: NOT in Lean; retain existing exact Python audit, or separately formalize if desired.
4. Nonlinear P2 demand-to-Jacobian economic bridge and generic N proof: only algebra conditional on the Jacobian was Lean-certified.
5. Stage8 frozen baseline may be changed only via a clearly labeled reopened checkpoint explaining new result, affected statements, and proof changes. Do not change canonical main-model source in this freeze.

**Stage 8 verdict: CONDITIONAL FREEZE — mathematical core stabilized and eligible for full-paper drafting, with no false claim of author review, unconditional novelty, or whole-model Lean proof.**
