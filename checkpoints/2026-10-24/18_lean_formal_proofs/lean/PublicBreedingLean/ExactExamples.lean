import Mathlib

/-!
# Proposition 3: exact-rational original benchmark and interacting benchmark

Lean checks the original adoption FOCs, exact welfare differences, global
national zero-welfare upper bounds, and strict strategic-substitute sign.

The published Python 9-KKT-regime enumeration of GLOBAL REGIONAL best
responses for the e>0 examples is NOT yet formalized in Lean; it must not
be described as formally established merely because the rational
candidate arithmetic checks in this file.
-/

namespace PublicBreeding
noncomputable section

def twoRegionNationalDelta (z e x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  z*(a₁+a₂)+x₁*a₁+x₂*a₂ -
  (a₁^2+a₂^2)-e*a₁*a₂-(x₁^2+x₂^2)

/-- Negative investment-induced nationwide surplus with positive cross
planting response coefficient; the proof permits ALL feasible x,a. -/
theorem national_zero_with_nonnegative_cross
    (z e x₁ x₂ a₁ a₂ : ℝ)
    (hz : z ≤ 0) (he : 0 ≤ e)
    (ha₁ : 0 ≤ a₁) (ha₂ : 0 ≤ a₂) :
    twoRegionNationalDelta z e x₁ x₂ a₁ a₂ ≤ 0 := by
  have hz₁ : z*a₁ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₁
  have hz₂ : z*a₂ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₂
  have hea : 0 ≤ e*a₁*a₂ :=
    mul_nonneg (mul_nonneg he ha₁) ha₂
  have hs₁ := sq_nonneg (x₁-a₁/2)
  have hs₂ := sq_nonneg (x₂-a₂/2)
  have ha₁sq := sq_nonneg a₁
  have ha₂sq := sq_nonneg a₂
  unfold twoRegionNationalDelta
  nlinarith

def originalX : ℝ := (389:ℝ)/6470
def originalA : ℝ := (141:ℝ)/6470

/-- The exact original Delta=0.34 candidate satisfies both competitive
farmers' interior KKT first-order equations. -/
theorem original_farmer_foc :
    (2:ℝ)*originalA+(3/10:ℝ)*originalA =
      -(1/100:ℝ)+originalX := by
  norm_num [originalA, originalX]

/-- Exact welfare loss for the original, already Python-global-Nash-audited
candidate. This does not prove that it is a global regional best response. -/
theorem original_negative_welfare_exact :
    twoRegionNationalDelta (-(1/100:ℝ)) (3/10)
       originalX originalX originalA originalA =
       -(2569157:ℝ)/418609000 := by
  norm_num [twoRegionNationalDelta, originalX, originalA]

theorem original_planner_global_zero
    (x₁ x₂ a₁ a₂ : ℝ) (ha₁ : 0 ≤ a₁) (ha₂ : 0 ≤ a₂) :
    twoRegionNationalDelta (-(1/100:ℝ)) (3/10)
      x₁ x₂ a₁ a₂ ≤ 0 := by
  apply national_zero_with_nonnegative_cross
  · norm_num
  · norm_num
  · exact ha₁
  · exact ha₂

def interactingX : ℝ := (9751:ℝ)/130096
def interactingA : ℝ := (1051:ℝ)/32524

/-- The e=0.01 strategic-substitutes parameter profile satisfies the
symmetric farmer's exact interior allocation condition. -/
theorem interacting_farmer_foc :
    (2:ℝ)*interactingA+(1/100:ℝ)*interactingA =
      -(1/100:ℝ)+interactingX := by
  norm_num [interactingA, interactingX]

/-- The local second cross effect is negative for the published e=0.01
example; an interaction sign is NOT itself a whole-game Nash proof. -/
theorem interacting_strategic_substitutes :
    -((1/100:ℝ)/(2*(2^2-(1/100:ℝ)^2))) =
        -(50:ℝ)/39999 ∧ -(50:ℝ)/39999 < 0 := by
  constructor <;> norm_num

theorem interacting_negative_welfare_exact :
    twoRegionNationalDelta (-(1/100:ℝ)) (1/100)
       interactingX interactingX interactingA interactingA =
       -(1933000423:ℝ)/211562115200 := by
  norm_num [twoRegionNationalDelta, interactingX, interactingA]

theorem interacting_planner_global_zero
    (x₁ x₂ a₁ a₂ : ℝ) (ha₁ : 0 ≤ a₁) (ha₂ : 0 ≤ a₂) :
    twoRegionNationalDelta (-(1/100:ℝ)) (1/100)
      x₁ x₂ a₁ a₂ ≤ 0 := by
  apply national_zero_with_nonnegative_cross
  · norm_num
  · norm_num
  · exact ha₁
  · exact ha₂

end
end PublicBreeding
