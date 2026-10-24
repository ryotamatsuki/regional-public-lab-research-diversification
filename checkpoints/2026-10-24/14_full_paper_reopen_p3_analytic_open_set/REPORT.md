# Checkpoint 14 — Reopen the full-paper decision: a theorem-level strengthening of Proposition 3

**Date:** 2026-10-24. **Verdict:** WITHDRAW checkpoint 13's premature full-paper NO-GO. **CONDITIONAL GO for investing in a full-length field-journal applied economic theory paper**, NOT submission GO, NOT canonical workflow Stage 14. Reopen the Stage 6/7.5 economic-contribution gate to incorporate the materially stronger analytic existence result. Original game/primitives/three archived propositions and proofs unchanged; this checkpoint proves a strengthening inside the same model. Existing Draft PR #2 remains unmerged.

## The economic question

When can every subnational public plant-breeding agency rationally fund strictly positive quality R&D, even though no public quality R&D whatsoever is the unique national-social optimum, **without fixed R&D entry/setup costs, patent races, price-setting sellers, or patent-license rents**? This is stronger than a local overinvestment comparison and matters for whether competing regional public innovation programs should exist in the first place.

*Do not call the generic phenomenon of socially wasteful R&D unprecedented*. Existing relevant papers include Alston, Freebairn & James (2001 AJAE) on inefficient noncooperative commodity advertising and Zhang (2022, Manchester School 90:59–76, DOI 10.1111/manc.12388) on the negative expected social value of an innovation from an R&D patent race and subsequent licensing (his mechanism does use upfront fixed R&D entry costs). Full theorem-level nonabsorption is not certified. The potentially distinctive aspect is a **non-patent public local quality-investment game with perfectly competitive acreage-adopting farmers, exact global zero public-investment planner, and continuously convex costs**.

## Precise analytic proposition P3+ — interval, not a lucky parameter point

Use the **original two-region linear four-product inverse-demand game** with:
t=1/2, b=c=n=1/5, k0=kappa=1, R=2, A sufficiently large (e.g., A=10) for positive transacted prices, and Delta=1/2+z. Then h=1/2, j=b-c=0, e=b+n-2c=0, d=kappa+2h=2. B has strictly positive eigenvalues 1/2 (twice), 11/10, 19/10. No fixed research project fee (C_i=x_i^2).

Define z_c=(-4+sqrt(13))/12 approximately -0.0328707270447. For **every** z in (z_c,0], farmers choose adoption via the globally valid KKT map

\[
a_i(x_i)=\min\{1,\max\{0,(z+x_i)/2\}\}.
\]

In the two-region stage-1 game, because e=j=0, the unilateral local objective difference from xi=0 is **independent of xj**:

\[
G_i(x_i,x_j)-G_i(0,x_j)
= {a_i\over4}+{3a_i^2\over4}-x_i^2.
\]

Its unique global maximizer is
\[
x_D={1+3z\over13}>0,\qquad a_D={1+16z\over26}>0.
\]

The national unique **global** welfare-maximizing research vector is x_P=(0,0), adoption a_P=(0,0). Yet the nationwide welfare loss at the symmetric, globally certified (indeed uniquely best responding) research Nash is

\[
W(x_D,x_D)-W(0,0)={(10z-1)(22z+3)\over338}<0
\]

throughout z in (z_c,0]. Because regions are symmetric and G_1+G_2=W, each region is itself strictly better off at **mutual research inactivity** than at the noncooperative positive-research Nash. This is a prisoners'-dilemma-type investment outcome, not a proven equivalence to the canonical 2x2 prisoner's dilemma.

### Self-contained proof of GLOBAL best response including planting corners

For 0<=xi<=-z (when z<=0), ai=0, hence Gi(xi,xj)-Gi(0,xj)=-xi²<=0.
For -z<xi<2-z, ai=(z+xi)/2; substitution gives the concave quadratic
\[
F(x_i)={z+x_i\over8}+{3(z+x_i)^2\over16}-x_i^2,\quad
F'(x_i)={1+3z-13x_i\over8},\quad F''=-13/8<0.
\]
Its unique vertex x_D=(1+3z)/13 lies in the interior for z>z_c (z_c>-1/16), and
\[
F(x_D)={48z^2+32z+1\over208}>0
\]
for all z in (z_c,0], while F(0) defined on the boundary lower branch is 0. The positivity endpoint condition is exactly z>z_c; no numerical optimization.
For xi>=2-z, ai=1 and the direct price benefit of further own research is one, so \(\partial G_i/\partial x_i=1-2x_i<0\). Therefore the global unique best response is x_D *for any opponent research* (since e=j=0), making (x_D,x_D) the unique public R&D Nash.

### Self-contained proof of the unique GLOBAL social zero choice

Before using the adoption FOC, welfare relative to no R&D/zero conversion is
\[
W-W_0=z\boldsymbol 1^\top a+x^\top a-\tfrac12a^\top Ha-\tfrac R2x^\top x,\quad
H=2I,\quad R=2.
\]
By completing the square for arbitrary x_i>=0 and 0<=ai<=1,
\[
W-W_0\le z\sum_i a_i-\tfrac12 a^\top(H-R^{-1}I)a
=z\sum_i a_i-\tfrac34\sum_i a_i^2\le0
\]
for z<=0, with equality only at a=x=0. Thus the benchmark includes every asymmetric region-research deviation and the no-research optimum is globally unique.

At z=0: x_D=1/13, a_D=1/26, W_D-W_0=-3/338; own unilateral gain of investing vs stopping given rival invests =1/208; welfare per-region loss compared with mutual no-R&D = -3/676.

