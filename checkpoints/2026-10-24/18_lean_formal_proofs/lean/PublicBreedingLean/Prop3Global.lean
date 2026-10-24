import Mathlib
import PublicBreedingLean.Core

/-!
# Proposition 3+: exact global optimality over ALL planting regimes

Unlike an FOC-only checker, this module defines competitive adoption as a
piecewise response and bounds local gains on all three research intervals.
It proves the nationwide welfare inequality on the LARGER jointly feasible
(x,a) set, without assuming adoption is at its equilibrium level.

Its interpretation as an agricultural market comes from the separate
source-model-to-Lean statement audit.
-/

namespace PublicBreeding
noncomputable section

def zCut : ℝ := (-4 + Real.sqrt 13) / 12
def localEffort (z : ℝ) : ℝ := (1+3*z)/13
def localAdoption (z : ℝ) : ℝ := (1+16*z)/26

/-- The 3-part KKT solution for growers' old/new planting share in P3+. -/
def plant (z x : ℝ) : ℝ :=
  if x ≤ -z then 0
  else if 2-z ≤ x then 1
  else (z+x)/2

/-- Regional payoff relative to the zero-research/zero-adoption baseline.
This definition must be independently matched to V, p, CS, and K. -/
def regionalGain (z x : ℝ) : ℝ :=
  let a := plant z x
  (z+x+1/4)*a - 5*a^2/4 - x^2

/-- The formula on the interior planting branch ONLY. -/
def middleGain (z x : ℝ) : ℝ :=
  (z+x)/8 + 3*(z+x)^2/16 - x^2

private theorem sqrt13_squared : (Real.sqrt (13:ℝ))^2 = 13 :=
  Real.sq_sqrt (by norm_num)

private theorem sqrt13_nonneg : (0:ℝ) ≤ Real.sqrt 13 :=
  Real.sqrt_nonneg _

theorem zCut_root : 48*zCut^2+32*zCut+1 = 0 := by
  unfold zCut
  nlinarith [sqrt13_squared]

theorem zCut_above_neg_sixteenth : -(1/16:ℝ) < zCut := by
  unfold zCut
  nlinarith [sqrt13_squared, sqrt13_nonneg]

theorem zCut_nonpos : zCut ≤ 0 := by
  unfold zCut
  nlinarith [sqrt13_squared, sqrt13_nonneg]

theorem optimum_admissible
    (z : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) :
    0 < localEffort z ∧
      0 < localAdoption z ∧ localAdoption z < 1 ∧
      -z < localEffort z ∧ localEffort z < 2-z := by
  have hcut := zCut_above_neg_sixteenth
  unfold localEffort localAdoption
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  · linarith

theorem plant_lower (z x : ℝ) (h : x ≤ -z) :
    plant z x = 0 := by
  simp [plant, h]

theorem plant_middle (z x : ℝ)
    (hlo : -z < x) (hhi : x < 2-z) :
    plant z x = (z+x)/2 := by
  simp [plant, not_le.mpr hlo, not_le.mpr hhi]

theorem plant_upper (z x : ℝ)
    (hlo : -z < x) (hhi : 2-z ≤ x) :
    plant z x = 1 := by
  simp [plant, not_le.mpr hlo, hhi]

theorem plant_at_local_effort
    (z : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) :
    plant z (localEffort z) = localAdoption z := by
  obtain ⟨_, _, _, hlo, hhi⟩ := optimum_admissible z hz hz0
  rw [plant_middle z (localEffort z) hlo hhi]
  unfold localEffort localAdoption
  ring

theorem gain_middle (z x : ℝ)
    (hlo : -z < x) (hhi : x < 2-z) :
    regionalGain z x = middleGain z x := by
  simp [regionalGain, plant_middle z x hlo hhi, middleGain]
  ring

/-- Quadratic optimality identity: an exact proof, not a numeric search. -/
theorem middle_quadratic_gap (z x : ℝ) :
    middleGain z (localEffort z) - middleGain z x =
      (13/16:ℝ)*(x-localEffort z)^2 := by
  unfold middleGain localEffort
  ring

theorem middle_global_max (z x : ℝ) :
    middleGain z x ≤ middleGain z (localEffort z) := by
  have hs := sq_nonneg (x-localEffort z)
  have hid := middle_quadratic_gap z x
  nlinarith

theorem middle_gain_at_optimum (z : ℝ) :
    middleGain z (localEffort z) = (48*z^2+32*z+1)/208 := by
  unfold middleGain localEffort
  ring

/-- Strict positivity on the OPEN lower interval: equality at zCut fails. -/
theorem positive_stationary_gain
    (z : ℝ) (hz : zCut < z) :
    0 < (48*z^2+32*z+1)/208 := by
  have hroot := zCut_root
  have hcut := zCut_above_neg_sixteenth
  have hfirst : 0 < z-zCut := by linarith
  have hsecond : 0 < 48*(z+zCut)+32 := by linarith
  have hmul := mul_pos hfirst hsecond
  have hfact : 48*z^2+32*z+1 =
      (z-zCut)*(48*(z+zCut)+32) := by
    nlinarith [hroot]
  nlinarith [hmul]

