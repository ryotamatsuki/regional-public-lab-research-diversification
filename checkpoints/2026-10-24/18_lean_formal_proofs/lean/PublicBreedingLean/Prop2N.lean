import Mathlib
import PublicBreedingLean.Core

/-!
# Proposition 2: N-region anonymous-adoption Jacobian inversion

Lean proves the symmetric-versus-orthogonal response identity for ANY real
N with N≠0 and L≠0. For application interpret N as a natural number >=2.
The economic Hessian entry structure must be established separately from
the restricted utility V with common phi and same-generation g.
-/

namespace PublicBreeding
noncomputable section

/-- Under an N-region symmetric Jacobian L I + 2g 11ᵀ,
one region has response u and each other region has response v.
The common g cancels exactly on the difference direction. -/
theorem p2_n_region_response
    (N L g fp u v : ℝ)
    (hN : N ≠ 0) (hL : L ≠ 0)
    (hown : L*u+2*g*(u+(N-1)*v)=fp)
    (hother : L*v+2*g*(u+(N-1)*v)=0) :
    u-(u+(N-1)*v)/N = (N-1)*fp/(N*L) := by
  have hdifference : L*(u-v)=fp := by
    linear_combination hown-hother
  have hcoeff :
      (u-(u+(N-1)*v)/N)*(N*L) =
        (N-1)*(L*(u-v)) := by
    field_simp [hN]
    ring
  apply (eq_div_iff (mul_ne_zero hN hL)).2
  calc
    (u-(u+(N-1)*v)/N)*(N*L) =
        (N-1)*(L*(u-v)) := hcoeff
    _ = (N-1)*fp := by rw [hdifference]

/-- N-region signed curvature wedge, conditional on the model-derived
Jacobian conditions above. No broad arbitrary-demand equivalence is assumed. -/
theorem p2_n_region_curvature_incidence
    (N L g fp u v a oldCurv newCurv : ℝ)
    (hN : N ≠ 0) (hL : L ≠ 0)
    (hown : L*u+2*g*(u+(N-1)*v)=fp)
    (hother : L*v+2*g*(u+(N-1)*v)=0) :
    (u-(u+(N-1)*v)/N)*
       ((1-a)*oldCurv-a*newCurv) =
    ((N-1)*fp/(N*L))*
       ((1-a)*oldCurv-a*newCurv) := by
  rw [p2_n_region_response N L g fp u v hN hL hown hother]

end
end PublicBreeding
