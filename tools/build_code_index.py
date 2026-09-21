#!/usr/bin/env python3
"""Render the Markdown code index from the reviewed public source map."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTRO = '''# Code index

Start with a chapter's diagram and code map. Every entry here links to a public,
commit-pinned file; SHA-256 values and Python symbol spans identify the inspected
implementation. These are source identities, not claims of hardware validation.

## Choose the version before editing

`g1-dex3-tabletop/main` preserves the August 25 demo baseline. Its
`experimental/september-calibration` branch preserves later calibration and
shared-runtime changes, including the formerly uncommitted implementation.
Entries label their branch; `demo-` entries supply the baseline counterparts
where a chapter also discusses the later version. The [source catalog](sources.md)
explains repository roles and validation boundaries.

For an agent, read the Mermaid source, mapped functions, invariants and evidence
together. Use the exact revision in the [machine-readable map](../assets/code-map.json).
`tools/check_code_map.py` reads those Git objects and parses Python without
importing robot software. The site build needs only this documentation repository.
Private working notes are not a prerequisite for resolving any code link.

'''

def render(manifest):
    sections = [INTRO]
    for entry in manifest['entries']:
        sections.append(f"## Code: {entry['id']}\n\n")
        sections.append(f"**Repository:** `{entry['repository']}`. **Path:** `{entry['path']}`.\n\n")
        branch = entry.get('branch')
        scope = f" **Branch:** `{branch}`." if branch else ''
        sections.append(f"[Pinned public source]({entry['public_url']}).{scope} Revision `{entry['revision'][:7]}`.\n\n")
        sections.append(f"File SHA-256: `{entry['sha256']}`.\n\n")
        if entry['symbols']:
            sections.append('| Symbol | Inspected lines |\n|---|---|\n')
            for symbol in entry['symbols']:
                sections.append(f"| [`{symbol['name']}`]({entry['public_url']}#L{symbol['line']}) | {symbol['line']}–{symbol['end_line']} |\n")
            sections.append('\n')
    return ''.join(sections).rstrip() + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the committed index differs')
    args = parser.parse_args()
    manifest = json.loads((ROOT/'docs/assets/code-map.json').read_text())
    output = render(manifest)
    target = ROOT/'docs/reference/code-index.md'
    if args.check:
        if target.read_text() != output:
            parser.error('Code index is stale; run python3 tools/build_code_index.py')
    else:
        target.write_text(output)
    print(f"Code index matches {len(manifest['entries'])} public source entries.")

if __name__ == '__main__':
    main()
