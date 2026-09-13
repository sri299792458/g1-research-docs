# Reading paths and results

The central contribution is a research workflow around the G1: observe the
actual machine, make physical assumptions explicit, preserve enough evidence
to diagnose failures, and then expand the task. Bring-up, grasp generation,
and execution live in different repositories because they have different
dependencies and failure modes.

## What was accomplished

| Area | Result in the available record | Practical limit |
|---|---|---|
| G1Pilot | Environment repairs, dry-mode fixes, topic/TF integration, camera and LiDAR checks | Complete autonomous navigation was not validated |
| MuJoCo | SDK-style arm/hand interface with locked-waist G1/Dex3 and OpenHomie legs | Initial backend; vendor locomotion and later watchdog semantics are not reproduced |
| Printed targets | Rounded AprilCubes and bilateral dorsal marker carriers | Nominal CAD does not establish manufactured accuracy |
| Pressure | Passive raw audit, baseline recording, mapping and RViz visualization | Raw counts; spatial probing was primarily on the right hand |
| Grasp library | Exact-hand descriptors, Isaac qualification, contact atlases, support studies | Simulated retention does not establish a tabletop pickup |
| Assembly | T/U/cube assembly and cube-to-box plans with visual replay | Symbolic attachment/drop, not physical magnetic assembly |
| Control | Measured acquisition, gravity feedforward, independent recovery, continuous command boundaries | Commissioning applies to recorded configurations |
| Manipulation | Physical 40/60 mm pickup/lift/replacement and direct stack trials | Completion is not a post-release placement measurement |
| Calibration | Reproducible capture, grouped evaluation, arm-geometry investigation | Residual remains; no September replacement bundle deployed |
| State estimation | Chair-motion study, hybrid observer, stationary-boundary integration | Fixed pelvis-origin assumption; no global position observability |
| Data | Raw MCAP and verified LeRobot conversion | Conversion loses full-rate ROS information |

## Three reading paths

For a new operator, read the hardware, camera, ownership, and runbook chapters.
Understand why seated direct control temporarily removes the normal controller
before running motion. Inspect an existing run and its recording manifest.

For an algorithm developer, start with object frames, grasp qualification,
CuRobo contracts, and task execution. A replacement planner must preserve the
measured-versus-commanded distinction and supply recoverable routes. A new
grasp generator must define its frame and finger command.

For a calibration researcher, read the results and investigation record before
proposing experiments. Broad pose coverage, measured-joint inputs, RGB-D fitting,
and many axis/link hypotheses were already examined. The camera was deliberately
adjusted between September datasets. These facts change what the residual means.

## Evidence labels

**Physical** means a real robot or hand experiment is recorded. **Simulation**
means contact or dynamics under a named model. **Offline** means retained-data
replay, planning, fitting, or software checks. **Proposed** means the work was
described but not established as complete. **Current implementation** can still
require physical validation.

A physical failure followed by an offline fix is not yet a successful physical
retry. The chapters preserve that distinction. The [source map](../reference/sources.md)
records complete journal coverage and the local-only evidence boundary.
