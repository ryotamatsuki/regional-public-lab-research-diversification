# Stage 7.5A — Contribution Robustness / Quantifier & Portability Certificate

Date: 2026-10-24. Canonical 7.5A, not project checkpoint 17. Pre-specification of three diagnostics was committed **BEFORE** calculations in PRESPECIFIED_ATTACKS.md, commit fdd3534208e8e46fb8aec08f95e3be0b6428257f. Three attacks have been independently re-solved and negative results retained. **Verdict: CONDITIONAL / FORMAL VERIFICATION BLOCKED; NO Stage7.5A GO and NO Stage8 Theory Freeze.** Canonical Stage6 remains accepted only provisionally per user's instruction; this certificate does not upgrade novelty.

## 1. Quantifier ledger and epistemic limits

| ID | Exact mathematical scope | Mechanism invariant | Strongest allowed claim | Portability |
|---|---|---|---|---|
| L1 | FOR ALL fixed x, concave V and convex K with competitive price taking and constrained a∈[0,1]^N; Hessian negative definite on feasible planting allocations | farmer FOC/KKT equals conditional W_a=0 | farm adoption is welfare-efficient CONDITIONAL ON R&D level | PORTABLE |
| P1A | FOR ALL symmetric interior states in N>=2 linear multi-market B positive-definite with identical regions, differentiable f and convex smooth K; margin by induced price transfers | sign of regional marginal wedge varies with a relative to a_star | sign law on specified interior and demand/region family | CONDITIONALLY PORTABLE |
| P1B/C | IF candidate xD is genuinely global symmetric Nash, planner globally interior, regularity R>1/min(M,L), THEN research ranking/welfare loss quadratic formula | endogenous variety share transmits x distortions | valid local–planner *ranking under stated sufficient global restrictions* | MODEL-SPECIFIC |
| C1 | IF both socially optimal and decentralized R&D/adoption solutions are symmetric interior in the linear/quadratic game, THEN aD-aP=(xD-xP)/M | follower linear response to quality | research and adoption deviations same sign, not independent failure | MODEL-SPECIFIC |
| P2 | FOR ALL equal-old/new, strictly convex C² separable phi satisfying particular common beta,r,g demand terms and symmetric interior follower allocation | local incidence depends on H(1-a)-H(a) | direction and neutral points within restricted demand class only | CONDITIONALLY PORTABLE |
| P3+ exact interval | FOR ALL z∈(zc,0] in **exact** e=j=0 numeric parameter slice: unique pure R&D Nash, social planner unique zero, welfare loss | local producer income responds to quality-induced endogenous conversion but nonnational incidence | analytic parameter interval with strict convex costs, not a universal public R&D theorem | MODEL-SPECIFIC |
| P3+ economic phenomenon | Exists a parametric family with strictly harmful positive local public R&D, and a separate e>0 true strategic substitute example; holds under one pre-specified quartic R&D cost diagnostic | external national price incidence in locally financed quality improvement | bounded persistence across one cost technology and nonzero coupling | CONDITIONALLY PORTABLE |
| P3 e>0 | EXISTS symmetric Nash at e=1/100, xD=9751/130096, national planner zero and strictly W loss; best response exact | some genuine strategic coupling survives | existence, not unique all Nash or all e>0 | MODEL-SPECIFIC |

The analytic e=j=0 P3+ subfamily has cross-research interaction exactly zero. The e>0 example is not an analytic open-interval theorem in e. The original Stage6 novelty remains limited and separate.

## 2. Actual preregistered alternative results — all three

### Test T1: real R&D cost altered to C_i=x_i²+x_i⁴ (rather than baseline x_i²)

Retain original old/new fixed-unit-land price-demand structure, e=j=0, z=0, original grower quadratic K and real quality effect f(x)=x. Farmer best response re-derived as a_i=clip(x_i/2,0,1). Local unilateral gain with ai in interior:
F_i(x_i)=x_i/8-(13/16)x_i²-x_i⁴.
Its second derivative is -(13/8)-12x_i²<0. The first derivative is (1-13x_i-32x_i³)/8, strictly decreasing, positive at 0 and negative at 1/13. Therefore the unique interior maximizer is the positive root of 32x³+13x-1=0, approximately **0.07584895060984409**, with adoption ~0.0379244753049220. At the other planting regime a=1 (x>=2), local objective becomes 1-x²-x⁴ and is strictly decreasing; x=0 gives zero gain. Therefore the strictly positive root is global unique BR and hence unique symmetric (indeed global) pure R&D Nash.

Nationwide welfare for all feasible xa is
W-W0=sum_i [x_i a_i-a_i²-x_i²-x_i⁴]
=sum_i[z a_i-3a_i²/4-(x_i-a_i/2)²-x_i⁴] when z=0.
The unique joint social optimum is x=a=0; at symmetric Nash W_D-W0=-(3/2)xD²-2*xD⁴ ≈-0.008695790437787707. **PASS**: P3+ phenomenon persists under meaningful nonquadratic research cost (DIAGNOSTIC ALTERNATIVE ONLY, not canonical theorem expansion).

### Test T2: old/new curvature no longer identical, while farmer adoption interior

