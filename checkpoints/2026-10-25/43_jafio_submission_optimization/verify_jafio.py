#!/usr/bin/env python3
"""Proof-preserving JAFIO revision regression; no all-paper formal-proof claim."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT / 'checkpoints/2026-10-25/38_stage13_full_paper_integration'

def find(pattern, text):
    return re.findall(pattern, text, flags=re.S)

def check_editorial_invariants():
    old = (BASE / 'paper.tex').read_text()
    new = (HERE / 'paper.tex').read_text()
    bib = (HERE / 'references.bib').read_text()
    for env in ('lemma', 'proposition', 'corollary', 'equation', 'align'):
        pattern = r'\\begin\{' + env + r'\}.*?\\end\{' + env + r'\}'
        assert find(pattern, old) == find(pattern, new), f'{env} changed'
    for pattern, label in ((r'\\\[.*?\\\]', 'unnumbered displays'),
                           (r'(?<!\\)\$[^$]*?(?<!\\)\$', 'inline math')):
        assert find(pattern, old) == find(pattern, new), f'{label} changed'
    proofs = r'\\begin\{proof\}(.*?)\\end\{proof\}'
    before, after = find(proofs, old), find(proofs, new)
    assert len(before) == len(after)
    # Proof prose may remove internal code filenames, but never its equations.
    for num, (a, b) in enumerate(zip(before, after), 1):
        for pat in (r'(?<!\\)\$[^$]*?(?<!\\)\$', r'\\\[.*?\\\]',
                    r'\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}'):
            assert find(pat, a) == find(pat, b), f'proof {num} math changed'
    labels = find(r'\\label\{([^}]+)\}', new)
    assert len(labels) == len(set(labels))
    refs = set(find(r'\\(?:ref|eqref|autoref)\{([^}]+)\}', new))
    assert refs <= set(labels), refs - set(labels)
    keys = set(re.findall(r'(?m)^@\w+\{\s*([^,\s}]+)', bib))
    citations = {k.strip() for group in find(r'\\cite(?:p|t|author|year)?(?:\[[^]]*\]){0,2}\{([^}]+)\}', new) for k in group.split(',')}
    assert citations == keys, (citations - keys, keys - citations)
    abstract = find(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', new)[0].strip()
    words = len(abstract.split())
    assert 100 <= words <= 230, f'abstract {words} words: review approx. 200 recommendation'
    assert '\n\n' not in abstract, 'abstract must be one paragraph'
    assert new.count(r'\end{document}') == 1 and new.rstrip().endswith(r'\end{document}')
    assert new.count(r'\appendix') == 1
    for token in ('ryotamatsuki', '松木', '@gmail', 'github.com/', 'checkpoints/', '/workspace/'):
        assert token.lower() not in (new + bib).lower(), f'anonymity/internal path: {token}'
    print(f'PASS JAFIO: frozen statements/displays/inline math; {len(before)} proof math blocks; {len(labels)} labels; {len(keys)} cited records; {words} abstract words')


def run_archived_regressions():
    paths = [
        'checkpoints/2026-10-25/31_stage9_reproducibility/verify_all.py',
        'checkpoints/2026-10-25/35_stage11_hostile_referee/independent_referee_reconstruction.py',
        'checkpoints/2026-10-24/12_geo_product_parent_theorem/verify_candidate_interval.py',
        'checkpoints/2026-10-24/12_geo_product_parent_theorem/verify_global_BR_at_delta_034.py',
        'checkpoints/2026-10-25/32_stage10_manuscript/verify_manuscript.py',
        'checkpoints/2026-10-25/38_stage13_full_paper_integration/verify_integration.py',
    ]
    for relative in paths:
        print('RUN', relative, flush=True)
        subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, check=True, timeout=300)
    print('PASS archived Stage 9/11 exact regressions and Stage 10/13 frozen source checks')


def check_log():
    log = HERE / 'paper.log'
    if not log.exists():
        print('PDF/log not built in this invocation; CI build and visual audit are separate gates')
        return
    text = log.read_text(errors='replace')
    assert not re.search(r'undefined citations|citation .* undefined|undefined references|reference .* undefined|LaTeX Error', text, re.I)
    assert (HERE / 'paper.pdf').read_bytes().startswith(b'%PDF-')
    print('PASS PDF signature and resolved references/citations')


if __name__ == '__main__':
    check_editorial_invariants()
    run_archived_regressions()
    check_log()
    print('PASS JAFIO regression (Lean build, source verification, policy and human accountability separately assessed)')
