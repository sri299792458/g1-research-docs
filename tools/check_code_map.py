#!/usr/bin/env python3
"""Verify chapter source identities and Python symbol locations without imports."""

import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def symbol_locations(nodes, prefix=""):
    result = {}
    for node in nodes:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            name = prefix + node.name
            result[name] = (node.lineno, node.end_lineno)
            result.update(symbol_locations(node.body, name + "."))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locations", type=Path, required=True,
                        help="Ignored JSON with a repositories mapping of IDs to checkout paths")
    parser.add_argument("--repository", help="Check only one repository ID")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "docs/assets/code-map.json").read_text())
    configuration = json.loads(args.locations.read_text())
    locations = configuration["repositories"]
    if "inspection_checkout" in configuration:
        locations.setdefault("g1pilot-dev", configuration["inspection_checkout"])
    entries = [e for e in manifest["entries"]
               if args.repository is None or e["repository"] == args.repository]
    if not entries:
        parser.error("repository has no entries in the code map")
    errors = []
    checked = 0
    for entry in entries:
        try:
            checkout = Path(locations[entry["repository"]])
            if entry["read_from"] == "git_object":
                data = subprocess.check_output(
                    ["git", "-C", str(checkout), "show",
                     entry["revision"] + ":" + entry["path"]],
                    stderr=subprocess.DEVNULL,
                )
            else:
                data = (checkout / entry["path"]).read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            if digest != entry["sha256"]:
                raise ValueError("file hash changed; review the diagram and contracts before updating the map")
            symbols = symbol_locations(ast.parse(data).body)
            for symbol in entry["symbols"]:
                expected = (symbol["line"], symbol["end_line"])
                if symbols.get(symbol["name"]) != expected:
                    raise ValueError("symbol location changed: " + symbol["name"])
            checked += 1
        except (KeyError, OSError, ValueError, SyntaxError, subprocess.CalledProcessError) as error:
            errors.append(f'{entry["id"]}: {error}')
    print(f"Verified {checked}/{len(entries)} source files and their mapped symbols.")
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
