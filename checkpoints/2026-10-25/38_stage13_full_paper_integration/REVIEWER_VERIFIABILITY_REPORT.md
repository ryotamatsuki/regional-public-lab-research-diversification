# Stage 13 — Reviewer Verifiability Report

**Scope level:** FULL: central findings rely on coupled constrained-farmer KKT, first-stage local/national surplus incidence and a global piecewise best-response proof. Stage 8 mathematical object and author-approved limits remain immutable; this is an exposition certification, not a new mathematical theorem.

## 1. Claimed mathematical objects, domains and proof vehicle

| Claim | Object/domain | Economic-to-math bridge retained after compression | Evidence type / what it does NOT establish |
| --- | --- | --- | --- |
| L1 conditional farmer efficiency | National quasilinear V on four differentiated varieties; growers price-takers with unit land each, convex switching, given x and planting [0,1]^2 | `eq:utility` -> `eq:demand` p=V_q -> `eq:adoptionfoc` same as W_a -> complementarity at both corners + strictly concave W(a;x) | Paper analytical constrained KKT + Lean Core conditional lemma; doesn't establish first-stage R&D efficiency |
| P1 incidence / adoption-share sign | **two regions, symmetric interior follower**, B PD, `xi=(2h-e)/(2L)>0`; aStar feasible for sign reversal | P1 proof retains inverse `eq:adoptionmatrix`, producer price/CS `eq:incidencebridge`, planner envelope `W_x=a-Rx` and **explicit on-follower equality x=M a-z** before signed factorization `eq:wedge` | Lean algebraic factorization + independent Stage11 primitive SymPy. Formula NOT off-follower equilibrium, not arbitrary nonquadratic demand |
| P1 adoption/effort gap | Only where symmetric stage-one regional Nash AND planner are feasible global interior choices; RM>1 denominators and curvature | `eq:efforts` + `eq:corollary` + squared welfare gap `eq:interiorwelfarecost` | Algebraic conditional implications, not all-parameter global Nash ranking |
| P2 restricted nonlinear incidence | N>=2 identical regions, separable **common phi old/new**, φ''>0, symmetric interior and invertible LφI+2g11' | `eq:nonlinearutility` / Appendix `eq:appprice` -> grower D_i `eq:appD` -> response Jacobian `eq:appJ` -> projection `eq:appcontrast` -> price incidence `eq:appincidence` -> `eq:nonlinearwedge` | Formal Prop2N certifies conditional Jacobian **algebra** only; primitive-to-Jacobian economic proof remains in appendix; unequal curvature gives -1/16 at half adoption (outside theorem) |
| P3+ locally positive globally welfare-harmful public R&D | Exact family e=j=0, z∈((-4+sqrt13)/12,0]; 0<=a<=1, x>=0, all own research deviations | Original four-good B -> **unreduced** `eq:offpathpayoff` valid at corners -> piecewise `eq:clamp` -> `eq:threebranches` -> positive global maximizer & endpoint cutoff `eq:appBR` -> full joint-feasible W square `eq:plannerbound` -> `eq:p3loss` | Paper global inequality and Lean Prop3Global/PrimitivesBridge/Uniqueness/Boundary proof-critical core. Does NOT prove all e≠0 or real-world budget cuts |
| Mutual-versus-unilateral coordination | z∈(zCut,0], symmetric P3 Nash vs (0,0) | Local `F_i(xD)>0` holds rival fixed, while `eq:mutuallocal` measures joint move | Exact analytic, no transfer mechanism solved |
| Coupled benchmark e=1/100 | One exactly rational parameter combination and one symmetric Nash; nine grower active-set statuses | Main text exact xD/aD/welfare figures and appendix statement of nine-status global unilateral deviation program | SymPy rational enumeration, Lean ExactExamples only candidate identities; no all-asymmetric Nash uniqueness |
| Secondary e=3/10 | One rational example, same bounded conclusion | Relegated to computational appendix without losing xD/aD/welfare figures or provenance | Exact program external + candidate Lean; not new general theorem |

## 2. Human-reviewable proof bridges: deletion forbidden

1. **Consumer surplus and local objective** must remain `G_i=Pi_i+CS/2-C_i`, `W=G_1+G_2=V-ΣK-ΣC`. Any regional surplus variation is a model assumption, not empirical fact.
2. **Constrained growers**: the price difference minus conversion marginal cost and the KKT corner signs appear near the first Lemma.
3. **P1 derivation**: price+income+CS reduction `eq:incidencebridge` and on-symmetric-follower `x=Ma-z` are essential to get the precise welfare wedge; not replaceable by a claim "a computer verified this".
4. **P2 incidence**: the appendix projection and induced price weighting cannot be compressed to "differentiating gives result" without loss of derivability.
5. **P3 full best response**: all 3 piecewise adoption regimes in the main body; all x>=0 deviations evaluated and zero/full branch ruled out; `eq:appBR` exact gap in appendix. Boundary z=zCut has **four** Nash profiles and must be excluded from uniqueness.
6. **P3 national benchmark**: full feasible joint (x,a) square completion retained main; global zero conclusion not inferred just from on-path local FOCs.
7. **External exact check**: e>0 coupled case must identify *9* grower active-set combinations, rational rather than approximate samples, and distinction from formal Lean coverage.
8. **Current source references**: 14 bibliography keys (all cited) must survive the introduction compression. The original Stage 9 frozen manuscript/Lean files still define the approved theory scope.

## 3. Computational verification disclosure

- **Formal Lean:** Lean 4.35.0/mathlib v4.35.0 earlier successful CI with 107 audited declarations (Stage 8 proof-critical scope only), not a universal Lean proof of the paper. PrimitivesBridge covers **exact P3+ special family**. Prop2N proves rank-one algebra **conditional on Jacobian equations**.
- **External SymPy:** Stages 9 and 11 full exact-rational checks, independent four-good source reconstruction and coupled e>0 nine-regime global unilateral BR test. Does not establish all asymmetric e>0 Nash uniqueness or general nonlinear primitive proof in Lean.
- **Human author:** self-attested completion of six-point mathematical review (Stage 7.5A record). The time, exact methods and hand-rederivations used by the author are not separately documented; no external referee is claimed.
- **Submission review:** Anonymous supplementary replication package has not yet been prepared; no author-identifying GitHub repository link should be inserted into double-blind BAE manuscript.
- **AI declaration:** The paper now transparently names ChatGPT and roles in literature, writing, mathematical scripts and Lean formalization; author assumes full responsibility. Do not imply machine code was accepted as AI authorship.

## 4. Adversarial counterexample, robustness and figure gate

The independent stage11 reconstruction explicitly rejected extrapolating P1 wedge off follower equilibrium. T2 unequal-curvature demand gives wedge -1/16 at a=1/2 and bars a universal half-share policy prescription. T1 quartic C preserves positive local/zero national only in tested case; T3 quartic switching preserves positive sign at one tested point. Analytic e=j=0 P3+ has **no** cross-research best-response derivative; auxiliary e=1/100 has a nonzero cross reaction but no generalized global uniqueness. This is a genuine boundary case portfolio, not decoration. Main figures/tables **zero**, no generator/source links needed.

## 5. Gate result

**Reader-verifiability: PASS at source level**, conditional on Stage 13 compilation. All derivation objects and their valid domains can be reconstructed from the main text and three analytic/computational appendices without needing the external Lean repository to infer missing equations. Real computer-proof verification still requires separately supplied reproducible sources. This document and Stage 13 automatic theorem/display identity gate should be checked together before Stage 14 production.
