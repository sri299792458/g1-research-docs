# Repositories and setup

Choose the repository for your task. Installing every summer dependency into
one Python environment recreates the ABI problems the later tools separated.

| Repository | Role |
|---|---|
| `g1pilot` (`dev`) | Initial MuJoCo digital twin and its arm/hand demonstration |
| `aprilcube` fork | Printed fiducials, rounding, detection APIs |
| `g1-aprilcube-demo` | GraspGen-X descriptors, Isaac qualification, assembly |
| `robot-calibration-aprilcube-prototype` | Calibration capture/analysis, Dex3 wrist markers, current V7 torso CAD and R2 fit coupons |
| `g1-dex3-tabletop` | Manipulation, bilateral calibration, recording/conversion |
| `dex3_pressure_tools` | Passive tactile inspection and RViz |
| `spark-data-collection` | Recording and documentation reference |

The [source catalog](../reference/sources.md) supplies public locations and
identifies exact revisions. The August demo and the later September work are
now both committed and public, on separate tabletop branches.

For printed mounts, start with [targets and mounts](../perception/targets.md).
The calibration/fixture repository remains separate from the manipulation
runtime. Opening its F3D, STEP, STL or Bambu exports does not require the ROS,
planner or dataset-conversion environments. Use the pinned V7 links in that
chapter; the consolidated `main` now includes that design and the bundle tools.

## Install only what your task needs

