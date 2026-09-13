# G1Pilot: first complete reading

Read on 2026-09-13: every line (1–1,328) of
[`g1pilot/running_notes.md`](../../g1pilot/running_notes.md), in consecutive ranges
1–340, 341–680, 681–1,015, and 1,016–1,328. File identity is recorded in
`source_snapshot.json`.

These are research notes for discussion, not a current operating procedure.
Verification below means verification reported in the original log. No ROS nodes,
robot commands, installations, or experiment reruns were launched for this reading.

**Source update, 2026-09-13:** the author supplied the newer GitHub `dev` branch,
which adds the MuJoCo backend in two commits after this local checkout. Its last
tracked running notes are identical to the log read here, then removed in the
July 1 commit. See the [remote MuJoCo reading](g1pilot-mujoco-reading.md). The
findings below concern the June 21 log; its missing digital-twin coverage does
not mean that work is absent from the remote repository.

## What this part of the work contributes

The log begins with the June 21 environment and G1Pilot integration work. It
records dependency repair, a no-robot development path, 38 issue dispositions,
explicit topic/frame ownership, native Humble setup, and physical camera/LiDAR
checks. Its opening goal is a working research environment and validation of
parts that can run without a connected robot.

Many entries describe syntax checks, builds, mock callbacks, or offline node
runs. The camera and LiDAR entries provide specific physical observations. This
distinction must survive any later summer narrative.

## Lessons and evidence to carry forward

### 1. A reproducible environment includes binary compatibility and interpreter choice

Source: lines 11–121, 151–159, 1,240–1,284.

The Docker work pinned Pinocchio against the chosen collision stack, corrected
Boost and Livox build options, controlled NumPy/OpenCV/setuptools versions, and
removed unused packages that introduced conflicting dependencies. Globally
prepending cmeel libraries had caused a double-free during interpreter shutdown.
Python Pinocchio was only used for two quaternion helpers, which were replaced
with SciPy Rotation.

Running colcon through the intended virtual-environment interpreter mattered
because generated console entry points otherwise could not import the installed
Unitree SDK. The later native Humble setup separated admin provisioning from a
single member setup command. Its listed checks are shell syntax/lint checks;
that paragraph alone does not establish a fresh end-to-end native installation.

Preserve the dependency reasons, not just a list of pins. The Docker/Jazzy and
native Humble histories also need their respective dates and machine contexts.

### 2. A no-robot mode must hold through the whole launch graph

Source: lines 71–121, issues 5–9 (260–346).

Dry mode initially had holes: a base-height callback used a missing robot object,
Dex3 setup ignored dry mode, launch files required a hardware interface before
evaluating arguments, and standalone manipulation could wait indefinitely for
the robot description. Fixes propagated dry-mode parameters and separated
state subscriptions from command publisher creation.

The reported dry Dex3 checks verified that command publishers were absent.
Offline initialization is valuable evidence, but does not validate robot control.

### 3. Working nodes need compatible messages, topics, and semantics

Source: issues 11–14 (362–450), 26 (963–979), 28 (997–1,023),
31 (1,075–1,100), and 38 (1,226–1,238).

The work aligned hand-goal topics, Dex3 action strings, arm enable/home commands,
joint-state array lengths, and RViz goal messages. Autonomous Joy messages had
used a different walk-enable button than the locomotion consumer expected.

Preserve examples showing how individually running components still failed to
connect. These topic names belong to the G1Pilot integration at this revision;
later tabletop interfaces must be documented from their own sources.

### 4. Frame ownership is part of the physical model

Source: issues 15–17 and reference comparisons (452–669).

Live IMU attitude had been published as though the IMU were rotating relative to
the pelvis. The corrected sensor frame came from the URDF. Duplicate fixed
transforms and competing publishers for the pelvis were also identified.

The recorded design gave OpenSoT body-pose TF ownership in offline visualization,
while real-robot body pose belonged to state estimation/localization. The final
issue-17 runtime TF sampling was stopped because of Docker image drift; retain
that limitation alongside its successful build/launch checks.

### 5. A copied model can need integration repairs and still require physical checks

Source: lines 495–745 and issues 19–22 (748–841).

The local LiDAR origin differed from the selected official revision. Adopting
the official inverted mounting convention also required removing a second
inversion in the local Livox compatibility frame. Other model work fixed a
duplicate joint, machine-specific mesh paths, missing helper frames, and launch
selection of Dex3 variants.

The June 21 live check recorded matching numeric TF and a bag with LiDAR and TF
messages. The visual floor/wall check remained listed as outstanding, and MOLA
was configured to ignore the LiDAR pose from TF. Therefore this is not evidence
that the complete navigation/localization stack had been physically validated.

