# Working with the G1

Tools and practical lessons for building research experiments on the Unitree G1.

<figure class="research-video">
  <video controls playsinline preload="none" poster="_static/g1-physical-cube-stacking.jpg" width="1920" height="1080" aria-label="Physical G1 cube pickup, stacking and hand withdrawal" aria-describedby="home-stacking-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-physical-cube-stacking.mp4" type="video/mp4">
    Your browser cannot play this video. Use the MP4 link below.
  </video>
  <figcaption id="home-stacking-caption">The G1 picks up a marker cube, stacks it on another, releases it and withdraws its hand. Physical robot demonstration, 91 seconds; silent.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-physical-cube-stacking.mp4">Open or download the video (MP4, 40 MB)</a></p>
</figure>

Cube stacking brought together the main parts of this work: camera and arm
calibration, object pose estimation, offline grasp qualification, CuRobo planning,
robot control and experiment recording. The
[demonstration chapter](manipulation/tasks.md) explains how those pieces fit
together and connects the result to its implementation and recorded evidence.

This guide explains the engineering behind that result, including the failures
that shaped the tools. Use it to understand the demonstrated system or to build
a different experiment on the G1.

## Behind the demonstration

| What you want to understand or reuse | Read next |
|---|---|
| How an application acquires control, keeps holding during planning and returns control after a run | [Control ownership and safety](control/ownership.md), [operating and recovering](control/runbook.md) |
| How the camera, printed targets and arm model establish where objects are | [Camera and network](hardware/camera.md), [targets and mounts](perception/targets.md), [object pose](perception/object-pose.md), [calibration](calibration/workflow.md) |
| How grasp proposals are qualified and used in checked motion plans | [Grasp qualification](manipulation/grasp-atlas.md), [CuRobo integration](manipulation/planning.md) |
| What was recorded, how it becomes LeRobot data and how to inspect it | [Recording and LeRobot](data/recording.md), [download and inspect the datasets](data/viewing.md) |

For physical setup, start with [the lab robot](hardware/robot.md).
[Repositories and setup](start/setup.md) helps you choose the code and environment
for the part you want to use. When something fails,
[debugging from evidence](reference/debugging.md) connects symptoms to the
observations that changed the implementation.

## Simulation and hand sensing

These investigations have their own setups and results. The initial MuJoCo
backend supports the G1Pilot arm and hand interfaces. The pressure tools inspect
Dex3 sensor readings without publishing hand commands.

<div class="media-pair">
  <figure>
    <a href="simulation/mujoco.html#demonstrations"><img src="_static/mujoco-rviz-short-demo.jpg" width="1280" height="720" loading="lazy" alt="RViz arm-pose controls beside the G1 in MuJoCo"></a>
    <figcaption><a href="simulation/mujoco.html">Initial MuJoCo digital twin</a> — arm and hand demonstrations, model choices and the SDK-facing simulation backend.</figcaption>
  </figure>
  <figure>
    <a href="sensing/pressure.html#seeing-the-pressure-display"><img src="_static/dex3-tactile-rviz-demo.jpg" width="1280" height="720" loading="lazy" alt="Dex3 taxel locations and changing pressure-count colors in RViz"></a>
    <figcaption><a href="sensing/pressure.html">Dex3 pressure sensing</a> — raw readings, baseline-relative visualization and the physical mapping study.</figcaption>
  </figure>
</div>

[Assembly and support experiments](manipulation/assembly.md) and
[moving-target MPC](manipulation/mpc.md) explain further planning studies and
their unresolved limits.

## Working with the code

The [system map](start/overview.md) explains the component boundaries; the
[code index](reference/code-index.md) links the files and functions discussed
in the chapters. Use the chapter's assumptions and failure behavior alongside
those links when working with a coding agent.

The guide distinguishes the demonstrated August tabletop code from September
calibration development. [Sources and attribution](reference/sources.md)
identifies the published revisions and upstream work.

This is a working draft. [Remaining review needs](reference/review.md) records
specific gaps. [About](about.md) describes authorship and project context;
[maintaining the guide](reference/maintenance.md) explains how to extend it.

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
Inspect the shared datasets <data/viewing>
```

```{toctree}
:hidden:
:caption: Perception and calibration
:maxdepth: 1

Object pose estimation <perception/object-pose>
Calibration model and workflow <calibration/workflow>
Calibration results and limits <calibration/results>
Calibration investigations <calibration/investigation>
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
