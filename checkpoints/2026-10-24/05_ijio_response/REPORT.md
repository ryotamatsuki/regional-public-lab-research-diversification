# Stage IJIO-Response — Independent theoretical and publication audit
**Date:** 2026-10-24  
**Project:** Regional Public Breeding, Varietal Replacement, and Distorted R&D Incentives  
**Sources:** `checkpoints/2026-10-24/04_varietal_replacement/` (read-only reference); prior two IJIO editorial decisions, 2026-02-16 and 2026-09-21  
**IJIO CRITICISM STATUS:** **PARTIALLY OVERCOME**  
**Submission research status:** **REVISE** (JARE/CJAE conditional prospects; not submission-ready)

> This checkpoint adds an independently derived, arbitrary-differentiable-demand incidence identity, a precise counterexample to a broad fixed-adoption claim, symbolic and numerical checks, a prior-art audit and a prioritized reorientation. It does **not** claim a previously unknown general law or certify acceptance by any journal. No previous checkpoint was modified.

## R1. Editorial criteria and summary verdict

The February IJIO decision on *Decentralized Public R&D, Demand Shifters, and the Over- and Underinvestment Threshold* (IJIO-D-26-00070) stated that competently executed modelling nevertheless lacked sufficient novel contribution. The September decision on *Private Compatibility and the Stability of Standards Coalitions* (IJIO-D-26-00585) specified a lack of a mechanism transferable beyond comparisons of linear Cournot configurations.

The present model has a more explicit economic **transmission channel**: local public quality investment changes farmers' varietal allocation, which changes prices, which redistributes receipts across producer regions and consumer regions. A nonlinear demand benchmark confirms reversal and disappearance of the wedge. **However, the general decomposition is a standard envelope/price-incidence calculation; this mathematical generalization alone does not establish new economic theory.** The conditional fixed-adoption neutrality and reversal are interesting for public breeding but insufficient to declare the IJIO objection completely overcome.

| Axis | Evidence | Assessment |
|---|---|---|
| Mathematical correctness | Independent 2-region SymPy identity, 24 nonlinear implicit/finite-difference cases, three linear benchmark replications and rational planner certificate | PASS within stated assumptions; not a formal full-game global proof |
| Mechanism | General fixed-demand-quality versus adoption-mediated incidence decomposition | PASS |
| Generality | Exact identity for arbitrary smooth V and asymmetric N; sign theorem remains demand-class-specific | PARTIAL |
| Novelty | Standard envelope/price incidence potentially absorbs the decomposition; nearest papers not exhausted full text | UNRESOLVED / high risk |
| Economic significance | Subsidy sign can change; but illustrative loss small and uncalibrated | PARTIAL |

## R2. The transferable general decomposition (new explicit synthesis, NOT verified novelty)

Let `q=q0+Sa`, where each column `S_i` replaces one unit of the old variety in region i with one unit of the new variety. Let aggregate quasi-linear gross utility be any `C^2` function `V(q,x)`, inverse prices `p=V_q`, and region-i conversion cost `K_i(a_i)`. Let producers be price takers, and suppose the interior adoption system holds:
`S_i^T p(q,x)=K_i'(a_i)`.

For local effort `x_i`, write `v_i=V_{q x_i}`, `H=diag(K_j'')-S^T V_{qq}S`; assume H nonsingular and the local adoption equilibrium differentiable. From the implicit function theorem:
`a_{x_i}=H^{-1} S^T v_i`.
Thus the equilibrium price response is `p_{x_i}=v_i+V_{qq} S H^{-1}S^T v_i`.

