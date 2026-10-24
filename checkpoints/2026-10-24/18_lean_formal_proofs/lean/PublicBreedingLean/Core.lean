import Mathlib

/-!
# Public breeding: adoption optimality and research-incidence proof cores

These theorems certify stated algebra/optimization implications. They do NOT
claim Lean has derived the original four-good model from utility primitives.
The model-to-formal-statement bridge is audited separately.
-/

namespace PublicBreeding

noncomputable section

/-- The reduced conditional social objective for competitive old/new adoption. -/
def adoptionObjective (m₁ m₂ d e a₁ a₂ : ℝ) : ℝ :=
  m₁ * a₁ + m₂ * a₂ -
    (d / 2) * (a₁ ^ 2 + a₂ ^ 2) - e * a₁ * a₂

/-- A KKT sign condition implies the residual cannot increase profit by
moving to another feasible planting share. Includes zero and full adoption. -/
theorem kkt_direction (a b resid : ℝ)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 1)
    (hk : (a = 0 ∧ resid ≤ 0) ∨
          (0 < a ∧ a < 1 ∧ resid = 0) ∨
          (a = 1 ∧ 0 ≤ resid)) :
    resid * (b - a) ≤ 0 := by
  rcases hk with hzero | hmid | hone
  · rcases hzero with ⟨ha, hr⟩
    subst a
    simpa using (mul_nonpos_of_nonpos_of_nonneg hr hb0)
  · rcases hmid with ⟨_, _, hr⟩
    simp [hr]
  · rcases hone with ⟨ha, hr⟩
    subst a
    exact mul_nonpos_of_nonneg_of_nonpos hr (by linarith)

/-- Conditional farmer/social adoption lemma: once follower KKT residuals
are certified from actual market prices, they globally maximize the same
national allocation objective. The strict-concavity conditions are d±e>0.
This proof includes planting corners and asymmetric deviations. -/
theorem conditional_adoption_global
    (m₁ m₂ d e a₁ a₂ b₁ b₂ : ℝ)
    (hplus : 0 < d + e) (hminus : 0 < d - e)
    (hb₁0 : 0 ≤ b₁) (hb₁1 : b₁ ≤ 1)
    (hb₂0 : 0 ≤ b₂) (hb₂1 : b₂ ≤ 1)
    (hk₁ : (a₁ = 0 ∧ m₁ - d * a₁ - e * a₂ ≤ 0) ∨
            (0 < a₁ ∧ a₁ < 1 ∧ m₁ - d * a₁ - e * a₂ = 0) ∨
            (a₁ = 1 ∧ 0 ≤ m₁ - d * a₁ - e * a₂))
    (hk₂ : (a₂ = 0 ∧ m₂ - d * a₂ - e * a₁ ≤ 0) ∨
            (0 < a₂ ∧ a₂ < 1 ∧ m₂ - d * a₂ - e * a₁ = 0) ∨
            (a₂ = 1 ∧ 0 ≤ m₂ - d * a₂ - e * a₁)) :
    adoptionObjective m₁ m₂ d e b₁ b₂ ≤
      adoptionObjective m₁ m₂ d e a₁ a₂ := by
  have hdir₁ := kkt_direction a₁ b₁ (m₁ - d*a₁-e*a₂) hb₁0 hb₁1 hk₁
  have hdir₂ := kkt_direction a₂ b₂ (m₂ - d*a₂-e*a₁) hb₂0 hb₂1 hk₂
  have hsq₁ : 0 ≤ (d + e) * ((b₁-a₁)+(b₂-a₂))^2 :=
    mul_nonneg (le_of_lt hplus) (sq_nonneg _)
  have hsq₂ : 0 ≤ (d - e) * ((b₁-a₁)-(b₂-a₂))^2 :=
    mul_nonneg (le_of_lt hminus) (sq_nonneg _)
  have hq : 0 ≤ (d/2)*((b₁-a₁)^2+(b₂-a₂)^2) +
      e*(b₁-a₁)*(b₂-a₂) := by nlinarith [hsq₁, hsq₂]
  have hid :
      adoptionObjective m₁ m₂ d e b₁ b₂ -
        adoptionObjective m₁ m₂ d e a₁ a₂ =
        (m₁-d*a₁-e*a₂)*(b₁-a₁) +
        (m₂-d*a₂-e*a₁)*(b₂-a₂) -
        ((d/2)*((b₁-a₁)^2+(b₂-a₂)^2) +
        e*(b₁-a₁)*(b₂-a₂)) := by
    unfold adoptionObjective
    ring
  linarith

