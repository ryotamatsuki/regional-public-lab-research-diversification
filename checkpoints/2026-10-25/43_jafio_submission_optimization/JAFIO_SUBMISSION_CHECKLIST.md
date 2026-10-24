# JAFIO submission checklist

Verified date: 2026-10-25 JST. **Overall CONDITIONAL / NOT READY for final submission.** This file separates source verification from implementation. Final manuscript/CI outcomes belong in REPORT.md and must not be inferred from this checklist.

## Current official evidence

The 2025-10-11 author guide supersedes the older 2024 guide. The complete 12-page official PDF was subsequently downloaded through direct urllib access and its full extracted text inspected. Web open had returned HTTP 405; that earlier access limit is superseded for this guide.

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

Official homepage welcomes theoretical articles and notes. **Choose Research Article**, because this manuscript needs linked results and globally sufficient proofs, rather than selecting Note merely because some examples are short. The full 2025 guide p.2 explicitly lists Research Article and Note, alongside Review, Book Review, Letter, Editorial, Economic Perspectives, Erratum, Comment and Reply. Category-specific length limits in the separate Manuscript Checklist remain unverified.

Source: https://www.degruyterbrill.com/journal/key/jafio/html

The older official manuscript-preparation guide explicitly accepts LaTeX, requests a PDF where mathematical material is present, links a journal LaTeX package, and places appendices before references. The complete 2025 guide confirms appendix placement before references (p.12), consecutively numbered editable displayed equations when referenced, Latin/Greek symbols (p.11), and supplementary files no larger than 10 MB each (p.12). Exact current portal slots and template compatibility require separate testing. Use .tex/.bib and PDF, preserve a self-contained source ZIP, and verify portal conversion before final submission. Do not describe an ordinary article.cls file as the official journal template. The old flexible heading-case instruction is superseded by the 2025 Title Case instruction.

Older official preparation guide:
https://www.degruyterbrill.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_MANUSCRIPT%20PREPARATION%20GUIDELINES.pdf

Official linked template URL (existence of link verified; ZIP compatibility not certified):
https://www.degruyter.com/publication/journal_key/JAFIO/downloadAsset/JAFIO_LaTeX-Template%20for%20Authors.zip

Older 2024 author guide corroborates double-blind review and a separate title-page upload. The complete 2025 guide independently confirms separate title-page requirements (p.9), including a short title of at most 75 characters, correspondence details and manuscript/table/figure/supplement counts. The actual portal must control any further changes. Anonymous referee files should have no identifying GitHub URLs, real author names, email, affiliations, local home paths or identifying PDF metadata. Audit scripts and the repository are author-facing working material; their existence does not make them suitable blinded supplementary files automatically.

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

Source: https://www.degruyterbrill.com/publishing/for-authors/author-policies/artificial-intelligence (complete HTML retrieved by direct urllib; September 2026 policy date and full policy text inspected).

See AI_USE_AND_AUTHOR_ACCOUNTABILITY.md for the factual record and proposed disclosure. Do not mark this gate PASS solely because Lean, SymPy or agents audited the paper.

## Final technical gates to record separately

- Final-commit GitHub Actions success with URL and SHA; all referenced exact and symbolic checks, plus scoped Lean build.
- Clean LaTeX/BibTeX build; no unresolved references/citations or significant box warnings.
- All PDF pages visually inspected; anonymous metadata and source archive checked.
- Stage 13 equation/theorem scope invariant; no unsupported nonlinear or strategic-interaction generalization.
- Full-text Winfree–McCluskey overlap check remains a targeted novelty limitation until obtained. No positive duplicate-theorem evidence currently justifies reopening all Stage 6 work.
- Research Article source ZIP, peer-review PDF, separate real title page, cover letter and publisher forms ready before actual final submission.

No final submission, journal communication, main-branch change or merge is performed by this checklist.

## Final format implementation — supersedes earlier provisional format notes
The complete 2025-10-11 guide, official linked LaTeX ZIP and Chicago Author-Date
Reference Style Sheet have now been downloaded and inspected. The paper applies
the unmodified official dgruyter.sty (and official logo), with an English/legacy
babel compatibility guard in paper.tex. No dummy DOI or acceptance data are used.
The template's generic numbered-reference example is superseded by the
journal-specific Chicago author-date style sheet. A clearly labelled LOCAL LPPL
adaptation of plainnat, jafio-chicago-local.bst, implements the 15 article/book
entries; it is not publisher-issued. Citation parentheses/year punctuation,
surname-first references, quoted article titles, year position, volume/issue,
page/article number and DOI URLs were checked. Appendices precede references.
Current headings have at least two sibling subheadings where subdivided.
Anonymous exact-code/Lean supplement was built and independently extracted/run;
it is below the 10MB per-file limit. Remaining portal verification and actual
author declarations are not resolved by these technical checks.
