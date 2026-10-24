# JAFIO submission checklist

Verified date: 2026-10-25 JST. **Overall CONDITIONAL / NOT READY for final submission.** This file separates source verification from implementation. Final manuscript/CI outcomes belong in REPORT.md and must not be inferred from this checklist.

## Current official evidence

The 2025-10-11 author guide supersedes the older 2024 guide. Its indexed sections were retrieved; direct publisher PDF requests returned HTTP 405. It was not downloaded or visually inspected in full.

| Item | 2025 guide requirement or evidence | Status/action |
| --- | --- | --- |
| Abstract | Approximately 200 words, one paragraph; self-contained | 197-word revised abstract inspected; no BAE 150-word cap. |
| Keywords | 3–6 lowercase terms, semicolon-separated | Five revised terms inspected; lowercase and semicolons fit. |
| Headings | Numbered Title Case; no terminal period; maximum four levels; split levels need two subheads | Revised Title Case inspected; final hierarchy QA remains in REPORT. |
| References | Alphabetical; follow separate Reference Style Sheet; text/list correspondence | Author–year natbib is provisional until exact sheet comparison. |
| Cover letter | Required, addressed to Editor-in-Chief, explaining novelty | Prepare separately; no invented author assertions. |
| ORCID | Explicit mandatory statement follows recommendation | Supply real ID on separate title page. |
| Declarations | Ethical/Legal template required, including data availability | Actual template completion pending. |
| Research AI use | Tool/purpose in Methods; preparation use in declarations template | Disclosure must cover substantive assistance. |
| Submission | ScholarOne dgjafio | No final submission authorized. |

Source: https://www.degruyterbrill.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_Instructions%20for%20Authors%20JAFIO.pdf (indexed pp.3,4,10).

## Journal route and source-file preparation

Official homepage welcomes theoretical articles and notes. **Choose Research Article**, because this manuscript needs linked results and globally sufficient proofs, rather than selecting Note merely because some examples are short. Current article-category-specific limits in the separate Manuscript Checklist remain unverified.

Source: https://www.degruyterbrill.com/journal/key/jafio/html

The older official manuscript-preparation guide explicitly accepts LaTeX, requests a PDF where mathematical material is present, links a journal LaTeX package, and places appendices before references. The 2025 guide's verified indexed sections do not contradict native LaTeX, but current exact upload slots, template package contents, equation-symbol formatting and appendix order were not independently downloaded. Use .tex/.bib and PDF, preserve a self-contained source ZIP, and verify portal conversion before final submission. Do not describe an ordinary article.cls file as the official journal template. The old flexible heading-case instruction is superseded by the 2025 Title Case instruction.

Older official preparation guide:
https://www.degruyterbrill.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_MANUSCRIPT%20PREPARATION%20GUIDELINES.pdf

Official linked template URL (existence of link verified; ZIP compatibility not certified):
https://www.degruyter.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_LaTeX-Template%20for%20Authors.zip

Older 2024 author guide corroborates double-blind review and a separate title-page upload. The newer guide and actual portal must control any further changes. Anonymous referee files should have no identifying GitHub URLs, real author names, email, affiliations, local home paths or identifying PDF metadata. Audit scripts and the repository are author-facing working material; their existence does not make them suitable blinded supplementary files automatically.

https://www.degruyterbrill.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_Instructions%20for%20Authors.pdf

## Required factual author input

| Item | Current status |
| --- | --- |
| Legal name, affiliation, corresponding email and ORCID | Not supplied as verified submission facts in this task. Do not infer from account/profile/repository. |
| Funding and competing interests | Author confirmation required; no unsupported “none” declaration. |
| Author contributions | Verify substantive human conception, economic interpretation, theory/proof review and final critical revision. AI/test success is not that evidence. |
| Final approval, originality and simultaneous submission | Actual author confirmation required. |
| Data statement | No empirical dataset; accurately describe code and proof materials actually available in blinded package. |
| Ethical/legal template and title page | Complete after factual author input; do not fabricate fields to make the package look final. |
| Supplementary reproducibility package | Check all input dependencies, paths, metadata and anonymity. Distinguish symbolic/numeric results from Lean theorem scope. |
| Reference Style Sheet | Exact punctuation/format not independently obtained; plainnat not certified as journal style. |
| Official LaTeX package | Obtain and test or receive office/portal confirmation that generic source is acceptable. |

These are specific unresolved submission facts, not assertions that the journal necessarily requires every possible declaration in the main anonymous manuscript.

## Fees

Checkpoint 42 establishes publisher support for no standard subscription-publication charges and no optional OA APC when OA is declined. Preserve that verified finding. A separate submission/handling fee has not been positively located; its absence is not independently guaranteed. Optional OA prices need not be accepted or paid. Do not request payment or choose OA in this task.

Source: https://www.degruyterbrill.com/publishing/about-us/new-website-faqs/authors-editors ; checkpoint42/REPORT.md. Final zero-cash gate: inspect the submission conditions for any mandatory charge or seek precise editorial confirmation if unresolved.

## September 2026 AI-policy gate

The publisher policy rejects AI-generated papers, excludes AI authorship, requires disclosure of substantial output and research-method use, and leaves responsibility with human authors. Simple proofreading receives different treatment. This project's actual assistance extends beyond proofreading. The policy is not interpreted here as an automatic ban on all AI-assisted research, or as automatic acceptance once a disclosure is added. The human intellectual contribution and review record remains necessary; seek publisher clarification if the production process falls into its ambiguous AI-generated-paper boundary.

Source: https://www.degruyterbrill.com/publishing/for-authors/author-policies/artificial-intelligence (indexed policy dated September 2026; direct fetch restricted).

See AI_USE_AND_AUTHOR_ACCOUNTABILITY.md for the factual record and proposed disclosure. Do not mark this gate PASS solely because Lean, SymPy or agents audited the paper.

## Final technical gates to record separately

- Final-commit GitHub Actions success with URL and SHA; all referenced exact and symbolic checks, plus scoped Lean build.
- Clean LaTeX/BibTeX build; no unresolved references/citations or significant box warnings.
- All PDF pages visually inspected; anonymous metadata and source archive checked.
- Stage 13 equation/theorem scope invariant; no unsupported nonlinear or strategic-interaction generalization.
- Full-text Winfree–McCluskey overlap check remains a targeted novelty limitation until obtained. No positive duplicate-theorem evidence currently justifies reopening all Stage 6 work.
- Research Article source ZIP, peer-review PDF, separate real title page, cover letter and publisher forms ready before actual final submission.

No final submission, journal communication, main-branch change or merge is performed by this checklist.
