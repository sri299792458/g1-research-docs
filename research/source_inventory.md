# Source inventory and reading coverage

This is the working research index, not the final documentation navigation. Line
numbers refer to the source files captured in `source_snapshot.json`. Source
paths below identify the repository directory and file, not a required filesystem
layout. Some evidence is local and has not been published with these notes.

## Primary running notes

| Source | Lines | Reading status |
|---|---:|---|
| [G1Pilot, June 21 log](https://github.com/sri299792458/g1pilot/blob/72acc803edefe583c24f53e76a21d8d4ed10ed14/running_notes.md) | 1,328 | Complete: lines 1–1,328 read sequentially on 2026-09-13. [Reading notes](g1pilot-reading.md). Remote `dev` adds later code; see below. |
| `robot-calibration-aprilcube-prototype/running_notes.md` | 1,864 | Complete through the identical shared block: lines 2–1,864 match tabletop lines 359–2,221; title inspected. |
| `g1-dex3-tabletop/running_notes.md` | 7,403 | Complete: lines 1–7,403 read sequentially. Includes uncommitted material. See tabletop-reading.md. |
| `g1-dex3-tabletop/third_party/aprilcube/running_notes.md` | 126 | Complete: all 126 lines. Fork changes above upstream, July 13–15. |

## Supporting evidence already located

- `g1-dex3-tabletop/docs/calibration-investigation-ledger.md`:
  read in the reference-review phase. Contains completed investigations and current
  operator corrections. Reconcile older findings against it.
- `dex3_pressure_tools/docs/OBSERVATIONS.md` and
  `dex3_pressure_tools/README.md`: read in the reference-review phase.
  Include local active-slot, idle-noise, topic-rate, and joint-order observations.
  Raw pressure deltas are not calibrated physical forces.
- `g1-dex3-tabletop/docs/data-recording.md`:
  located; full reading pending.
- `robot-calibration-aprilcube-prototype/docs/`:
  located; read individual linked studies as their claims are examined.
- The [published Spark documentation](https://rpm-lab-umn.github.io/spark-data-collection/),
  plus the local `spark-data-collection/data_pipeline/docs/`, `mkdocs.yml`, and
  `.github/workflows/docs-pages.yml`:
  reference structure and representative content reviewed. MkDocs Material selected for the first draft; publication remains deferred.
- `GR00T-WholeBodyControl`, `Isaac-GR00T`, and `g1pilot_ws` are present locally.
  Their presence alone does not establish original author contributions or
  completed experiments. Find local evidence before including them as summer work.
- G1Pilot's `docs/LAB_G1_ONBOARD_PROFILE.md`, `docs/LAB_LAPTOP_SETUP_HUMBLE.md`,
  `docs/DEX3_PRESSURE_VISUALIZATION.md`, and `static_review.md` are located;
  full reading pending.
- The initial local scan found no tracked MuJoCo-named files in the June 21
  G1Pilot checkout. The author's subsequently supplied remote `dev` branch
  establishes the digital twin's location in G1Pilot. The local scan did not
  cover that newer branch. GR00T simulation code is also present locally; its
  existence alone still does not establish original authorship or completed tests.

## Remote G1Pilot development branch — supplied by the author

Source: [GitHub `dev`](https://github.com/sri299792458/g1pilot/tree/dev), inspected
at `6b5af59b109e2ee687920fdf66ded6182725e945` in an isolated, ignored clone under
`.sources/g1pilot-dev`. The working source checkout was not updated or changed.

- [MuJoCo source reading](g1pilot-mujoco-reading.md): README, simulation modules,
  launch/environment path, diagnostic, and generators read completely. This is
  implementation reading, not a recovered experiment log or runtime validation.
- [Remote source snapshot](g1pilot-dev-source.json): per-file reading coverage,
  hashes, commit history, and release-asset metadata.
- Remote `dev` adds two commits after the local June 21 checkout. The July 1
  commit removes `running_notes.md`; the previous tracked copy is identical to
  the local 1,328-line log already read.
- The initial digital twin source-location question is resolved. The author
  confirmed there are no additional development notes and only this initial
  work was done. Further note-location searches are unnecessary.
- Two simulation demo videos and the reachability map are available in the
  July 1 release. Metadata inspected; media content and map not yet reviewed.

## Reading method

1. Read notes sequentially in manageable ranges and record completed coverage.
2. Extract the problem, attempted approach, observed result, lesson, limitation,
   and later correction, with a source line or artifact reference.
3. Distinguish source-reported checks from independent inspection performed here.
4. Keep physical knowledge and media gaps visible for focused author discussion.
5. Update the working notes and commit meaningful documentation progress.

## Additional public grasp-generation source

`g1-aprilcube-demo` at `f190470742f43101e9a22affaca80554722706ac`: all 3,209 running-note lines and 204 README lines read. See [reading notes](grasp-demo-reading.md). This fills the July descriptor, intrinsic/support qualification, and assembly history. Later tabletop notes supersede its hardware-close and tripod guidance.

Supporting reads completed for the draft: pressure LAB_PROTOCOLS, MATH_AND_SIGNALS, MAPPING_AND_MARKERS, DEPENDENCIES; G1Pilot onboard and native Humble profiles; prototype control/recovery and dorsal mount documents; tabletop recording contract and relevant README sections. Source prose is reconciled against later dated log entries.
