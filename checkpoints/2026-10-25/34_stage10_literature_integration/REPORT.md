# Stage 10-L — Limited Literature Integration and Final PDF Regression

**Date:** 2026-10-25 JST
**Branch:** `research/2026-10-24-ijio-response-audit`; Draft PR #2.
**Parent gates:** Stage 6 bounded agricultural-institution-specific prior-absorption closure, Stage 8 Theory Freeze v2, Stage 9 GO, Stage 10 GO.
**Decision:** **PASS / COMPLETE — targeted literature integration; preserve frozen research theory, do not reopen general novelty claims.**

## Final output

- Revised manuscript: `checkpoints/2026-10-25/32_stage10_manuscript/paper.tex`.
- Verified references: `checkpoints/2026-10-25/32_stage10_manuscript/references.bib`.
- Exact frozen-proposition regression: `checkpoints/2026-10-25/32_stage10_manuscript/verify_manuscript.py`.
- Historical Stage 10 original completion certificate `checkpoints/2026-10-25/33_canonical_stage10_gate_closure/REPORT.md` remains an archived statement about the previous 10-page draft. **This addendum supersedes its citation count and PDF pagination, not its model/proof freeze.**
- **Bibliography:** 14 distinct registered journal/book records; **all 14 are explicitly cited in the manuscript**. Previously 9 records with only 5 cited. Added 5 new verified records and integrated 4 formerly uncited existing records.
- **New final PDF:** 11 pages, A4, bibliography printed across pages 10–11 with all 14 entries. PDF lives as [GitHub Actions artifact 12569999242](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40118920477) and can be downloaded from the successful workflow run; artifacts have finite retention. This checkpoint commits neither a binary PDF nor a new unverified numerical figure.

## Reference-by-reference narrative function

| Literature group | Source | What current text attributes to it | What's different here |
| --- | --- | --- | --- |
| Public agricultural research | **Swinnen & de Gorter (1998)**, AJAE 80(1):107–115, DOI 10.2307/3180273 | Government response of commodity policies changes measured public-research social benefit | Simultaneous territorial public quality *efforts*, competitive old/new conversion, nationwide welfare |
| Agricultural research, practice | **Richards & Padilla (2002)**, JAAE 34(3):401–415, DOI 10.1017/S1074070800009202 | Dynamic commodity R&D/promotion applied to Washington apples | Static upstream regional public research game with fixed land follower |
| New products and positive benefits | **Wang & Çakır (2020)**, Agricultural Economics 51(3):445–457, DOI 10.1111/agec.12564 | Empirical consumer-surplus gains from Honeycrisp variety introduction | Paper's negative-welfare special family is *not* a claim that all actual new varieties are harmful |
| Public breeding and licensing | **Akhundjanov et al. (2020)**, Economic Modelling 86:88–100, DOI 10.1016/j.econmod.2019.06.004 | Public university-bred apple commercialization and licensing | Quality selected directly by public local lab, not license design after innovation |
| Classic private promotion welfare | **Dixit & Norman (1978)**, Bell JE 9(1):1–17, DOI 10.2307/3003609 | Private vs social return to advertising, familiar welfare incidence | No generic first-ever excessive research claim |
| Commodity competition | **Alston, Freebairn & James (2001)**, AJAE 83(4):888–902, DOI 10.1111/0002-9092.00217 | Commodity group noncooperative promotion may overspend | Territorial public local G_i and national full CS benchmark, resource replanting |
| Funding mechanisms | **Freebairn & Alston (2001)**, AJARE 45(1):117–145, DOI 10.1111/1467-8489.00136 | Levy and subsidy funding can affect producers' optimal advertising | Own budget directly creates quality and local objective includes half CS; not first-ever government support |
| Socially optimal promotion | **Cardon & Pope (2003)**, JARE 28(2):185–200, DOI 10.22004/ag.econ.31098 | Optimal generic advertising depends on agricultural market structure, may be zero in conditions | Exact public breeding positive research Nash versus zero nationwide funding is model-specific, not generic discovery |
| Related markets incidence | **Kinnucan & Miao (2000)**, AJAE 82(3):672–678, DOI 10.1111/0002-9092.00059 | Generic advertising distributional impacts on related products | Public continuous quality effort stage is added, not attributed to them |
| Resource allocation | **Balagtas & Kim (2007)**, AJAE 89(4):932–946, DOI 10.1111/j.1467-8276.2007.01037.x | Related-product demands and shared production inputs | Cannot claim novelty of resource reallocation alone |
| Geographical new products | **Lence et al. (2007)**, AJAE 89(4):947–963, DOI 10.1111/j.1467-8276.2007.01036.x | Geographic differentiation/new product development/marketing organization | Competitive growers conditional efficiency old; separate public research R&D game is research object |
| Quality R&D strategic policy | **Jinji & Toshimitsu (2013)**, Japan and the World Economy 28:132–142, DOI 10.1016/j.japwor.2013.09.002 | International oligopoly firms and strategic R&D subsidies/taxes with quality differentiation | Labs directly choose quality; growers are price-takers; no universal public R&D theorem claim |
| Socially negative innovation | **Zhang (2022)**, The Manchester School 90(1):59–76, DOI 10.1111/manc.12388 | Negative expected social value possible in cost-reducing patent-R&D race | This paper's continuous public quality investment and competitive farmer conversion are different |
| Japan institutions | **OECD (2019)**, Innovation, Agricultural Productivity and Sustainability in Japan, DOI 10.1787/92b8dff7-en | Prefectural research labs and locally adapted varieties | Institutional motivation only, not empirical validation of G_i=Pi_i+CS/2-C_i |

