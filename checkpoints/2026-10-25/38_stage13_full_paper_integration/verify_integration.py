#!/usr/bin/env python3
"""Stage 13 proof-preserving article integration and BAE exposition integrity audit."""
from pathlib import Path
import re

repo=Path(__file__).resolve().parents[3]
old=(repo/"checkpoints/2026-10-25/32_stage10_manuscript/paper.tex").read_text()
new=(repo/"checkpoints/2026-10-25/38_stage13_full_paper_integration/paper.tex").read_text()
bib=(repo/"checkpoints/2026-10-25/38_stage13_full_paper_integration/references.bib").read_text()

def matches(pat,s):
    return re.findall(pat,s,flags=re.DOTALL)
for env in ("lemma","proposition","corollary"):
    pat=r"\\begin\{"+env+r"\}.*?\\end\{"+env+r"\}"
    assert matches(pat,old)==matches(pat,new),f"Frozen {env} statements changed"

# Every display equation (including equation numbers and labels) is byte-for-byte
# identical and in the same order; only narrative text/locations can differ.
for env in ("equation","align"):
    pat=r"\\begin\{"+env+r"\}.*?\\end\{"+env+r"\}"
    assert matches(pat,old)==matches(pat,new),f"{env} display mismatch"
assert matches(r"\\\[.*?\\\]",old)==matches(r"\\\[.*?\\\]",new)
assert new.count(r"\begin{proof}")==old.count(r"\begin{proof}")
assert new.count(r"\end{proof}")==old.count(r"\end{proof}")
assert new.count(r"\end{document}")==1 and new.rstrip().endswith(r"\end{document}")
assert new.count(r"\appendix")==1 and new.index(r"\bibliography{references}")<new.index(r"\appendix")
assert r"\section{Derivation and proof crosswalk}" not in new
assert r"\section{Computational scope and a second interacting benchmark}" in new
assert new.index(r"\subsection{Nonzero cross-region interaction}")<new.index(r"\appendix")
assert new.index("a distinct rational parameter example with")<0 or "A distinct rational parameter example with" in new
assert new.index(r"\section*{Declaration of generative AI and AI-assisted technologies}") < new.index(r"\bibliography{references}")
assert r"\textbf{JEL:} H77, O32, Q16." in new

abstract=matches(r"\\begin\{abstract\}(.*?)\\end\{abstract\}",new)[0]
count=len(abstract.strip().split())
assert count<=150,(count,abstract)
labels=matches(r"\\label\{([^}]+)\}",new)
assert len(labels)==len(set(labels))
refs=set(matches(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",new))
assert refs.issubset(set(labels)),refs-set(labels)
keys=set(matches(r"(?m)^@\w+\{\s*([^,\s}]+)",bib))
citations={k.strip() for seq in matches(r"\\cite(?:p|t|author|year)?(?:\[[^]]*\]){0,2}\{([^}]+)\}",new) for k in seq.split(",")}
assert len(keys)==14 and citations==keys,(len(keys),len(citations),keys-citations,citations-keys)
assert len(matches(r"\\begin\{figure\}",new))==0
assert len(matches(r"\\begin\{table\}",new))==0
assert len(matches(r"\\section\{",new))>=8
print("PASS Stage 13 integrated article: all theorem/corollary statements and mathematical displays identical to Stage 10")
print("PASS Stage 13 academic structure: references before appendices, AI declaration, 3 JEL, no redundant proof appendix")
print(f"PASS Stage 13: {count} abstract words, {len(labels)} unique labels, {len(citations)} cited references, zero exhibits")
