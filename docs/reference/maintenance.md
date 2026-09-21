# Maintaining this guide

The guide uses **Sphinx, MyST Markdown and Furo**. Most contributions change
a Markdown page under `docs/`, an image/caption, or an entry in the navigation.
Building the guide does not require ROS, CUDA, robot repositories or hardware.

## Install and preview

From the repository root, with Python 3.10 or newer:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/sphinx-build -n -W --keep-going -b html docs site
.venv/bin/python -m http.server 8000 --directory site --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Rebuild after changing a page, then refresh the
browser. If the system Python lacks `venv`/`ensurepip` and you already use uv:

```bash
uv venv --python 3.10 .venv
uv pip install --python .venv/bin/python -r requirements-docs.txt
```

The dependency input is `requirements-docs.in`; `requirements-docs.txt` pins
the resolved build. Update deliberately, rebuild and review before committing
a new lock. The first draft was built with Python 3.10.

## Edit a page

Use normal headings, links, fenced code and Markdown tables. MyST adds
directives for notes, figures and navigation. Copy a nearby example instead
of inventing a custom component. The hidden `toctree` blocks at the bottom of
`docs/index.md` define the sidebar groups. Add a new page there and link it
from the appropriate reading path.

Use Mermaid for code diagrams; the [diagram guide](diagrams.md) gives the
shared syntax, diagram types and rendering checks.

Technical chapters follow the system rather than the order of the summer's
experiments: diagram, code map, interface/assumption explanation, then design
lessons and evidence. Keep the timeline in the archive. Place a historical
failure beside the rule it explains, so a reader can understand what a change
must preserve without reading a journal first.

## Maintain the code pointers

The [code index](code-index.md) and `docs/assets/code-map.json` identify the
files and symbols behind chapter maps. Public links pin a commit and were
compared with the inspected file bytes. For uncommitted implementations,
retain the local-snapshot label, exact repository-relative path and hash.
Do not replace it with a convenient link to older code.

When a source changes, review its diagram and contracts, update symbol line
spans and the file hash in the JSON/index, and update affected chapter links.
An optional static check uses an ignored location file:

```json
{"repositories": {"g1-dex3-tabletop": "/path/to/g1-dex3-tabletop"}}
```

```bash
python3 tools/check_code_map.py --locations .local/source_locations.json \
  --repository g1-dex3-tabletop
```

The checker reads files and parses Python syntax; it does not import robot
modules or run hardware code. A mismatch calls for review, not automatic hash
replacement. Building the guide requires none of these source checkouts.

## Review and publish an edit

Keep procedure prerequisites and expected observations near the instructions.
Date hardware results and identify their configuration. Preserve the reason
for a step when a failed experiment explains it. New research should update
the current procedure while leaving the historical correction traceable.

Run the strict build above and `git diff --check`. Sphinx treats warnings,
including missing internal references, as failures. The GitHub workflow runs
the same build for pull requests and publishes successful main-branch builds
to Pages.

## Why this framework

Material for MkDocs matched SPARK, but its maintainers announced maintenance
mode and a move toward Zensical. Zensical preserves much of that authoring
experience but was still labelled alpha when reviewed on September 13, 2026.
The author also pointed to UW Lab and cuRobo: both use Sphinx; UW Lab uses
Sphinx Book Theme, and cuRobo uses Furo. Both enable MyST Markdown.

For this project, the selected tradeoff is an established Python documentation
builder, Markdown authoring and minimal theme customization. Furo gives a
compact technical reading layout and Sphinx can add API references later.
There is no need to install every extension used by those much larger projects.

Decision sources: [Material announcement](https://squidfunk.github.io/mkdocs-material/blog/2025/11/11/insiders-now-free-for-everyone/),
[Zensical status](https://zensical.org/about/roadmap/),
[UW Lab configuration](https://github.com/uw-lab/UWLab/blob/main/docs/conf.py),
[cuRobo configuration](https://github.com/NVlabs/curobo/blob/main/docs/conf.py).

## Publication and handoff

The author created `sri299792458/g1-research-docs` for following the draft.
The Pages workflow builds static HTML and deploys it through GitHub Actions;
repository Pages settings must use **GitHub Actions** as their source. The
README records the live link once publication is verified.

For the later lab copy, preserve Git history and tag the reviewed summer
version. Update `html_baseurl` and repository/edit links in `docs/conf.py`,
enable Pages, and check media access. Link the personal portfolio version
and the lab's maintained version from both READMEs. Date later lab additions
so the original summer contribution remains identifiable.
