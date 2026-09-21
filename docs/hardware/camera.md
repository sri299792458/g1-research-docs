# Camera and network

The camera must be a dependable measurement source before it can support
calibration or planning. USB acquisition, service ownership, DDS discovery,
image freshness, and geometric calibration are separate checks.

## Recorded topology

The onboard audit found Ubuntu 20.04 ARM64/Tegra with ROS Foxy and CycloneDDS;
the later research laptop used Ubuntu 22.04/Humble. PC2's recorded Ethernet
address was `192.168.123.164` on `eth0`. The laptop interface varied with
the adapter; `enp134s0` is a lab example, not a required interface name.

The audit also found an incorrect robot clock in 1970. An archive filename
from that audit is not wall-clock evidence. Later analysis keeps sensor header
time and bag receipt time separately; merely enabling NTP does not prove
synchronization.

Unitree DDS channels such as `rt/lowstate` appear on the ROS graph as
`/lowstate`. Recording `/rt/lowstate` produced an RGB-only bag with empty
robot topics. Topic discovery also does not imply that the current Python
environment can deserialize `unitree_hg`; source the matching message workspace.

## One camera owner

The factory `video_hub_pc4` process can own the RGB device while no standard
ROS camera topics exist. TeleImager and the ROS RealSense driver are alternative
consumers of the same hardware.

The focused repository's `tools/g1_realsense_pc2.sh` carries the commissioned
camera lifecycle: lock the ownership change, release the factory video service,
start and verify the intended driver, and restore the service on stop or a
failed start. Camera-dependent hardware launchers use it. A tracked driver
process that is alive but produces no frames is not a healthy camera; a clean
stop/start recovered one such case.

Use the repository's ownership helper rather than starting several camera
applications. Its actions change PC2 services even though they do not command
robot joints.

## Profiles used at different stages

| Stage | Profile and evidence |
|---|---|
| June direct USB/TeleImager | 640 × 480 color at 30 FPS; laptop ZMQ client received about 30 FPS |
| Focused calibration/manipulation | RGB8 1280 × 720 at 15 FPS, matching frozen CameraInfo |
| Native depth recording | Unaligned Z16 640 × 480 at 15 FPS |
| Motion streams | Separate raw gyro and accelerometer; no synthesized orientation |
| Offline alignment | Depth/color intrinsics and factory static transforms retained |

A black WebRTC preview in June remained a separate playback issue after the
Python/ZMQ path worked. It did not invalidate the successful camera acquisition.
The original USB/UVC failure was resolved by moving the cable to another PC2
port. The author supplied `PXL_20260803_142502363.jpg` to illustrate this
troubleshooting step: try another port if the camera negotiates USB 2, then
verify the negotiated speed. The photograph does not establish a universally
correct socket.

```{figure} ../assets/images/realsense-pc2-usb-ports.jpg
:alt: Close-up of the G1 PC2 connection panel with the RealSense USB cable connected and adjacent ports visible.
:width: 340px

RealSense USB connection at PC2, photographed August 3. If the negotiated link
is USB 2, try another port and verify the driver-reported speed. The photo
illustrates the connection area; use the runtime check to establish USB 3.
```

The [camera lifecycle helper](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tools/g1_realsense_pc2.sh#L317) requires the fresh driver log to
contain `Device USB type: 3.2`, alongside the serial and stream-profile checks.
The [standard hardware wrapper](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tools/g1_tabletop_hardware.sh) stops and starts
the camera before tabletop, stacking, bilateral-calibration and seat-compliance
commands, so a failed startup check prevents that wrapper from launching the
task. This checks the commissioned driver's exact **3.2** log string, rather
than parsing all possible USB 3 versions. Directly reusing an already-running
node takes a different branch and does not repeat the USB check.

The port photograph remains useful for resolving startup failure even though
the standard launch path enforces the connection requirement. This is a static
code finding, not a new hardware test; the script hashes are retained with the
[September media review](../reference/media.md#author-supplied-september-media).

## Calibration stream semantics

The optimizer assumes rectified color coordinates and uses the projection
matrix `P[:3, :3]`. It does not silently combine raw distorted pixels with a
rectified model. Topic names alone are insufficient: inspect the actual
CameraInfo, profile, dimensions, distortion contract, and frozen hashes.

The D435i's factory depth-to-color transform is internal sensor calibration.
The robot-to-color transform is a different quantity. The manually adjustable
head makes a nominal URDF camera transform an initialization, not a measured
extrinsic. Mark and preserve the head angle within a dataset; after adjustment,
obtain a new camera registration.

## Freshness and pairing

Keep the sensor header timestamp, local monotonic receipt time, complete
measured-state window, and selected frame. Calibration captures are stationary,
with state samples bracketing each image. One early buffered-image incident
showed why receipt proximity alone cannot prove exposure freshness.

For moving or continuous analysis, map producer clocks explicitly. The seat
study found substantial offsets and different RGB/depth phases. Treating all
header stamps as one synchronized clock can manufacture motion.

Evidence: G1Pilot June camera postmortem/onboard audit; tabletop August 13–16
camera and recording entries; [recording contract](../data/recording.md).
