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

The prototype's lines 2–1,864 are byte-for-line equivalent to tabletop lines
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
