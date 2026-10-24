# Stage 10 Reviewer-verifiability map

FULL reviewer-verifiability audit required for all proofs. Academic ref can reconstruct chain from paper without executing the Lean project.

| Result | Primitive-to-theorem bridge in manuscript | Certified computation, if any | Quantifier / boundary |
| --- | --- | --- | --- |
| Lemma (conditional efficiency) | Eq utility -> inverse prices -> farmer KKT with 0/1 adoption corners -> same conditional W_a and strict concavity | Core.lean restricted KKT | All fixed x under strict concavity; NOT global ex-ante funding efficiency |
| P1 | Four prices and aggregate CS explicitly reduced under *interior* grower FOC -> inverse H response -> planner envelope -> xi(aStar-a) | Core.lean algebra; Stage9 independent four-good SymPy | Symmetric *interior* two-region state; sign reverses only if aStar in (0,1) |
| Corollary and symmetric welfare difference | Conditional global and interior xD,xP -> FOC subtraction -> aD-aP and completed square | Core.lean and Stage 9 independent identities | Only if both are feasible, globally certified symmetric interior solutions |
| P2 | Eq restricted N-region gross utility -> Appendix market prices and D_i -> rank-one Jacobian inverse/projection -> induced weighted price incidence -> H_phi old/new sign | Prop2N.lean verifies conditional Jacobian algebra; Stage9 N=3 primitive exact 2/9 case | N≥2 symmetric interior, *same phi* on old/new; unequal-curvature half-neutral counterexample -1/16 outside theorem |
| P3+ | Four-good B -> unreduced offpath local research F_i(x,a) -> three planting branches -> globally unique BR -> full x,a national W square completion -> unique planner zero and strict loss | PrimitivesBridge, Prop3Global, Uniqueness, Boundary in Lean; independent SymPy Stage 9 | Every z in (zc,0], e=j=0; z=zc exactly four Nash; no generic research BR coupling |
| e>0 coupled case | Gross utility -> 9 grower KKT regimes -> exact-rational candidate global unilateral BR -> negative W | Stage 9 exact SymPy 9 candidates/7 active ranges; Lean ExactExamples only candidate/planner algebra | Supports named e=1/100 example, no all-asymmetric Nash uniqueness or generic e>0 theorem |

**Proof artifact boundary:** Lean 4.35.0/mathlib v4.35.0 verified only proof-critical mathematical statements; the complete economic P1 primitive derivation and nonlinear P2 primitive-Jacobian incidence reside in manuscript equations and independent SymPy test. Nonzero e global BR is SymPy, not Lean. No peer-review certification asserted.

**Equilibrium/counterfactual safeguards:** zCut endpoint excluded from uniqueness; xP conditional interior formula not used for negative z; symmetric planner globality relies on original exact model only; complete-adoption F=z+x-1-x², not interior extrapolation.
