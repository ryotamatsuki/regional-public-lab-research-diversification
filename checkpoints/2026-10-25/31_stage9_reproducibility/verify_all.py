#!/usr/bin/env python3
"""Stage 9 frozen-source integrity and exact symbolic regression runner.

Only relies on Python 3.11 stdlib and pinned SymPy from requirements.txt.
Mathematical proofs/Lean/PDF have separate build targets. Do not interpret
this script's success as a full Lean or full journal manuscript certificate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

STAGE9 = Path(__file__).resolve().parent
ROOT = STAGE9.parents[2]
MANIFEST = STAGE9 / "frozen_source_manifest.json"
MANUSCRIPT = ROOT / "checkpoints/2026-10-24/20_stage9_10_manuscript/paper.tex"
BIBLIOGRAPHY = ROOT / "checkpoints/2026-10-24/20_stage9_10_manuscript/references.bib"
SYMBOLIC_TESTS = (
    "checkpoints/2026-10-24/21_stage11_adversarial_preflight/check_core_independent.py",
    "checkpoints/2026-10-24/21_stage11_adversarial_preflight/check_nonlinear_primitive.py",
    "checkpoints/2026-10-24/17_stage4A_75A_certification/verify_portability_compact.py",
    "checkpoints/2026-10-24/17_stage4A_75A_certification/verify_p3_boundary_multiplicity.py",
)


def git_blob_hash(content: bytes) -> str:
    # Git SHA-1 is SHA1("blob <length>\\0" + bytes); hashes are Git object IDs,
    # not an assertion of cryptographic collision resistance for new secrets.
    header = b"blob " + str(len(content)).encode("ascii") + b"\\0"
    return hashlib.sha1(header + content).hexdigest()


def check_frozen_blobs() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    for relative, expected in sorted(manifest["files"].items()):
        target = ROOT / relative
        if not target.is_file():
            raise AssertionError(f"Missing frozen source: {relative}")
        observed = git_blob_hash(target.read_bytes())
        if observed != expected:
            raise AssertionError(f"Frozen source changed: {relative} expected {expected} got {observed}")
    print(f"PASS: {len(manifest['files'])} frozen Git blob object IDs match")


def check_manuscript_structure() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    bib = BIBLIOGRAPHY.read_text(encoding="utf-8")
    if text.count(r"\end{document}") != 1 or not text.rstrip().endswith(r"\end{document}"):
        raise AssertionError("Invalid LaTeX document terminator")
    if text.count(r"\appendix") != 1:
        raise AssertionError("Expected exactly one LaTeX appendix")
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    if len(labels) != len(set(labels)):
        raise AssertionError("Duplicated LaTeX labels")
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text)
    missing_refs = sorted(set(refs) - set(labels))
    if missing_refs:
        raise AssertionError(f"Missing equation/section labels: {missing_refs}")
    keys = set(re.findall(r"(?m)^@\w+\s*\{\s*([^,\s}]+)", bib))
    raw_cites = re.findall(r"\\cite(?:p|t|author|year)?(?:\[[^]]*\]){0,2}\{([^}]+)\}", text)
    cites = {key.strip() for group in raw_cites for key in group.split(",")}
    if cites - keys:
        raise AssertionError(f"Missing BibTeX keys: {sorted(cites - keys)}")
    if r"\bibliography{references}" not in text:
        raise AssertionError("Expected manuscript to reference accompanying references.bib")
    if r"\label{eq:mutuallocal}" not in text:
        raise AssertionError("Unilateral-vs-mutual regional payoff distinction not traceable")
    print(f"PASS: manuscript structure, {len(labels)} unique labels, {len(cites)} cited BibTeX keys")


def run_existing_checks() -> None:
    for path in SYMBOLIC_TESTS:
        result = subprocess.run(
            [sys.executable, str(ROOT / path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=180,
        )
        print(f"---- {path} ----")
        print(result.stdout.rstrip())
        if result.returncode != 0:
            print(result.stderr.rstrip(), file=sys.stderr)
            raise RuntimeError(f"Exact symbolic regression failed: {path}")
    print(f"PASS: {len(SYMBOLIC_TESTS)} existing independent/pre-registered symbolic regressions")


if __name__ == "__main__":
    check_frozen_blobs()
    check_manuscript_structure()
    run_existing_checks()
    print("STAGE9 PYTHON/PROVENANCE VERIFICATION PASS (Lean and PDF separately assessed)")
