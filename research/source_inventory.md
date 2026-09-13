# Source inventory and reading coverage

This is an internal research index, not the documentation navigation. Line
numbers refer to the local files captured in `source_snapshot.json`.

## Primary running notes

| Source | Lines | Reading status |
|---|---:|---|
| [G1Pilot](../../g1pilot/running_notes.md) | 1,328 | Not yet read sequentially; first reading pass starts here. |
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

## Reading method

1. Read notes sequentially in manageable ranges and record completed coverage.
2. Extract the problem, attempted approach, observed result, lesson, limitation,
   and later correction, with a source line or artifact reference.
3. Distinguish source-reported checks from independent inspection performed here.
4. Keep physical knowledge and media gaps visible for focused author discussion.
5. Update the working notes and commit meaningful documentation progress.
