import Mathlib
import PublicBreedingLean.Prop3Global

/-!
# Exact model-to-theorem bridge for P3+ (NO farmer interior FOC assumed)

This module starts with the four-good true-quality quasilinear utility and
competitive prices for the special P3+ subfamily t=1/2, b=c=n=1/5.
It proves the off-equilibrium regional and national welfare identities over
arbitrary old/new planting shares, including full adoption.

The market price formulas here are the *derivatives of the four-good utility*
in quantity coordinates. We check gross utility minus total expenditure
matches consumer surplus. This is a special-case economic reduction, not
a proof of the full P1/P2 generic market structures.
-/

namespace PublicBreeding
noncomputable section

def grossUtility (A z x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  A*(1-a₁) + (A+1/2+z+x₁)*a₁ +
  A*(1-a₂) + (A+1/2+z+x₂)*a₂ -
  ((1-a₁)^2+a₁^2+(1-a₂)^2+a₂^2)/2 -
  ((1-a₁)*a₁+(1-a₂)*a₂)/2 -
  ((1-a₁+a₁)*(1-a₂+a₂))/5

def priceOld (A a : ℝ) : ℝ := A-6/5+a/2
def priceNew (A z x a : ℝ) : ℝ := A+z+x-1/5-a/2

def competitiveCS (A z x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  grossUtility A z x₁ x₂ a₁ a₂ -
  (priceOld A a₁*(1-a₁)+priceNew A z x₁ a₁*a₁+
   priceOld A a₂*(1-a₂)+priceNew A z x₂ a₂*a₂)

/-- The four-good consumer surplus is exactly half of q'Bq. -/
theorem cs_from_four_goods (A z x₁ x₂ a₁ a₂ : ℝ) :
    competitiveCS A z x₁ x₂ a₁ a₂ =
       6/5-(a₁+a₂)/2+(a₁^2+a₂^2)/2 := by
  unfold competitiveCS grossUtility priceOld priceNew
  ring

def producerIncome (A z x a : ℝ) : ℝ :=
  priceOld A a*(1-a)+priceNew A z x a*a-a-a^2/2

def regionalObjective (A z x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  producerIncome A z x₁ a₁ +
  competitiveCS A z x₁ x₂ a₁ a₂/2-x₁^2

def nationwideObjective (A z x₁ x₂ a₁ a₂ : ℝ) : ℝ :=
  producerIncome A z x₁ a₁+producerIncome A z x₂ a₂+
  competitiveCS A z x₁ x₂ a₁ a₂-x₁^2-x₂^2

/-- Local investment effect derived without substituting farmers' FOC:
the same formula works for a=0 and a=1. -/
theorem full_regional_off_equilibrium_reduction
    (A z x₁ x₂ a₁ a₂ : ℝ) :
    regionalObjective A z x₁ x₂ a₁ a₂ -
      regionalObjective A z 0 x₂ 0 a₂ =
      (z+x₁+1/4)*a₁-5*a₁^2/4-x₁^2 := by
  unfold regionalObjective producerIncome competitiveCS
    grossUtility priceOld priceNew
  ring

/-- The regional formula actually implemented by Prop3Global is the
four-good welfare expression evaluated at the competitive planting response. -/
theorem local_objective_matches_full_market
    (A z x₁ x₂ a₂ : ℝ) :
    regionalObjective A z x₁ x₂ (plant z x₁) a₂ -
      regionalObjective A z 0 x₂ 0 a₂ =
      regionalGain z x₁ := by
  rw [full_regional_off_equilibrium_reduction]
  unfold regionalGain
  ring

/-- National welfare is derived directly from four-good producer and
consumer surpluses, not by extrapolating an interior-follower FOC. -/
theorem full_national_off_equilibrium_reduction
    (A z x₁ x₂ a₁ a₂ : ℝ) :
    nationwideObjective A z x₁ x₂ a₁ a₂ -
      nationwideObjective A z 0 0 0 0 =
      nationalGain z x₁ x₂ a₁ a₂ := by
  unfold nationwideObjective nationalGain
    producerIncome competitiveCS grossUtility priceOld priceNew
  ring

/-- Fixed (x₁,x₂), competitive planting FOC: inverse price gain equals
marginal real replacement cost (1+a₁). -/
theorem farm_price_foc_reduced (A z x a : ℝ) :
    priceNew A z x a-priceOld A a-(1+a)=z+x-2*a := by
  unfold priceNew priceOld
  ring

end
end PublicBreeding
