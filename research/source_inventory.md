# Source inventory and reading coverage

This is an internal research index, not the documentation navigation. Line
numbers refer to the local files captured in `source_snapshot.json`.

## Primary running notes

| Source | Lines | Reading status |
|---|---:|---|
| [G1Pilot, local June 21 log](../../g1pilot/running_notes.md) | 1,328 | Complete: lines 1–1,328 read sequentially on 2026-09-13. [Reading notes](g1pilot-reading.md). Remote `dev` adds later code; see below. |
| [Calibration prototype](../../robot-calibration-aprilcube-prototype/running_notes.md) | 1,864 | Pending. Lines 2–1,864 match tabletop lines 359–2,221. |
| [G1 Dex3 tabletop](../../g1-dex3-tabletop/running_notes.md) | 7,403 | Pending; earlier heading inventory is not sequential reading. |
| [AprilCube notes](../../g1-dex3-tabletop/third_party/aprilcube/running_notes.md) | 126 | Pending; check provenance before attributing work. |

## Supporting evidence already located

- [Calibration investigation ledger](../../g1-dex3-tabletop/docs/calibration-investigation-ledger.md):
  read in the reference-review phase. Contains completed investigations and current
  operator corrections. Reconcile older findings against it.
- [Dex3 observations](../../dex3_pressure_tools/docs/OBSERVATIONS.md) and
  [README](../../dex3_pressure_tools/README.md): read in the reference-review phase.
  Include local active-slot, idle-noise, topic-rate, and joint-order observations.
  Raw pressure deltas are not calibrated physical forces.
- [Tabletop recording contract](../../g1-dex3-tabletop/docs/data-recording.md):
  located; full reading pending.
- [Prototype research documents](../../robot-calibration-aprilcube-prototype/docs/):
  located; read individual linked studies as their claims are examined.
- [Spark documentation source](../../spark-data-collection/data_pipeline/docs/),
  [MkDocs configuration](../../spark-data-collection/mkdocs.yml), and
  [Pages workflow](../../spark-data-collection/.github/workflows/docs-pages.yml):
  reference structure and representative content reviewed. No G1 site technology
  or publication workflow has been selected.
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
