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
The guide retains calibration corrections through September 7 and fixture-fit
evidence through September 13. Reported offline,
simulation and hardware outcomes are distinguished; unresolved procedures are
labelled at their point of use.

Start with the [system map](docs/start/overview.md), then follow a chapter's
diagram and code entry points. The [code index](docs/reference/code-index.md)
links pinned public source and distinguishes the August demo baseline from the
September calibration branch. Authorship and project
context are under [About](docs/about.md). Earlier drafts remain in Git history.

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
| `tools/build_code_index.py` | Generate/check the Markdown index from the code map |
| `requirements-docs.in` / `.txt` | Direct dependencies and pinned build environment |
| `.github/workflows/docs.yml` | Strict build on changes; Pages deployment from main |

The [source catalog](docs/reference/sources.md) identifies published code and
validation limits. Personal research notes remain private. The five August 25
runs are converted to LeRobot; [dataset downloads](docs/data/recording.md#dataset-downloads)
for those runs and the calibration captures are available on Google Drive.

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
