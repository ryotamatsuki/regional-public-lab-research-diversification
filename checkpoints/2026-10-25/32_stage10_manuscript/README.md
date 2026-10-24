# Stage 10 — theory-first manuscript (working submission draft)

**Source of truth:** Stage 8 Theory Freeze v2 at ../30_canonical_stage8_theory_freeze_v2/REPORT.md. Stage 9 source manifest pins the *earlier* provisional text separately; do not overwrite that frozen historical source.

## Purpose

The article analyses territorial public breeding research preceding private competitive old/new crop allocation. Keep the original economic model, conditional lemma, P1, P2, P3+ and all exact proof restrictions unchanged; improve positioning and text clarity rather than add generalized strategic R&D claims.

## Production assets

- paper.tex: revised single-question agricultural applied theory manuscript. Anonymous and neutral title page.
- references.bib: original seven entries plus the 2019 OECD institution source and a 2020 public-university cultivar licensing comparator.
- verify_manuscript.py: compares *all* displayed mathematical environments and theorem statements to the Stage 8-frozen original; the sole permitted equation change is to correct H → H_\phi in the P2 display. Checks LaTeX labels and citation keys.
- GitHub Actions .github/workflows/public-breeding-stage10.yml: runs that check and builds a PDF with BibTeX, errors on unresolved labels/citations, and uploads PDF as a workflow artifact. Source-level checks are not independent journal referee review.

Previous successful frozen Lean and Stage 9 SymPy CI are not inflated into "the entire paper is formally proved." This manuscript uses the same static two-stage agricultural model and reports its bounded exact results. No quantitative policy recommendations about actual prefectures.

Manuscript figures/tables: **none essential**. Every main result is carried by a stated proposition or compact analytic displayed equation and proof. A fabricated parameterized plot would not supply a new insight. The Stage 10 figure/table gate passes with zero exhibits; appendices retain derivation bridges.

**Submission remains prohibited until Stage 11 and formal journal-specific checks.** Journal-specific article format and publication fee selection are Stage 12/14 questions.
