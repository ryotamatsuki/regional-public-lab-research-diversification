# Stage 06 — Two-region complete equilibrium

Date: 2026-10-24. The baseline remains the Stage 04 model; this document derives a complete **interior-branch** solution of the two-stage game, together with the planner solution. Boundary cases need separate KKT conditions. Numerical results use independent Python/SymPy calculations.

## Primitives

The goods are ordered (1O,1N,2O,2N). Inverse demand is p=alpha-Bq with alpha=(A,A+Delta+x1,A,A+Delta+x2), q=(1-a1,a1,1-a2,a2), and

\[
B=\begin{pmatrix}1&t&b&c\\t&1&c&n\\b&c&1&t\\c&n&t&1\end{pmatrix}.
\]

Gross utility is V=alpha'q-q'Bq/2; each region has adoption cost K_i=k0*a_i+kappa*a_i^2/2 and public R&D cost C_i=R*x_i^2/2. Local welfare G_i=Pi_i+CS/2-C_i, national welfare W=G1+G2. Define h=1-t, j=b-c, e=b+n-2c, d=kappa+2h, M=d+e, L=d-e, D=d^2-e^2, z=Delta+h+j-k0. Assume B positive definite, kappa>0, R>0, and a differentiable interior adoption equilibrium.

## Proposition 1. Competitive adoption, prices and surpluses

The interior farmer condition gives

\[
\begin{pmatrix}d&e\\e&d\end{pmatrix}\binom{a_1}{a_2}=\binom{z+x_1}{z+x_2},
\qquad a_i={z\over M}+{d x_i-e x_j\over D}.
\]

At any interior adoption equilibrium,

\[
p_{iO}=A-1-b+h a_i+j a_j,\quad
p_{iN}=A+\Delta+x_i-t-c-h a_i-(n-c)a_j.
\]

The adoption condition implies p_iN=p_iO+k0+kappa*a_i, hence regional net producer surplus is

\[
\Pi_i=A-1-b+h a_i+j a_j+{\kappa\over2}a_i^2.
\]

National CS and the reduced regional and aggregate objectives are

\[
CS=1+b-(h+j)(a_1+a_2)+h(a_1^2+a_2^2)+e a_1 a_2,
\]

\[
G_i=A-{1+b\over2}+{h-j\over2}(a_i-a_j)
+{\kappa+h\over2}a_i^2+{h\over2}a_j^2
+{e\over2}a_i a_j-{R\over2}x_i^2,
\]

\[
W=2A-1-b+{d\over2}(a_1^2+a_2^2)+e a_1a_2-{R\over2}(x_1^2+x_2^2).
\]

These expressions were checked symbolically, including G1+G2=W. Importantly, **the simplified Pi, G, W that use the farmers' FOC cannot be used as off-equilibrium fixed-adoption formulas.**

## Proposition 2. Research reaction functions and Nash

Define

\[
\eta={1\over2L}\left({(2\kappa+2h-e)z\over M}+h-j\right).
\]

Along the adoption equilibrium,

\[
{\partial G_i\over\partial x_i}
=\eta-\left(R-{\kappa+h\over D}\right)x_i-{e\over2D}x_j.
\]

For R>(kappa+h)/D, the interior candidate best response is

\[
BR_i(x_j)={\eta-e x_j/(2D)\over R-(\kappa+h)/D}.
\]

The mixed research derivative is -e/(2D); e>0 means strategic substitutes, e<0 complements, and e=0 independent marginal reactions **within the interior branch**.

Define \(\xi=(2h-e)/(2L)\). The symmetric solution is

\[
x_D={ (1-\xi)z+ M(h-j)/(2L)\over RM-1+\xi},\qquad
a_D={z+x_D\over M}.
\]

It is a genuine Nash equilibrium only if x_D>=0, 0<a_D<1 and every unilateral deviation (including those inducing corner adoption) is no better. General parameter values may yield piecewise solutions. The archived Stage 04 script checks all adoption regimes exactly for the three numerical examples.

## Proposition 3. Social planner

**Before** substituting the farmers' FOC, planner welfare is

\[
W=2A-1-b+z(a_1+a_2)+x_1a_1+x_2a_2
-{1\over2}a'Ha-{R\over2}x'x,\quad
H=\begin{pmatrix}d&e\\e&d\end{pmatrix}.
\]

