# Canonical Stage 11 — Independent Hostile Referee / Certification-Regression Audit

**Date:** 2026-10-25 JST
**Article:** *Regional Public Breeding and Variety Replacement: Decentralized Research Incentives and National Welfare*
**Correct production source:** `checkpoints/2026-10-25/32_stage10_manuscript/paper.tex`, 14 cited records in its adjacent `references.bib`.
**Branch:** `research/2026-10-24-ijio-response-audit`, Draft PR #2; original Stage 8 Theory Freeze v2 unchanged.
**Canonical workflow:** `research-paper-workflow/THEORY_PAPER_RESEARCH_PIPELINE.md`, Stage 11, against the narrowed Stage 6 and Stage 7.5 applied agricultural research goals.

## 1. Verdict and independence boundary

**STAGE 11: GO — BOUNDED, COMPACT AGRICULTURAL APPLIED-THEORY PAPER ONLY.**

- **FATAL mathematically demonstrated defects: NONE in the frozen claimed parameter domains** following independent symbolic reconstruction and previous full-branch Lean/CI audit.
- **Known-model absorption: generic mechanisms ARE absorbed; application-level integrated claim survives in examined primary-published-source scopes.** Do not represent this as a new general public-R&D theorem or exhaustive world-first priority certificate.
- **One newly detected MINOR proof-exposition problem was repaired**: P1 factorization explicitly needs the follower's symmetric interior KKT relation `x=Ma-z`; the revised proof now says so. A second MINOR abstract scope-inflation problem was repaired by replacing "changes sign" with "can change sign under stated conditions" and removing the suggestion of unrestricted demand-curvature generalization.
- **Economics/journal significance: MATERIAL RESIDUAL EDITORIAL RISK**: limited application-specific marginal externality, stylized regional CS/2 allocation, and an analytical P3+ Nash with zero first-stage BR coupling may be judged incremental by editors. These are accurately disclosed and do not logically force an invented additional theorem. Whether a particular field journal will accept is **UNKNOWN**, not certified by an internal self-audit.
- This is an adversarial AI-assisted internal review using **new independent-from-production primitive reconstruction**, independent CI scripts and primary-source checks. It is **not** a separate human referee, not an editor's opinion, and not an acceptance forecast.
- **Next Stage 12:** journal/format/fee suitability, not automatic submission. Existing Stage 6 narrowly closed, Stage 7.5/7.5A GO, Stage 8 GO, Stage 9 GO, and Stage 10 GO are prerequisites satisfied within their archived explicitly limited scopes.

## 2. Independent mathematics and whole-game reconstruction (new code)

**New source:** `checkpoints/2026-10-25/35_stage11_hostile_referee/independent_referee_reconstruction.py`, standalone SymPy script that imports **none** of the Stage 9 verification modules, redefines original four-good market primitives, and reruns independent exact checks. The Stage 11 CI executes that script, the revised Stage 10 frozen-claim verifier, and **all six** Stage 9 exact regression scripts in one job:
`https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40120134074` — **SUCCESS** on final abstract+proof revised manuscript SHA `51a20176ec7abca22b242e6851147d18e03b27a7`.

### 2.1 From primitives and all relevant FOCs

Four quantities `q=(1-a1,a1,1-a2,a2)`, national `V=alpha'q-q'Bq/2`, inverse national prices `p=alpha-Bq`. Producer receipts net of real conversion costs, `CS=V-p'q`, local `G_i=Pi_i+CS/2-R*x_i^2/2`, national `W=G1+G2`. Independently deriving `W_ai` recovers both grower private KKT residuals `z+x_i-d*a_i-e*a_j` exactly; with B PD and strict adoption-cost convexity they maximize W for every fixed research vector, including constrained corners.

From full primitive totals and the follower inverse Hessian `H^{-1}`, we rederive the `G1_x1-W_x1` marginal wedge. **IMPORTANT hostile test**: if the follower optimality condition is OMITTED, the proposed P1 factorization does **not** hold off the follower equilibrium when e is nonzero. Only after `x=Ma-z` on the symmetric interior continuation do we obtain `[h-j-(2h-e)a]/(2L)=xi(aStar-a)` identically. The manuscript already limited the proposition to the follower equilibrium, and the revised proof now makes that necessary substitution explicit; no invalid unconditional theorem remains.

