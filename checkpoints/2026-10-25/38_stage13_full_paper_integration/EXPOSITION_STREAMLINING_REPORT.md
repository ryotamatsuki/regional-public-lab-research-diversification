# Stage 13 — Exposition Streamlining Report

**Date:** 2026-10-25 JST.  
**Stage 12 target:** *Bio-based and Applied Economics* (BAE), **Full Research Article**. Not a Policy Paper or "Research Note". Current official 2026 guide: https://oaj.fupress.net/index.php/bae/about/submissions (full articles normally 6,000–8,000 words **including abstract, appendices, references**; abstract <=150; max five keywords and three JEL; references before appendices; Word/OpenOffice/RTF, double-spaced, 12pt and numbered headings; anonymous manuscript). Stage 13 streamlines the academic argument, **not** the journal packaging/conversion finished by Stage 14.

**Certified paper scope:** Narrow institutional agricultural applied theory, not a novel general public R&D/game theory result; Stage 11 refereeing internal GO subject to source-absorption and editorial significance residual risks. Theory Freeze v2 unchanged.

## 1. Scope/profile, quantitative changes

- Profile: **THEORY-FIRST — concise applied agricultural research article**.
- Primary logical chain: decentralized public breeding quality -> efficient competitive old/new grower substitution -> local-versus-national research incidence -> conditional adoption-share wedge -> exact P3+ welfare-negative global research Nash -> bounded variants.
- Stage 10 original 34,127 UTF-8 characters -> Stage 13 32,422, a reduction of 1,705 characters (**5.0% overall**, including unchanged proof-heavy mathematical appendix). Introduction **614 -> 437 word-like tokens**, reduction **177 / 28.8%**. Abstract **156 -> 129** words; official 150-word cap satisfied. JEL **4 -> 3** (`H77,O32,Q16`).
- **30 displayed mathematical environments unchanged**, all underlying lemma/proposition/corollary source statements unchanged; same number of proofs; 14 distinct bibliography citations retained. All mathematics, parameter intervals, price/adoption primitives, four-good model, full off-path P3+ branch proof and numerical values remain intact.
- Reordered back matter to **References before Appendix**, following BAE manuscript-file order. Added a specific declaration of AI assistance and a theoretical data/code paragraph before bibliography. No claimed fee waiver or external journal acceptance.
- Moved **secondary e=3/10 coupling benchmark** (all parameters, effort/adoption fractions, welfare magnitude and exact computation limits) from main robustness subsection into a named appendix on computation. Kept **e=1/100** main-body evidence because without it the e=j=0 global theorem could be mistaken for strict interregional research best-response competition.
- Removed the administrative appendix "Derivation and proof crosswalk" containing internal checkpoint folder names, which were not publication-facing economics; retained **all essential primitive-to-Jacobian** and global three-branch proof appendices. The research-only crosswalk and Git SHA remain documented in Stage 11 and separate Reviewer Verifiability Report.

## 2. Introduction compression — arrival budget

New five-paragraph Introduction:
1. **Question/why/institution:** cross-border prices and decentralized prefectural public breeding (OECD cited).
2. **Model/findings/method:** public leader research + competitive grower land substitution, sign-reversing conditional marginal wedge, globally harmful positive investment with all planting regimes.
3. **Agricultural precedent:** public research policy, grower/innovation welfare and public-university apple licensing (Swinnen/de Gorter; Richards/Padilla; Wang/Çakır; Akhundjanov).
4. **Theory priority/precise incremental novelty:** standard noncooperative promotion, related commodities, shared-input reallocation, quality R&D policy, negative patent racing; all 14 source records cited; only institutional research-adoption game is claimed.
5. **Applicability limit:** CS/2 weighting, deterministic research and absent licensing/heterogeneity/dynamics; no empirical budget prescription.

**Reader-arrival contract:** question in first intro paragraph; mechanism and full headline finding by second; exact primitive players and G_i/W in first model subsection; first main P1 wedge in Section 3; P3+ exact national zero benchmark in Section 4; robustness in Section 5; complete special-class price incidence in Appendix A; global branch comparison in Appendix B. Exact page numbers must be read from rendered revised PDF in final Stage 13 report; no universal page landmark used.

**Pass:** literature no longer delays the economic question and result; introduction length proportional to concise applied theoretical paper without dropping the near-parent priority statements.

## 3. Section-purity / classification register

