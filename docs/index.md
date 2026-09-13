# Working with the G1

During the summer, I used the Unitree G1 to understand what it would take to
make the robot useful for research: what it could do, where its models and
interfaces fell short, and what tooling would let someone else build on the work.

The work grew from G1Pilot bring-up and an initial MuJoCo backend into printed
fiducial targets, Dex3 sensing, camera and arm calibration, offline grasp
qualification, CuRobo planning, physical cube manipulation, and continuous
recording. Much of the effort went into the transitions between these pieces:
acquiring control without a jump, preserving the command while planning,
recognizing a failed grasp, and returning the robot to a known state.

This guide preserves those details. It explains the working tools and the
experiments that changed them, including approaches that looked reasonable
but failed on the real system. The aim is for the next lab member to start
from that experience and extend it with confidence.

```{admonition} First draft · summer work with follow-up through September 7, 2026
:class: note

This draft awaits the author's review. Procedures and results have different
evidence levels. The latest manually preclosed calibration workflow still
needs new route generation and physical validation; moving-target MPC
remains experimental. Missing installation details and media are collected
in the [review queue](reference/review.md).
```

## Where to begin

| Your goal | Start with |
|---|---|
| Understand the summer's contributions | [Overview and results](start/overview.md), then [timeline](start/timeline.md) |
| Start working with the lab robot | [Hardware](hardware/robot.md), [setup](start/setup.md), and [control ownership](control/ownership.md) |
| Understand a failed grasp or route | [Grasp atlas](manipulation/grasp-atlas.md), [planning](manipulation/planning.md), and [debugging](reference/debugging.md) |
| Work on calibration | [Workflow](calibration/workflow.md), [results](calibration/results.md), and [investigations](calibration/investigation.md) |
| Use the recordings | [Recording and LeRobot](data/recording.md) |
| Continue the documentation | [Maintenance](reference/maintenance.md) and [sources](reference/sources.md) |

## How the pieces connect

During a manipulation task, measured robot state and object observations feed
route planning, then the fixed-rate controller executes the checked motion.
On a narrow screen, scroll diagrams horizontally or select **Expand**.

```mermaid
flowchart LR
  accTitle: From observation to execution
  accDescr: Observe the robot and scene, plan the approach and return, then execute motion and check the grasp.
  O["Observe robot<br/>and scene"] --> P["Plan approach<br/>and return"]
  P --> E["Execute motion<br/>and check grasp"]
```

[Calibration](calibration/workflow.md) supplies the camera/arm model;
the [grasp library](manipulation/grasp-atlas.md) supplies qualified candidates.
The independent [PC2 watchdog](control/ownership.md) handles its defined fault
recovery, while the recorder preserves robot state and commands through cleanup.

After the run, the retained evidence supports two separate uses:

```mermaid
flowchart LR
  accTitle: Using the recorded evidence
  accDescr: Raw recordings and task records support failure analysis and model or tooling improvements. An offline conversion also creates LeRobot training episodes.
  R["Raw recordings<br/>and task records"] --> A["Analyze outcomes<br/>and failures"]
  A --> I["Refine models<br/>and tooling"]
  R --> D["Convert to LeRobot<br/>training episodes"]
```

The [recording chapter](data/recording.md) explains what survives conversion
and why the raw evidence remains useful.

The [G1Pilot digital twin](simulation/mujoco.md) is a separate early development
path. It offers familiar SDK interfaces in MuJoCo; it does not reproduce the
proprietary Unitree walking controller or certify the later tabletop pipeline.

This guide follows the practical style of the earlier
[SPARK documentation](https://rpm-lab-umn.github.io/spark-data-collection/).
The [source catalog](reference/sources.md) explains which supporting records
are public and which still require a lab archive.

```{toctree}
:hidden:
:caption: Start here
:maxdepth: 1

Reading paths and results <start/overview>
Summer timeline <start/timeline>
Repositories and setup <start/setup>
```

```{toctree}
:hidden:
:caption: Hardware and control
:maxdepth: 1

The lab robot <hardware/robot>
Camera and network <hardware/camera>
Ownership and safety <control/ownership>
Operating and recovering <control/runbook>
G1Pilot bring-up <control/g1pilot>
```

```{toctree}
:hidden:
:caption: Perception and calibration
:maxdepth: 1

Printed targets and mounts <perception/targets>
Object pose estimation <perception/object-pose>
Calibration model and workflow <calibration/workflow>
Calibration results and limits <calibration/results>
Investigation record <calibration/investigation>
Body motion and state estimation <perception/state-estimation>
```

```{toctree}
:hidden:
:caption: Grasping and planning
:maxdepth: 1

GraspGen-X and the grasp atlas <manipulation/grasp-atlas>
Assembly experiments <manipulation/assembly>
CuRobo planning contracts <manipulation/planning>
Pickup and stacking <manipulation/tasks>
Moving-target MPC <manipulation/mpc>
```

```{toctree}
:hidden:
:caption: Sensing, simulation, and data
:maxdepth: 1

Dex3 pressure <sensing/pressure>
MuJoCo digital twin <simulation/mujoco>
Recording and LeRobot <data/recording>
```

```{toctree}
:hidden:
:caption: Reference and maintenance
:maxdepth: 1

Debugging from evidence <reference/debugging>
Sources and attribution <reference/sources>
Media catalog <reference/media>
Maintaining this guide <reference/maintenance>
Writing diagrams <reference/diagrams>
Draft review queue <reference/review>
```