/-- The special a*=1/2 crossing follows from symmetry j=e/2. -/
theorem p1_half_share (h j e : ℝ)
    (hj : e = 2*j) (hJ : 2*h-e ≠ 0) :
    (h-j)/(2*h-e) = (1/2 : ℝ) := by
  rw [hj] at hJ ⊢
  apply (div_eq_iff hJ).2
  ring

/-- P1A: transform the direct regional/national welfare incidence into
the adoption-threshold formula. The economic incidence decomposition
is established outside this theorem from p=V_q and farmer KKT. -/
theorem p1_wedge_factorization
    (h j e k a : ℝ)
    (hJ : 2*h-e ≠ 0) (hL : k+2*h-e ≠ 0) :
    (h-j-(2*h-e)*a)/(2*(k+2*h-e)) =
      ((2*h-e)/(2*(k+2*h-e))) * ((h-j)/(2*h-e)-a) := by
  have hid : ((h-j)/(2*h-e))*(2*h-e)=h-j := by
    exact (eq_div_iff hJ).mp rfl
  have hnum :
      h-j-(2*h-e)*a =
        (2*h-e)*((h-j)/(2*h-e)-a) := by
    calc
      _ = ((h-j)/(2*h-e))*(2*h-e)-(2*h-e)*a := by rw [hid]
      _ = _ := by ring
  rw [hnum]
  ring

/-- P1B: the two symmetric research first-order conditions imply the
exact decentralized/planner research gap without presupposing its sign. -/
theorem p1_effort_gap_from_focs
    (R M ξ z xD xP aStar aP : ℝ)
    (hD : (R*M-1+ξ)*xD = (1-ξ)*z+ξ*M*aStar)
    (hP : (R*M-1)*xP = z)
    (haP : aP = R*xP) :
    (R*M-1+ξ)*(xD-xP) = ξ*M*(aStar-aP) := by
  subst aP
  linear_combination hD - (1-ξ)*hP

/-- Corollary: the adoption gap is the response of the competitive
farmer's symmetric planting share to the researcher effort gap. -/
theorem adoption_gap_corollary (z xD xP M : ℝ) (hM : M ≠ 0) :
    (z+xD)/M - (z+xP)/M = (xD-xP)/M := by
  ring

/-- P1C: completing the square on the symmetric planner objective.
The RHS is positive when R>1/M and xD≠xP. -/
theorem p1_welfare_gap
    (R M z xD xP : ℝ) (hM : M ≠ 0)
    (hP : (R*M-1)*xP = z) :
    ((z+xP)^2/M - R*xP^2) -
      ((z+xD)^2/M - R*xD^2) =
      (R-1/M)*(xD-xP)^2 := by
  have hfactor := congrArg (fun w : ℝ => w*(xD-xP)) hP
  field_simp
  nlinarith [hfactor]

/-- P2: symmetric/antisymmetric adoption response to a local quality shock.
This proves the Hessian-cancellation core for the *restricted*
separable-demand class; the equations hown/hother must be derived from
the economic price/planting model, rather than assumed as the result. -/
theorem p2_zero_sum_response (L g fp u v : ℝ)
    (hL : L ≠ 0)
    (hown : (L+2*g)*u+2*g*v = fp)
    (hother : 2*g*u+(L+2*g)*v = 0) :
    u-v = fp/L := by
  have h : L*(u-v) = fp := by
    linear_combination hown-hother
  apply (eq_div_iff hL).2
  nlinarith [h]

/-- The N=2 curvature wedge is driven by the difference of the
quantity-weighted old/new inverse-demand slopes. -/
theorem p2_curvature_wedge_two_regions
    (L g fp u v a oldCurv newCurv : ℝ)
    (hL : L ≠ 0)
    (hown : (L+2*g)*u+2*g*v = fp)
    (hother : 2*g*u+(L+2*g)*v = 0) :
    ((u-v)/2) * ((1-a)*oldCurv-a*newCurv) =
      fp/(2*L) * ((1-a)*oldCurv-a*newCurv) := by
  rw [p2_zero_sum_response L g fp u v hL hown hother]
  ring

/-- P2's half-share neutrality critically requires equal curvature. -/
theorem p2_half_share_neutral (curv : ℝ) :
    (1-(1/2:ℝ))*curv-(1/2:ℝ)*curv = 0 := by
  ring

/-- An explicit negative portability result: old/new curvature asymmetry
produces nonzero incidence even at 50% adoption. -/
theorem p2_asymmetric_curvature_counterexample :
    ((1/2:ℝ) * ((1-(1/2:ℝ))*1-(1/2:ℝ)*2))/4 = -1/16 := by
  norm_num

end
end PublicBreeding
