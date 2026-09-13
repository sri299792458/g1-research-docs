# G1Pilot MuJoCo backend: remote development branch

Read on 2026-09-13 after the author supplied
[`sri299792458/g1pilot`, branch `dev`](https://github.com/sri299792458/g1pilot/tree/dev)
as the source for the initial digital twin.

Pinned source: [`6b5af59b109e2ee687920fdf66ded6182725e945`](https://github.com/sri299792458/g1pilot/commit/6b5af59b109e2ee687920fdf66ded6182725e945).
File hashes, exact coverage, and media metadata are in
[`g1pilot-dev-source.json`](g1pilot-dev-source.json).

## Source correction

The local checkout read earlier ends at `72acc80`, dated June 21. The supplied
branch contains two additional commits:

- June 30, `72b820f`: locked-waist manipulation and MuJoCo support.
- July 1, `6b5af59`: the Dex3 MuJoCo backend and its documentation/media links.

The earlier local search was accurate for that checkout but did not cover the
author's remote development branch. The digital twin is now located in G1Pilot.

The July 1 commit removes `running_notes.md` from Git and explicitly ignores
local notes. The last tracked version in `72b820f` has 1,328 lines and is
byte-for-byte identical to the June 21 local log already read. It contains no
additional MuJoCo iteration history. The author subsequently answered that there
are no further notes and only this much work was done. Treat the available
implementation and demos as the initial work's scope; the search for additional
MuJoCo development notes is closed.

## Reading performed

Read completely: the remote README and `.gitignore`; all three substantive
`g1pilot/simulation/` modules; the simulation launch file; `source_g1.sh`;
the baseline diagnostic script; and both model-generation scripts. The exact
file lengths and SHA-256 hashes are recorded in the source snapshot.

Inspected the generated XML's structure with an XML parser: 41 actuators,
89 sensor elements, and no movable waist-roll or waist-pitch joint. This was
static inspection. No simulator, ROS node, policy, generator, or hardware
command was executed. Application-side OpenSoT/Dex3 changes have not yet received
a full code reading in this pass.

## What the implementation establishes

### Backend and ownership

The fork introduces a MuJoCo backend behind G1Pilot's application layer. The
plant owns physics, simulated state, lower-body policy execution, and command
combination. Its DDS bridge stores commands and publishes state; the bridge
does not directly own the MuJoCo model/data.

The implemented command inputs are `rt/arm_sdk` and
`rt/dex3/{left,right}/cmd`. Published state includes `rt/lowstate`, both Dex3
state topics, torso IMU, and wireless-controller messages. The plant applies
position/velocity feedback gains and feedforward torque when stepping physics.

This supplies a concrete account of the author's SDK-based tooling: the
application can use familiar command/state interfaces against a simulated
backend. Full vendor firmware behavior is outside what these files establish.

Source: [plant and DDS bridge](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/g1pilot/simulation/mujoco_plant.py).

### Lower-body policy and joint mapping

OpenHomie provides a 12-action leg policy. Its observation includes 27 active
body joints: 12 legs, waist yaw, and 14 arm joints. Six 76-value observations
form the configured 456-value history. The policy wrapper supports ONNX and
TorchScript and validates the input/output widths.

The plant defaults to standing. It also exposes walking command arguments;
the presence of those arguments is not a recorded walking-validation result.
Default simulated physics step is 0.002 s, with policy updates every ten steps.
These are configured simulation intervals, not a measured wall-clock benchmark.

The physical-model constraint is locked waist roll/pitch. The simulation keeps
the Unitree body motor IDs while omitting those two active joints. The generated
model contains 27 active body actuators plus seven actuators in each Dex3 hand.

Sources: [policy math/loader](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/g1pilot/simulation/openhomie_policy.py),
[motor mapping](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/g1pilot/simulation/lowcmd_utils.py),
and the plant.

### Model provenance and hand selection

The MuJoCo generator selects the GR00T activated-finger revision-1.0 XML as its
default source, removes movable waist roll/pitch, adds scene elements, and
rebuilds actuators and sensors for the plant. Its validation function explicitly
checks hand joints, actuator counts, and inherited finger damping. The source
selection describes intended provenance; this reading did not rerun generation
against an independently pinned upstream checkout.

A separate generator produces the locked-waist Dex3 URDF for visualization.
The simulation launch can select the visual/controller hand path, while the
plant's default physical XML remains the Dex3 model. The launch retains a
separate locked-waist model for the OpenSoT solver.

Sources: [MuJoCo generator](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/scripts/generate_openhomie_g1_29dof_xml.py),
[URDF generator](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/scripts/generate_g1_lock_waist_dx3_urdf.py),
and [launch file](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/launch/mujoco_openhomie_manipulation.launch.py).

### Environment and external artifacts

The environment script exposes real/simulation profiles and defaults simulation
to loopback and domain 1. Existing environment overrides can be retained, so
those defaults alone do not establish isolation after arbitrary profile changes.
The script defaults ROS to FastDDS while Unitree SDK2 Python uses CycloneDDS.

The OpenHomie policy file is external: the code accepts an environment/CLI path
or a conventional sibling reference-repository location. The large reachability
map is a GitHub release asset. A future setup page must explain both dependencies
with the version used, rather than assuming they come with the source checkout.

Source: [environment setup](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/scripts/source_g1.sh)
and the pinned README.

## Existing media and evidence limits

The [July 1 release](https://github.com/sri299792458/g1pilot/releases/tag/mujoco-demo-media-2026-07-01)
was checked through GitHub's release API. It contains:

- [RViz arm-control demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-rviz-arm-demo.mp4)
  — 12,915,563 bytes.
- [Dex3 open/close demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-dex3-open-close-demo.mp4)
  — 1,649,508 bytes.
- `g1_29dof_lock_waist_reachability.npz` — 232,680,472 bytes.

The videos and map have been located, not downloaded or reviewed. Their names
describe the intended demonstrations; they do not independently establish
stability duration, physical fidelity, or task-success rates. The release text
also allows assets to be replaced, so preserve hashes if specific media later
become evidence in the documentation.

The README supplies an eight-second headless example. It does not include that
run's output or a quantitative stability report. The baseline diagnostic script
implements observation comparisons, but no saved results were located in the
tracked tree inspected here. Keep available checks separate from completed tests.

## Details to reconcile before drafting operating instructions

- The diagnostic script's generated-XML comparison still expects 29 actuators,
  95 sensor elements, and 113 sensor values. The current generator expects
  41 actuators, 89 sensor elements, and 107 values. Static XML inspection agrees
  with the latter actuator/sensor-element counts. That comparison path refers
  to a different model shape and should not be copied as a current passing check.
- The simulation bridge latches received commands; its inspected callbacks do
  not track receipt age or implement the later robot watchdog/ownership lifecycle.
  Document its actual supported interface scope when explaining simulation use.
- The simulation's named Dex3 order puts index before middle. The June physical
  pressure-study notes describe middle before index in the observed right-hand
  motor state. Reconcile the specific models/message conventions before writing
  a single general-purpose joint-order table. This observation is not a physical
  remapping test or proof that a particular robot driver is wrong.
- A full examination of the application-side changes, upstream policy/model
  revisions, and demo footage remains pending. The author confirmed there are
  no additional development notes to recover.

These are documentation findings. No change to the source implementation or new
experiment is implied. The documentation organization remains for discussion.
