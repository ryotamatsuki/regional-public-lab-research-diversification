import Mathlib
import PublicBreedingLean.Prop3Global

/-!
# Excluded lower endpoint of Proposition 3+

At z = zCut the local public researcher is indifferent between zero effort
and a positive interior effort. That is why Proposition 3+ requires z>zCut.
This module proves two DISTINCT best-response efforts globally, including
the nonadoption and saturation regimes. It does not require a tie-break.
-/

namespace PublicBreeding
noncomputable section

theorem cutoff_effort_formula :
    localEffort zCut = Real.sqrt 13 / 52 := by
  unfold localEffort zCut
  ring

theorem cutoff_effort_plant_interior :
    -zCut < localEffort zCut ∧ localEffort zCut < 2-zCut := by
  have hlow := zCut_above_neg_sixteenth
  have hhigh := zCut_nonpos
  unfold localEffort
  constructor <;> linarith

theorem cutoff_positive_effort :
    0 < localEffort zCut := by
  have hlow := zCut_above_neg_sixteenth
  unfold localEffort
  linarith

theorem cutoff_gain_zero_at_positive_effort :
    regionalGain zCut (localEffort zCut) = 0 := by
  obtain ⟨hlo,hhi⟩ := cutoff_effort_plant_interior
  rw [gain_middle zCut (localEffort zCut) hlo hhi]
  rw [middle_gain_at_optimum]
  rw [zCut_root]
  norm_num

theorem cutoff_gain_zero_at_no_effort :
    regionalGain zCut 0 = 0 := by
  have hcut := zCut_nonpos
  have ha : plant zCut 0 = 0 :=
    plant_lower zCut 0 (by linarith)
  simp [regionalGain, ha]

/-- For every nonnegative unilateral effort, the researcher's payoff at
the exact lower threshold is no larger than at zero investment. -/
theorem cutoff_global_gain_nonpositive
    (x : ℝ) (hx : 0 ≤ x) :
    regionalGain zCut x ≤ 0 := by
  by_cases hlow : x ≤ -zCut
  · have ha := plant_lower zCut x hlow
    simp [regionalGain, ha]
    nlinarith [sq_nonneg x]
  · have hlo : -zCut < x := lt_of_not_ge hlow
    by_cases hhigh : 2-zCut ≤ x
    · have ha := plant_upper zCut x hlo hhigh
      have hlow2 : 2 ≤ x := by have hzc := zCut_nonpos; linarith
      have hg : regionalGain zCut x = zCut+x-1-x^2 := by
        simp [regionalGain, ha]
        ring
      rw [hg]
      nlinarith
    · have hhi : x < 2-zCut := lt_of_not_ge hhigh
      rw [gain_middle zCut x hlo hhi]
      have hd := middle_global_max zCut x
      rw [middle_gain_at_optimum, zCut_root] at hd
      norm_num at hd
      exact hd

/-- All positive global best responses at the excluded boundary coincide
with the positive stationary solution. The other optimum is x=0. -/
theorem cutoff_exact_best_response_set
    (x : ℝ) (hx : 0 ≤ x) :
    regionalGain zCut x = 0 ↔
      x = 0 ∨ x = localEffort zCut := by
  constructor
  · intro heq
    by_cases hzero : x = 0
    · exact Or.inl hzero
    · right
      by_cases hlow : x ≤ -zCut
      · have ha := plant_lower zCut x hlow
        have hg : regionalGain zCut x = -x^2 := by
          simp [regionalGain, ha]
        rw [hg] at heq
        nlinarith
      · have hlo : -zCut < x := lt_of_not_ge hlow
        by_cases hhigh : 2-zCut ≤ x
        · have ha := plant_upper zCut x hlo hhigh
          have hzc := zCut_nonpos
          have hx2 : 2 ≤ x := by linarith
          have hg : regionalGain zCut x = zCut+x-1-x^2 := by
            simp [regionalGain, ha]
            ring
          rw [hg] at heq
          nlinarith
        · have hhi : x < 2-zCut := lt_of_not_ge hhigh
          rw [gain_middle zCut x hlo hhi] at heq
          have hopt := cutoff_gain_zero_at_positive_effort
          obtain ⟨hlopt, hropt⟩ := cutoff_effort_plant_interior
          rw [gain_middle zCut (localEffort zCut) hlopt hropt] at hopt
          have hgap := middle_quadratic_gap zCut x
          have hs : (x-localEffort zCut)^2 = 0 := by
            rw [heq,hopt] at hgap
            nlinarith
          nlinarith
  · rintro (rfl | rfl)
    · exact cutoff_gain_zero_at_no_effort
    · exact cutoff_gain_zero_at_positive_effort

/-- A fully verified two-action global BR set means there are four
ordered pure-Nash research profiles at z=zCut, because e=j=0 gives
independent regional reaction functions. This is the formal basis for the
excluded-boundary multiplicity warning in the paper. -/
theorem cutoff_four_nash_actions (x₁ x₂ : ℝ)
    (hx₁ : 0 ≤ x₁) (hx₂ : 0 ≤ x₂) :
    (regionalGain zCut x₁ = 0 ∧ regionalGain zCut x₂ = 0) ↔
    ((x₁=0 ∨ x₁=localEffort zCut) ∧
     (x₂=0 ∨ x₂=localEffort zCut)) := by
  constructor
  · rintro ⟨h₁,h₂⟩
    exact ⟨(cutoff_exact_best_response_set x₁ hx₁).mp h₁,
           (cutoff_exact_best_response_set x₂ hx₂).mp h₂⟩
  · rintro ⟨h₁,h₂⟩
    exact ⟨(cutoff_exact_best_response_set x₁ hx₁).mpr h₁,
           (cutoff_exact_best_response_set x₂ hx₂).mpr h₂⟩

end
end PublicBreeding