### 2.2 Exact P3+ globality, boundaries, benchmark

Original e=j=0 family `t=1/2,b=c=n=1/5,k0=kappa=1,R=2,A=10,Delta=1/2+z`:
- Independently computed B eigenvalues: `19/10,11/10,1/2,1/2`, all strictly positive;
- ORIGINAL off-equilibrium local incremental payoff, with other region fixed: `F_i(x,a)=(z+x+1/4)a-5*a^2/4-x^2`. This is valid at **all** adoption corners and is not the interior-optimality-shortcut expression incorrectly extended to a corner;
- Follower all-branch continuation is `a=clamp((z+x)/2,0,1)` with zero-/interior-/full-adoption payoff functions `-x^2`, `(z+x)/8+3(z+x)^2/16-x^2`, and `z+x-1-x^2`;
- On the middle branch, exact unique stationary effort `xD=(1+3z)/13`, and `F(xD)-F(x)=13*(x-xD)^2/16`;
- At cutoff `zCut=(-4+sqrt(13))/12`, zero and `sqrt(13)/52` tie, and independently separable public best responses make **four Nash profiles**. This lower endpoint must be excluded from P3+ uniqueness;
- National planner: over the entire **joint feasible x>=0, a in [0,1]^2**, `W-W0=z*sum(a)-(3/4)*sum(a^2)-sum((x-a/2)^2)<=0` for z<=0; equality only at x=a=0;
- At the strictly positive unique regional equilibrium in `(zCut,0]`, `WD-WP=(10z-1)*(22z+3)/338<0`;
- Exact finite off-path checks for z=0,-1/50,-3/100 compared deviation candidates across three adoption branches including x=10 and x=100 and found no greater payoff. These finite checks **supplement, not replace**, the full analytic proof with continuous x and every eligible z.

Separate nonzero-e case `e=1/100` remains supported by **exact rational nine-active-set** global unilateral Nash check under Stage 9; not independently derived fully in this standalone Stage 11 code, not Lean-globalized, and does not prove uniqueness of all asymmetric e>0 equilibria. Crucial **e=j=0 means no intergovernmental research best-response cross-dependence** in analytic P3+, even though territorial payoff incidence is interdependent.

### 2.3 Direct adverse counterexample to inflated P2 claim

For N=2, phiOld''=1, phiNew''=2, convex crop conversion K''=1, g=0, f'=1 and symmetric a=1/2, the payoff-incidence wedge is **-1/16**, NOT zero. Source-level exact rational test newly reconstructed after correcting a test-only float-versus-rational equality issue (initial run `40119927443` failed and historical failure is preserved). The published P2 requires a *common old/new phi* and **does not** encompass this alternative, so this is **a verified boundary, not a falsification of the stated proposition**. Stage 9 prior T1 quartic research cost and T3 quartic crop switching cost checks also pass in the final Stage 11 CI and are not promoted into all-function theorems.

## 3. Known-model-in-disguise / theorem absorption and genuine prior art

**Reduction:** With follower a(x) chosen efficiently, `dW/dx_i=a_i-Rx_i` (or f'(x_i)a_i-C_i') by the planner envelope, and `dG_i/dx_i-dW/dx_i=-dG_j/dx_i` from `W=G1+G2`. Thus the generic marginal wedge **is standard territorial price/consumer-surplus incidence**, not a new general externality theorem. The observed candidate threshold in P1 is a parameterization of this identity, and generic no-research nationwide optima despite private incentives have existing literature counterparts. This is a useful institutional characterization only if article is framed narrowly.

