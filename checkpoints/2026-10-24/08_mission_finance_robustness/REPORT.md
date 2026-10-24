# Stage 08 — Does research-incentive reversal survive alternative public-breeding missions and finance?

2026-10-24. This memo extends the *same* two-region linear-demand game of Stage 04/06/07. **Finding: conditional robustness, not invariance.** Do not edit or replace the archived original propositions.

## 0. Institutional motivation

Breeding finance need not come solely from subnational taxes: UC Davis reports that its public strawberry breeding program receives most funding via licensing varieties [1]; Washington State University reports distribution of vegetatively propagated plant royalties among breeders, its college research office and university innovation office [2]. These are *institutional motivation*, not evidence for numerical parameters below. A historical California State Auditor investigation documents the licensing and funding flow [3]. UC Davis has explicitly stated its mission is not royalty-revenue maximization [4].

[1] https://www.ucdavis.edu/news/uc-davis-ends-strawberry-licensing-agreements-eurosemillas (2024).
[2] https://news.wsu.edu/news/2025/11/19/wsu-royalty-revenues-eclipse-19m-in-fy25/ (2025).
[3] https://information.auditor.ca.gov/reports/summary/2014-121 (2015).
[4] https://www.ucdavis.edu/news/state-audit-recommends-adjustments-uc-davis-strawberry-program (2015).

## 1. Existing linear game and objective generalization

Each region has quantities (1-a_i,a_i) and public research x_i>=0; competitive adoption a_i(x_i,x_j) follows the Stage 06 2x2 system. Set

h=1-t, j=b-c, e=b+n-2c, d=kappa+2h, M=d+e, L=d-e, D=d²-e², z=Delta+h+j-k0.

Assume B positive definite, adoption and research are interior where differentiated, R>0 and kappa>0. Original public objective G_i=Pi_i+CS/2-R*x_i²/2 and national W=Pi_1+Pi_2+CS-R*(x_1²+x_2²)/2. Extend public **behavioral** objective to

Gtilde_i = lambda*Pi_i + omega*CS - tau*R*x_i²/2,

where lambda is the policy weight on local producer surplus, omega the weight on total consumer surplus, tau the **effective marginal local financing incidence**, distinct from automatically taking one minus a nominal national grant fraction. These altered weights need not sum to measured local welfare; this is intentional and is not a Pareto welfare measure.

The farmers' adoption and actual W continue to include the full physical research costs.

## 2. Proposition A — Exact generalization of the marginal research wedge

On the symmetric interior branch, a=(z+x)/M. The unilateral (opponent x_j fixed) derivatives are

Pi_i' = [d*(h+kappa*a)-j*e]/D,
CS_i' = [-(h+j)+(2h+e)*a]/M,
W_i'=a-R*x.

Consequently,

Gtilde_i'-W_i'
 = xi*(a_star-a)
 + (lambda-1)*Pi_i'
 + (omega-1/2)*CS_i'
 + (1-tau)*R*x,

where xi=(2h-e)/(2L)>0 and a_star=(h-j)/(2h-e).

Define

C0 = lambda*(h*d-j*e)/D - omega*(h+j)/M,
C1 = lambda*kappa*d/D + omega*(2h+e)/M,
T = tau*R - C1/M.

The symmetric-stage-1 research FOC is

Gtilde_i'(x,x)=C0+C1*(z+x)/M-tau*R*x,

and the candidate symmetric Nash is x_D=(C0+C1*z/M)/T, a_D=(z+x_D)/M.

The social planner remains x_P=z/(R*M-1), a_P=R*x_P for an **interior** feasible optimum. Exact subtraction yields

x_D-x_P = [C0+(C1-tau)*a_P]/T.

For T>0 and a genuine interior symmetric Nash (including global unilateral optimality against corner-adoption deviations), **the sign of decentralized over/under-investment is precisely the sign of this numerator**. If C0>0 and tau>C1 with 0<C0/(tau-C1)<1, there is a unique interior reversal threshold

