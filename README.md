# Working with the G1

A practical guide to the lab's Unitree G1 research tools, developed through
[sri299792458](https://github.com/sri299792458)'s summer 2026 work. Chapters
connect Mermaid diagrams to source code, interfaces, procedures and the
hardware lessons a future researcher needs to preserve.

**[Read the guide](https://sri299792458.github.io/g1-research-docs/)** ·
[Review queue](docs/reference/review.md) · [Contributing](CONTRIBUTING.md)

This is a complete first draft awaiting the author's review. It covers G1Pilot,
an initial MuJoCo backend, Dex3 sensing, printed targets, camera/arm calibration,
GraspGen-X, CuRobo, physical cube manipulation and recording/LeRobot conversion.
The guide retains later corrections through September 7. Reported offline,
simulation and hardware outcomes are distinguished; unresolved procedures are
labelled at their point of use.

Start with the [system map](docs/start/overview.md), then follow a chapter's
diagram and code entry points. The [code index](docs/reference/code-index.md)
distinguishes pinned public source from local snapshots. Authorship and the
optional historical timeline are under [About](docs/about.md).

## Preview locally

The site uses **Sphinx + MyST Markdown + Furo**. No ROS, CUDA or robot access
is needed to build it. From the repository root, with Python 3.10 or newer:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/sphinx-build -n -W --keep-going -b html docs site
.venv/bin/python -m http.server 8000 --directory site --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Rebuild and refresh after editing. The
[maintenance page](docs/reference/maintenance.md) includes the uv alternative,
dependency updates, navigation and GitHub Pages setup.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Markdown chapters and site configuration |
| `docs/assets/` | Selected images, captions/provenance catalog and minimal CSS |
| `docs/assets/code-map.json` | Exact files, hashes, symbols and public URLs behind code maps |
| `tools/check_code_map.py` | Optional static verification against available source checkouts |
| `research/` | Sequential source-reading records, revisions and hashes |
| `running_notes.md` | Documentation decisions, corrections and progress |
| `requirements-docs.in` / `.txt` | Direct dependencies and pinned build environment |
| `.github/workflows/docs.yml` | Strict build on changes; Pages deployment from main |

Source reading covers all located primary running notes. Some supporting
research is still local/uncommitted in its original repository; the
[source catalog](docs/reference/sources.md) makes those limits explicit.
Hashes identify that evidence but are not an archive of it.

## Ownership and continuity

The personal repository lets the author review the draft and retain the summer
portfolio record. When reviewed, a lab-organization copy should preserve Git
history and a tagged summer version, then accept dated lab extensions. The
handoff must include media and access to supporting evidence, not just HTML.
The lab destination and final tag remain to be chosen.

The author's earlier [SPARK documentation](https://rpm-lab-umn.github.io/spark-data-collection/)
is a reference for practical explanations. The documentation license and final
asset attribution review remain in the review queue; existing upstream notices
must be preserved.