**Specific primary comparators revisited:**
1. **Alston, Freebairn & James (2001), AJAE**: https://academic.oup.com/ajae/article-abstract/83/4/888/110933 — two independent commodity producer groups, noncooperative promotion and classic overpromotion compared with joint producer-profit maximization. Those results absorb the generic "beggar thy neighbor" story, but the examined base game lacks this paper's regional government payoff with nationally allocated consumer surplus, four-cultivar switching follower, and national PS+CS planner counterfactual. Do NOT assert its general extensions cannot encompass the application.
2. **Balagtas & Kim (2007), AJAE**: existing Stage 6 identified supply/input reallocation across agricultural product markets plus promotion optimization. This removes any first-ever shared-resource reallocation claim. Published full-text theorem scope remains partly access-limited.
3. **Lence, Marette, Hayes & Foster (2007), AJAE**: https://academic.oup.com/ajae/article-abstract/89/4/947/146334 ; accessible source WP https://www.card.iastate.edu/publications/06-mwp-9 . Its producer organization, geographic differentiation, fixed development costs, old/new production and conditional allocation precedents are close. The original verified propositions analyze alternative producer controls and fixed new-product development, not a directly identical pair of public territorial continuous-research leaders, private KKT followers and national zero-effort theorem.
4. **Swinnen & de Gorter (1998), AJAE**: https://academic.oup.com/ajae/article-abstract/80/1/107/48205 — endogenous agricultural commodity policy and public-research welfare, not the exact two-local-lab funding game. Its existence prevents asserting this paper first considers politically determined agricultural research impacts.
5. **Cardon & Pope (2003), JARE**: https://ageconsearch.umn.edu/record/31098/ — zero social-optimal generic advertising possible under specified market conduct. Social zero is NOT novel standing alone.
6. **Jinji & Toshimitsu (2013), Japan and the World Economy**: https://www.sciencedirect.com/science/article/abs/pii/S0922142513000479 — quality-differentiated private firms and strategic R&D subsidies/taxes with Cournot/Bertrand. This prevents a broad strategic quality R&D claim, but its instrument, actor and game differ.
7. **Akhundjanov et al. (2020), Economic Modelling**: https://www.sciencedirect.com/science/article/abs/pii/S0264999318312938 — university innovator and newly bred apple variety, commercialization/licensing and growers, not locally jointly welfare-weighted ex ante public effort.
8. **Wang & Çakır (2020), Agricultural Economics**: https://onlinelibrary.wiley.com/doi/10.1111/agec.12564 — positive estimated consumer welfare from actual Honeycrisp introduction; our theoretical social-zero example is not an empirical allegation that real public crop breeding is harmful.
9. **Zhang (2022), The Manchester School**: https://onlinelibrary.wiley.com/doi/10.1111/manc.12388 — socially negative expected innovation through private patent-R&D/licensing, not generic new negative-innovation-priority for us.

**Conclusion:** No **direct proposition-wise isomorphism** was identified in available closer models that invalidates the **bounded applied institutional** claim as formulated. This is a scope-limited review; full paywalled source texts have not all been obtained, and no globally exhaustive absence-of-prior-art proof is claimed. No regression of the Stage 6 limited novelty classification was demonstrated. The manuscript now has **14 explicitly cited, functionally relevant references**, including previously neglected public agricultural research and quality R&D ancestors.

## 4. Required adversarial attack matrix