Farmers' competitive adoption is welfare-maximizing conditional on research x, so planner effort has envelope derivative \(\partial W/\partial x_i=a_i-Rx_i\). In the symmetric interior planner solution:

\[
x_P={z\over RM-1},\qquad a_P=R x_P.
\]

If RH-I is positive definite, joint welfare is strictly concave in (a,x), and constrained KKT conditions certify the global planner solution including zero-effort boundaries.

At any symmetric interior configuration, all requested levels simplify to

\[
p_O=A-1-b+(h+j)a,\quad p_N=p_O+k_0+\kappa a,
\]
\[
\Pi=A-1-b+(h+j)a+\kappa a^2/2,
\quad CS=1+b-2(h+j)a+(2h+e)a^2,
\]
\[
G=A-(1+b)/2+Ma^2/2-Rx^2/2,\quad
W=2A-1-b+Ma^2-Rx^2.
\]

## Numerical equilibrium table (Python verified)

Parameters: A=10, t=0.5, b=n=0.6, c=0.45, k0=kappa=1, R=2. Thus h=0.5, j=0.15, e=0.3, d=2, M=2.3, L=1.7, D=3.91. Eigenvalues of B are (0.35,0.45,0.65,2.55); eigenvalues of RH-I are (2.4,3.6). The closed-form interior effort best response and symmetric Nash are

\[
BR_i(x_j)={135\Delta-7-15x_j\over632},\quad
x_D={135\Delta-7\over647},\quad a_D={680\Delta-203\over1294}.
\]

Mixed derivative = -15/391; best-response slope = -15/632. Interior planner levels are \(x_P=(20\Delta-7)/72,\ a_P=(20\Delta-7)/36\), but **only within the feasible interior region**.

| Delta | Outcome | x | a | pO | pN | Pi per region | CS national | G per region | W national |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.80 | Nash | 0.156105 | 0.263524 | 8.571291 | 9.834815 | 8.606013 | 1.347697 | 9.255493 | 18.510986 |
| 0.80 | Planner | 0.125000 | 0.250000 | 8.562500 | 9.812500 | 8.593750 | 1.356250 | 9.256250 | 18.512500 |
| 1.70 | Nash | 0.343895 | 0.736476 | 8.878709 | 10.615185 | 9.149908 | 1.347697 | 9.705493 | 19.410986 |
| 1.70 | Planner | 0.375000 | 0.750000 | 8.887500 | 10.637500 | 9.168750 | 1.356250 | 9.706250 | 19.412500 |
| 0.34 | Nash | 0.060124 | 0.021793 | 8.414165 | 9.435958 | 8.414403 | 1.572287 | 9.196931 | 18.393863 |
| 0.34 | Planner boundary | 0 | 0 | 8.400000 | 9.390000* | 8.400000 | 1.600000 | 9.200000 | 18.400000 |

*At a=0 the counterfactual new-variety inverse demand price is NOT a transacted price.*

The welfare loss in Delta=0.34 is 0.006137367 (0.0334% of W0=18.4), a unitless theoretical illustration, **not** empirical calibration.

## All-parameter boundaries

For any x, the farmer equilibrium is the unique solution of max over 0<=a<=1 of (z+x)'a - (1/2)a'Ha. Let residual r_i=z+x_i-(Ha)_i. KKT: if 0<a_i<1, r_i=0; if a_i=0, r_i<=0; if a_i=1, r_i>=0. For corner regimes, evaluate payoffs using the ORIGINAL p, Pi and CS, then solve each local government's piecewise global best response (interior stationary points, boundaries and switching thresholds). Thus the boxed formulas are a **complete symbolic description of the interior stage-game** and explicit test rules for boundaries, not a single closed form for all conceivable parameter combinations.

## Verification and publication caveats

SymPy independently verified the full regional objective FOC, mixed derivative, aggregate welfare identity and welfare envelope. Python's original 4-good market implementation independently reproduced all table entries, checked planner's global concavity, and screened unilateral research deviations, corroborating Stage 04's archived exact-rational example-specific global Nash checks. Strategic substitute/complementarity itself is established R&D theory, not an independently novel IJIO-level proposition.
