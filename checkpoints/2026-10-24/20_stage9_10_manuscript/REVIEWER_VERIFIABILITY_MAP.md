# Stage 10 — Reviewer Verifiability Map

1. Lemma 1: V(q;x) and prices p=∇_qV -> competitive planting KKT pN-pO=K'(a) -> planner's adoption derivative -> conditional global concavity. Lean Core.conditional_adoption_global certifies quadratic concavity+KKT implication; full generic model bridge is a manuscript argument, not Lean FULL CLAIM.

2. Proposition 1: B matrix and farmer linear system -> symmetric a=(z+x)/M, response to unilateral x -> price incidence and consumer-surplus allocation -> ξ(a★-a) wedge. Lean Core.p1_wedge_factorization, p1_effort_gap_from_focs certify algebra; original payoff bridge manuscript proof.

3. Corollary: planner xP and regional xD FOCs -> exact effort difference -> farmer a gap. Lean Core.adoption_gap_corollary. Conditions for global x comparisons must be explicit.

4. Proposition 2: restricted anonymous separable demand -> Jacobian (L I+2g 11ᵀ) -> own-vs-average adoption response -> curvature wedge. Lean Prop2N.p2_n_region_response and curvature_incidence certify conditional Jacobian algebra only; not arbitrary nonlinear demand.

5. Proposition 3+: four-good gross utility -> inverse prices -> full off-equilibrium local gain (z+x+1/4)a -5a²/4 -x² -> plant=clip((z+x)/2,0,1) -> piecewise BR and uniqueness -> national welfare square completion -> exact loss and cutoff. Lean PrimitivesBridge, Prop3Global, Uniqueness, Boundary. The full branch matters: saturated payoff is z+x-1-x², not interior-only formula.

6. Interacting e>0 examples: original four-good payoff -> exact farmer KKT -> 9 adoption regimes global BR (existing exact Python, NOT Lean) -> exact national bound (Lean ExactExamples). Do not claim all asymmetric Nash uniqueness.
