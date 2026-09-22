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
For hardware photographs, use [editable annotated figures](media.md#annotated-hardware-figures)
with captions in Markdown. Their small generation helper needs only Python.

## Review for reader value

Keep the subsystem structure stable. Before expanding a chapter, identify the
question it answers and what a researcher can use afterward: a setup, an
interface, a diagnosis, a checked result or a clear limit.

- Introduce the physical item or engineering problem before internal names.
- Explain inputs, outputs and conditions before listing implementation details.
- Keep code links close to the behavior they implement, or collect several
  entry points in a focused section after the explanation.
- Use a diagram only when it clarifies a relationship, sequence or branch.
  A target-selection table and an assembly photograph can be more useful.
- Keep experiment details that explain a decision or establish its limits.
  A task-specific walkthrough is useful only when reproducing that task is
  the reader's goal; an integration example should not become a second manual
  for every component it uses.

Control, recording, hardware, calibration, grasping and simulation each have
reusable contributions. Do not remove a subsystem merely because another is
more immediately useful. Place a historical failure beside the rule it
explains, and preserve specific counterexamples to prevent repeated mistakes.

Git retains superseded pages and drafts, including deleted files. The current
site does not need a separate archive of earlier documentation.

## Maintain the code pointers

The [code index](code-index.md) and `docs/assets/code-map.json` identify the
files and symbols behind chapter maps. Public links pin a commit and were
compared with the inspected file bytes. All current entries are public Git
objects. Tabletop entries identify the demonstrated `main` or later
`experimental/september-calibration` branch; preserve that distinction.

When a source changes, review the explanation, any diagrams and the contracts, update symbol line
spans and the file hash in the JSON, and update affected chapter links.
Regenerate the index with `python3 tools/build_code_index.py`; CI checks that
it matches the map with `python3 tools/build_code_index.py --check`.
An optional static check uses an ignored location file:

```json
{"repositories": {"g1-dex3-tabletop": "/path/to/g1-dex3-tabletop"}}
```

```bash
python3 tools/check_code_map.py --locations .local/source_locations.json \
  --repository g1-dex3-tabletop
```

The source clone must contain the recorded commits. A normal clone/fetch of
the tabletop repository should include both published branches; a shallow
checkout of only `main` does not contain the September objects. The checker
reads the pinned Git objects rather than requiring a checkout of each branch.

The checker reads files and parses Python syntax; it does not import robot
modules or run hardware code. A mismatch calls for review, not automatic hash
replacement. Building the guide requires none of these source checkouts.

## Review and publish an edit

Keep procedure prerequisites and expected observations near the instructions.
Date hardware results and identify their configuration. Preserve the reason
for a step when a failed experiment explains it. New research should update
the current procedure while leaving the historical correction traceable.

Run `python3 tools/build_code_index.py --check`, the strict build above and
`git diff --check`. Sphinx treats warnings,
including missing internal references, as failures. The GitHub workflow runs
the same build for pull requests and publishes successful main-branch builds
to Pages.

After changing annotated figures, also run
`python3 tools/build_hardware_figures.py --check` and inspect the rendered page.

## Keep the build simple

Sphinx builds the site, MyST lets maintainers write Markdown, and Furo provides
the reading layout. The selected stack supports the current guide without
requiring a custom frontend. Add an extension only for a concrete authoring
need, and keep ordinary page edits possible without robot dependencies.

## Publication and handoff

Images and video posters are versioned with the Markdown; publication videos
are versioned release assets. Their captions, source hashes and preparation
recipes are in `docs/assets/media.json`. See [media maintenance](media.md#recreating-a-publication-copy)
to recreate a selected copy without changing its original. No media-preparation
tools are required for the normal Sphinx build.

The [dataset downloads](../data/recording.md#dataset-downloads) use Google
Drive links with separate README/checksum files. Before publishing a link,
verify that readers can download it without the owner's account. Record size,
version and format on the dataset page. Preserve these files separately from
the documentation repository and include them in the lab handoff.

The author created `sri299792458/g1-research-docs` for following the draft.
The Pages workflow builds static HTML and deploys it through GitHub Actions;
repository Pages settings must use **GitHub Actions** as their source. The
README records the live link once publication is verified.

For the later lab copy, preserve Git history and tag the reviewed summer
version. Update `html_baseurl` and repository/edit links in `docs/conf.py`,
enable Pages, and check media access. Link the personal portfolio version
and the lab's maintained version from both READMEs. Date later lab additions
so the original summer contribution remains identifiable.