| Attack | Classification after targeted editorial changes | Reason / disposition |
| --- | --- | --- |
| Classic result disguised as novelty | MINOR — CONTROLLED | Generic promotion over-spending, price incidence and private adoption efficiency acknowledged as known in Introduction |
| Parent model recentering/matrix/KKT identity | MINOR — CONTROLLED | Direct identity `G_i,x-W_x=-G_j,x` reproduced; bounded application only |
| Whole-game exact parent theorem / novelty | MATERIAL EDITORIAL RISK — NOT FATAL within bounded claims | No printed exact isomorphism in verified scope, but generic ingredients known and priority not universally certified |
| Assumption engineered to force result | MATERIAL EDITORIAL RISK — DISCLOSED | Positive x / national zero requires exact parameter slice, CS/2 weighting and static conversion, all stated as assumptions |
| Alternative demand/contract/information | MINOR — BOUNDED | P2 unequal curvature is real counterexample outside theorem; licensing, uncertain discovery and dynamic replanting not covered |
| Corners/participation/boundaries | PASS | 0, partial, full adoption all handled; zCut four equilibria excluded |
| SPNE/global proof vs local FOC | PASS | P3 exact three-branch global BR and unrestricted national feasible-space inequality |
| Welfare merely redistribution | PASS | W=V-real K-real C, strict negative net national gain; not just producer-price transfers |
| Numerical example treated as proof | PASS WITH EXPLICIT SPLIT | Analytic e=0 family proven, separate e>0 exact SymPy global BR not all e/Lean |
| Manuscript formula/proof drift | MINOR — REPAIRED | Explicit symmetric follower KKT substitution added; all lemma/prop/corollary texts unchanged |
| P2 generality and quantifier inflation | MINOR — REPAIRED/BOUNDED | P2 common phi essential, asymmetric counterexample preserved; abstract narrowed |
| Stage7.5A robustness classification inflation | PASS | T1/T3 bounded positive instances, T2 negative result preserved; no all-class generalization |
| Proof assistant scope inflation | PASS | Lean P3 core, P2 conditional Jacobian, e>0 exact SymPy; no claim complete Lean proof |
| Benchmark terminology drift | PASS | National full W versus local G_i; mutual no-effort benefit different from own unilateral cutback |
| Institutional realism/CS share | MATERIAL EDITORIAL RISK — BOUNDED | CS/2 not estimated governmental objective; real legal, fiscal, and orchard features outside model |
| Editorial-value/whole-paper completeness | GO FOR COMPACT INSTITUTION-SPECIFIC STUDY; NOT RIO/IJIO GENERAL THEORY | One clear public-breeding fiscal/adoption question, exact global paradox and limits; no empirical implementation prescribed |
| Figure/table reader value | PASS | No essential exhibits; all economic mathematics in short main body and derivation appendices |
| Reader proof bridge absent or code required | PASS after amendment | Four-good prices, local payoff F, all planting branches, welfare square, cutoff and P2 Jacobian projection in manuscript |
| Late bibliography and prose drift | PASS | 14 cited references, Stage10 frozen-thm QA; no new mathematical theorem |
| Journal fit, editor importance | STAGE 12 DECISION NEEDED | Field agriculture applied-theory venue potentially, with real rejection risk, no presumption of BAE eligibility or impact |

**Severity summary:** `FATAL=0`; unmitigated **new** mathematics/claim-scope majors `=0`; **material editorial vulnerabilities remain** (narrow novelty, artificial policy weighting, exact zero-coupling main parameter slice). These must accompany any Stage 12 recommendation. Do not use "no unmitigated majors" to mean automatic publication.

## 5. Independent skeptical editorial-value and research-question completeness

**Strongest desk-reject case:** The generic incidence and Beggar-Thy-Neighbor incentive are classical; the paper's headline exact existence parameter family is constructed with e=0 (so no first-stage strategic interaction between the labs' **best-response functions**), half national consumer surplus in each government utility is stylized, crop acreage substitutes smoothly without varietal IP and orchard vintage costs, and the article has no calibrated magnitude or implemented policy instrument. A journal can reasonably decide 11 pages of formally exact LQ arithmetic are insufficient advancement. Such a desk rejection would not imply the theorem false.

**Best positive field-note case:** It concretely disentangles two different levels of decision-making in real decentralized public agricultural experimentation: competitive growers' privately optimal **variety conversion** at fixed quality does not imply regional public labs' prior **research investment** is nationally optimal. The sign of the latter distortion depends on planting composition (under exact conditions); the analytic example certifies a **globally** inefficient but individually rational public research decision with no fixed R&D fee or farmer market power, and identifies its boundary and fragile demand-curvature assumptions. In the modest *application-specific* publication category, the mathematical precision and transparent limitations contribute an interpretable diagnostic.

**Economic question answered:** WHO decides/finances quality, WHO switches crop land, WHY the downstream allocation is efficient yet upstream funding not, WHEN the marginal incentive sign can reverse in the specified interior model, and WHETHER a strict positive-local/zero-national welfare paradox can occur globally (exact P3+). Those are answered. Fiscal coordination instruments, taxes, licensing contracts, uncertain innovation and real region/crop estimates are **NOT ANSWERED** and must stay out of claimed policy prescriptions. They are meaningful future work, not missing theorems secretly presented as proved.

