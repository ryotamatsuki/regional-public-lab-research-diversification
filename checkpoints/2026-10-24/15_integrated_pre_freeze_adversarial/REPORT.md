# Checkpoint 15 — Final integrated pre-freeze audit: mathematics, novelty, theorem scope

**Date:** 2026-10-24. **Project checkpoint 15 is NOT canonical workflow Stage 15.** Original public-breeding game, original propositions, model files and archived checkpoints remain unchanged. The three earlier core results are supplemented by an explicit conditional-adoption efficiency Lemma, an interior-equilibrium adoption-gap Corollary and an analytic strengthening P3+.

## 1. Decision, separated by domain

**MATHEMATICS:** PASS for the explicitly checked original two-region primitives, P1 welfare wedge, restricted P2 nonlinear price incidence, and analytic P3+ theorem, subject to exact domain limitations below. Rerun exact e>0 whole-unilateral-deviation test passed; no claim of *all* e>0 equilibria unique.

**NOVELTY:** UNRESOLVED / PARTIALLY ABSORBED. Classic public/private promotion investment and related-market price-incidence literature already contains much of the generic externality intuition and resource reallocation. The complete published-parent theorem mapping for some decisive sources is unclosed; absence of access is not evidence of novelty.

**ECONOMIC CONTRIBUTION:** CONDITIONAL GO for continued **full-paper research**, rather than earlier premature NO-GO. P3+ is a substantive analytical existence proposition, not merely an isolated numerical parameter point. A reputable field editor may still assess the result as too close to generic rent-shifting games.

**CANONICAL THEORY FREEZE:** BLOCKED: project cannot show completed independent Stage 4A, Stage 6 parent absorption, Stage 7.5A quantifier/portability plus closed Formal Verification Gate, and authentic author verification. No canonical Stage 8 GO and no submission authorization at this stage.

## 2. Mathematics reproduction and scope

Independently rebuilt the four-product gross utility V=alpha'q-q'Bq/2, inverse prices p=V_q, quantities (1-a1,a1,1-a2,a2), farm producer payoffs Pi_i=p_i'q_i-K_i(a_i), consumer surplus CS=V-p'q, local objective G_i=Pi_i+CS/2-R x_i^2/2 and national W=G1+G2. Symbolically verified FOC and envelope equalities from the primitives, not only cited reduced-form profit expressions.

The research-adoption Lemma is a **conditional** efficiency lemma: at every fixed research vector x, competitive farm adoption obeys exactly the KKT maximizing W with that same x; B positive definite and K convex imply unique a(x), including zero/full endpoints. It says nothing about x itself being efficient.

Let h=1-t, j=b-c, e=b+n-2c, d=kappa+2h, M=d+e,L=d-e, xi=(2h-e)/(2L)>0 and a_star=(h-j)/(2h-e). P1 at interior symmetric farmer adoption states
\[
G_{i,x_i}-W_{x_i}=\xi(a_\star-a).
\]
The **effort ranking** and the proposed adoption-gap Corollary require both a *symmetric interior decentralized global Nash* and an *interior globally optimal social research vector*, plus regularity/strict Hessian conditions:
\[
x_D-x_P={\xi M\over RM-1+\xi}(a_\star-a_P),\qquad
a_D-a_P={x_D-x_P\over M}.
\]
These formulas are NOT valid as written at the zero-investment P3+ planner corner. A local welfare-gradient diagnosis at aD is a Corollary, not an implementable grant rule.

P2, in the stated symmetric separable nonlinear demand class only, has signed marginal wedge proportional to
\[
H(1-a)-H(a),\quad H(q)=q\phi''(q).
\]
In a fully independent two-region adoption-Hessian calculation, terms from common same-generation coupling g cancel in the local/national price-incidence difference; the exact coefficient is 1/(2[K''+phi''(1-a)+phi''(a)]). This result must not be labeled universal across arbitrary nonlinear utilities. A zero *interior marginal wedge* does not establish equality of all global optima when adoption corners exist.

### P3+ analytic, globally certified parameter interval

Use original model with t=1/2, b=c=n=1/5, k0=kappa=1, R=2, A=10, Delta=1/2+z. Here j=e=0. Define zc=(-4+sqrt(13))/12. For every z in (zc,0],
\[
a_i(x_i)=\operatorname{clip}((z+x_i)/2,0,1),\quad
x_D=(1+3z)/13>0,\quad a_D=(1+16z)/26>0.
\]

