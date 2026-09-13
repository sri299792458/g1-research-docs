# Repositories and setup

Choose the repository for your task. Installing every summer dependency into
one Python environment recreates the ABI problems the later tools separated.

| Repository | Role |
|---|---|
| `g1pilot` | ROS/OpenSoT integration, navigation work, MuJoCo backend |
| `aprilcube` fork | Printed fiducials, rounding, detection APIs |
| `g1-aprilcube-demo` | GraspGen-X descriptors, Isaac qualification, assembly |
| `robot-calibration-aprilcube-prototype` | Early calibration, fixtures, commissioning |
| `g1-dex3-tabletop` | Manipulation, bilateral calibration, recording/conversion |
| `dex3_pressure_tools` | Passive tactile inspection and RViz |
| `spark-data-collection` | Recording and documentation reference |

The [source catalog](../reference/sources.md) supplies public locations and
identifies local-only material. The tabletop checkout includes uncommitted
September work; Git HEAD alone does not reproduce that version.

## Environment boundaries

| Runtime | Recorded environment | Purpose |
|---|---|---|
| Focused control | Python 3.10 / ROS Humble | ROS ABI and Unitree transport |
| Focused planner | Python 3.11 / Torch/Warp/CUDA | GPU work outside control |
| Conversion | Python 3.12 / CPU Torch / LeRobot v0.6.1 | Offline encoding |
| Early prototype | Python 3.12 / ROS Jazzy | Historical calibration work |
| G1Pilot | Docker/Jazzy and native Humble paths | Match checkout and machine |
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

This is transcribed from the inspected source, not a fresh-machine installation
test. The hardware launcher also expects the commissioned PC2 watchdog, SSH
access, camera lifecycle helper, and official `unitree_hg` message support.
The lab's `g1pilot_ws` supplied message definitions without launching G1Pilot.

Check CUDA independently:

```bash
.venv-planner/bin/python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
```

Two recorded UVM failures returned error 999 even though `nvidia-smi` saw the
GPU; reboot restored the existing environment. See
[debugging](../reference/debugging.md) before rebuilding dependencies.

## Native G1Pilot setup

After an administrator has installed system prerequisites, the per-user path is:

```bash
scripts/setup_humble_user_workspace.sh
source ~/g1pilot_ws/env_humble.sh
scripts/build_humble_workspace.sh --packages-up-to g1pilot
```

Keep NumPy/OpenCV/Pinocchio constraints with that revision. Running colcon with
the wrong interpreter previously generated entry points that could not import
the SDK in the intended environment.

## Adapting to another machine

Record the actual Ethernet interface, ROS/interpreter, DDS domain, camera
serial/profile, robot model, and installed hands. Materialize Git LFS meshes
before trusting a render. Review scripts' local path assumptions instead of
copying a lab username. The [runbook](../control/runbook.md) distinguishes
offline commands, subscribers, and motion owners.

Evidence: tabletop README and setup scripts; G1Pilot lab setup notes; recording
documentation. Revisions and remaining portability gaps are in the
[source catalog](../reference/sources.md).