theorem positive_local_gain_at_optimum
    (z : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) :
    0 < regionalGain z (localEffort z) := by
  obtain ⟨_, _, _, hlo, hhi⟩ := optimum_admissible z hz hz0
  rw [gain_middle z (localEffort z) hlo hhi]
  rw [middle_gain_at_optimum]
  exact positive_stationary_gain z hz

/-- Global first-stage local BR: the lower, interior and saturated
competitive adoption regimes are all included. -/
theorem local_global_best_response
    (z x : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) (hx : 0 ≤ x) :
    regionalGain z x ≤ regionalGain z (localEffort z) := by
  obtain ⟨_, _, _, hoptlo, hopthi⟩ := optimum_admissible z hz hz0
  have hopt :
      regionalGain z (localEffort z) =
        middleGain z (localEffort z) :=
    gain_middle z (localEffort z) hoptlo hopthi
  by_cases hlow : x ≤ -z
  · have hg : regionalGain z x = -x^2 := by
      simp [regionalGain, plant_lower z x hlow]
    have hpos := positive_local_gain_at_optimum z hz hz0
    nlinarith [sq_nonneg x]
  · have hlo : -z < x := lt_of_not_ge hlow
    by_cases hhigh : 2-z ≤ x
    · have hg : regionalGain z x = z+x-1-x^2 := by
        simp [regionalGain, plant_upper z x hlo hhigh]
        ring
      have hsum : 0 ≤ x + (2-z) - 1 := by linarith
      have hs : 0 ≤ (x-(2-z)) * (x+(2-z)-1) :=
        mul_nonneg (sub_nonneg.mpr hhigh) hsum
      have hedge : middleGain z (2-z) = 1-(2-z)^2 := by
        unfold middleGain
        ring
      have hmid := middle_global_max z (2-z)
      rw [hg, hopt]
      nlinarith
    · have hhi : x < 2-z := lt_of_not_ge hhigh
      rw [gain_middle z x hlo hhi, hopt]
      exact middle_global_max z x

/-- National *unreduced* welfare minus the zero-research allocation.
Strategies and planting shares are free and need not be equilibrium levels. -/
def nationalGain (z x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  z*(a₁+a₂) + x₁*a₁ + x₂*a₂ -
    a₁^2-a₂^2-x₁^2-x₂^2

theorem national_square_identity
    (z x₁ x₂ a₁ a₂ : ℝ) :
    nationalGain z x₁ x₂ a₁ a₂ =
    z*(a₁+a₂) -
      (3/4:ℝ)*(a₁^2+a₂^2) -
      (x₁-a₁/2)^2-(x₂-a₂/2)^2 := by
  unfold nationalGain
  ring

/-- Nationwide planner zero: valid for all feasible R&D and planting
levels, including asymmetric efforts, corners and off-equilibrium planting. -/
theorem national_global_zero
    (z x₁ x₂ a₁ a₂ : ℝ)
    (hz : z ≤ 0)
    (hx₁ : 0 ≤ x₁) (hx₂ : 0 ≤ x₂)
    (ha₁ : 0 ≤ a₁) (ha₂ : 0 ≤ a₂)
    (ha₁max : a₁ ≤ 1) (ha₂max : a₂ ≤ 1) :
    nationalGain z x₁ x₂ a₁ a₂ ≤ 0 := by
  have hneg₁ : z*a₁ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₁
  have hneg₂ : z*a₂ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₂
  rw [national_square_identity]
  nlinarith [sq_nonneg a₁, sq_nonneg a₂,
             sq_nonneg (x₁-a₁/2), sq_nonneg (x₂-a₂/2)]

theorem national_at_zero (z : ℝ) :
    nationalGain z 0 0 0 0 = 0 := by
  norm_num [nationalGain]

theorem national_at_symmetric_local
    (z : ℝ) :
    nationalGain z (localEffort z) (localEffort z)
      (localAdoption z) (localAdoption z) =
      ((10*z-1)*(22*z+3))/338 := by
  unfold nationalGain localEffort localAdoption
  ring

theorem national_at_local_strictly_negative
    (z : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) :
    nationalGain z (localEffort z) (localEffort z)
      (localAdoption z) (localAdoption z) < 0 := by
  rw [national_at_symmetric_local]
  have hcut := zCut_above_neg_sixteenth
  have hneg : 10*z-1 < 0 := by linarith
  have hpos : 0 < 22*z+3 := by linarith
  have hproduct := mul_neg_of_neg_of_pos hneg hpos
  nlinarith

end
end PublicBreeding
