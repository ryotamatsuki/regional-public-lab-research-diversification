import Mathlib
import PublicBreedingLean.Prop3Global

/-!
# Strict uniqueness of both outcomes in Proposition 3+

These results upgrade the previously kernel-checked global upper bounds to
UNIQUENESS, without changing the economic primitives.
-/

namespace PublicBreeding
noncomputable section

/-- The positive best response is unique on the open cutoff interval. -/
theorem p3_unique_global_best_response
    (z x : ℝ) (hz : zCut < z) (hz0 : z ≤ 0) (hx : 0 ≤ x)
    (heq : regionalGain z x = regionalGain z (localEffort z)) :
    x = localEffort z := by
  obtain ⟨_, _, _, hoptlo, hopthi⟩ := optimum_admissible z hz hz0
  have hopt :
      regionalGain z (localEffort z) =
        middleGain z (localEffort z) :=
    gain_middle z (localEffort z) hoptlo hopthi
  by_cases hlow : x ≤ -z
  · have hxzero : regionalGain z x = -x^2 := by
      simp [regionalGain, plant_lower z x hlow]
    have hstrict := positive_local_gain_at_optimum z hz hz0
    rw [hxzero] at heq
    nlinarith [sq_nonneg x]
  · have hlo : -z < x := lt_of_not_ge hlow
    by_cases hhigh : 2-z ≤ x
    · have hsat : regionalGain z x = z+x-1-x^2 := by
        simp [regionalGain, plant_upper z x hlo hhigh]
        ring
      have hsum : 0 ≤ x+(2-z)-1 := by linarith
      have hfactor : 0 ≤ (x-(2-z))*(x+(2-z)-1) :=
        mul_nonneg (sub_nonneg.mpr hhigh) hsum
      have hbound : middleGain z (2-z) = 1-(2-z)^2 := by
        unfold middleGain
        ring
      have hweak : z+x-1-x^2 ≤ middleGain z (2-z) := by
        rw [hbound]
        nlinarith [hfactor]
      have hdist : 0 < 2-z-localEffort z := by linarith
      have hdistSq : 0 < (2-z-localEffort z)^2 :=
        sq_pos_of_pos hdist
      have hgap := middle_quadratic_gap z (2-z)
      have hstrict : middleGain z (2-z) <
          middleGain z (localEffort z) := by nlinarith
      rw [hsat, hopt] at heq
      linarith
    · have hhi : x < 2-z := lt_of_not_ge hhigh
      rw [gain_middle z x hlo hhi, hopt] at heq
      have hgap := middle_quadratic_gap z x
      have hs : (x-localEffort z)^2 = 0 := by
        rw [heq] at hgap
        nlinarith
      have hzero : x-localEffort z=0 :=
        (sq_eq_zero_iff).mp hs
      linarith

/-- For the national planner, equality in the global welfare upper bound
forces both public research efforts AND both new-variety shares to zero. -/
theorem p3_national_global_zero_unique
    (z x₁ x₂ a₁ a₂ : ℝ)
    (hz : z ≤ 0)
    (ha₁ : 0 ≤ a₁) (ha₂ : 0 ≤ a₂)
    (hW : nationalGain z x₁ x₂ a₁ a₂ = 0) :
    x₁=0 ∧ x₂=0 ∧ a₁=0 ∧ a₂=0 := by
  rw [national_square_identity] at hW
  have hz₁ : z*a₁ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₁
  have hz₂ : z*a₂ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hz ha₂
  have hs₁ := sq_nonneg (x₁-a₁/2)
  have hs₂ := sq_nonneg (x₂-a₂/2)
  have ha₁sq : a₁^2=0 := by
    nlinarith [sq_nonneg a₁, sq_nonneg a₂]
  have ha₂sq : a₂^2=0 := by
    nlinarith [sq_nonneg a₁, sq_nonneg a₂]
  have ha₁zero : a₁=0 := (sq_eq_zero_iff).mp ha₁sq
  have ha₂zero : a₂=0 := (sq_eq_zero_iff).mp ha₂sq
  subst a₁
  subst a₂
  norm_num at hW
  have hx₁sq : x₁^2=0 := by
    nlinarith [sq_nonneg x₁, sq_nonneg x₂]
  have hx₂sq : x₂^2=0 := by
    nlinarith [sq_nonneg x₁, sq_nonneg x₂]
  have hx₁zero : x₁=0 := (sq_eq_zero_iff).mp hx₁sq
  have hx₂zero : x₂=0 := (sq_eq_zero_iff).mp hx₂sq
  exact ⟨hx₁zero,hx₂zero,rfl,rfl⟩

end
end PublicBreeding