At a unilateral action xi the local incremental objective from xi=0 is
\[
F(x_i)=a_i/4+3a_i^2/4-x_i^2.
\]
(i) If xi<=-z, ai=0 and F=-xi². (ii) If -z<xi<2-z, F is strictly concave with F''=-13/8, unique xD and F(xD)=(48z²+32z+1)/208>0 in the stated interval. (iii) If xi>=2-z, ai=1 and F'=1-2xi<0. Thus the global best-response is **unique** xD and independent of the opponent's effort: (xD,xD) is the unique Nash in this **j=e=0** subfamily. It is a collective public-investment externality case, but **it does NOT have strictly strategic R&D substitutes** since e=0; do not sell this analytic interval by itself as a strict strategic-competition result.

For any **feasible** xi>=0 and ai in [0,1],
\[
W-W_0=z(a_1+a_2)+x'a-\sum_i a_i^2-\sum_i x_i^2
\le z(a_1+a_2)-3\sum_i a_i^2/4\le0,
\]
with equality only a=x=0. Consequently the nationwide planner's unique **global** optimal allocation has xP=aP=0, and
\[
W_D-W_0={(10z-1)(22z+3)\over338}<0.
\]
Since W=sum_i G_i and evaluated profiles are symmetric, each region's local welfare at mutual x=0 exceeds its payoff at mutual Nash investment, even while unilateral stopping is not optimal.

### Nonzero interaction, separately checked

Other admissible original parameters t=1/2,b=c=1/5,n=21/100,k0=kappa=1,R=2,Delta=49/100 give e=1/100>0 and, at symmetric interior, research cross derivative -50/39999<0. Reconstructed xD=9751/130096, aD=1051/32524, W_D-W0=-1933000423/211562115200. Independently reran the nine farm adoption active-set branches, their breakpoints and stationary/boundary candidates for all unilateral R&D deviations; local xD is a **strict unique global best response given opponent xD**, including all high-effort saturation deviations. Therefore this symmetric profile IS a Nash with strictly strategic-substitute research and global planner zero. We **have NOT excluded every alternative asymmetric Nash** at e>0. Strict inequalities/continuity imply local parameter robustness, not an explicit formula valid for every e>0.

### Independent verification artifacts

- Existing archived: checkpoints 04, 06, 07, 12, 14 and exact tests.
- Rerun: /mnt/data/public_breeding_stage14/verify_wasteful_rd_open_set.py and verify_e_positive_global_nash.py (both PASS).
- New independent primitive-level audit: /mnt/data/public_breeding_integrated_final_audit.py and public_breeding_integrated_final_audit_results.json. Thirteen algebraic/exact-rational assertions PASS, including P1 conditional adoption envelope, P2 nonlinear sign, P3+ welfare and the strictly nonzero-coupling comparison. A copy of the evidence summary is committed alongside this report.

## 3. Novelty and parent-model anti-absorption

- **Alston, Freebairn & James (2001), AJAE**, DOI 10.1111/0002-9092.00217: competing producer groups, related commodities, demand-enhancing advertisement, socially wasteful rent shifting; the explicit original independent supply and producer-group joint-profit planner differ from fixed old/new land shares and national PS+CS. **General economic intuition PARTIALLY ABSORBED; exact strong-parent theorem UNRESOLVED**. https://digitalcommons.calpoly.edu/agb_fac/10/
- **Balagtas & Kim (2007), AJAE**, DOI 10.1111/j.1467-8276.2007.01037.x: competitive allocation of shared raw inputs across correlated dairy product markets under promotion already established. The accessible 2005/2006 draft maximizes aggregate producer interests over promotion choices, not two territorial public laboratories simultaneously choosing quality. **SHARED-INPUT REALLOCATION ALREADY KNOWN; final published mathematical results not fully checked**.
- **Lence, Marette, Hayes & Foster (2007), AJAE**, DOI 10.1111/j.1467-8276.2007.01036.x: geographically differentiated agricultural innovations, competitive land allocation and welfare; examined earlier full working paper differs by collective producer regime/fixed development costs versus two local continuous public efforts. **No direct model isomorphism in checked draft; generic theorem absorption unresolved**.
- **Kinnucan & Miao (2000), AJAE**, DOI 10.1111/0002-9092.00059: related-commodity marketing incidence; published full text inaccessible; **UNRESOLVED**.
- **Zhang (2022), Manchester School**, DOI 10.1111/manc.12388: negative innovation value in a patent-race/licensing R&D model with sunk participation; **negative-social-value innovation as a headline is KNOWN**.
- **Oehmke et al. (2000), Agribusiness**, DOI 10.1002/(SICI)1520-6297(200024)16:1%3C68::AID-AGR6%3E3.0.CO;2-I: public agricultural R&D incentives already extensively treated, but abstract does not establish the current public-breeding Nash-zero-planner result.

