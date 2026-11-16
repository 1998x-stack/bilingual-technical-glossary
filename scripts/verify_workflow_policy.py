#!/usr/bin/env python3
"""P0 release safety: forbid repository-writing jobs in committed workflows.

Checks intentional, high-risk patterns without extra PyYAML dependencies. All
publication content must land through PRs; Pages may deploy committed docs.
"""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
WORKFLOWS=ROOT/'.github/workflows'
DANGEROUS=[
    (re.compile(r'(?im)^\s*contents\s*:\s*write\s*(?:#.*)?$'),"contents:write"),
    (re.compile(r'(?im)(?:^|[;&|\s])git\s+push\b'),"git push"),
    (re.compile(r'(?im)(?:^|[;&|\s])git\s+commit\b'),"git commit"),
    (re.compile(r'(?im)git\s+reset\s+--hard'),"git reset --hard"),
    (re.compile(r'(?im)persist-credentials\s*:\s*true'),"persisted checkout credentials"),
]
def check_workflows(root=ROOT):
    errors=[]
    files=sorted((root/'.github/workflows').glob('*.yml'))
    if len(files)<10: errors.append("Expected full workflow inventory; discovered fewer than 10.")
    for path in files:
        data=path.read_text(encoding='utf-8')
        # Skip comments to avoid matching explanatory warning text.
        content='\n'.join(line for line in data.splitlines() if not line.lstrip().startswith('#'))
        for pattern,issue in DANGEROUS:
            if pattern.search(content): errors.append(f'{path.name}: forbidden {issue}')
        if path.name=='pages.yml':
            if "needs: verify" not in data: errors.append("Pages deploy must depend on its read-only validation job.")
            if "pages: write" not in data: errors.append("Pages deployment must have Pages-only write scope.")
        elif 'permissions:' not in data or not re.search(r'(?m)^\s*contents:\s*read\s*$',data):
            errors.append(f'{path.name}: explicit read-only content permission required')
        if path.name.startswith('sync-') or path.name.startswith('build-') or path.name in (
            'kafka-pdf.yml','university-mathematics.yml','discrete-mathematics.yml','compiler-glossary.yml'):
            if 'actions/upload-artifact@' not in data:
                errors.append(f'{path.name}: generated outputs must be uploaded as reviewable artifacts')
    return errors

if __name__=='__main__':
    problems=check_workflows()
    if problems:
        print(f"FAIL — {len(problems)} workflow-policy violations")
        for problem in problems: print(' -',problem)
        sys.exit(1)
    print("PASS — read-only domain jobs, no direct pushes, validated Pages deployment")
