# Stage 13J / 14J — Theorem-Scope Invariance Audit

Date: 2026-10-25 JST. Baseline: Stage 13 integrated `paper.tex` in checkpoint 38. Revised source: adjacent `paper.tex`. Scope: existing Theory Freeze v2, not a new theory or a new general-priority certificate.

## Result and evidence classes

**Source-level mathematical invariance: PASS.** `verify_jafio.py` compares every lemma, proposition and corollary environment byte-for-byte with Stage 13, and separately compares every numbered equation, align display, unnumbered display, and original inline mathematical expression in order. The sole added mathematical clarification supplies the already-verified interacting example primitives n=21/100 and Delta=49/100 relative to the existing family; the checker separately asserts this exact text and the archived script values, then excludes that new clarification from the original-math sequence comparison. The five proof environments retain their full mathematical content. The only proof edit replaces an internal Lean filename with a description of the same conditional verification role. All original primitive-to-price, planting-KKT, incidence, global branch and planner square-completion arguments remain in the manuscript.

The current check also verifies unique labels, complete internal references, citation/BibTeX equality, a single-paragraph abstract, and absence of author-identifying repository links or internal workspace paths. Those mechanical checks do not certify economic originality, final journal style, author identity, funding declarations, or human scholarly accountability.

**Fresh local exact regression: PASS.** The full Stage 9 runner checked all 25 frozen Git blob object IDs and all six archived symbolic regressions. The independent Stage 11 reconstruction then rederived the follower gradients, P1 wedge on the follower FOC, P3 original off-path regional objective, three adoption regimes, square gap, unrestricted national planner bound, cutoff tie and welfare-loss identity. Its negative test rejects an off-follower P1 extension; the unequal-curvature midpoint wedge remains −1/16. The runner additionally executes the two existing checkpoint-12 scripts for the secondary e = 3/10 candidate and exact global unilateral best response at the specified parameter point; their historic broader novelty warnings are not new Stage-6 failures.

The initial local attempt failed because SymPy was absent. Installing the declared `sympy==1.13.3` resolved this **environment** failure. No theory, archived test, or mathematical claim was changed. Local Python is 3.12; CI explicitly uses Python 3.11 and the same pinned SymPy.

**Lean source preservation: PASS; fresh kernel build is a separate CI gate.** All ten formal-source/configuration objects in the Stage 9 manifest match the freeze. The new combined JAFIO workflow rebuilds these unchanged sources and audits axioms on the final revision commit; its actual outcome must be recorded in `REPORT.md`. A historical green run is not substituted for that new run. Mathlib is selected by its v4.35.0 tag and dependencies resolved by `lake update`; this is not a claim of a newly locked transitive dependency manifest.

## Frozen result and proof boundaries

| Result | Preserved claim | Preserved limitation / assurance |
| --- | --- | --- |
| Conditional adoption lemma | Given research, constrained competitive planting globally maximizes national welfare under the stated strict concavity and common real conversion costs | Does not establish efficient research; conditional quadratic KKT core is formalized, economic interpretation remains a manuscript argument |
| P1 | Symmetric interior four-good linear-demand wedge and feasible adoption threshold; conditional effort/adoption comparisons | Follower condition is required; globally interior benchmarks and denominator restrictions are not inferred merely from FOCs |
| P2 | Symmetric interior restricted common-old/new-curvature separable demand class, N ≥ 2, specified fiscal share and positive response conditions | Lean checks conditional Jacobian algebra; the full utility-to-incidence economic bridge is not entirely formalized; arbitrary demand and unequal-curvature midpoint neutrality are not claimed |
| P3+ | Every z in the exact stated open-lower/closed-upper interval yields a unique positive regional research equilibrium, unique national zero optimum, strict welfare loss | Three planting branches cover all nonnegative unilateral research; national square bound covers the larger joint feasible set; analytic best responses are independent |
| P3+ cutoff | Exactly two optimal actions per region and four pure research profiles at the excluded lower endpoint | No unique-equilibrium claim at that endpoint |
| Interacting e = 1/100 example | Exact symmetric candidate, nine-KKT-regime unilateral global BR verification and national welfare loss | External exact computation certifies global BR; Lean candidate/planner algebra does not prove nine-regime globality or uniqueness among all asymmetric equilibria |
| Secondary e = 3/10 example | Existing exact candidate and welfare benchmark retained | Separate instance, not generic nonzero-e robustness |
| Quartic and unequal-curvature checks | Existing bounded positive and negative checks retained | No general functional-form robustness theorem |

## Economic narrative review

The revised abstract and prose distinguish efficient private replacement from efficient public development, identify regional price/consumer-surplus incidence, and explicitly disclose independent best responses in the analytic P3+ family. Discussion remains conditional and does not derive an optimal subsidy, interregional agreement, research-budget cut, or organizational consolidation. No theorem formula, player, objective, action set, cost, demand, timing or quantifier has been added or strengthened. An existing numerical example now specifies its previously omitted primitive values; this is a reconstruction clarification, not a new model. No mathematical reason to reopen Stage 4/4A/7.5A was identified.

The Stage 6 downgrade remains binding: general price incidence, overpromotion and conditional competitive efficiency are existing mechanisms. The contribution is a bounded public-breeding application and whole-game characterization. New JAFIO-specific literature overlap is adjudicated separately in `JAFIO_FIT_AND_EDITORIAL_AUDIT.md`; source invariance alone cannot close that novelty question.

## Reproduction

Run `python checkpoints/2026-10-25/43_jafio_submission_optimization/verify_jafio.py` from the repository root with SymPy 1.13.3 installed. The runner executes Stage 9, the independent Stage 11 script, and unchanged Stage 10/13 source checks. After a clean LaTeX/BibTeX build, it also rejects unresolved references/citations and checks the PDF signature. The combined workflow rebuilds the proof core in a separate job and uploads the review PDF, log, resolved bibliography, and minimal anonymous LaTeX source ZIP.

PDF page rendering/visual review, current publisher policy, bibliographic primary-source verification, and substantive human-author accountability remain distinct checks. They must not be marked PASS from this script alone.