a_crit = C0/(tau-C1).

For a_P<a_crit local research is excessive; for a_P>a_crit insufficient. If these conditions fail, a threshold may lie outside the feasible interval, be absent, or the direction may change in other ways. The derivation and proof depend only on existing Stage 06 price and surplus identities and solving a linear FOC. T>0 alone is NOT a sufficient all-parameter global Nash certificate.

## 3. Proposition B — Finance incidence

For lambda=1, omega=1/2, write s=1-tau. The wedge is

Gtilde_i'-W_i' = xi*(a_star-a) + s*R*x.

Evaluating at the planner (whose optimal x is unchanged by **pure financing transfers**, assuming funding itself creates no resource costs or tax distortions) yields

sign(x_D-x_P) = sign[xi*(a_star-a_P)+s*a_P],

subject to the equilibrium conditions above.

For the original b=n benchmark a_star=1/2 and xi=7/34. When 0<=s<xi/2=7/68 (~0.10294), the threshold across feasible 0<a_P<1 is

a_crit = xi/(2*(xi-s)).

At s=.05, a_crit=35/53≈.660377 and the two checked cases with a_P=.25 and .75 remain respectively over/under. At s=.10, a_crit=595/612≈.972222, so both checked cases overinvest. At s>=xi/2, **no high-adoption underinvestment occurs within 0<=a_P<=1** under this benchmark, although feasible interior conditions must still be checked.

A nominal national subsidy s_nom financed by equal taxes on the two regions is NOT the same as effective subsidy s: regional i bears (1-s_nom)C_i + (s_nom/2)(C_i+C_j), so the marginal local incidence is tau=1-s_nom/2, not 1-s_nom. This is a two-region balanced-budget illustration, not a calibrated fiscal institution.

Purely internal within-region lump-sum financing does NOT change any choice: if local farmers pay lump-sum L_i(x_i) to the public research institution and the regional government pays C_i-L_i, aggregate regional G_i=(Pi_i-L_i)+CS/2-(C_i-L_i)=Pi_i+CS/2-C_i, provided the payment does not change planting decisions.

## 4. Proposition C — Objective weighting

With unchanged finance lambda=tau=1 and symmetric same-variety substitution b=n (hence e=2j), an arbitrary consumer-surplus weight omega gives

Gtilde_i'-W_i' =
 [xi - 2*(omega-1/2)*(h+j)/M] * (1/2-a).

Thus **the 50% threshold is exactly robust to omega**, provided the coefficient remains positive. It is positive for omega<=1/2 under positive definiteness and h+j>0, and can remain positive for moderate omega>1/2. Extreme consumer overweighting can eliminate or reverse the directional comparison.

With producer weight lambda≠1 the additional term (lambda-1)*Pi_i' generally does not vanish at a=1/2. The threshold shifts or disappears. For the rational benchmark and omega=1/2,tau=1: lambda=.8 gives threshold a_crit≈.17552; lambda=1.2 gives a_crit≈1.46543 (thus no within-[0,1] reversal). This is a genuine limitation of the unconditional 50% assertion.

## 5. Proposition D — Exogenous per-adoption royalty paid to the local public breeder

Let ell>=0 be a fixed, exogenously set license fee per unit of **new-variety area**, paid by local farmers and received by their public research institute. Hold the fee constant while research is chosen. Competitive adoption becomes

H a = (z-ell)*1 + x,    H=[[d,e],[e,d]].

Farmer net profit is Pi_i^farm=Pi_i^gross-ell*a_i. Regional welfare counts public royalty income +ell*a_i, so there is no fake resource benefit: G_i=Pi_i^farm+ell*a_i+CS/2-C_i=Pi_i^gross+CS/2-C_i. True W likewise cancels the royalty payment and receipt.

