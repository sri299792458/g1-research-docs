# Maintaining and extending the guide

Edit ordinary Markdown under `docs/`. The site uses Sphinx, MyST and Furo with
minimal customization. Follow the [local build instructions](README.md) and
[maintenance guide](docs/reference/maintenance.md).

## Make a change another researcher can assess

1. Read the relevant page and evidence. The [source inventory](research/source_inventory.md)
   records coverage; the [snapshot](research/source_snapshot.json) records identity.
2. Keep the change focused on one procedure, result, correction or topic.
   Technical chapters begin with a Mermaid diagram and verified file/symbol
   map, followed by interfaces, assumptions, lessons and validation. Keep the
   summer timeline in the archive rather than the main reading path.
3. State prerequisites and expected observations. Preserve the reason for a
   step when a previous failure explains it.
4. Distinguish proposals, static inspection, offline tests, simulation, physical
   experiments and deployed behavior. Give the run/date/configuration where known.
5. Keep later corrections traceable. An old note's next step is not automatically
   a current recommendation, and a completed recording is not a scored success.
6. Update `running_notes.md` for material decisions and the source inventory
   when reading coverage changes.
7. Run `.venv/bin/sphinx-build -n -W --keep-going -b html docs site` and
   `git diff --check`; review the rendered page, including mobile-width tables/media.

Add new pages to the hidden MyST `toctree` blocks in `docs/index.md`. The CI
workflow runs the strict build and deploys main to Pages. A documentation edit
does not require running any robot experiment.

## Evidence and attribution

Use commit-pinned URLs where the exact source is public. Identify local or
uncommitted evidence by path, hash and status rather than substituting a public
link with different contents. Absolute machine paths belong in ignored `.local/`
files. The source snapshot is not a backup; archive the underlying evidence
as part of the lab handoff.

For calibration, read the source repository's `AGENTS.md` and
`docs/calibration-investigation-ledger.md` first. Preserve operator corrections,
completed experiments and held actions. The documentation task does not
authorize reopening hardware investigations or modifying source repositories.

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
