# Assembly and support experiments

These experiments explored whether the grasp library and CuRobo could support
T/U/cube assembly and placement into a box. They produced kinematic plans,
replays and support-conditioned grasp studies; they did not demonstrate physical
G1 assembly.

The reusable lessons concern access to a supported object, paired arm goals
and consistent attachment geometry. Start here when extending beyond cubes;
use [pickup and stacking](tasks.md) for the demonstrated hardware workflow.

| Experiment | Useful result | Boundary of the evidence |
|---|---|---|
| T/U/cube assembly | Role/alternative search and complete pick/mate/place planning | Attachment events are symbolic |
| U-shape pickup | Resting orientation strongly limits usable grasps | Intrinsic retention alone did not predict supported pickup |
| Cube into an open box | Explicit wall geometry and broader orientation search | Displayed drop is a kinematic event |


## T/U/cube assembly

The assembly planner used a fixed-torso, 28-joint model without the lower body,
explicit voxel geometry and composite attachments. Magnetic snaps were
symbolic state transitions, not simulated magnetic forces. Nominal and shuffled
runtime scenes passed kinematic replay, but those demonstrations do not show
physical G1 assembly.

```{figure} ../assets/images/unibot_seated_aprilcube_scene_v1.png
:alt: Rendered G1 beside a table containing a cube, T and U shape in the assembly planning scene.

The early assembly scene used observed seated state and 45 mm voxel parts.
This render illustrates planning geometry, not a completed hardware task.
[Provenance](../reference/media.md).
```

Initially, some region/keepout fields were parsed without affecting planning,
and arm assignment was hard-coded. Those findings matter when extending the
planner: an accepted configuration field is not evidence that the constraint
is enforced. The final record does not support a generic arbitrary-flat-part
assembly capability.

## Why the U shape was difficult

The right-hand U atlas had 675 intrinsic passes, yet only four were open-hand
clear in the early flat-support test, and none passed the native pickup.
Six support orientations made the resting geometry explicit. A broad
42-physics-trial test still produced no passes.

```{figure} ../assets/images/u_legs_six_tabletop_supports.png
:alt: Six U-shape resting orientations, including flat, upright, inverted and either outer leg down.

Changing support changes access to the object. Counts in this source figure
are geometric candidates, not simulated or physical successes.
[Provenance](../reference/media.md).
```

Upright support was more productive: 1,837 tested candidates led to 405
discovery passes and 365 replay passes, with 13/14 passing in one visual review.
The larger broad-support search generated 100,000 raw proposals from 391 seeds;
983 cleared the geometric approach corridor, but none passed physical
simulation. One apparent near-lift involved about 203 N of hand/table contact
and was rejected.

An additional LightningGrasp adaptation produced pose plus joint solutions:
287 solutions, 574 support pairs, 14 eligible physical tests and zero passes.
Twenty overclosure tests also failed. This constrained the tested approach;
it does not prove that every possible U pickup strategy is impossible.

## CuRobo integration lessons

A goal set contains alternative endpoints for a planning problem. It is not
the same as an independent batch of complete motion-planning problems.
Independent batches of 16/32 exceeded memory; eight ran, but 1,240 plans took
about 156 s. Thirty-two-alternative goal sets and prefix backtracking better
matched the assembly search.

With multiple tools, independent goal-set indices did not preserve an intended
paired row. The corrected paired-mate test used singleton two-tool hypotheses.
Attachment updates also had to reach both IK and trajectory-optimization
managers. Updating only one leaves the solvers reasoning about different robots.

## Cube to an open box

The box was represented by a floor and four walls. A filled AABB would model
the usable interior as an obstacle. Twenty-four orientation alternatives
solved cases where eight yaw-only goals failed; seeds 7 and 19 passed the
kinematic plan. The displayed drop was symbolic and should be captioned as
kinematic replay rather than a physics-validated release.

Newton right-arm cube/T/U lift demonstrations prescribed exact arm motion
while simulating fingers and object. T/U trials exceeded soft finger limits by
up to 0.228 rad. They therefore do not validate whole-arm dynamics or hardware
joint-limit behavior.

The later physical work narrowed the task to carefully qualified cube
[pickup and stacking](tasks.md). This reduction made the full sensing,
ownership, planning, contact and recovery sequence testable on the robot.

Evidence: grasp-demo support, assembly and replay entries. See the
[source catalog](../reference/sources.md) and [media catalog](../reference/media.md).

## Follow the code

| Implementation concern | Code entry point | Responsibility |
|---|---|---|
| Task, observations and alternatives | [runtime_assembly.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/g1_aprilcube_demo/planning/runtime_assembly.py#L189) · `RuntimeAssemblyPlanner` | Load the task/scene and assign holder/worker roles. |
| Complete mode search | [runtime_assembly.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/g1_aprilcube_demo/planning/runtime_assembly.py#L189) | Follow `qualify_modes`, `_plan_complete_mode` and `execute` within the planner. |
| Support-conditioned candidates | [support_atlas.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/g1_aprilcube_demo/grasping/support_atlas.py#L462) · `evaluate_support` | Check geometric pickup access for a specified resting support. |

In `RuntimeAssemblyPlanner`, follow the scene/attachment updates as well as the accepted trajectories. A symbolic mate or drop changes planning state; it does not simulate magnetic force or verify that the real part remains attached.

## Checks and evidence to inspect

The grasp-demo repository’s `tests/test_runtime_assembly.py` and `tests/test_runtime_role_assignment.py` are the software regression entry points. The support trials and replay outcomes above bound the demonstrated capability. None establishes physical G1 assembly.
