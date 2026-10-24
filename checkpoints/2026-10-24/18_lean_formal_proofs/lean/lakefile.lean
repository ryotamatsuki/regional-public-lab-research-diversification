import Lake
open Lake DSL

package «PublicBreedingLeanProofs» where
  -- The paper's mathematical proof-critical Lean targets only.

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.35.0"

@[default_target]
lean_lib PublicBreedingLean where
  srcDir := "."
