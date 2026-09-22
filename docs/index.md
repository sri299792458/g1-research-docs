# Working with the G1

This guide explains the tools and practical knowledge developed while working
with the G1: controlling the robot, recording experiments, understanding its
sensors and geometry, and building planning or simulation on those foundations.
The aim is to help another researcher build a different experiment without
having to rediscover the same failures.

## Start with the reusable systems

| What you need | Start here |
|---|---|
| Acquire control, hold during slow work and recover from failures | [Control ownership and safety](control/ownership.md), [operating and recovering](control/runbook.md) |
| Record an experiment and inspect the result | [Recording, signals and LeRobot conversion](data/recording.md), [dataset downloads](data/recording.md#dataset-downloads) |
| Prepare the robot and its sensors | [Hardware and hand installation](hardware/robot.md), [camera/network](hardware/camera.md), [pressure sensing](sensing/pressure.md) |
| Understand or improve camera/arm geometry | [Targets and mounts](perception/targets.md), [calibration](calibration/workflow.md), [completed investigations](calibration/investigation.md) |
| Add grasping or motion planning | [Grasp qualification](manipulation/grasp-atlas.md), [CuRobo integration](manipulation/planning.md) |
| Develop against a simulated robot | [Initial MuJoCo digital twin](simulation/mujoco.md) |

The [cube-stacking demonstration](manipulation/tasks.md) is an integration
example, showing how several of these systems were exercised together.
Assembly and moving-target experiments record further lessons and unresolved
limits for extending the system.

The demonstrated manipulation code and later experimental calibration code
remain distinct. Use [repositories and setup](start/setup.md) to choose an
environment and the [source catalog](reference/sources.md) to identify its revision.

## How to use the guide

Hardware pages pair photographs or CAD views with files and fitting details.
Operating pages explain prerequisites, actions and outcomes. Implementation
pages explain the design, failures that shaped it and the code to change.
Diagrams appear where a sequence or relationship needs a visual explanation.

For code work, start with the [system map and entry points](start/overview.md)
and the relevant chapter. The [code index](reference/code-index.md) supplies
commit-pinned files, symbols and file hashes for readers and coding agents.
The prose records assumptions and evidence that a file list alone cannot convey.

This is a working draft. Remaining gaps include parts of the electrical
installation procedure, some physical fit checks and run-to-video associations;
see the [review queue](reference/review.md). To improve a chapter, follow
[Maintaining this guide](reference/maintenance.md). [About](about.md) records
authorship and project context.

```{toctree}
:hidden:
:caption: Start here
:maxdepth: 1

System map and code entry points <start/overview>
Repositories and setup <start/setup>
```

```{toctree}
:hidden:
:caption: Hardware and setup
:maxdepth: 1

The lab robot <hardware/robot>
Dex3 pressure sensing <sensing/pressure>
Camera and network <hardware/camera>
Printed targets and mounts <perception/targets>
```

```{toctree}
:hidden:
:caption: Control and safety
:maxdepth: 1

Ownership and safety <control/ownership>
Operating and recovering <control/runbook>
```

```{toctree}
:hidden:
:caption: Recording and datasets
:maxdepth: 1

Recording and LeRobot <data/recording>
```

```{toctree}
:hidden:
:caption: Perception and calibration
:maxdepth: 1

Object pose estimation <perception/object-pose>
Calibration model and workflow <calibration/workflow>
Calibration results and limits <calibration/results>
Investigation record <calibration/investigation>
Body motion and state estimation <perception/state-estimation>
```

```{toctree}
:hidden:
:caption: Grasping and manipulation
:maxdepth: 1

GraspGen-X and the grasp atlas <manipulation/grasp-atlas>
CuRobo integration <manipulation/planning>
Cube stacking: integration example <manipulation/tasks>
Assembly experiments <manipulation/assembly>
Moving-target MPC <manipulation/mpc>
```

```{toctree}
:hidden:
:caption: Simulation
:maxdepth: 1

MuJoCo digital twin <simulation/mujoco>
```

```{toctree}
:hidden:
:caption: Reference and maintenance
:maxdepth: 1

Debugging from evidence <reference/debugging>
Sources and attribution <reference/sources>
Code index <reference/code-index>
Media catalog <reference/media>
Maintaining this guide <reference/maintenance>
Writing diagrams <reference/diagrams>
Remaining review needs <reference/review>
About this guide <about>
```
