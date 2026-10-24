# Formal Verification Gate — applicable / not tested (blocking)

Date: 2026-10-24. This is a required Stage 7.5A **negative current-state certificate**, not a formal proof.

**Decision: FORMALIZATION APPLICABLE — NOT TESTED. Stage 7.5A GO forbidden.**

## Environment / reproducibility evidence

- Python/SymPy 1.14.0 symbolic and exact rational tests ran; SciPy 1.17 for independent numerical supporting observations.
- Checked executables lean, lake, elan, coqc, isabelle, agda, z3, cvc5: none installed in local PATH. No local Lean/lake binary discovered under /opt or /home/oai.
- Direct network DNS resolution of github.com failed, so no Lean/mathlib installation/build was performed.
- No Lean source is claimed compiled or accepted by its kernel. No axiom or placeholder inventory from a real Lean proof currently exists.
- Existing SymPy arithmetic PASS is not a valid proof-assistant PASS.

## Proof-critical target map for Lean 4 + mathlib (preferred)

| Paper claim | Target proof theorem (tentative signature; not code claimed to compile) | Core to formalize | Model/economic scope OUTSIDE this target |
|---|---|---|---|
| P3+ parameter interval | forall z:Real, zc<z -> z<=0 -> (1+3*z)/13>0 and (1+16*z)/26>0 and (1+3*z)/13<2-z | square-root lower-bound algebra, strict endpoints, admissibility | farmer price formation, interpretation of x and adoption |
| P3+ local globality | forall z∈(zc,0], forall x>=0, Fpiecewise(x,z)<=Fpiecewise(xD,z), equality only x=xD | genuinely complete 3-branch piecewise a(x)=clip((z+x)/2,0,1); no unproved helper that assumes xD is best response | choice to model K as quadratic and local public CS weight |
| P3+ national optimum | forall z<=0, x1,x2>=0 and 0<=a1,a2<=1: z*sum a+sum x*a-sum a²-sum x²<=0; equality iff x=a=0 | square completion and uniqueness across larger feasible (x,a) domain | full four-good V -> this reduced welfare identity unless separately proved |
| P3+ welfare loss | forall z∈(zc,0], (10*z-1)*(22*z+3)/338<0 | exact factor sign and interval | real-world economic effect size |
| P3+ boundary | at z=zc, exactly two BR {0,sqrt13/52} per player and 4 Nash profiles | exact zero gain at stationary positive optimum, piecewise globality, independent responses | nonzero e game Nash multiplicity |
| P1/Corollary | symbolically rational identity xD-xP=... under denominators!=0 and positivity assumptions | equality, positive sign and quantifier fidelity | entire equilibrium correspondence or empirical interpretation |

## Statement fidelity / no-smuggling protocol

Required code must define strategy domains as nonnegative real efforts and closed unit-interval adoption, not just assume candidate research is the global best response. Treat positivity of the model B Hessian and follower KKT in a separate economic->formal mapping, or explicitly state them as external lemmas not certified. Ensure lower endpoint zc is excluded in the strict uniqueness theorem. Prove the case split x<=-z / -z<x<2-z / x>=2-z exhausts nonnegative x given z<=0; do not assume a single interior formula globally. The planner's complete-square certificate must include equality uniqueness, not just nonpositivity. No sorry/admit, project-specific unproved axioms or a convenient "isCandidate" hypothesis equivalent to the desired conclusion.

Record precise lean/mathlib versions, lakefile/manifest, clean build command, workflow logs, project theorem names, axioms report, and future scope changes before certifying PASS. If only proof-critical arithmetic is accepted, certify **PROOF-CRITICAL CORE**, not FULL ECONOMIC MODEL.

## Next gate

Complete an actual proof-assistant source and clean build in a compatible Lean/mathlib environment, map theorem signatures back to current checkpoint-17 scope certificate, check all placeholders and imported hypotheses, and record authentic author intellectual review. Until then **Stage7.5A CONDITIONAL, Stage8 BLOCKED**. The user's provisional acceptance of Stage6 does not silently discharge the formal gate.