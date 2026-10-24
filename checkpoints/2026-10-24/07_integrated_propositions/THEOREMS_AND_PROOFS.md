# Stage 07 — Three propositions from the solved equilibrium: minimal assumptions and short proofs

2026-10-24. **Status: mathematically verified within the explicit domains below; journal novelty remains a separate issue.** This checkpoint reuses Stage 04's nonlinear demand result and exact global unilateral deviation method and Stage 06's complete equilibrium. All earlier checkpoints remain unchanged.

## 0. Common primitives / equilibrium lemma (linear model)

Two regions, old/new fruit per region, national inverse demand p=alpha-Bq with alpha=(A,A+Delta+x1,A,A+Delta+x2), and symmetric 4x4 positive-definite demand matrix B with diagonal 1, within-region old/new t, across-region old/old b, old/new c, new/new n. Each region has unit land and competitive farmers; q_i=(1-a_i,a_i), K(a)=k0*a+kappa*a^2/2 and C(x)=R*x^2/2; local public breeder maximizes G_i=Pi_i+CS/2-C_i, national W=G1+G2. Here x_i>=0, 0<=a_i<=1, kappa>0, R>0, and direct own-new-variety quality shifts are additive.

Set h=1-t, j=b-c, e=b+n-2c, d=kappa+2h, M=d+e, L=d-e, D=d^2-e^2 and z=Delta+h+j-k0. Positive definiteness implies 2h>|e|, d>|e|, so M,L,D>0.

**Adoption** at an interior equilibrium:
\[
H a=z{\bf1}+x,\quad H=\begin{pmatrix}d&e\\e&d\end{pmatrix},\qquad
a_i={z\over M}+{d x_i-e x_j\over D}.
\]
At boundaries, maximize (z1+x)'a-a'Ha/2 over the unit square; do NOT extrapolate the interior solution.

**Market outcomes** at interior adoption:
\[
p_{iO}=A-1-b+h a_i+j a_j,\qquad
p_{iN}=A+\Delta+x_i-t-c-h a_i-(n-c)a_j,
\]
\[
\Pi_i=A-1-b+h a_i+j a_j+\kappa a_i^2/2,
\quad CS=1+b-(h+j)(a_1+a_2)+h(a_1^2+a_2^2)+e a_1a_2.
\]
The original definitions of Pi and CS, not the FOC-simplified formulas, must be used in boundary regimes.

**Envelope lemma**:
\[
W(x)=2A-1-b+\tfrac12(z{\bf1}+x)'H^{-1}(z{\bf1}+x)-\tfrac R2 x'x,\quad W_{x_i}=a_i-Rx_i.
\]
Provided \(R>1/\min(L,M)\), the planner's joint (a,x) objective is strictly concave and the constrained planner is unique. The symmetric *interior* planner is \(x^P=z/(RM-1),\ a^P=Rx^P\); only use if feasible.

Define \(J=2h-e>0,\ \xi=J/(2L)>0,\ a^*=(h-j)/J\).

## Proposition 1. Exactly when local effort is excessive versus insufficient

**(A: unilateral marginal wedge)** At an arbitrary symmetric interior state (x,a), with x1=x2=x and a1=a2=a,
\[
G_{i,x_i}-W_{x_i}={h-j-Ja\over2L}
=\xi(a^*-a).
\]
If a* is interior, the marginal wedge is positive when a<a*, zero at a=a*, and negative when a>a*. If b=n, then a*=1/2. Neither the 1/2 benchmark nor an interior threshold is universal.

**(B: actual symmetric equilibrium effort ranking)** Define the symmetric interior **candidate**
\[
x^D={ (1-\xi)z+M(h-j)/(2L)\over RM-1+\xi},
\qquad a^D={z+x^D\over M}.
\]
Assume (i) the candidate is feasible, (ii) it is a *global* best response against itself including all adoption-boundary deviations, (iii) the planner is interior, and (iv) \(R>1/\min(L,M)\). Then:
\[
\boxed{x^D-x^P={\xi M\over RM-1+\xi}(a^*-a^P).}
\]
All factors multiplying (a*-aP) are positive: **excess effort iff aP<a***, equality iff aP=a*, insufficient effort iff aP>a*. This is a direct ranking of equilibrium effort, not merely marginal incentives.

