# Maintaining and extending the guide

Edit ordinary Markdown under `docs/`. The site uses Sphinx, MyST and Furo with
minimal customization. Follow the [local build instructions](README.md) and
[maintenance guide](docs/reference/maintenance.md).

## Make a change another researcher can assess

1. Read the relevant page and its [source catalog](docs/reference/sources.md)
   and [code index](docs/reference/code-index.md). Choose the demonstrated main
   or the September experimental branch explicitly before changing a procedure.
2. Keep the change focused on one procedure, result, correction or topic.
   Technical chapters begin with a Mermaid diagram and verified file/symbol
   map, followed by interfaces, assumptions, lessons and validation. Git history
   preserves superseded drafts; the current site presents the current guide.
3. State prerequisites and expected observations. Preserve the reason for a
   step when a previous failure explains it.
4. Distinguish proposals, static inspection, offline tests, simulation, physical
   experiments and deployed behavior. Give the run/date/configuration where known.
5. Keep later corrections traceable. An old note's next step is not automatically
   a current recommendation, and a completed recording is not a scored success.
6. Record reader-relevant corrections in the chapter and commit description.
   Keep personal running notes and unpublished design proposals outside public
   history, for example under ignored `.local/`.
7. Run `.venv/bin/sphinx-build -n -W --keep-going -b html docs site` and
   `git diff --check`; review the rendered page on desktop. Mobile layout polish
   is deferred to the final presentation review.

Add new pages to the hidden MyST `toctree` blocks in `docs/index.md`. The CI
workflow runs the strict build and deploys main to Pages. A documentation edit
does not require running any robot experiment.

## Evidence and attribution

Use commit-pinned URLs to the exact public implementation. The current code map
contains only published source files; private working notes are not required to
resolve those links. Update the JSON map and regenerate the Markdown index with
`python3 tools/build_code_index.py` when reviewed source identities change.
If new evidence is not public, state that limitation instead of linking to a
different implementation. Absolute machine paths belong in ignored `.local/`
files. Source hashes are not backups; preserve underlying evidence separately.

For calibration, read the [investigation summary](docs/calibration/investigation.md)
and the technical reports linked from it. If working in the author's original
checkout, its `AGENTS.md` and private investigation ledger supply additional
operator corrections and completed experiments. Do not restart experiments
just because private notes are unavailable. A documentation edit does not
authorize hardware investigations or source-repository changes.

Give upstream tools/models their credit. Keep claims proportional to the
reported evidence and write in a direct lab-guide voice.

## Media and the future lab copy

Add selected publication images with meaningful alt text and captions. Update
`docs/assets/media.json` with the source, context, review status and checksum.
Keep larger videos in versioned releases and originals in backed-up lab storage.
Test playback independently from download links. Do not commit raw bags,
credentials or expiring share URLs.

Before the lab handoff, tag the reviewed summer version, preserve Git history,
update repository/site/edit links, confirm media ownership/access, and cross-link
the personal portfolio and maintained lab copy. Date later extensions. The
license, lab destination and tag remain author-review decisions.
