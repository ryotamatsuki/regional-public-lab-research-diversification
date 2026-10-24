# Stage 4A — Independent Mathematical Adversarial Certification

Date 2026-10-24. Canonical Stage 4A. User explicitly holds Stage 6 conditional for now. **Decision: GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS for precisely scoped L1/P1/C1/P2/P3+ existence statements**; do NOT equate this with Stage 7.5A GO, formal-verification PASS, economic novelty, or Stage 8 freeze. Review inputs were existing checkpoint 06/07/14/15 derivations, and archival exact global tests, so this is NOT an original-construction-blind reviewer; a distinct primary-utility-based symbolic reconstruction and pre-committed cost/demand falsification was performed. No claim of independent human peer review.

## Evidence and structure
Original four goods q=(1-a1,a1,1-a2,a2), V=alpha(x)'q-q'Bq/2, p=V_q, G_i=pi_i+CS/2-R*x_i²/2, W=G1+G2, x_i>=0, a_i in [0,1]. Nonlinear P2 is the documented separate *restricted* separable demand specification. Cross-market prices are equilibrium outcomes, not independent strategic actions.

Independent reproduction:
- Original quadratic examples: reran /mnt/data/public_breeding_three_propositions_verify.py in this session; seven symbolic identities and all three exact global one-sided Nash checks PASS at Delta=4/5,17/10,17/50. Original family code audit remains in checkpoints 04/07.
- Analytic P3+: reran /mnt/data/public_breeding_stage14/verify_wasteful_rd_open_set.py — PASS.
- Nonzero e=1/100 Nash: reran /mnt/data/public_breeding_stage14/verify_e_positive_global_nash.py — PASS, all 9 KKT regimes considered, nine objective global candidates, seven nonempty active-set research intervals; beyond x_i=5 derivative is negative. A strict unilateral optimum at x_i=9751/130096 given rival x_j=9751/130096; welfare loss -1933000423/211562115200; research cross derivative -50/39999.
- Independent ORIGINAL-PRIMITIVES checker /mnt/data/stage4a_75a_independent.py, exact SymPy, three preregistered alternatives executed. Source T2/T3 calculations start with 4 independent q variables, differentiate V to get p, reconstruct regional Pi and national CS, re-solve follower FOCs, and differentiate full objectives. Not only a substitution into the archived shortcut formula.

## Claim-by-claim theorem certificate

| Claim / proof | Exact quantified claim | Adversarial attack and result | Status, limitation |
|---|---|---|---|
| L1 adoption efficiency | FOR EVERY fixed R&D vector x, competitive adoption is unique global maximizer of W over a∈[0,1]^N, if V strictly concave in fixed-resource allocations, K convex, common genuine prices p=V_q | Direct compare farmer p_new-p_old-K' complementarity to planner derivative W_a and symmetric negative-definite Hessian; zero/full adoption corners obey matching KKT | PASS. Conditional on fixed x, NOT endogenized research efficiency |
| P1 local-national wedge | At ANY *symmetric interior* follower allocation with differentiable response in positive-definite linear B market and convex K, sign is governed by a_star-a; N>=2 original symmetry (see original Stage04) | Reconstruct price incidence from primitives; nonlinear grower-cost alternative (T3, see below), full KKT evaluated at quarter-adoption; value 7/151 exact | PASS. Does not automatically order Nash and planner |
| P1B/P1C symmetric equilibrium ranking and welfare loss | Under symmetric, globally verified local Nash and global interior planner in linear/quadratic two-region benchmark with R>1/min(M,L), xD-xP=xi*M(a_star-aP)/(RM-1+xi), and W_P-W_D=(R-1/M)*(xD-xP)^2 | Re-ran exact Nash deviation screen Delta .8 & 1.7, reconstructed welfare concavity and fixed-cost objective, gave exact welfare gap 10143/6697744 for both | PASS *for specified conditions*. No corner or arbitrary parameter global claim |
| C1 adoption gap | Under SAME symmetric interior restrictions, aD-aP=(xD-xP)/M | Subtract independently verified follower FOCs, test rational examples | PASS as algebraic Corollary, no separate causal failure |
| P2 nonlinear curvature | For equal old/new phi, separable convex price curvature and listed common beta/r/g terms, at symmetric interior wedge sign is H(1-a)-H(a), H(q)=q phi''(q) | Different phi_O/phi_N curvature T2 with true 4-good welfare reconstruction; at a=1/2 wedge exactly -1/16; prevents claiming symmetric half-share neutrality for arbitrary preferences | PASS WITH RESTRICTED SCOPE; neutral H is only *marginal interior*, no universal global welfare identity |
| P3 original Delta=.34 | Given exact original parameters, xD=389/6470, aD=141/6470 symmetric Nash and planner global (0,0); W_D<W0 | Exhaustive rational unilateral active sets re-run (10 candidates) and unreduced national W complete-square positive matrix eigenvalues 6/5,9/5 | PASS existence; unproven uniqueness of ALL potential asymmetric Nash |
| P3+ analytic interval | FOR ALL z∈(zc,0], zc=(-4+sqrt(13))/12, original e=j=0 family: unique global public-research pure Nash xD=(1+3z)/13>0 and aD=(1+16z)/26>0, unique joint planner zero, W_D-W0=(10z-1)(22z+3)/338<0 | Piecewise proof (zero-adoption, strict concave interior, saturated adoption) and exact planner square-completion over unrestricted x>=0 and a in [0,1]; lower endpoint indifference regression run | PASS within e=j=0, cannot say strictly strategic R&D substitutes in this analytic family |
| P3+ e>0 example | EXISTS symmetric Nash in original model with e=.01 and strictly negative effort cross-partial, national global optimum zero, W_D<W0 | Re-run full 9-state KKT deviation screen, direct-price local W and global planner bound, off-interior switching checked. | PASS for symmetric EXISTENCE ONLY; *no general all-asymmetric Nash uniqueness claim* |

