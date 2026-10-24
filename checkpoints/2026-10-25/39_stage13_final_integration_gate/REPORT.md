# Canonical Stage 13 — Full Paper Integration: Final Gate Certificate

**Date:** 2026-10-25 JST  
**Manuscript:** *Regional Public Breeding and Variety Replacement: Decentralized Research Incentives and National Welfare*  
**Branch:** \`research/2026-10-24-ijio-response-audit\`, Draft PR #2; frozen Stage 8 and original Stage 9 artifacts unmodified.  
**Journal-facing profile:** *Bio-based and Applied Economics* (BAE), **Full Research Article**; RAFE and REA remain Stage 12 fallback venues.  
**Decision:** **STAGE 13 GO — COMPLETE INTEGRATED THEORY-FIRST MANUSCRIPT, proof-preserving and source/PDF verified.** Journal submission still **NOT READY**: Stage 14 package requires Word/RTF, double-spacing, line numbers, anonymization, accurate author/funding disclosures, highlights and cover-letter verification.

## 1. Authoritative production assets and provenance

- \`checkpoints/2026-10-25/38_stage13_full_paper_integration/paper.tex\`, Git blob **\`a54aa3f176cfd523487df0fe6dea589914a27262\`**; a **distinct new manuscript** from the Stage 10 ancestor \`32_stage10_manuscript/paper.tex\` blob \`76598a904e931d34587e10deadb5598d0598ec1b\`. The prior Stage 8 theory remains frozen.
- \`38_stage13_full_paper_integration/references.bib\`: original verified **14** BibTeX sources unchanged, all cited in the integrated main text.
- \`38_stage13_full_paper_integration/EXPOSITION_STREAMLINING_REPORT.md\` (section and content necessity map, reader-arrival targets, exhibit scarcity, and cost/format limitations).
- \`38_stage13_full_paper_integration/REVIEWER_VERIFIABILITY_REPORT.md\` (claim-to-primitive, mathematical domain, derivation/proof, and Lean/SymPy certified-object map).
- \`38_stage13_full_paper_integration/verify_integration.py\`: automated exact theorem/proposition/corollary and **30 displayed equation block** equality comparison against Stage 10, preserving original mathematical statements. Proof counts, LaTeX label links, 14 BibTeX citations, 150-word abstract and 3-JEL checks.
- \`.github/workflows/public-breeding-stage13.yml\`: validates integrated paper, reruns frozen Stage10 checker, builds PDF using LaTeX/BibTeX, checks log/PDF and uploads a 30-day artifact. Workflow paths narrowed to source/validator changes so audit-note changes do not cause redundant recompilation.

## 2. Substantive integration findings

**Introduction compression:** 614 -> **437** whitespace-delimited words (28.8% reduction); question/main result in the first two paragraphs; 14 bibliographical references retained through structured agricultural-research vs general price-incidence theory paragraphs. No generic first-ever "research is overfunded" assertion. Specific public agricultural quality research + competitive old/new planting + joint national welfare is the bounded contribution.

**Abstract:** 156 -> **129** words, no unconditional demand-curvature welfare claim. **JEL:** four -> **three** (\`H77, O32, Q16\`). Five keywords unchanged. Abstract and JEL now meet BAE technical numerical thresholds, but **not** complete journal submission formatting.

**Main text:** Original P1 on-symmetric-follower optimality \`x=Ma-z\`, local vs national derivative, conditional equilibrium comparison retained. Restricted old/new **same phi** demand P2 and its primitive-to-Jacobian proof retained. P3+ unreduced four-product local objective, zero/partial/full planting branches, exact \`zCut=(-4+sqrt13)/12\` strict lower boundary, joint full-feasible-space W square completion, and independent research best responses retained. Mutual-vs-unilateral government welfare interpretation retained.

**Nonzero-e examples:** \`e=1/100\` rational case remains in main robustness to show the analytic e=j=0 example does **not** imply cross-research strategic substitution; the secondary \`e=3/10\` parameter and exact rational case moved to computational appendix. Both verified outcomes and explicit distinction of SymPy external global BR vs Lean candidate are intact; no all-asymmetric uniqueness claimed.

**Appendix:** Original "Derivation and proof crosswalk" discussing internal checkpoint filesystem removed as a redundant nonacademic artifact. Essential mathematical appendices remain: (A) nonlinear restricted-demand primitive-to-price/Jacobian/weighted incidence, (B) P3+ continuous global deviations and excluded cutoff, (C) rational interacting verification scope plus secondary e=3/10 example. Separate research report contains formal source mapping. No reader must open Lean to reconstruct the proof-critical bridge.

**Final scientific language:** Discussion interprets conditional public research welfare and omitted institutions; Conclusion does not introduce new theorem or empirical grant proposal; real regional consumer surplus weights not estimated. A section explicitly discloses AI assistance with literature, writing, symbolic math and Lean, and human author responsibility. Data statement notes **no empirical dataset**, with reproducibility scripts existing but journal-safe anonymous supplement yet to be assembled.

**References order:** Main text -> disclosure/data statements -> 14 references -> analytic/computational appendices, as requested by BAE official guide. No figures or tables: all economically useful propositions are conveyed by in-text math and verifiable appendix; no invented numerical plot or unverified source.

## 3. Exact build and reproducibility evidence

**Stage13 one-time source-build SUCCESS:** [GitHub Actions run 40123147956](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40123147956), after correction of a test-only case-sensitive Python \`str.index\` error. It completed Stage 13 theorem/display identity check, prior Stage10 frozen theorem check, LaTeX+BibTeX build and PDF/error-log validity checks. Original failed run [40123065261](https://github.com/ryotamatsuki/regional-public-lab-research-diversification/actions/runs/40123065261) is archived and attributed **solely to the malformed checker condition**, which was repaired without touching paper mathematics.

**Artifact:** \`regional-public-breeding-stage13-integrated-paper\`, GitHub artifact ID **\`12571678414\`**. Actual ZIP downloaded from CI into the current working container, extracted and verified \`paper.pdf\`: **245,280 bytes, 11 A4 pages (595.276 x 841.89pt)**, PDF signature and \`pdfinfo\` checked; text extracted. All **11 pages** rendered to images at 95 dpi and contact-sheet inspected, with no conspicuous text/math cropping, reference truncation, empty trailing page or missing bibliography.

**Reader arrival measured on final PDF:**
- **p. 1**: abstract, economic question and headline positive-local/zero-national contribution;
- **p. 2**: start of Section 2 economic environment, regional objectives, utility/price definitions;
- **p. 3**: Section 3 decentralized research incentives, signed-wedge P1;
- **p. 5**: Section 4 globally harmful regional research, exact P3+ family and all-branch proof across pp. 5–6;
- **p. 7**: Section 5 robustness and limits including nonzero e, opening institutional interpretation;
- **p. 8**: Discussion, Conclusion, publisher-required AI declaration and initial references;
- **p. 9**: remaining bibliography and Appendix A;
- **p. 10**: Appendix A continuation, Appendix B global-deviation proof;
- **p. 11**: Appendix B continuation and Appendix C exact coupled benchmark scope.

**Proof/quantifier anti-regression:** Stage13 source checker PASSED for exactly identical lemma/proposition/corollary environments and every displayed equation (same label/number order). Stage11 has already verified 4-good independent primitive derivation, all corner regimes, P3 global welfare and e>0 rational check on Stage 10 source; Stage 13 left those proofs and equations byte-identical. It does **not** claim a fresh Lean kernel build from this new editorial commit or a new all-parameter Nash theorem.

**An earlier successful PDF on 5a1fdd51c was built before adding only documentary reports/CI trigger rules.** No economic/LaTeX scientific source changed after \`a54aa3f...\`. The final independent workflow run on the report/CI path should be read only as a redundant confirmation, not a substitute for source identity. The current Stage13 manuscript blob was refetched and compared.

## 4. BAE rules: satisfied now versus deferred legitimately to Stage 14

**Already consistent (Stage 13):** theory-forward Full Research Article rather than Policy Paper; <=150 abstract, <=3 JEL, five keywords; anonymous title; source-level numbered sections; references before appendix and no uncited references; truthful AI-use statement; mathematical content, proofs and annotations self-contained; all 14 sources attributed.

**Still to prepare at Stage 14 (NOT falsely marked passed):**
1. Submission-ready **Word/OpenOffice/RTF editable manuscript**, BAE **12-point double-spaced and line-numbered**, journal reference style and equation editability. Current 11pt single-spaced LaTeX is a valid research master/PDF but not BAE upload file.
2. Accurate **word count including abstract, footnotes, appendix, declarations and references**; BAE Full Articles "normally 6,000–8,000", not an absolute documented lower exclusion. This proof-heavy concise paper may be below the norm; do not pad by importing unsupported economic claims. Seek journal editorial exception or transparently justify concise content in letter.
3. **Separate title page** with the real author's supplied name/affiliation/contact; do not invent or publish home/employer details, workplace authorization or conflicts of interest. The connected repository/Lean URLs may reveal personal identity: anonymize blinded replication files before external submission.
4. **3–5 editable Highlights** (<=85 characters each), **journal-specific Cover Letter**, 3 suitable nonconflicted referees (two non-domestic per BAE), and all authors' submission approval; do not invent reviewer addresses.
5. Verify author's actual funding, other employment policies, conflict status, AI disclosure wording and data/code deposition/access route; current AI section identifies ChatGPT and human oversight, but final factual approval is needed.
6. Journal metadata, DOI/link formatting, originality/source verification and final publisher-facing QA. BAE is Diamond OA with no fees, not an assurance of acceptance.

## 5. Final verdict and next stage

**STAGE 13: GO — fully integrated academic argument and mathematically traceable submission-master PDF** for a bounded agriculture-specific field theory research article. No new model assumption, theorem, proof or literature absorption is asserted. The high-risk editorial shortcomings from Stage 11 remain: known generic price incidence/overpromotion; stylized CS/2 regional objective; analytic e=j=0 example lacks research strategic BR coupling; no calibrated instrument or empirically proven inefficiency. Their open acknowledgement is required in a BAE submission.

**Stage 14 next**: formal publisher-specific production and final technical QA; complete the Word/RTF submission package without altering frozen economic claims, and obtain only genuine author's specifics where unavoidable. **NOT READY TO SUBMIT, NOT PR-MERGED.**