| Original/new content cluster | Class | Decision and reason |
| --- | --- | --- |
| Abstract | CORE | Compress, retain uncertainty/conditions, no fabricated policy impact |
| Intro: funding, growers, four-good market, national result | CORE | Essential low-latency economic narrative |
| Intro: priority comparison across 14 original sources | CORE/HELPFUL | Essential known-mechanism credit but shortened into two functions: agriculture and generic micro theory |
| Intro: assumptions/caveats | CORE | Prevent unconditional generality/real-world optimality overclaim |
| Section 2 full game: timing, strategies, B matrix, CS/2, planting corners | CORE | Mathematical object; remains self-contained |
| Section 2 conditional efficiency lemma | CORE | Separates downstream adoption efficiency from upstream public research |
| Section 3 P1, incidence bridge and *on-KKT* condition | CORE | Main economic signed-wedge mechanism; protect price and CS derivation |
| Section 3 conditional symmetric planner/district comparison | HELPFUL | Quantifies research/adoption gaps but isn't new universal theorem |
| Section 3 P2 equal-curvature class | CORE (bounded) | Explains genuine dependence on demand shape and negative scope |
| Section 4 P3+ global 0,partial,1 planting proof | CORE | Strongest existence result, exact boundary and unrestricted planner benchmark |
| Section 4 unilateral-versus-mutual payoff distinction | CORE | Avoids known analytic interpretation regression |
| Section 5 quartic and unequal-curvature stress tests | HELPFUL -> **condensed** | Retain successful AND failed tests with exact bounds, prevent portability inflation |
| Section 5 primary e=1/100 interacting rational example | HELPFUL (scope-critical) | Shows positive interaction beyond independent-BR example, exact SymPy not Lean-global |
| Section 5 secondary e=3/10 rational benchmark | APPENDIX | Adds bounded supporting evidence but distracts from theorem |
| Section 5 institutional/external validity | CORE | Limits applicability, empirical and legal abstractions |
| Discussion/Conclusion repeated mechanism/policy caveat | CORE after compression | Two distinct jobs: policy scope versus answer to question; no new theorem |
| Appendix "Derivation and proof crosswalk" mentioning internal checkpoint paths | DELETE from article, RETAIN AS AUDIT ARTIFACT | Unnecessary workflow jargon; proofs and mapping persist in manuscript-facing appendices and Stage 13 reviewer report |
| Appendix nonlinear price/Jacobian/incidence derivation | APPENDIX (proof-critical) | Must be retained exactly; Lean only conditional rank-one algebra |
| Appendix global-deviation/cutoff proof | APPENDIX (proof-critical) | Must be retained exactly; prevents interior-only Nash extrapolation |
| Appendix computational method and second e>0 example | APPENDIX | Supports replicability while main body stays focused |
| AI and data-code declaration | CORE publisher compliance | AI assisted prose, literature, formal and numeric proof tasks, human author responsible |
| Bibliography | CORE | 14 cited sources; now before technical appendices |
| Figure/table | NONE | No independent economically grounded inference requires an exhibit |

## 4. Five-exhibit thought experiment

**Main figures = 0; main tables = 0**; no mandatory exhibit is invented. Main result transport vehicles are **three propositions, one lemma and one corollary**, together with essential displayed equations. A schematic timing picture would duplicate a concise two-stage sentence. A welfare plot for synthetic parameters would add scale without economic inference. Absent exhibits do not reduce theorem verifiability when branch equations and scope conditions remain printed.

## 5. Compression-without-damage and remaining risk

**Preserved:** four-good B and public CS/2 objectives; constrained planting KKT including adoption corners; P1 strictly symmetric interior and feasible threshold sign; national versus region first-stage global qualification; restricted *same old/new phi* P2 and negative asymmetric-curvature T2; P3+ exact z in (zCut,0], four Nash at boundary; off-equilibrium local payoff from unreduced V; all research unilateral regimes and full feasible planner square-completion; e=0 independence vs separate rational e>0 checks; formal proof scope e>0 SymPy only.

**Known unresolved for Stage 14:** Current PDF-producing source remains LaTeX 11pt single-spaced, whereas BAE requests Word/OpenOffice/RTF and 12pt double-spaced with line numbers. Need journal-style references, Highlights, separate title page and author details, double-blind-safe code links, exact all-inclusive word count, actual funding and conflict assertions, cover letter and final AI disclosure review. BAE Full Article normal 6,000–8,000 words: do NOT add new economics or filler merely to meet a soft normal-range description; raise shorter format fit and any exceptional length permission honestly. Current LaTeX is an integrated theory master, NOT an upload-ready BAE Manuscript File.

**Stage-13 close depends on current 38/ CI PDF and page inspection.** This report is the auditable architecture change certificate; see accompanying Reviewer Verifiability Report for specialized derivation audit.