## Selection and exclusion principles

This is a **source-checked, purpose-driven** citation set, not an exhaustive bibliography. Prior Stage 6 compared further work (e.g. de Gorter & Swinnen 1996, Toshimitsu 2014, Häckner & Herzing 2026). They were not added to the compact 11-page manuscript because their role would substantially duplicate either the fiscal/public-research, strategic R&D, or adoption-market citations retained above. Reopen literature scope only if Stage 11 identifies an essential near-parent or demonstrable citation omission.

Primary bibliographic publisher/journal records checked for *new* sources:
- Swinnen & de Gorter 1998: https://academic.oup.com/ajae/article-abstract/80/1/107/48205
- Freebairn & Alston 2001: https://doi.org/10.1111/1467-8489.00136 and https://www.mendeley.com/catalogue/4aabc9c5-9bf2-3abb-8e32-2719d2d32d91/
- Richards & Padilla 2002: https://doi.org/10.1017/S1074070800009202 (journal volume and pages checked against Cambridge 2002 issue; journal article published 2002 though online metadata may show 2015 digitization)
- Jinji & Toshimitsu 2013: https://www.sciencedirect.com/science/article/abs/pii/S0922142513000479
- Wang & Çakır 2020: https://onlinelibrary.wiley.com/doi/10.1111/agec.12564
- Original prior sources and access limitations in `checkpoints/2026-10-24/25_stage6_final_absorption_closure/REPORT.md`.

**Reading-depth disclosure:** Published bibliographic metadata, primary publisher abstracts and earlier Stage 6 original proposition comparisons were checked. Not every new article's full publisher proof text was accessible, and this bibliography improvement does not certify full-article nonabsorption or the priority of a novel *general* theorem.

## Mathematical and manuscript change control

- Changes were restricted to the Introduction's literature/context/contribution paragraphs, five extra reference records, and one reference-completeness assertion in the existing Stage 10 verifier.
- No model assumptions, objective function, price matrix, research/adoption strategy spaces, exact parameter family, lemma, proposition, corollary, theorem proof, mathematical display or substantive e>0 computation changed.
- Automated regression enforces identical theorem and corollary statements with Stage 8-frozen original, exactly 30 display math blocks with the **same single inherited P2 H→H_phi notation correction**, 32 unique LaTeX labels, exactly 14 cited bibliography keys, no orphan bibliography entries, and resolved citations.
- It is acceptable that literature integration extends the compact manuscript to **11 pages**: reference coverage and readable type size take precedence over artificially staying at 10.

## Actual final CI and PDF inspection

**Final run [40118920477](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40118920477): SUCCESS.** Its log shows:
```
PASS: Stage 10 frozen lemma/proposition/corollary statements identical
PASS: 30 math display blocks, one P2 notation correction only
PASS: 32 unique labels, 14 resolved citation keys
Validated PDF byte size: 249280
```
- LaTeX + BibTeX fully built using the same Stage 10 workflow; final log passed unresolved references/citations test; 14 bibliography records visibly rendered.
- Downloaded the final GitHub artifact (ID `12569999242`), extracted actual `paper.pdf`, checked 11 A4 pages with `pdfinfo`, read the rendered bibliography with `pdftotext`, and rendered **all 11 pages** to a PNG contact sheet for visual inspection. No conspicuous overlap or typesetting defect on inspection.
- Earlier failed/canceled interim workflow results (before BibTeX file was added) remain in GitHub Actions and are superseded by the definitive green run.

## Gate status and handoff

**STAGE 10-L PASS:** limited literature correction finished, manuscript now cites 14 relevant and grounded publications/institutional sources with nondecorative roles; Theory Freeze v2 and Stage 9 reproducibility remain intact. The prior Stage 10 general construction gate stays GO after this repair.

**Next canonical step:** Stage 11 independent hostile-referee review of the **updated** `32_stage10_manuscript/paper.tex` rather than old 5-citation/10-page PDFs. Still NOT SUBMISSION GO; Stage 12 journal/fees/format and later checks are open. Do not merge Draft PR #2 or alter main during this bibliographic operation.