**Editorial balance:** limited **GO** to the compact diagnostic agricultural applied-theory path selected at Stage 7.5; **NO-GO** to stronger universal strategic-public-R&D-theory framing. A referee could still rationally reject it based on limited incremental impact. That risk is expressly preserved.

## 6. Manuscript edits and version discipline

In `32_stage10_manuscript/paper.tex`:
1. One line added to P1 proof: **the final wedge factorization explicitly substitutes `x=Ma-z` from symmetric interior farmer optimality**, preventing an off-equilibrium extrapolation.
2. Abstract conditioned the research wedge's sign reversal on *specified interior and parameter restrictions* instead of suggesting it occurs generally.
3. Abstract states restricted demand-curvature scope, not general unrestricted nonlinear robustness.

These are **exposition/claim-scope corrections only**, not alterations to players, games, utility, matrices, national welfare, theorem/corollary statements, formal Lean code or benchmarks. Stage10 verifier checks precisely 30 identical displayed math environments relative to frozen original other than the inherited purely notational `H_phi` correction; lemma/proposition/corollary exact statement comparison remains PASS. The *original* Stage8 frozen theory and Stage9 pinned source files are intentionally unchanged.

**CI evidence:**
- First standalone Stage11 check failed only due to Python float-vs-SymPy Rational type comparison for an exact -1/16 value; fixed test computation with `S.Rational`, archived failure not erased.
- Stage11 final on revised paper: [run 40120134074](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40120134074), **SUCCESS**: new independent reconstruction + Stage10 theorem/citation check + all six Stage9 pinned regressions. In logged independent recheck: KKT and offpath P1, full four-good primitive P3 F_i, 3 adoption regimes, exact B eigenvalues, cutoff tie, full social-W completion, exact z samples and T2 nonneutrality. Stage10 check logs 30 display blocks, 32 labels, **14** referenced literature keys; Stage9 reruns six checks including e>0 9-regime candidate comparisons.
- Final revised Stage10 PDF build [run 40120134071](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40120134071): **SUCCESS**, job 120949745882. Verified current final file built with LaTeX/BibTeX, final unresolved-reference/citation check and PDF-signature check, with downloadable workflow artifact ID `12570359418`. Earlier 14-citation PDF run 40118920477 is superseded. This is the revised abstract/P1 proof source, not the old frozen 10-page draft.

## 7. Routing and nonclaims

**Stage11 GO on bounded economic-theory scientific audit**: may proceed to formal **Stage 12 venue choice and APC/non-OA/Diamond publication-fee and format gate** after confirming the revised PDF run and making journal-specific AI declaration/authorship source compliance checks as applicable. No journal is selected, no acceptance inferred, and author signature is not reconstructed beyond prior self-attestation.

Do not reopen Stage 4A, Stage 6 or Stage 7.5A without a real new theorem absorption, mathematical counterexample within theorem domain, or a proposed change to theoretical primitives. Don't add invented new empirical numbers or a coordination grant theorem solely to force higher journal prestige. Keep PR #2 Draft, no merge into main and no submission.

## 8. Final PDF artifact inspection

Final Stage 10 PDF obtained from successful run 40120134071, artifact 12570359418. Container inspection: **11 A4 pages**, 249442 bytes, PDF 1.7. Text extraction found intended public R&D citations and full bibliography. **All 11 pages** rendered and inspected together for obvious text/math overflow, missing references, page errors; none detected. Overview-scale visual review is not a line-by-line final proofread.

Final revised manuscript Git blob SHA is `76598a904e931d34587e10deadb5598d0598ec1b`. Original Stage 8 frozen mathematics and Stage 9 pinned sources remain unchanged.

**Canonical Stage 11 status:** **GO for bounded compact agricultural applied-theory path**; material editorial novelty/significance and institutional weighting risks explicitly preserved. Stage 12 venue/fee/format gate next; NOT submission GO.