Crucially, under royalty-distorted competitive adoption, the planner envelope is **not** the no-royalty expression: instead

W_i'=a_i + ell/M - R*x_i

for symmetric fees and interior adoption. In the two-region model,

G_i'-W_i'=xi*(a_star-a)+ell*e/D.

Thus a fixed fee shifts the incentive threshold to

a_star_fee=a_star + ell*e/(D*xi),

provided xi>0. The constrained social planner, which chooses **research x but not the fee or farmers' adoption**, still has x_P=z/(R*M-1) in a symmetric interior equilibrium: fee reduces induced a, while the residual adoption distortion adds ell/M in the planner's research derivative.

At ell=.1 the benchmark threshold moves from .5 to about .537267, and the two tested cases remain respectively excessive and insufficient R&D. If the institution chooses ell endogenously, or if license receipts are not attributed to the same regional welfare unit, these results do NOT automatically hold. A planner that can eliminate the royalty distortion is also a different benchmark.

## 6. Independent exact proof and equilibrium audit

Local independent Python/SymPy audit completed **11 symbolic identities**: general local FOC, planner envelope, baseline wedge, decomposition, local Pi and CS derivative, research ranking via compact rational variables, exact symmetric-omega midpoint, royalty-modified planner envelope, royalty wedge, royalty constrained-planner effort.

Exact Fraction arithmetic then exhaustively enumerated 9 possible competitive-farmer adoption active sets, all regime switching thresholds in unilateral x_i, and all stationary points and boundaries of each resulting quadratic local payoff, proving global best-response optimality for **16 scenario-point pairs** (8 institutional configurations at Delta=.8 and Delta=1.7). Beyond x_i=5, adoption is saturated and payoff declines strictly, certifying that no large one-sided deviation was omitted.

Parameters A=10, t=.5, b=n=.6, c=.45, k0=kappa=1, R=2. All units theoretical, not empirically calibrated.

| Local institution | xD at Delta=.8 (xP=.125) | xD at Delta=1.7 (xP=.375) | Outcome |
|---|---:|---:|---|
| Original | .156105 | .343895 | over / under |
| tau=.95 | .166146 | .366014 | over / under |
| tau=.90 | .177567 | .391174 | over / over |
| omega=.25 | .175576 | .324424 | over / under |
| omega=.75 | .135133 | .364867 | over / under |
| lambda=.8 | .111491 | .270807 | under / under |
| lambda=1.2 | .203183 | .421021 | over / over |
| fee ell=.1 | .166151 | .353941 | over / under |

Research-cost incidence and political weights alter government incentives even when the underlying farmer product market and public-breeding technology are unchanged. Pure internal accounting transfers do not. Fee funding changes equilibrium planting decisions and must be handled separately.

## 7. Research and journal implications / explicit limits

**Proposition 1 is locally structurally robust** to small perturbations in the institutional parameters at parameter points where research and adoption equilibria are unique, interior, and strict, because objective derivatives and equilibria vary continuously. The **exact 50% crossover is NOT generally robust** to differentiated producer weights, effective cost shares, or adoption-proportional royalties. The specific nonlinear-demand vanishing-wedge condition from Stage 07 is also not guaranteed when objectives or financing depart from the original; do not silently claim Proposition 2 extends to every altered institutional environment.

For the paper, retain the simple public-regional-welfare baseline. A one-page robustness section with exact C0,C1,T and a tiny appendix table will be more transparent than replacing the game by public/private mixed R&D oligopoly. This is an analytical contribution **candidate**, not an independent journal-novelty finding: literature absorption must still be audited.

The exact independent script and full JSON results were saved during this same research session under /mnt/data/verify_public_breeding_funding_mission.py and /mnt/data/public_breeding_funding_mission_results.json; this Markdown report records verified results, but those runtime files are **not automatically committed to GitHub**. Replication code should be uploaded separately before a release-ready paper is claimed.