**(C: exact welfare cost)** With both outcomes on the same interior adoption branch,
\[
\boxed{W(x^P,x^P)-W(x^D,x^D)
=(R-1/M)(x^D-x^P)^2.}
\]
This is a full-coordination welfare comparison in the symmetric model, not a unilateral marginal wedge.

**Shortest proof:** The envelope lemma gives W_i'=a-Rx. Differentiating local payoff G_i=Pi_i+CS/2-Rx_i²/2 and substituting the linear adoption response gives, at a symmetric point, \(G_{i,x_i}=a-Rx+(h-j-Ja)/(2L)\). Subtract to prove (A). The Nash FOC gives \((RM-1+\xi)x^D=(1-\xi)z+M(h-j)/(2L)\). The planner FOC gives \((RM-1)x^P=z\) and aP=RxP. Subtracting and factoring gives (B). On the symmetric path, \(W(x,x)=2A-1-b+(z+x)^2/M-Rx^2\), a concave quadratic with vertex xP; completing the square gives (C). QED.

**Scope:** A holds at the symmetric interior point even if that point is not an equilibrium; B and C additionally need equilibrium / optimum feasibility and global unilateral-deviation checks. Never transfer B's sign to a boundary optimum by continuity without proof.

## Proposition 2. Demand-curvature reversal and zero wedge in a nonquadratic class

For **N>=2** symmetric producer regions and competitive conversion, consider a separate extension with twice differentiable (in q), strictly concave gross utility:
\[
V(q,x)=\sum_{i,s}\alpha_{is}(x_i)q_{is}-\sum_{i,s}\phi(q_{is})
-\frac{\beta}{2}Q^2-\frac r2\sum_i Q_i^2-\frac g2(Q_O^2+Q_N^2),
\]
where phi''(q)>0 on (0,1), beta,r,g>=0, one unit of land per region, own-new-variety quality shift f(x_i) with f'>0, convex K and the symmetric interior adoption equilibrium. All populations have equal CS shares 1/N. Define Hphi(q)=q phi''(q) and Lphi=K''(a)+phi''(1-a)+phi''(a)>0.

Then:
\[
\boxed{G_{i,x_i}-W_{x_i}
=f'(x)\frac{N-1}{N L_\phi}
\bigl[H_\phi(1-a)-H_\phi(a)\bigr].}
\]