## Explicit D1 deviations, D2 multiplicity, D3 indifference

- Farmer follower: strict concavity gives unique KKT equilibrium for every x, even at extreme x and saturation.
- P3+ within OPEN lower endpoint and closed upper z=0: region-specific best response independent of rival, globally unique positive optimum; thus *entire pure research Nash correspondence unique* for this slice. No selection or added dominance/tie-break.
- **NEW exact boundary falsifier**: at excluded z=zc the local positive stationary optimum x_c=sqrt(13)/52 has exactly the same local payoff as no research x=0. Those are **both global best responses**, for any rival, because e=j=0. Thus the complete 2-region game has exactly four pure Nash profiles at this endpoint: (0,0), (0,x_c), (x_c,0), (x_c,x_c). No unique-outcome or welfare-selection-free extension to z>=zc may include this endpoint. This is preserved in verify_p3_boundary_multiplicity.py.
- For e=.01 strict interacting instance, original P3+ e>0 **only claims existence of one globally verified symmetric Nash**. Alternative Nash outside it have NOT been excluded; any attempt to claim uniqueness or selection-free welfare would reopen Stage 4A. No tie-breaking imposed.
- At the zero-adoption branch x<=-z, derivative/payoff is not extrapolated from the interior F expression: it is -x² and makes zero research weakly best at the exact boundary. Saturated branch x>=2-z derivative =1-2x<0. For all stage 14 fixed-cost baseline cases x beyond 5 has derivative <0 and was not silently excluded by a numerical optimizer.
- Planner benchmark optimizes the full feasible product adoption and R&D set (x>=0, 0<=a<=1) under common welfare accounting; it is the *constrained relevant nationwide planner*, not a claim of unlimited entry, migration or dynamic adaptation.

## Original P3+ complete-square and best-response proof critical core

At e=j=0, demand/timing fixed as archived:
a_i(x_i)=clip((z+x_i)/2,0,1).
Relative local objective F_i(x_i)=a_i/4+3*a_i^2/4-x_i^2. For zero-adoption F=-x_i^2. For interior
F=(z+x_i)/8+3(z+x_i)^2/16-x_i^2,
F''=-13/8,
argmax xD=(1+3z)/13 and F(xD)=(48z²+32z+1)/208>0 iff z>zc within the chosen range. For a=1, F=1-x_i² and derivative 1-2x_i<0. Hence xD is unique global BR for z∈(zc,0].

Nationwide relative welfare is W-W0=z*sum a_i +sum x_i*a_i -sum a_i² -sum x_i². Completion of squares gives
W-W0= z*sum a_i -3/4 sum a_i² -sum (x_i-a_i/2)²<=0 for z<=0,
with equality only x=a=0. Social loss at Nash factors (10z-1)(22z+3)/338<0.

## Classification, independent implementation and future formal proof

- Mathematics: independent exact proof/symbolic confirmation in current *claimed* mathematical domains.
- Formalization: **APPLICABLE**, especially exact P3+ global best-response cases, planner inequality, z lower-bound, and excluded endpoint multiplicity. This preliminary decision is Stage4A acceptable; final Lean/other proof-assistant build is part of Stage7.5A, not certified here.
- Stage4A **GO** subject to the claim scopes above. This is not a mathematical proof of e>0 complete Nash-set uniqueness, welfare across all e>0 equilibria, arbitrary \phi demand signs, empirical quantitative R&D harm, or Stage6 novelty.
- If the declared claim scope broadens at manuscript drafting, Stage4A is no longer current and needs re-certification.

**Reviewer provenance:** Same AI assistant has seen old equations and code; the new code does not use original model solvers for T2/T3, and T1's new global proof is algebraic. The earlier independent exact deviation enumeration is RE-RUN, not independent human validation. No authentic author signoff falsely recorded.