Let `r_j^{(i)}=q_j^T V_{qq}S H^{-1}S^T v_i` (region j's **endogenous-adoption-mediated** price receipts), and `d_j^{(i)}=q_j^T v_i` (its direct quality-mediated price receipts). Let `CS=V-p^Tq`; regional objective `G_i=Pi_i+omega_i CS-C_i` with `Pi_i=p_j^T q_j-K_i`. For the social objective `W=sum_j Pi_j+CS-sum_j C_j`, the exact unilateral marginal wedge is

```text
D_i := dG_i/dx_i - dW/dx_i
     = [d_i - omega_i sum_j d_j - (1-omega_i) V_xi]
       + [r_i - omega_i sum_j r_j].
```

This identity does not require linear inverse demand, symmetric regions, a particular N, or quadratic K. It requires a common market inverse demand derived from V, price-taking farmers, interior conversion, non-singular H, quasi-linearity, and exogenous CS incidence weights. It does not sign the wedge.

**Proof:** By the adoption FOC, `dPi_j/dx_i=q_j^T dp_j/dx_i` (the individual conversion derivative cancels). From `CS=V-p^Tq`, `dCS/dx_i=V_xi-q^T dp/dx_i`. Aggregate welfare satisfies `dW/dx_i=V_xi-C_i'` by the same envelope condition. Substitution gives the identity.

**Own-variety quality-shift corollary:** If `V(q,x)=V0(q)+sum_i f_i(x_i)q_{iN}` and each locality carries only its own producer profit, then `V_xi=d_i=f_i' a_i` and all other direct d_j vanish. Therefore the first bracket is zero, and
`D_i=r_i-omega_i sum_j r_j`.
With **fixed adoption** (all a responses set identically zero), `D_i=0`. This corollary is true under these explicit restrictions, **not** under arbitrary V.

**Counterexample to unconditional A0:** Hold all adoption fixed and add `epsilon*x_1*q_{2N}` to V. Then `V_x1=epsilon*a_2`, direct revenue effect accrues to region 2, and `dG_1/dx_1-dW/dx_1=-epsilon*a_2` despite a being fixed. For epsilon=0.2 and a_2=0.25, the wedge is -0.05. Therefore it is false to claim that fixed adoption always neutralizes decentralization for general quality spillovers.

**Also important:** Endogenous adoption is NOT sufficient for nonzero D_i: incidence terms may offset, as the log/entropy example below demonstrates. The intellectually defensible claim is therefore a *conditional channel*, not a universal necessary-and-sufficient theory.

## R3. Two analytically tractable special cases

**(a) Quadratic V and symmetric N:** Define `h=1-t`, `e=b+n-2c`, `L=K''(a)+2h-e`. Under positive definite demand matrix, equal consumer shares and symmetric interior adoption,

```text
D_i = f'(x) * (N-1)/N * [h+c-b+(e-2h)a] / L.
a* = (h+c-b)/(2h-e)   (provided 2h-e>0).
```

The sign changes at a* **only if a* lies in (0,1)**. When b=n, a*=1/2. The prior checkpoint already contains this result; the present independent SymPy two-region calculation reproduces it. The sign of the unilateral **marginal** wedge cannot automatically rank equilibrium effort levels.

**(b) Nonquadratic separated demand:** For
`V=sum_k alpha_k(x)q_k-sum_k phi(q_k)-beta Q^2/2-r sum_j Q_j^2/2-g (Q_O^2+Q_N^2)/2`,
take `Hphi(z)=z phi''(z)`, `Lphi=K''(a)+phi''(1-a)+phi''(a)`. At symmetric interior points,

```text
D_i = f'(x) (N-1)/(N Lphi) [Hphi(1-a)-Hphi(a)].
```

If Hphi increases with quantities, adoption below 1/2 implies D_i>0 and above 1/2 implies D_i<0. When Hphi is constant, D_i=0 **despite active endogenous conversion**. If Hphi decreases, the signs reverse. For phi''(q)=delta*q^(gamma-1), gamma>0/0/<0 gives exactly these three regimes. This is a *special class*, not a proof for all nonlinear demand functions; N and g do not enter the sign formula at a given symmetric a (though they affect equilibrium a).

## R4. Independent reproducibility findings

An independently authored Python audit, not importing the 04 checkpoint model, performed:

- SymPy symbolic replication for arbitrary quadratic substitution coefficients in the two-region interior case.
- 3 linear benchmark equilibria with unilateral-research best response evaluated numerically, social planner's **symmetric** benchmark, finite-difference marginal wedges, and fixed-adoption derivatives.
- 24 independent nonlinear cases: N=2/3/5, gamma=-1/0/1/2, a=0.25/0.75. In each: implicit Jacobian prediction, closed-form wedge, and fresh finite differences of locally re-solved adoption equilibria.
- Maximum absolute nonlinear finite-difference discrepancy in these 24 cases: **1.28e-9**; linear-wedge finite-difference discrepancy: **3.30e-10**.
- Exact rational social-planner zero-effort certificate at Delta=0.34: `z=-1/100` and eigenvalues of `H-I/R` equal `6/5, 9/5` (strictly positive). Hence
  `W-W0 <= z sum_j a_j - .5 a^T(H-I/R)a <= 0`
  on the feasible set. This establishes **national** global optimality of zero research for the example, not a global proof for all market structures.

Benchmark replication (rounded; Delta varies with t=.5, b=n=.6, c=.45, k=1, k0=1, R=2):
| Delta | Decentralized symmetric x | Planner symmetric x | Decentralized a | Planner a | W decentralized | W planner |
|---|---:|---:|---:|---:|---:|---:|
| 0.80 | .156105 | .125000 | .263524 | .250000 | 18.510986 | 18.512500 |
| 1.70 | .343895 | .375000 | .736476 | .750000 | 19.410986 | 19.412500 |
| 0.34 | .060124 | .000000 | .021793 | .000000 | 18.393863 | 18.400000 |

For Delta=.34, theoretical welfare loss is 0.006137367 or approximately **0.033355%** of W0; these are **unitless model magnitudes, NOT measured real-world effects**. The archived 04 checkpoint reports stronger exact rational global unilateral-best-response checks; those archived proofs were reviewed, but this independent script does not reimplement their exhaustive interval enumeration. This distinction matters.

## R5. Independent prior-art / nonabsorption audit

This audit inspected official journal/publisher HTML or abstracts and, for Manenti–Sandrini (2025), accessible full-text HTML. **It has not reconstructed every competing proof, so nonabsorption is NOT certified.**

| Work | Verified relevant mechanism | Relationship | Verification depth |
|---|---|---|---|
| Akhundjanov, Gallardo, McCluskey & Rickard (2020), *Economic Modelling* 86:88–100, DOI 10.1016/j.econmod.2019.06.004 | Public-university apple-variety commercialization; licenses and downstream profits | Very close institutionally, but chiefly commercialization/licensing, not the proposed decentralized ex-ante R&D choice | Publisher abstract + bibliographic record |
| Jinji & Toshimitsu (2013), *Japan and the World Economy* 28:132–142, DOI 10.1016/j.japwor.2013.09.002 | Strategic quality R&D policy; quality ranking and export-country subsidies/taxes | Research subsidies may switch sign already; such switching is not novel as a conclusion | Publisher summary |
| Galushko, Gray & Oikonomou (2012), *CJAE* 60:295–316, DOI 10.1111/j.1744-7976.2011.01235.x | Public breeder's welfare motive and IP knowledge sharing with farmers | Public breeder/heterogeneous farmers already known | Publisher abstract |
| Hervouet & Langinier (2018), *JARE* 43:118–150 | Breeders' rights, farm self-reproduction and too much/too little innovation | Over/underinvestment in varietal innovation already known | Official journal abstract |
| Manenti & Sandrini (2025), *Journal of Industrial Economics* 73:391–410, DOI 10.1111/joie.12414 | Endogenous directions and effort under patentability; general theory and Cournot illustration | Adding a decision stage alone will not distinguish the paper | Accessible publisher full text |
| Manenti & Sandrini (2026), *Technology Licensing and the Direction of Innovation*, SSRN doi 10.2139/ssrn.6312327 | Licensing changes R&D direction/intensity under uncertainty | Adjacent but different margins; direct theorem-by-theorem nonabsorption remains OPEN | Abstract, full article NOT inspected |

Publisher pages:  
https://www.sciencedirect.com/science/article/abs/pii/S0264999318312938  
https://www.sciencedirect.com/science/article/abs/pii/S0922142513000479  
https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1744-7976.2011.01235.x  
https://jareonline.org/articles/plant-breeders-rights-patents-and-incentives-to-innovate/  
https://onlinelibrary.wiley.com/doi/full/10.1111/joie.12414  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6312327

**Label-stripping test:** Remove the terms prefecture, crop, farmer and new variety. The general theorem says 'a local decision maker differs from the sum of local welfare payoffs because downstream quantity adjustment redistributes price receipts across jurisdictions'. This is a conventional fiscal-externality/business-stealing/pecuniary-externality structure, plausibly available in prior work. Novelty must be carried by a **specific, falsifiable incidence reversal / policy-design result that existing public-R&D + adoption theory does not already encompass**, not by the general identity itself.

## R6. Economic significance, policy and observables

The appropriate question is **not** whether any grant expands public breeding, but whether a national matching grant moves a region's R&D toward or away from socially valued research at the actual conversion share and cross-variety demand curvature. The archived 04 checkpoint's calibrated-*looking* but uncalibrated theoretical examples show a 10% grant may reduce welfare in an already-overinvesting case while improving it in an underinvesting case. The transfer-financing conventions must be explicit; grants are not a free resource gain.

Empirical bridge: variety-by-year planted hectares or harvested area, age of orchards and replacement costs, realized varietal prices/shipments, substitution across origins and harvest windows, R&D budgets and lagged attributes. The model requires quantity-specific inverse-demand curvature, not simply a high value of observed new-variety market share. Identification should distinguish R&D-caused adoption from correlated quality/weather shocks. A causal estimate, simulation calibrated to estimated demand, or disciplined parameter bounds would materially improve policy significance; none was performed in this checkpoint.

## R7. Adversarial referee challenge

1. 'Only standard R&D competition plus adoption': **partially valid**; answer must rest on an independently demonstrated reversal condition/policy consequence.
2. 'Over/under is already known': **valid**; novelty cannot be the sign alone.
3. 'Adoption just makes prices endogenous': **substantial unresolved risk**; the general identity supports this criticism.
4. 'Linear/symmetric restrictions': **partly mitigated** by the unrestricted identity and nonlinear exact sign-class result; non-symmetric *sign* theorem unresolved.
5. 'Envelope formula is not novel': **valid**; explicitly conceded.
6. 'Agriculture application is not broad IO contribution': **valid at IJIO level** absent transportable novel result and empirical/model significance.

## R8. Journal fit assessment (subjective editorial-risk assessment, NOT estimated acceptance probabilities)

Use A/B/C/D as defined in the request (A reasonable external review; B plausible after revisions; C current contribution/completeness lacking; D fit poor). At this stage **no journal receives A**, since nonabsorption and evidence remain incomplete.

| Journal | Grade | Reason |
|---|---|---|
| IJIO | C | Transferable identity exists, but a standard incidence effect is not a demonstrated substantial novel IO mechanism |
| RIO | C/B (conditional) | IO innovation policy fits, but requires distinct non-absorbed proposition and broader lessons |
| JARE | B | Officially welcomes creative agricultural economics; breeder-rights innovation theory precedent |
| CJAE | B | Officially publishes theoretical and policy research in agricultural economics; IP/public breeding precedent |
| ARER | B | Worldwide agricultural/resource economics fit; empirical/institutional anchoring still needed |
| AJAE | C | Originality and policy relevance requirements not yet met convincingly |
| ERAE | C | Innovative theory is in scope but generality and differentiation insufficient currently |
| Agricultural Economics | C/B | Better after econometric/calibrated or substantively grounded policy connection |

Official scope sources: https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187 ; https://jareonline.org/editorial-policies/ ; https://onlinelibrary.wiley.com/page/journal/17447976/homepage/guide.htm ; https://www.cambridge.org/core/journals/agricultural-and-resource-economics-review/information/author-instructions ; https://academic.oup.com/erae/pages/About ; https://www.aaea.org/publications/ajae ; https://iaae-agecon.org/page/journal_policies

## R9. Research iteration and minimum model

**Retain** the two-region/two-generation competitive farmers, endogenous one-dimensional conversion, local quality effort and regional ownership. Use the **general incidence identity as a framing lemma**, not the headline novelty claim. Use one analytically clean nonlinear demand class for a signed proposition; move the N-region matrix exposition and supporting algebra to the Appendix. Avoid introducing endogenous licensing, product design or R&D direction until a distinctive mechanism requires it.

Research avenues considered:
- H1 Replacement as mediator: strong mathematical clarity; **novelty risk remains**.
- H2 Territorial seed-use permissions: unique institution, but must endogenize/compare rights regimes to produce a new proposition; substantial added complexity; **exploratory only**.
- H3 Counter-theorem to conventional R&D sign: the sign reversal and entropy neutrality survive; but reversals known more broadly; **requires closer equivalence audit**.
- H4 Grant-policy rule tied to observable varietal composition: most promising practical extension; derive an implementable robust sign test, welfare-weighted contribution and real data ranges; **selected for next research gate**.

Do NOT claim an unproved new law from H4 now. No arbitrary ad hoc regime addition is justified.

## R10. Prioritized outstanding tasks

**Required before submission:** (1) exact theorem-by-theorem near-prior equivalence audit including 2026 licensing full text; (2) nontrivial policy/design proposition beyond the envelope incidence formula; (3) unilateral global Nash and planner certification for final chosen parameter domain, plus boundary conversion; (4) defensible agronomic institutional evidence and plant-breeding-specific rationale; (5) coherent English paper integrating proofs and literature.

**Desirable before submission:** empirical bounds or estimation for substitution/conversion costs, explicit asynchronous harvest windows, heterogeneity/sensitivity, subsidy finance alternatives.

**Future work only:** endogenous research directions, dynamic orchard ageing, stochastic innovation, endogenous geographic licensing, fully asymmetric arbitrary N global equilibrium, general existence theorem.

### Reproducibility/provenance
This report complements, does not replace, `checkpoints/2026-10-24/04_varietal_replacement/`. The independent exact/numerical calculations ran under Python 3 with NumPy, SciPy, SymPy. Script output may differ at approx 1e-8 because scipy optimization is numerical. The general arbitrary-V decomposition is proved algebraically, but a mechanically verified proof assistant certificate was NOT produced. Baseline strong global best-response claims should be attributed to the archived code rather than this independent audit. This is a research audit, not an accepted publication or an assertion of prior-art completeness.
