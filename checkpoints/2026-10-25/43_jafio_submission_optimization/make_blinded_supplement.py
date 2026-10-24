#!/usr/bin/env python3
"""Create a minimal anonymous, source-preserving reproducibility archive."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PYTHON_SOURCES = (
    'checkpoints/2026-10-24/21_stage11_adversarial_preflight/check_core_independent.py',
    'checkpoints/2026-10-24/21_stage11_adversarial_preflight/check_nonlinear_primitive.py',
    'checkpoints/2026-10-24/17_stage4A_75A_certification/verify_portability_compact.py',
    'checkpoints/2026-10-24/17_stage4A_75A_certification/verify_p3_boundary_multiplicity.py',
    'checkpoints/2026-10-24/14_full_paper_reopen_p3_analytic_open_set/verify_analytic_wasteful_rd.py',
    'checkpoints/2026-10-24/14_full_paper_reopen_p3_analytic_open_set/verify_positive_e_global_nash.py',
    'checkpoints/2026-10-25/35_stage11_hostile_referee/independent_referee_reconstruction.py',
    'checkpoints/2026-10-24/12_geo_product_parent_theorem/verify_candidate_interval.py',
    'checkpoints/2026-10-24/12_geo_product_parent_theorem/verify_global_BR_at_delta_034.py',
)
LEAN = ROOT / 'checkpoints/2026-10-24/18_lean_formal_proofs/lean'
README = '''# Anonymous reproducibility materials

This archive accompanies a theoretical study of regional public breeding and variety replacement. It contains no empirical data, author records, repository history, or internal review reports.

## Exact Python checks

Use Python 3.11 and install the declared dependency:

    python -m pip install -r requirements.txt
    python run_python_checks.py

The nine independent/self-contained scripts retain their original mathematical code unchanged. The runner uses only the Python standard library and runs each script in an isolated subprocess. Assertions failing produce a nonzero exit status. Printed historical checkpoint labels describe the scripts' original verification scope, not additional publication claims.

Checks cover the four-good utility/price/follower bridge, the conditional linear-demand wedge, exact nonlinear incidence instance, bounded alternative costs and unequal-curvature counterexample, the analytic harmful-research parameter family and boundary multiplicity, and two separate interacting rational examples. Exact external active-set computations verify unilateral global best responses in those specified examples. They do not prove uniqueness among all asymmetric equilibria or all-parameter robustness.

## Lean proof-critical core

Install elan/Lean, then run:

    cd lean
    lake update
    lake build

The toolchain selects Lean 4.35.0, with mathlib v4.35.0. Dependency download requires Internet access. No generated dependency cache or downloaded third-party source is bundled. The mathlib tag is specified; no claim is made that a transitive dependency manifest is locked in this archive.

The formal sources verify encoded conditional quadratic/KKT and first-order identities, the exact analytic family's global research/planner proof core, excluded-boundary multiplicity, and specified candidate/welfare identities. The general-N module verifies conditional Jacobian algebra; it does not formalize the whole nonlinear economic derivation. For the interacting examples, full nine-regime global best-response checks are Python evidence, not a Lean theorem.

## Integrity, interpretation and assistance

SHA256_MANIFEST.json records the SHA-256 of every other archive member. Original Python and Lean source bytes are preserved. These materials do not certify economic originality, empirical relevance or human-author rederivation. ChatGPT assisted the manuscript and development/review of verification scripts and formal sources, beyond language correction; bounded computational checks do not replace the human author's responsibility. Consult the manuscript's AI-use declaration and proof-scope explanations.
'''


def make_runner(names):
    return '''#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parent
FILES = ''' + repr(names) + '''
for name in FILES:
    print('RUN', name, flush=True)
    subprocess.run([sys.executable, str(ROOT / 'python' / name)], cwd=ROOT, check=True, timeout=300)
print('PASS all nine exact Python checks; Lean and economic interpretation assessed separately')
'''


def scan(name, payload):
    text = payload.decode('utf-8').lower()
    for token in ('ryotamatsuki', 'matsuki', '松木', 'ehime', '/workspace/', '@gmail', 'git@', 'git.chatgpt', 'libfile_', 'author_intellectual_contribution_record'):
        assert token not in text, f'Identifying/internal content in {name}: {token}'
    # Allow only the generic public mathlib dependency link.
    if 'github.com/' in text:
        assert name == 'lean/lakefile.lean'
        assert 'github.com/leanprover-community/mathlib4' in text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='extract archive and run its standalone Python runner')
    args = parser.parse_args()
    members = {}
    names = []
    for relative in PYTHON_SOURCES:
        source = ROOT / relative
        names.append(source.name)
        target = 'python/' + source.name
        assert target not in members
        members[target] = source.read_bytes()
    for source in sorted(LEAN.rglob('*.lean')):
        relative = source.relative_to(LEAN)
        if '.lake' in relative.parts:
            continue
        members['lean/' + relative.as_posix()] = source.read_bytes()
    members['lean/lean-toolchain'] = (LEAN / 'lean-toolchain').read_bytes()
    members['README.md'] = README.encode()
    members['requirements.txt'] = b'sympy==1.13.3\n'
    members['run_python_checks.py'] = make_runner(names).encode()
    for name, payload in members.items():
        scan(name, payload)
    manifest = {name: hashlib.sha256(payload).hexdigest() for name, payload in sorted(members.items())}
    members['SHA256_MANIFEST.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    destination = HERE / 'JAFIO_Blinded_Reproducibility.zip'
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for name, payload in sorted(members.items()):
            info = ZipInfo(name, date_time=(2026, 10, 25, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, payload)
    print(f'PASS anonymous archive: {len(names)} exact Python scripts; {len(members)} members; source bytes preserved', flush=True)
    if args.test:
        with tempfile.TemporaryDirectory(prefix='blinded-reproduction-') as directory:
            folder = Path(directory)
            with ZipFile(destination) as archive:
                archive.extractall(folder)
            for name, digest in manifest.items():
                assert hashlib.sha256((folder / name).read_bytes()).hexdigest() == digest
            subprocess.run([sys.executable, str(folder / 'run_python_checks.py')], cwd=folder, check=True, timeout=900)
        print('PASS extracted archive integrity and standalone Python runner')

if __name__ == '__main__':
    main()
