# Maintaining the G1 guide

- Read README.md, CONTRIBUTING.md and the source catalog before editing.
  If private `.local/maintainer-context.md` and `running_notes.md` are available,
  read them for author decisions and continuity; they are not publication inputs.
- Organize by subsystem/task, with Mermaid diagrams and commit-pinned code maps.
  Preserve interfaces, invariants, practical lessons and validation limits.
- Keep the demonstrated August tabletop main distinct from the September
  experimental calibration branch. Match links to the inspected file bytes.
- Distinguish static inspection, offline tests, simulation, physical trials and
  deployed behavior. Completed recordings are not scored task successes.
- For calibration, follow the investigation summary and retained operator
  corrections. In the original source checkout, read its AGENTS.md and ledger.
  Documentation work does not authorize restarting experiments or hardware use.
- Keep personal running notes, research reviews and design proposals private.
  Use ignored local storage and check public history before publication.
  Never publish `.local/`, `research/`, raw notes, credentials or raw bags.
- Preserve original source checkouts, recordings and media. Documentation edits
  do not authorize changing another repository or deleting datasets.
- Maintain private running notes locally and public documentation in Git.
  Agent-authored commits must use the project author's established identity:
  `srinivas <srinivas299792458@gmail.com>`. Do not add assistant attribution.
- Build with Sphinx + MyST + Furo; keep customization minimal. Use the shared
  Mermaid conventions and review desktop rendering. Mobile polish is deferred.
- Update docs/assets/code-map.json deliberately and regenerate the code index
  with `python3 tools/build_code_index.py`. Run its `--check`, the strict Sphinx
  build, `git diff --check` and desktop browser checks for affected content.
- Hardware photo annotations use editable SVG layouts in
  docs/assets/hardware-figures.json. Keep captions/instructions in Markdown.
  Regenerate with tools/build_hardware_figures.py and run its --check after edits.
- Keep datasets outside Git. Selected Drive downloads have separate README and
  checksums. Do not claim a public link exists before the upload is verified.
- Keep the personal portfolio and eventual lab-maintained copy attributable,
  with clear ownership of source, media and datasets during handoff.
