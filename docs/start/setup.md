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
| Inspect recorded episodes | Dataset viewer, or the separate conversion environment when converting raw bags |
| Develop tabletop planning/execution | Focused control and planner environments below, plus their model/message dependencies |
| Explore the simulator | The independent [MuJoCo setup](../simulation/mujoco.md#set-up-the-pinned-version) |
| Inspect hand pressure | The pressure repository's ROS workspace and [passive launch](../sensing/pressure.md#topic-rate-changes-what-you-can-observe) |

## Choose a tabletop checkout

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

From the focused source repository, the documented setup is:

```bash
git submodule update --init --recursive
./tools/setup_control_env.sh
./tools/setup_planner_env.sh
./tools/install_robot_calibration_local.sh
./tools/setup_recording_benchmark.sh
./tools/g1_tabletop.sh inspect
```

`inspect` loads the selected calibration bundle and checks the local model
revisions against the recorded provenance. Its JSON includes
`commands_robot: false` and the bundle/model identities. A successful result
checks those local artifacts; it does not test state freshness, camera transport
or watchdog recovery on a connected robot.

These commands are transcribed from the inspected source, not a fresh-machine
installation test. The hardware launcher also expects the commissioned PC2 watchdog, SSH
access, camera lifecycle helper, and official `unitree_hg` message support.
The lab's `g1pilot_ws` supplied message definitions without launching G1Pilot.

Check CUDA independently:

```bash
.venv-planner/bin/python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
```

Two recorded UVM failures returned error 999 even though `nvidia-smi` saw the
GPU; reboot restored the existing environment. See
[debugging](../reference/debugging.md) before rebuilding dependencies.

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