**Four-line proof:** The adoption Jacobian is \(J_a=L_\phi I_N+2g{\bf1}{\bf1}'\), so \(a_{x_i}=f'J_a^{-1}{\bf e}_i\). By the producer-surplus and CS envelope identities, \(G_{i,x_i}-W_{x_i}=[H_\phi(1-a)-H_\phi(a)]\{a_{i,x_i}-N^{-1}\sum_j a_{j,x_i}\}\), since aggregate-Q and region-total terms cancel under unit land and the generation-common g term cancels in the CS incidence difference. The eigenvalue of J_a on the zero-sum adoption subspace is Lphi. Thus \(a_{i,x_i}-N^{-1}\sum_j a_{j,x_i}=f'(N-1)/(NL_\phi)\), proving the formula. QED.

If Hphi is strictly increasing, the wedge is + for a<1/2 and - for a>1/2. If Hphi is constant, the wedge is zero even with **endogenous** adoption. If decreasing, the signs reverse. For phi''(q)=delta q^(gamma-1) with delta>0, Hphi=delta q^gamma and gamma>0,=0,<0 realizes the three regimes.

**Critical limit:** This is an analytic extension to this demand family, NOT a sign theorem for arbitrary smooth demand, asymmetric regions or boundary adoption. The result concerns marginal incentives, not in general the ranking of two nonquadratic Nash/efficient equilibria.

## Proposition 3. Positive decentralized effort when the national optimum is zero

Use exact rational parameters
\[
A=10,\quad t=1/2,\ b=n=3/5,\ c=9/20,\ k_0=\kappa=1,\ R=2,\ \Delta=17/50.
\]
Then h=1/2, j=3/20, e=3/10, d=2, M=23/10, L=17/10, and z=-1/100.

**Local decentralized solution:**
\[
\boxed{x_1^D=x_2^D=389/6470>0,\quad a_1^D=a_2^D=141/6470>0.}
\]
A complete exact-rational unilateral-deviation verification (all 3^2 producer adoption active sets, switching points, quadratic vertices and upper tails) finds that against x_j=389/6470, the global best response is exactly x_i=389/6470. This is stronger than an interior FOC check.

**Planner:** The **unreduced** national welfare relative to zero effort and zero adoption is
\[
W-W_0=z{\bf1}'a+x'a-\tfrac12a'Ha-\tfrac R2x'x.
\]
Completing the square in x:
\[
W-W_0\le z{\bf1}'a-\tfrac12a'(H-R^{-1}I)a.
\]
The eigenvalues of H-R^-1 I are \(6/5,9/5\), both >0. Because z=-1/100<0 and a>=0, this upper bound is <=0, equality only at a=0 and x=0. Thus the **unique global planner optimum** is xP=aP=0.

**Exact welfare gap:**
\[
\boxed{W^P-W^D=2569157/418609000
=0.006137366850688829\ldots>0.}
\]
The benchmark welfare levels are WP=92/5=18.4 and WD=18.3938626331... . These are unitless theoretical magnitudes, not a calibration.

**Proof of global local optimality certificate:** On every feasible conversion-active-set interval, local G_i(x_i,x_j) is quadratic in x_i. The exact verification constructs all changes of KKT active set for x_i in [0,4] (from the 9 possible combinations), evaluates every interval endpoint and interior quadratic vertex, and selects the global maximum; x_i=389/6470 is exact. Beyond 4, the deviator has fully adopted its new variety, the rival's adoption is fixed, and its objective's effort derivative is \(1-2x_i<0\). Hence no larger deviation is profitable. The executable independent checker is supplied alongside the report; the existing Stage 04 checker reaches the same exact optimum. QED.

## Reproduction results / separation of epistemic statuses

SymPy tested 7 algebraic identities, all zero after simplification. Three independent exact-fraction global-Nash screens reproduced:

| Delta | xD | aD | xP | aP | Distinct global candidate count |
|---|---|---|---|---|---|
| 4/5 | 101/647 | 341/1294 | 1/8 | 1/4 | 7 |
| 17/10 | 445/1294 | 953/1294 | 3/8 | 3/4 | 6 |
| 17/50 | 389/6470 | 141/6470 | 0 | 0 | 10 |

For Delta=4/5 and 17/10, the welfare loss equals \(10143/6697744\); for 17/50 the loss is \(2569157/418609000\). The exact local Nash verification is **example-specific**; it does not make interior candidates globally Nash for every parameter. The Stage 04 nonlinear checker independently confirmed the restricted Proposition 2 for N=2,3,5 and several power curvatures via finite differences; the present report provides its short analytical proof.

## Paper architecture and assumptions

**Main text**: primitives / stage game -> competitive adoption equilibrium lemma -> local vs social wedge Proposition 1A -> equilibrium effort-ranking Proposition 1B and welfare cost Proposition 1C -> curvature mechanism Proposition 2 (short proof) -> concrete zero-effort counterexample Proposition 3 -> policy implications and literature comparisons.

**Appendix**: full 4x4 price system, region CS accounting, nonquadratic Jacobian inversion, exact rational active-set calculations, alternative N-region linear formulas. Do not make fixed-adoption counterfactual the paper's central research question.

**Must not overclaim**: nonlinear Proposition 2 is a **restricted class**, not arbitrary demand; derivative wedge and equilibrium ranking are different objects; equilibrium comparative statics need global deviation checks; the abstract envelope identity and signs of strategic substitute/complementarity are known tools and not thereby novel economics; the results do not establish real-world quantitative welfare loss or journal publication eligibility.

**Proof difficulty**: standard graduate microeconomics, matrix inversion, envelope theorem, implicit differentiation, quadratic concavity, and basic exact-rational optimization. No advanced fixed-point theorem is required for these claims.
