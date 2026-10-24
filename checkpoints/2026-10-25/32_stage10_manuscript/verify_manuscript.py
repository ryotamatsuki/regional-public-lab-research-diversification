#!/usr/bin/env python3
"""Stage 10 conservative LaTeX integrity checks against Stage 8 frozen source."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OLD = ROOT / "checkpoints/2026-10-24/20_stage9_10_manuscript/paper.tex"
NEW = ROOT / "checkpoints/2026-10-25/32_stage10_manuscript/paper.tex"
BIB = NEW.with_name("references.bib")
a=OLD.read_text(encoding="utf-8")
b=NEW.read_text(encoding="utf-8")
bib=BIB.read_text(encoding="utf-8")
assert b.count(r"\end{document}") == 1 and b.rstrip().endswith(r"\end{document}")
assert b.count(r"\appendix")==1
assert "Anonymous draft for internal research verification" not in b
assert "Stage 10 working manuscript" not in b
assert "the existing source-level assessment does not yet" not in b
assert r"H_\phi(1-a)-H_\phi(a)" in b

def contents(pattern, text):
    return re.findall(pattern,text,flags=re.DOTALL)

# Equations remain identical except the explicit P2 notation typo correction.
equation = r"\\begin\{(equation|align)\}(.*?)\\end\{\1\}"
eq_a=contents(equation,a)
eq_b=contents(equation,b)
assert len(eq_a)==len(eq_b),(len(eq_a),len(eq_b))
changed=[]
for i,((ka,xa),(kb,xb)) in enumerate(zip(eq_a,eq_b)):
    assert ka==kb
    if xa != xb:
        if xa.replace(" H(1-a)-H(a),"," H_\\phi(1-a)-H_\\phi(a),") != xb:
            raise AssertionError(f"Unapproved mathematical expression drift in equation block {i+1}")
        changed.append(i)
assert len(changed)==1, changed

# Lemma, proposition and corollary statements remain byte-identical.
for env in ("lemma","proposition","corollary"):
    regex=r"\\begin\{"+env+r"\}.*?\\end\{"+env+r"\}"
    old=contents(regex,a)
    new=contents(regex,b)
    assert old==new,f"Frozen {env} statement changed"
assert b.count(r"\begin{proof}")==a.count(r"\begin{proof}")
assert b.count(r"\end{proof}")==a.count(r"\end{proof}")

labels=re.findall(r"\\label\{([^}]+)\}",b)
assert len(set(labels))==len(labels)
needed=set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",b))
assert needed.issubset(labels),sorted(needed-set(labels))
bibkeys=re.findall(r"(?m)^@\w+\s*\{\s*([^,\s}]+)",bib)
assert len(bibkeys)==len(set(bibkeys))
cites={v.strip() for inner in re.findall(r"\\cite(?:p|t|author|year)?(?:\[[^\]]*\]){0,2}\{([^}]+)\}",b) for v in inner.split(",")}
assert cites.issubset(set(bibkeys)),sorted(cites-set(bibkeys))
assert len(bibkeys)==14 and len(cites)==14, (len(bibkeys),len(cites))
assert set(bibkeys)==cites, f"Uncited references: {sorted(set(bibkeys)-cites)}"

for term in ("eq:plannerbound","eq:threebranches","eq:mutuallocal","app:globalP3","app:nonlinearproof"):
    assert term in labels
assert r"\bibliography{references}" in b
print("PASS: Stage 10 frozen lemma/proposition/corollary statements identical")
print(f"PASS: {len(eq_b)} math display blocks, one P2 notation correction only")
print(f"PASS: {len(labels)} unique labels, {len(cites)} resolved citation keys")
