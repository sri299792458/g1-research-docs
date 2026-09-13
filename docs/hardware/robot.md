# The lab robot

The summer work used a G1 with two Dex3 hands, a head-mounted RealSense
D435i, and an Ethernet-connected development computer referred to as PC2.
Manipulation was developed with physical support and a load-bearing harness.
The exact configuration changed during the work; a machine-mode number is
not a substitute for inspecting the robot.

## Configuration that matters

| Item | Recorded fact | Consequence |
|---|---|---|
| Body state | `mode_machine=5`, 29-joint logical layout | Decode the matching HG messages; do not confuse it with an FSM |
| Hands | Seven joints per Dex3, independently commanded | Body and hand arrays have different mappings |
| Head pitch | Manually adjustable, non-motorized and unsensed | Changing it invalidates the complete camera extrinsic |
| Early waist setup | June operator confirmed mechanically locked roll/pitch | Initial MuJoCo model fixes those two joints |
| Later standing work | September bags show measured waist roll/pitch movement | June's mechanical condition cannot be assumed for later runs |
| Seated work | Arms initially supported on table, body on chair | Takeover and lifting change the camera/table relationship |
| Camera | D435i on PC2 USB | Camera ownership and physical USB routing matter |
| IMUs | Pelvis in LowState; separate torso IMU | They measure different rigid bodies |

Do not reconcile these dates by silently selecting one “G1 configuration.”
A new run should record the physical waist hardware, hands, camera angle,
support, and selected model. The pending [hardware review](../reference/review.md)
includes a photograph of the complete current arrangement.

## Dex3 installation and cable routing

The author installed the Dex3 hands and bought JST extension cables as part
of the practical setup. The available notes do not establish the connector
series, pinout, cable length, purchased part number, or installation sequence.

This is a real documentation gap. A generic JST cable description is not enough
to reproduce the connection. The installation section needs the actual cable
and connector photographs, both mating ends, routing and strain relief, and
the steps used when replacing the dummy hands. Those details will be added
from the author's hardware walkthrough.

The [dorsal marker mount](../perception/targets.md) is a separate installation:
it attaches a printed target to the rigid hand shell. Its M3 screws do not
describe how the hand attaches to the robot wrist.

## Joint names are the interface

The body layout places left arm joints at indices 15–21 and right arm joints
at 22–28. Waist yaw/roll/pitch occupy 12–14; arm-SDK blend weight occupies
slot 29 in the 35-slot HG command message. The full message therefore has
more slots than physical body joints.

The pressure study physically observed right-hand motor order as thumb 0/1/2,
middle 0/1, index 0/1. A URDF tree, CuRobo model, or simulation bridge may
list index before middle. Always map by the named model/message convention;
slicing seven unnamed values caused real integration failures.

Likewise, the two palm frames are not interchangeable. The canonical grasp
adapter uses a proper rotation and signed finger mapping. Dorsal marker
placement is on opposite palm-Y sides. Reflecting an image or copying the
right-hand transform does not produce a valid left-hand coordinate frame.

## Physical support is part of the experiment

A rigid seat reduced observed camera movement during arm lifts, but the
cushion/rigid runs were not posture-matched. The result supports the practical
choice of rigid support; it does not isolate a cushion stiffness parameter.

Record the chair, feet, harness, arm support and camera witness mark with a
run. None of these is captured completely by a URDF. A model that agrees with
the vendor model can still disagree with manufactured geometry: the later
[wrist-spacing investigation](../calibration/investigation.md) is the clearest
example.

Evidence: G1Pilot June log and onboard profile; tabletop August 16 and September
standing logs; author-provided Dex3 cable context. [Source identities](../reference/sources.md).

