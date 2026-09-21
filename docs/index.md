# Working with the G1

This guide explains the G1 research tools: how they connect, where they are
implemented, and what must remain true when you change them. Start with a
subsystem below, follow its diagram into the code, and use the recorded
results and failures to understand its limits.

## Tabletop system at a glance

```mermaid
flowchart TB
  accTitle: G1 tabletop components and their interfaces
  accDescr: Calibration supplies the camera and arm model for observations. Observations and an offline grasp library feed planning. Checked routes feed execution, which is monitored by PC2 and recorded for analysis.
  C["Camera and arm<br/>calibration"] -->|model| O["Robot state<br/>and object pose"]
  O -->|scene and start state| P["CuRobo<br/>route planning"]
  G["Offline grasp<br/>qualification"] -->|candidate pool| P
  P -->|checked route and return| E["Fixed-rate<br/>execution"]
  W["PC2 watchdog"] -.->|lease and recovery| E
  E -->|state, commands and outcome| R["Raw recording<br/>and offline analysis"]
```

This is a component map, not a launch sequence. The [system map](start/overview.md)
explains the interfaces; [ownership and safety](control/ownership.md) explains
the control lifecycle. Select **Expand** or scroll horizontally on a narrow screen.

```{admonition} Working draft · summer research and subsequent corrections
:class: note

Procedures and results have different
evidence levels. The latest manually preclosed calibration workflow still
needs new route generation and physical validation; moving-target MPC
remains experimental. Missing installation details and media are collected
in the [review queue](reference/review.md).
```

## Choose the right source

| Work | Source to use |
|---|---|
| August 25 cube-stacking demo | [Tabletop `main`](https://github.com/sri299792458/g1-dex3-tabletop/tree/7400aff201c2f73ef2a64e546d72bd66cbe87fd6) |
| Later calibration development | [Tabletop September branch](https://github.com/sri299792458/g1-dex3-tabletop/tree/59c21b1388c636176dea67ea7ed3e253f8510783) — experimental, with no replacement calibration deployed |
| Wrist targets, V7 torso mount and calibration tools | [Calibration/fixture `main`](https://github.com/sri299792458/robot-calibration-aprilcube-prototype/tree/f295def18bd936031fba325d4e8bdfc71fea671a) |
| Offline grasp generation and assembly studies | [Grasp-demo `main`](https://github.com/sri299792458/g1-aprilcube-demo/tree/2b7274b11f1862ebfcd05b48ff678d995e55269e) |

The [source catalog](reference/sources.md) also covers the MuJoCo twin and tactile
tools. Each code link pins the version being explained; September changes are
kept separate from the physical demo baseline.

## Find the part you need

| Your goal | Start with |
|---|---|
| Locate an implementation or give an agent context | [System map](start/overview.md), then the relevant chapter's code map |
| Start working with the lab robot | [Hardware](hardware/robot.md), [setup](start/setup.md), and [control ownership](control/ownership.md) |
| Understand a failed grasp or route | [Grasp atlas](manipulation/grasp-atlas.md), [planning](manipulation/planning.md), and [debugging](reference/debugging.md) |
| Work on calibration | [Workflow](calibration/workflow.md), [results](calibration/results.md), and [investigations](calibration/investigation.md) |
| Understand Dex3 pressure sensors | [Pressure sensing](sensing/pressure.md) |
| Work with the initial simulator | [MuJoCo digital twin](simulation/mujoco.md) |
| Use the recordings | [Recording and LeRobot](data/recording.md) |
| Continue the documentation | [Maintenance](reference/maintenance.md) and [sources](reference/sources.md) |

## Read a chapter alongside its code

Technical chapters start with a focused Mermaid diagram and a table mapping
its parts to source files and symbols. The explanation then follows the data
or control flow, including assumptions, rejected approaches and validation.
Mermaid source remains in the Markdown, so an agent can read the graph too.

All mapped implementations now have public, commit-pinned links. The
[code index](reference/code-index.md) records the branch, file hash and symbols,
including both demo and September versions where their code differs.
The [About page](about.md) records authorship and project context.

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
CuRobo planning contracts <manipulation/planning>
Pickup and stacking <manipulation/tasks>
Assembly experiments <manipulation/assembly>
Moving-target MPC <manipulation/mpc>
```

```{toctree}
:hidden:
:caption: Recording and datasets
:maxdepth: 1

Recording and LeRobot <data/recording>
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
Draft review queue <reference/review>
About this guide <about>
```