| Task | Environment to prepare |
|---|---|
| Read the guide or download data | Browser; no robot software |
| Print or edit a fixture | Slicer or CAD application and the linked fixture files |
| Inspect recorded episodes | [Local browser viewer](../data/viewing.md); conversion software only when starting from raw bags |
| Develop tabletop planning/execution | Focused control and planner environments below, plus their model/message dependencies |
| Explore the simulator | The independent [MuJoCo setup](../simulation/mujoco.md#set-up-the-pinned-version) |
| Inspect hand pressure | The pressure repository's ROS workspace and [passive launch](../sensing/pressure.md#topic-rate-changes-what-you-can-observe) |

## Choose a tabletop checkout

The tabletop baseline has one known public-dependency gap: its pinned AprilCube
commit is not currently available from the configured GitHub fork. See
[source availability](../reference/sources.md#aprilcube-runtime-pin-availability).
The checkout commands below identify the intended versions, but recursive
submodule setup cannot finish on a fresh machine until that pin is restored or
replaced with a tested version. Downloading the public fixture files or viewing
the datasets does not depend on this runtime setup.

For the August 25 demo baseline:

```bash
git clone --branch main https://github.com/sri299792458/g1-dex3-tabletop.git
cd g1-dex3-tabletop
git switch --detach 7400aff201c2f73ef2a64e546d72bd66cbe87fd6
git submodule update --init --recursive
```

The detached commit matches this guide; use a new branch when making changes.
For September calibration development, make a separate checkout so its changed
runtime and route requirements stay explicit:

```bash
git clone --branch experimental/september-calibration \
  https://github.com/sri299792458/g1-dex3-tabletop.git g1-calibration-dev
cd g1-calibration-dev
git switch --detach 59c21b1388c636176dea67ea7ed3e253f8510783
git submodule update --init --recursive
```

September's final operator-preclosed lifecycle still needs new route certificates
and hardware validation. Publishing its code did not change that status. The
[calibration workflow](../calibration/workflow.md) describes that version.

## Environment boundaries

| Runtime | Recorded environment | Purpose |
|---|---|---|
| Focused control | Python 3.10 / ROS Humble | ROS ABI and Unitree transport |
| Focused planner | Python 3.11 / Torch/Warp/CUDA | GPU work outside control |
| Conversion | Python 3.12 / CPU Torch / LeRobot v0.6.1 | Offline encoding |
| Early prototype | Python 3.12 / ROS Jazzy | Historical calibration work |
| MuJoCo twin | ROS Humble/Jazzy workspace, MuJoCo, SDK and OpenHomie policy | Separate simulation environment; see the [simulation setup](../simulation/mujoco.md#set-up-the-pinned-version) |
| This guide | Python 3.10+ / pinned docs requirements | No ROS or CUDA |

### Tabletop control, planning and recording

Start from the selected tabletop checkout above, with `uv`, ROS Humble and
the planner's CUDA dependencies available. The commissioned control environment
uses Python 3.10. Select Humble explicitly if the machine also has Jazzy;
automatic ROS discovery in the scripts prefers Jazzy.

```bash
G1_TABLETOP_ROS_PREFIX=/opt/ros/humble ./tools/setup_control_env.sh
./tools/setup_planner_env.sh
ROS_DISTRO=humble ./tools/setup_recording_benchmark.sh
./tools/g1_tabletop.sh inspect
```

| Setup script | Result | When needed |
|---|---|---|
| `setup_control_env.sh` | `.venv`, Python 3.10, Unitree bindings and a local CycloneDDS prefix | Tabletop control and inspection |
| `setup_planner_env.sh` | `.venv-planner`, Python 3.11 and GPU planning dependencies | Planning; kept outside the control interpreter |
| `setup_recording_benchmark.sh` | MCAP storage plugin under `deps/rosbag2_mcap_prefix/` | Raw episode recording; despite its name, this script installs the plugin rather than running the benchmark |

The recording installer downloads and extracts ROS packages into the checkout;
it does not install them system-wide. These environments do not start the camera
or establish robot ownership.

`inspect` loads the selected calibration bundle and checks the local model
revisions against the recorded provenance. Its JSON includes
`commands_robot: false` and the bundle/model identities. A successful result
checks those local artifacts; it does not test state freshness, camera transport
or watchdog recovery on a connected robot.

These commands are source-checked, not a fresh-machine installation test.
The hardware launcher additionally needs the message workspace, camera access
and PC2 runtime described below.

Check CUDA independently:

```bash
.venv-planner/bin/python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
```

Two recorded UVM failures returned error 999 even though `nvidia-smi` saw the
GPU; reboot restored the existing environment. See
[debugging](../reference/debugging.md) before rebuilding dependencies.

### Optional solver and conversion environments

`./tools/install_robot_calibration_local.sh` builds the native calibration solver.
Prepare it when fitting a calibration; consuming the saved August bundle does
not require a new fit. [Calibration](../calibration/workflow.md) distinguishes
offline solving from collection and deployment.

Raw-to-LeRobot conversion uses a separate Python 3.12 environment and local
SPARK/LeRobot checkouts. Follow [conversion and retention](../data/recording.md#conversion-and-retention)
only when converting raw recordings. Downloaded LeRobot episodes need a viewer,
not the control, planner or calibration solver environments.

## Connect the software to the lab setup

The [hardware wrapper](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tools/g1_tabletop_hardware.sh)
sets up ROS, DDS, message definitions and recording before invoking the task.
The shorter `g1_tabletop.sh` command does not perform that network setup.

| Setting | Commissioned default or requirement | What to check on another machine |
|---|---|---|
| `G1_TABLETOP_ROS_PREFIX` | `/opt/ros/humble` for the Python 3.10 control environment | Interpreter and ROS Python ABI must agree |
| `G1_TABLETOP_UNITREE_ROS_SETUP` | `../g1pilot_ws/install/setup.bash` | Source the workspace containing the official `unitree_hg` definitions; launching G1Pilot is unnecessary |
| `--network-interface` | Required real laptop interface | Identify the connected adapter with `ip -brief address`; do not copy the lab interface name |
| `--domain-id` | `0` | Match all participants; the commissioned camera helper separately hardcodes domain 0 |
| `RMW_IMPLEMENTATION`, `CYCLONEDDS_URI` | CycloneDDS; wrapper builds an interface configuration if unset | Existing values are respected, so a stale shell can retain the wrong middleware or interface |

After sourcing the matching ROS and message workspaces in a terminal,
`ros2 interface show unitree_hg/msg/LowState` checks message availability.
Seeing a topic in `ros2 topic list` does not establish that its messages can be
decoded or are fresh. Unitree `rt/lowstate` appears as ROS `/lowstate`, without
an extra `/rt` prefix. Continue with the [camera checks](../hardware/camera.md)
and [operating checklist](../control/runbook.md) for the connected system.

### Prepare PC2 recovery separately from arming it

PC2 needs its own watchdog Python runtime. The fixture repository's
[runtime installer](https://github.com/sri299792458/robot-calibration-aprilcube-prototype/blob/f295def18bd936031fba325d4e8bdfc71fea671a/tools/install_pc2_watchdog_runtime.sh)
provisions a versioned environment and selects it through
`/home/unitree/.local/share/g1-aprilcube-watchdog/current/venv/bin/python`.
It expects commissioned SSH access, a clean pinned Unitree SDK checkout,
CycloneDDS build artifacts, and PC2's Python 3.8/build prerequisites. Read its
preflight checks before using it; cloning the tabletop submodules alone does
not supply all these dependencies.

Provisioning checks imports and dependencies. It does **not** arm recovery or
start a permanent watchdog service. During a hardware session the laptop
launches the remote agent, waits for readiness and arms the lease at the
defined ownership boundary. [Ownership and safety](../control/ownership.md)
explains those states and the required recovery acknowledgements.

## Simulation setup

The [MuJoCo chapter](../simulation/mujoco.md#set-up-the-pinned-version) contains
the pinned simulator checkout, dependency scripts, pretrained policy download,
and separate plant/application launch commands. Set it up when working on the
twin; the tabletop workflow does not require launching G1Pilot.

## Adapting to another machine

Record the actual Ethernet interface, ROS/interpreter, DDS domain, camera
serial/profile, robot model, and installed hands. Materialize Git LFS meshes
before trusting a render. Review scripts' local path assumptions instead of
copying a lab username. The [runbook](../control/runbook.md) distinguishes
offline commands, subscribers, and motion owners.

Evidence: tabletop README and setup scripts; G1Pilot lab setup notes; recording
documentation. Revisions and remaining portability gaps are in the
[source catalog](../reference/sources.md).