The exact replay path is preserved in the source at line 731. Its availability
has not yet been checked in this documentation workspace.

### 6. Robot mode and physical configuration need separate evidence

Source: lines 869–939.

The recorded robot reported mode 5, while the operator confirmed mechanically
locked waist roll/pitch. The note distinguishes that observed hardware condition
from the vendor mode-to-model mapping. Model joint-name mapping was introduced
so removing fixed joints would not silently shift motor/model indices.

The same section contains proposed model/configuration follow-ups, not proof that
each was completed. Later calibration/control notes must resolve the current
policy. Do not turn this June entry into an instruction to change machine mode.

### 7. An emergency-stop branch has to be reachable and its scope explicit

Source: issue 23 (843–867).

An outer condition excluded emergency-stop states before the intended passive
command branch could run. The fix moved emergency handling ahead of solving.
The log explicitly limits that helper to arm motors 15–28; it does not include
waist, legs, or Dex3 motors. Verification in that entry is syntax/diff checking.

This is an early software finding, not the later commissioned whole-system
safety procedure. The later source notes are needed to explain how robot
ownership, watchdogs, and recovery evolved.

### 8. Initial commands and failed transitions matter as much as normal motion

Source: issue 24 (918–939), issues 29–30 (1,025–1,073).

OpenSoT read live state but originally initialized its model from a nominal
posture. The fix used named live joint mappings; unavailable/offline values
could still use nominal values, which must not be hidden in a broad claim that
every command was fully guarded by measured state.

The balancing path could proceed to Start and mark itself balanced after a
failed or interrupted attempt. A separate startup issue sent an FSM action
before SDK initialization. Both fixes are described with software checks, not
physical commissioning results in these entries.

### 9. A stream of messages can carry an old command

Source: issues 32–34 (1,102–1,155).

The autonomous node could produce commands while disabled. The mux could ignore
recent manual input and replay its last autonomous command indefinitely. Work
addressed all three behaviors, including a default 0.25 s auto-command freshness
limit in the mux.

The log explicitly says this does not replace a lower-level locomotion watchdog.
Retain both the failure mechanism and the layer where the correction applies.

### 10. Planning failure must remain visible to the caller

Source: issues 35–38 (1,157–1,238).

The path planner had converted unknown occupancy to free space and produced a
straight-line fallback even when planning failed. The recorded fix preserved
unknown cells and returned an empty path. The dummy map remained an explicit
offline component instead of a default real-robot map source.

Remaining limitations were stated: frame assumptions, diagonal corner cutting,
and collision checking of the final smoothed path were not resolved by that fix.
Do not describe this as a fully qualified autonomous navigation system.

### 11. Investigating a suspected bug can establish that the code should stay

Source: issue 25 (941–961).

A static review suggested multiplying the OpenSoT output by the control interval.
The upstream check showed that the bounded variable was already a per-step
increment. Applying the proposed extra multiplication would have changed its
meaning. The actual change concerned offline collision visualization.

This is a useful example of the author's point about iterative understanding:
a plausible code edit was rejected after checking the underlying contract.

### 12. The head-camera access failure was traced to a physical USB path

Source: lines 1,285–1,328.

The final postmortem records USB/UVC errors on the old PC2 path. After moving the
D435i to another USB port, an ordinary-user color pipeline received frames at
640 × 480 and 30 FPS. TeleImager's laptop ZMQ client then received JPEGs at about
30 FPS. Browser WebRTC remained black and was recorded as a separate issue.

The note distinguishes camera acquisition, transport, browser playback, and ROS
depth-cloud production. It rejects the earlier missing-package/permission/setup
explanations for that specific physical failure. Preserve that resolved cause;
do not present all initial hypotheses as equally open.

## Evidence and discussion gaps

- This file does not describe the author's initial MuJoCo digital twin. The
  subsequent remote-branch reading locates the implementation. Later iteration
  notes were requested; the author confirmed there are no additional notes and
  that the available material covers the work done. That question is closed.
- The actual stable/unstable PC2 USB ports are not identified by an installation
  photo in this note. A later hardware page would benefit from that evidence.
- The physical Dex3 installation and purchased JST extensions are not documented
  here. Keep this author-supplied work item visible for later discussion.
- Source changes have been reported here, not audited against every current code
  path. Check the implementation and later notes before drafting runnable guides.
- Do not carry the old command examples directly into new operator instructions.
  The current control/safety lifecycle is in later repositories.

## Next reading

Read the prototype history and tabletop notes sequentially, preserving the
relationship between inherited history and new tabletop work. Use the completed
calibration ledger to reconcile later corrections. Discuss the material and
organization with the author before turning these findings into chapters.
