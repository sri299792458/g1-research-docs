# Documentation running notes

## 2026-09-13 — Purpose, scope, and collaboration established

### Author's intent

The documentation should be a useful resource for other people who want to work
on the G1. The summer work explored the robot's capabilities and limitations and
built internal tools and safety procedures for research on top of the SDK.
Successful documentation should enable someone else to build on that work.

The author emphasized that generating code is easier than recovering the
judgment earned through iterations on physical hardware. The running notes must
be read line by line and understood deeply; the final codebase alone does not
explain the development process, failures, and physical results.

### Explicit scope and process decisions

- Cover all summer G1 work, not only `g1-dex3-tabletop`.
- Work back and forth with the author; do not write the documentation in one shot.
- The author is still considering how to organize it. No table of contents is accepted.
- Maintain our own `running_notes.md` and Git repository.
- The author can provide images and videos where needed.
- The Spark site is an example reference for documentation style and depth.

### Work described by the author — inventory, not proposed chapters

- Practical Dex3 installation, including the JST extension cables bought for it.
- 3D-printed AprilCubes for object-pose estimation.
- Calibration of the head-mounted RealSense using 3D-printed Dex3 wrist marker mounts.
  The head pitches manually; it is not motorized. Inaccurate G1 forward kinematics
  made calibration difficult. Specific findings must be taken from the evidence
  and the calibration ledger rather than generalized to every error source.
- GraspGen-X for offline grasp proposals.
- Substantial G1 control and safety pipeline development.
- CuRobo trajectory planning for cube stacking.
- Exploration of Dex3 pressure sensors.
- An initial MuJoCo G1 digital twin, motivated by the proprietary default walking
  controller. Its implemented and validated scope remains to be read from sources.
- Extension of SPARK-style logging to G1.

### Work started

Created `/home/kanth042/g1-research-docs` as a separate local Git repository on
`main`. This is an internal documentation workspace, with no site publication or
reader-facing chapters yet. No source-repository files or Git state were changed.

The initial inventory found 1,328 lines of G1Pilot notes, 1,864 lines of prototype
notes, and 7,403 lines of tabletop notes. A further 126-line AprilCube note file is
present under the tabletop repository's `third_party` directory.

The prototype's lines 2–1,864 have identical line contents to tabletop lines
359–2,221. This is inherited history, not a second independent experiment record.
Record shared coverage explicitly when read; do not double-count results.

Some sources contain uncommitted work, including the tabletop running notes.
Record local file hashes as well as commit IDs so later citations describe the
material actually read. The source snapshot is an inventory, not a backup.

The prior conversation reviewed the Spark site's structure, representative
procedures, design pages, and fixture documentation, plus the G1 calibration
ledger and selected existing documents. Those reads do not constitute a complete
reading of the source running notes. Exact new coverage is maintained in the
source inventory.

### Open items for later discussion

- Exact summer date boundaries: located notes extend into September; inclusion
  in the historical narrative is not yet settled. Later corrections still matter.
- Location and validation scope of the initial MuJoCo digital twin work.
- Precise Dex3 installation and JST cable details, with photographs where useful.
- Which demonstrations, photos, and videos should illustrate individual lessons.
- Reader entry points and documentation organization, after source understanding.

## 2026-09-13 — G1Pilot running notes read completely

Read all 1,328 lines sequentially, in four contiguous ranges. Detailed findings,
source ranges, reported verification, and limitations are preserved in
[`research/g1pilot-reading.md`](research/g1pilot-reading.md).

The reading adds early environment, SDK integration, frame/model, and navigation
work to the summer inventory. It contains 38 issue dispositions and physical
LiDAR/TF and camera-access evidence. Do not confuse offline visualization with
the separately mentioned initial MuJoCo digital twin.

Three examples worth discussing when shaping the eventual documentation:

- The physical PC2 USB path resolved the camera-access failure; the working ZMQ
  stream and unresolved browser playback were different observations.
- Repeated messages can replay a stale autonomous command. The mux fix had a
  specific scope and did not substitute for a lower-level watchdog.
- An apparently plausible solver time-scaling change was rejected after checking
  that the solver already returned a per-step increment.

The early arm emergency helper, live-state initialization change, and balancing
fixes must retain their recorded limitations. Later hardware commissioning and
operator corrections govern any future executable procedure.

Asked the author where to find the initial MuJoCo digital twin repository/folder
and notes. No answer was available when this entry was written. The question is
about locating existing work, not approval to create or run a simulator.

The initial Git commit is `a0f1ed9`. Commits in this new workspace use the explicit
agent identity `Codex <codex@localhost>` because no global user identity was
configured. Global Git configuration was not changed.

Remaining sequential reading is recorded as pending in the source inventory.
No reader-facing chapter, final table of contents, or website has been drafted.

Documentation checks: all local Markdown link targets exist, the source snapshot
parses as JSON, all nine snapshotted source files still match their initial
SHA-256 hashes, and `git diff --check` passes. These are documentation checks;
none independently validate the robot software discussed in the source notes.
