# Research checkpoints — 2026-10-24

These files preserve exploratory research produced up to 2026-10-24 at the owner's request. They do not certify novelty or override the unresolved verdict in the repository's claim boundary.

## Reading order

| Directory | Contents | Role |
| --- | --- | --- |
| [01_public_lab_audit](01_public_lab_audit/) | Prior-art audit, model checks and results | Audit of the earlier research-direction project |
| [02_public_breeding_baseline](02_public_breeding_baseline/) | Two-region quality and varietal-replacement model | Baseline model candidate |
| [03_direction_and_access](03_direction_and_access/) | Research direction and cultivation-access comparison | Alternative exploratory direction |
| [04_varietal_replacement](04_varietal_replacement/) | General regional count, nonlinear demand, proofs and verification | Latest candidate discussed in the current research session |

Start with [the latest research note](04_varietal_replacement/research_note_ja.md).

## Status and limits

- The latest note proposes public breeding, endogenous farmer adoption and old/new acreage reallocation as a research direction.
- The mathematical claims and verification scopes are specified in each note; the latest code checks exact two-region examples and symmetric interior identities.
- Literature non-absorption is not finally certified. Some close papers were checked only through abstracts or working-paper versions.
- Journal assessments are conditional research judgments, not acceptance predictions.
- The earlier direction/access model and the latest quality/replacement model are different candidates. Their propositions must not be combined without an additional derivation.
- Historical reports and results are preserved as produced. In particular, earlier journal-ranking records are not used as the current definition of the journal target.
- This save adds an evidence checkpoint. It does not execute the repository's final prior-art gate or promote a manuscript to submission-ready status.

## Reproduction

The latest verification requires Python 3, NumPy and SciPy:

```bash
cd checkpoints/2026-10-24/04_varietal_replacement
python3 verify_breeding.py
```

It rewrites verification_results.json. Previously completed verification is documented in the saved note and results. No new empirical estimation was performed during this GitHub save.

Third-party journal PDFs and transient helper files are excluded.