Replace equal phi by phi_O(q)=q²/2, phi_N(q)=q², with g=1/10 in the original nonlinear common same-generation term, two regions and K_i(a)=a+a²/2. Set old/new quality intercept difference 19/10 and symmetric positive research x1=x2=1/10 so that symmetric a1=a2=1/2 is exactly an interior competitive allocation. The modified adoption Jacobian is minus [[21/5,1/5],[1/5,21/5]]. Rebuild **p=V_q**, CS=V-p'q, Pi_i=p_i'q_i-K_i and W=Pi1+Pi2+CS-sum x_i², then differentiate with the new implicit adoption response. Exact:
\[
G_{1,x_1}-W_{x_1}=-1/16\ne0
\]
at a=1/2. In the original equal-curvature P2 the corresponding signed expression is zero at a=1/2. **FAIL OF UNCONDITIONAL HALF-SHARE NEUTRALITY**, as expected; not a counterexample to the written P2 because it deliberately violates the essential equal-old/new phi assumption. This is a genuine negative portability result, and the failure boundary is the old/new curvature asymmetry. Do not erase it by redefining a different threshold.

### Test T3: nonquadratic orchard conversion K(a)=a+a²/2+a⁴/4

Original linear demand t=1/2,b=n=3/5,c=9/20, A=10; change K (not demand), choose x1=x2=1/10 and Delta=269/320 so symmetric a1=a2=1/4 exactly satisfies new farmer first-order condition. The new K''(a)=1+3a²=19/16. Compute V and all four prices from independent q variables, derive the new follower Jacobian/KKT and differentiate G_i and W along follower response, NOT the old quadratic cost response. Exact:
\[
G_{1,x_1}-W_{x_1}=7/151>0.
\]
The P1 price-incidence expression, correctly using K''(a)+2h-e, also evaluates to 7/151. Hence the P1 sign mechanism **survives** a nonquadratic grower conversion technology at this tested interior state; original Stage04 supplies N-general proof under convex K.

## 3. Exact adverse boundary regression P3+ — multiple equilibria at zc

Define zc=(-4+sqrt13)/12. At z=zc, positive stationary x_c=(1+3zc)/13 = sqrt13/52, with a_c=(zc+x_c)/2>0. The *interior-branch payoff gain* F(x_c)=0, and at x=0 the follower adopts a=0 and gain is also exactly 0. Piecewise zero-planting, concave interior and saturated old/new regimes prove NO OTHER maximizing effort. Since e=j=0 the local best-response set is {0,x_c} independently of rival. Thus **exactly four pure research Nash equilibria** exist at z=zc.

The P3+ theorem uses the **strict lower bound z>zc**; therefore its uniqueness claim is correct. Do NOT include lower equality while asserting unique Nash, and do NOT use interior-branch F(0) at the no-adoption corner. This is a first-class negative boundary result, not an abandoned numerical run. Proof script: verify_p3_boundary_multiplicity.py.

## 4. Main and headline claims' failed portability and stop decisions

- P1's local sign law genuinely survives general convex K within linear symmetry (T3), but sign/rank cannot be made arbitrary-demand or global without an independent theorem. CONDITIONAL PORTABILITY; no revision to main model.
- P2's equal-old/new separable demand *is an essential economic symmetry*. T2 falsifies a broader half-share claim in a credible asymmetric quality-demand alternative. CONDITIONALLY PORTABLE, NOT generic. The stop rule precludes retuning the alternative after seeing failure.
- P3+ has exact global proof within quadratic real R&D costs, one independent nonquadratic real-cost success T1, and original separate nonzero e=1/100 exact symmetric Nash success. Therefore retain bounded economic phenomenon, but **the exact z interval and unique pure Nash formula are MODEL-SPECIFIC**. No proof of general market-wide harmful R&D, all-asymmetric Nash uniqueness at e>0, or independent of local welfare shares. No rescuing modification authorized.
- Policy reading: the national planner optimizes *the same existing technologies and population* x>=0,a∈[0,1]. It is not an operational intergovernmental contracting mechanism; no claim about observed real citrus welfare or actionable 50% funding rule.

## 5. Stage7.5A formal proof and authorship hard gate

See FORMAL_VERIFICATION_GATE.md and AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md in this checkpoint. Key targets are the exact P3+ lower-bound inequality, piecewise global effort BR and nationwide welfare square-completion, not an inflated "entire economic model formally proved" slogan.

**Local environment**: SymPy 1.14, SciPy 1.17 available. No lean/lake/elan executable, no Lean/mathlib cache. Network name lookup for GitHub failed. Hence **no auditable Lean build and no Formal Verification PASS**. The workflow explicitly forbids treating inconvenience/no executable as a justification for N/A when proof-critical formal core would help. **FORMALIZATION APPLICABLE — NOT TESTED**, blocks Stage7.5A GO and Stage8.

The author has not yet personally signed a substantive contribution/limitation review. Leave contribution record as **AWAITING AUTHOR SUBSTANTIVE REVIEW**, do not make an AI green check a surrogate for author accountability.

**Final Stage7.5A status: CONDITIONAL / BLOCKED** despite the credible portability evidence and scope classifications. No baseline source files altered. Re-run this gate after Lean (or other valid proof assistant) target builds cleanly and author review is documented. Stage6 is held provisional, per explicit request.