## STRONGER: nonzero cross-region strategic substitution, certified with exact KKT deviations

Because e=0 in the explicit analytic family, the first-stage cross derivative is zero. **Do not pretend the analytic closed-form family itself has strictly strategic substitutes.** To test that this is not a no-interaction artefact, use the *same original game* with t=1/2,b=c=1/5,n=21/100,kappa=k0=1,R=2,Delta=49/100, A=10. Then z=-1/100, j=0,e=1/100>0 and

\[
{\partial^2G_i\over\partial x_i\partial x_j}
=-{e\over2(d^2-e^2)}=-{50\over39999}<0.
\]

The symmetric interior candidate is x_D=9751/130096 ≈0.0749523429, a_D=1051/32524 ≈0.0323145985. The nationwide planner uniquely selects zero R&D because z<0 and H-R^{-1}I remains positive definite. Welfare delta is the strictly negative exact rational

\[
W_D-W_0=-1933000423/211562115200\approx-0.009136799.
\]

**Full exact global deviation audit was rerun**: enumerate the 9 old/new adoption KKT active sets, partition xi in [0,5], enumerate all within-regime quadratic stationary points and endpoints (9 candidates, 7 nonempty regimes), check the unique highest local payoff at x_i=x_D against x_j=x_D. Next best candidate is xi=1/50; best-response gain is positive exact rational 346042207950657/141037884098080000. For xi>=5, own new adoption is fully saturated and own derivative 1-2xi<0, so no unbounded deviation was missed. Thus (x_D,x_D) is a **genuine** strictly positive, strategically substitutable *symmetric* Nash equilibrium. **No global uniqueness claim over all possibly asymmetric equilibrium pairs** was established for this e>0 configuration.

The strict payoff gap to alternative distant responses plus local strict curvature and all strictly feasible interior adoption permit a small open parameter neighborhood of this e>0 example with the same phenomenon; proving its precise maximal open set remains outside the result.

Independently run local source:
- /mnt/data/public_breeding_stage14/verify_wasteful_rd_open_set.py
- /mnt/data/public_breeding_stage14/results.json
- /mnt/data/public_breeding_stage14/verify_e_positive_global_nash.py
- /mnt/data/public_breeding_stage14/strict_positive_e_result.json
These exact output paths are local artifacts **not automatically committed** with this Markdown.

## Previous premature editorial decision and revised editorial routing

Checkpoint 13 reasoned that full-paper publication requires 3 independently novel deep theorems and declared NO-GO. **That is not a necessary criterion**: a focused full-length paper can have one major substantive theorem, its mechanism/robustness characterization, and a substantial welfare corollary if novel and important. The previous judgment undervalued P3 because it treated the archived Delta=.34 case only as a small uncalibrated example; the above analytic interval/global-welfare theorem materially improves the claim, without changing the model.

Recommended potential organization: P1 adoption-dependent local–national marginal research wedge; P2 restricted demand-curvature limits/neutrality; **P3+ nationally harmful positive public R&D with no fixed R&D setup cost, on an open parameter set with strict best-response proof**; append policy interpretation and institutional US/EU public fruit breeding examples, with no fake scale prediction.

**Full-paper RESEARCH route: CONDITIONAL GO; do not write submission-ready 20-page paper yet**, unless confirmed parent-theorem nonabsorption and editorial importance. Main novelty objections remain:
(1) Generic beggar-thy-neighbor competition (AFJ 2001) and negative-social-value innovation (Zhang 2022) are prior art;
(2) our price-incidence wedge is generic envelope math, and half-adoption reversal is symmetry-specific;
(3) exact primary theorem matching with Balagtas/Kim 2007, Kinnucan/Miao 2000 is unresolved.
Before a full-paper freeze run canonical Stages 2/6 and 7.5 economic valuation, Stage 4A formal theorem scope/uniqueness, Stage 7.5A portability and formal verification, Stage 11 manuscript hostile review, and then Stage 12 journal positioning. **NO submission GO is granted.**

Strongest distinct claim to test against prior art: not merely a wasteful R&D race, but **nationally dominated, strictly positive decentralized PUBLIC innovation investment despite (i) no patent/licensing/rent exclusion, (ii) competitive growers' endogenous orchard conversion, (iii) continuous strictly convex R&D costs, (iv) each region itself preferring bilateral inactivity**.

## Source ledger

- Alston, Freebairn & James 2001, *Beggar-Thy-Neighbor Advertising*, AJAE, doi:10.1111/0002-9092.00217, https://digitalcommons.calpoly.edu/agb_fac/10/ .
- Zhang, Anzhou 2022, *Competition and the negative expected social value of cost-reducing innovation*, The Manchester School 90(1):59-76, doi:10.1111/manc.12388, https://onlinelibrary.wiley.com/doi/10.1111/manc.12388 . Full accessible HTML explicitly explains patent race, licensing fixed fee and sunk entry costs; **negative innovation social value is known, so do not claim the category novel**.
- Akino & Hayami 1975, *Efficiency and Equity in Public Research: Rice Breeding in Japan's Economic Development*, AJAE 57(1):1-10, doi:10.2307/1238834, https://academic.oup.com/ajae/article-abstract/57/1/1/94985 . Agricultural underinvestment backdrop only.
- Lence et al 2007, *Collective Marketing Arrangements for Geographically Differentiated Agricultural Products*, AJAE 89(4):947–963; earlier archived source-level working paper; group development not simultaneous public breeding.
