# Sources and attribution

The guide connects public code to recorded hardware, simulation and offline
results. Choose the implementation version before adapting a procedure: the
successful August demo and the later calibration development are separate branches.

## Published repositories

| Repository / branch | Inspected revision | What belongs here |
|---|---|---|
| [Tabletop `main`](https://github.com/sri299792458/g1-dex3-tabletop/tree/7400aff201c2f73ef2a64e546d72bd66cbe87fd6) | `7400aff` | August 25 demo baseline: seated control, cube perception, grasp/planning contracts, stacking, recording and conversion |
| [Tabletop September branch](https://github.com/sri299792458/g1-dex3-tabletop/tree/59c21b1388c636176dea67ea7ed3e253f8510783) | `59c21b1` | Later calibration runtime, diagnostics, shared-control changes and regression fixtures; includes the previously uncommitted work |
| [Calibration and fixtures `main`](https://github.com/sri299792458/robot-calibration-aprilcube-prototype/tree/f295def18bd936031fba325d4e8bdfc71fea671a) | `f295def` | Reusable calibration tools, bundle support, wrist markers, V7 torso structure and R2 coupons |
| [Grasp/assembly `main`](https://github.com/sri299792458/g1-aprilcube-demo/tree/2b7274b11f1862ebfcd05b48ff678d995e55269e) | `2b7274b` | Offline GraspGen-X descriptors, qualification, support studies and assembly planning |
| [G1Pilot June implementation](https://github.com/sri299792458/g1pilot/tree/72acc803edefe583c24f53e76a21d8d4ed10ed14) | `72acc80` | Initial ROS/OpenSoT integration and hardware bring-up |
| [G1Pilot July simulator](https://github.com/sri299792458/g1pilot/tree/6b5af59b109e2ee687920fdf66ded6182725e945) | `6b5af59` | Initial MuJoCo/OpenHomie backend, supplied on `dev` |
| [Dex3 pressure tools](https://github.com/sri299792458/dex3_pressure_tools/tree/e0b706df507160799b70732c7cc3244924ce8f5e) | `e0b706d` | Passive recording, baseline-relative visualization and taxel mapping |

The tabletop demo revision preserves runtime code, tests, configuration and
submodule pins from `d1b0103`, the commit recorded by the August 25 runs. The
September branch is one additional commit over that clean main. It carries the
September 4 checkpoint and later local changes together. Neither a newer branch
nor a passing offline test replaces the demonstrated configuration.

The fixture repository remains separate from tabletop. Its consolidated main
includes both V7/R2 and the earlier calibration-bundle addition; there is no need
to choose between former development branches to obtain those files. It still
has the [documented physical fit limits](../perception/targets.md#torso-charuco-carrier).
AprilCube and the other upstream dependencies remain pinned submodules of the
code repositories; initialize the revisions recorded by the chosen checkout.

## Follow the implementation and its evidence

The [code index](code-index.md) supplies exact file URLs, hashes and Python
symbols. Its [JSON map](../assets/code-map.json) can be consumed by an agent or
checked against a clone. All mapped implementation files are public. A chapter
using September-specific code labels that boundary explicitly.

Public technical reports live alongside their implementation—for example the
[grasp descriptor study](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/docs/dex3_rev1_descriptor.md),
[September runtime summary](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/docs/september-calibration.md)
and [torso fit record](https://github.com/sri299792458/robot-calibration-aprilcube-prototype/blob/f295def18bd936031fba325d4e8bdfc71fea671a/artifacts/g1_mount_v7/FIT_STATUS.md).
The [media catalog](media.md) records the selected photographs/videos and their
review limits; captions distinguish physical footage from rendered replay.

Personal running notes, design proposals and raw investigation records remain
private. They informed the explanations, but this guide does not require readers
to obtain a private journal to locate code. Raw sessions and full analysis work
directories are separate from a source clone. When their findings are summarized,
the chapter states the experiment, measured quantity and limits rather than
pretending the underlying dataset is included.

## What was checked

The draft's source reading covered the G1Pilot, grasp-demo, tabletop and
calibration-prototype logs, the later investigation ledger and the V7 fit update.
Inherited prototype notes were treated as shared history, not independent trials.
Later operator corrections govern conflicting older reports. Calibration
corrections extend through September 7 and fixture fit evidence through
September 13, 2026.

Unless labelled as an independently rerun check, experiment results and historic
test counts are reported from retained evidence. During source publication,
selected September offline regressions passed **317 tests with seven skipped**.
That checked software packaging and regressions; it did not commission the final
standing lifecycle. The documentation checks verify links, file identities,
rendering and the site build without operating the robot.

The five August 25 episodes are available as a LeRobot download. The August 12
calibration archive includes original captures, selected fit inputs and the
historical bundle. Both have [versioned downloads and checksums](../data/recording.md#dataset-downloads)
on Google Drive, separate from the source repositories.

## Attribution and continuity

The research and this guide are by
[srinivas (`sri299792458`)](https://github.com/sri299792458), building on Unitree's
SDK/models, AprilCube, GraspGen-X, CuRobo, Isaac/PhysX, Newton, MuJoCo, OpenHomie,
GR00T, ROS, Pinocchio/OpenSoT and SPARK. Including a dependency does not imply
original authorship of that dependency.

The author's [SPARK documentation](https://rpm-lab-umn.github.io/spark-data-collection/)
provides the reference for practical depth. A later lab copy should preserve
attribution, useful public history and access to published source/media.
No blanket documentation license has been assigned yet; preserve existing
upstream notices and settle the license before the final handoff.