A published paper's abstracts, its author preprint, and its final proofs are not interchangeable. Missing full published text cannot be silently treated as an absence-of-absorption certificate. The present P1 wedge is standard price-income-incidence/envelope mathematics; P2 is a signed restricted-demand corollary; P3+ contributes a relatively sharper *institutional existence and welfare characterization* that might sustain a full-length applied economic theory paper conditional on editorial scrutiny. No novelty from the mere use of two regions, four goods, or a 50-percent threshold.

## 4. Quantifier ledger / strongest prohibited overclaims

| Result | Maximum defensible claim | Claim to prohibit |
|---|---|---|
| Lemma farm allocation | For every fixed x given PD B, convex K and specified competitive market, farmer allocation = conditional welfare-optimal a(x), corners included | Adoption is always socially efficient when R&D also endogenous |
| P1 | Symmetric interior marginal sign; interior Nash–planner effort ordering only with global optimality and regularity verification | universal ordering for boundary solutions or arbitrary N player games |
| Corollary adoption gap | Symmetric interior linear/quadratic Nash and social optimum with M>0 and good denominators | new independent externality or valid without corners |
| P2 | Specific symmetric separable nonlinear preferences, H(q) derivative sign | every demand system or global equilibrium sign |
| P3+ | Existence across z in (zc,0] for exact e=j=0 original-family slice, unique Nash and nationwide-zero global optimum | all public R&D races welfare destroying; strict strategic interaction throughout analytic slice |
| P3+ robustness | One exact e>0 strictly strategic-substitute Nash example (and small open neighborhood) and nationwide optimal zero | unique equilibrium set or all e>0 without proof |
| Finance weights | Archive stage08 sensitivity, not in current three theorem core | same threshold after changing fiscal costs and local objectives |

## 5. Reviewer attack and truthful publication decision

The strongest objection is that the analytic P3+ family sets e=j=0, disabling cross-region research response; the remaining inefficient investment stems from a standard regional producer-price versus half-national-consumer-surplus externality. A separate exact e>0 example proves that interaction is not *required* to be zero, but does not elevate the analytic interval into a general multi-region competition theorem. Producer promotion, interlinked agricultural output reallocations, and negative innovation value all have famous predecessors. The present paper has no estimated demand system, proven-sized real-world welfare loss, or implementable federal research coordination instrument. Claiming three unrelated new mechanisms would likely fail peer review.

Countervailing value: P3+ reveals a *fixed-cost-free, globally certified positive subnational public-quality-investment equilibrium despite nationwide globally optimal zero R&D* in an environment of perfectly competitive replanting farmers, with additional nonzero strategic interaction robustness. P1 diagnoses the distortion and P2 specifies why demand curvature may neutralize/reverse it. This is potentially more substantial than the isolated numeric case and justifies a full-paper research path at established agricultural economics venues; **acceptance is not predicted**.

The paper is a diagnostic theory. WHY / constrained national SHOULD are modeled; enforceable fiscal coordination COULD (grant design, finance, contracts, information) is not, and must not be claimed. The editor may demand a policy implementation mechanism or real-market calibration; that is an honest audience-specific risk, not a universal mandatory rule for theoretical work.

## 6. Canonical workflow stage-gate status and exact next action

- Stage 4A independent mathematical adversarial certification: substantial supporting SymPy and KKT evidence, **formal final certified coverage not signed**. Need theorem-to-proof map and clarity around complete e>0 equilibrium set.
- Stage 6 novelty re-kill: **UNRESOLVED** decisive final versions; keep uncertainty explicitly rather than looping indefinitely.
- Stage 7.5 completeness: full-paper research **CONDITIONAL**, chiefly P3+ as main welfare outcome; policy implementation beyond claim scope.
- Stage 7.5A quantifier/portability: this report supplies a claim-scope ledger but not the formally completed certificate; no blind cross-model transfer.
- Formal Verification Gate: **APPLICABLE, NOT TESTED**. P3+ rational inequality/vertex/boundary cases and core P1/Farm lemma are suitable limited formal-verification targets; Lean/mathlib toolchain not present in current environment, and no proof-assistant verified build or formal claim mapping exists. Tool absence is NOT a valid NOT-APPLICABLE rationale. Gate remains BLOCKING.
- Stage 8 theory freeze: **BLOCKED** until Stage4A/7.5A GO and formal verification gate closed. Do not call Stage 10 manuscript begun, or claim external human referee validation.

**Route:** Retain 3 propositions + farm Lemma + adoption-gap Corollary without changing original primitives. An outline or proof/section architecture can be drafted provisionally, but formal canonical manuscript construction requires the above certs. Narrowed research next step: (i) published-parent decisive theorem mapping with honest access status; (ii) final Stage4A/7.5A signoff and limited proof-assistant certificate; (iii) author review; then Stage8 freeze and proceed to manuscript. Stop repeated generalist web searches that do not change this evidence.
