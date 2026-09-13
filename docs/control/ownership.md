# Ownership and safety

Robot control has two independent questions: which process is allowed to send
commands, and which controller is actually responsible for the body. The
summer's safety work made both explicit.

## Three state concepts

| Concept | Meaning on the recorded robot |
|---|---|
| Motion service `ai` | Normal Unitree high-level controller is available |
| No active motion service | Direct debug lowcmd ownership is available |
| Locomotion FSM | 0 zero torque; 1 Damp; 3 seated; 4 Ready |
| LowState `mode_machine=5` | Machine/message layout, not locomotion state |

Restoring `ai` does not select seated or Damp. A service response and an FSM
read-back establish different facts. While `ai` is released, the wireless
remote may have no high-level controller to receive its state requests.

## Standing and seated control

| | Standing calibration | Seated manipulation |
|---|---|---|
| Entry | Ready, FSM 4 | Seated, FSM 3, arms supported |
| Command channel | `rt/arm_sdk` | `rt/lowcmd` |
| Ownership | Firmware blend via slot 29 | Release motion service, own complete body |
| Body handling | Measured waist hold and arm commands | Complete measured 29-joint position hold |
| Normal end | Certified return, arm weight zero | Supported return, restore AI, verify 0 → 1 → 3 |
| Fault fallback | PC2 requests verified Damp | PC2 restores AI and verifies zero torque |

These paths cannot be substituted for each other. A successful seated takeover
does not test standing firmware blend behavior. The initial MuJoCo backend
does not implement either complete lifecycle.

## Startup order is a safety property

The standing watchdog regression is especially instructive. Three SDK publisher
initializations each slept about 0.2 seconds. Starting the 0.5-second PC2
heartbeat lease first guaranteed a long enough gap for recovery to begin.

The retained bag showed hand timeout packets before acquisition, then a leg
torque collapse, then elbow movement. The visible elbow error was downstream
of safety recovery. Raising the acquisition allowance would have hidden the
wrong symptom.

The corrected sequence constructs inert DDS endpoints first, then arms PC2,
then sends the first commands after fresh-state checks. For seated takeover,
a separate keepalive covers the blocking motion-service release through the
first complete lowcmd write. A watchdog armed too early or with a gap in its
coverage is not independent protection.

## Command continuity and measured state

Acquisition seeds commands from fresh measured joints. Later planning boundaries
have two simultaneous truths:

- measured body/finger state defines the current collision scene;
- the exact command already being published defines the next command boundary.

Substituting the measured arm vector for the active command at an arm switch
caused a 0.020277314 rad discontinuity. The executor rejected it. Shared
command-bound snapshot and plan-installation helpers preserve both held arm
commands while retaining measured body geometry.

The exact trajectory join is intentionally much tighter than physical tracking
error. Float32 roundoff is repaired only after proving it is numerical and
anchoring sample zero to the serialized command. A real displacement is never
made acceptable by widening that numerical threshold.

## Timing, gravity and process boundaries

The recorded controller runs at 250 Hz. Motion increments use the fixed 4 ms
period, preventing a late tick from issuing a larger catch-up step. The focused
configuration uses 100 ms state freshness, a 250 ms local control-gap fault,
and a separate 500 ms PC2 heartbeat timeout. These are implementation settings,
not formal guarantees for general-purpose Linux.

Arm gravity feedforward follows the pinned Unitree XR Pinocchio/RNEA approach.
It reduced drift in a physical zero-motion seated test to 0.008317 rad.
It does not make measured joints equal command targets or identify exact
hardware masses and friction.

Heavy planning runs in a separate process. So do PNG/session commits and raw
MCAP writing. A Python thread did not isolate control from a 12.3 MB JSON
serialization/hashing operation: measured interpreter stalls reached roughly
76–90 ms. The worker now constructs and hashes the full calibration request;
the control process sends a small snapshot and file/hash references.

## Finish control before tearing down resources

Camera/ROS and planner shutdown once happened before seated handback. The
control thread and local callbacks paused for about 209 ms while the independent
bag still saw healthy LowState traffic. Cleanup now resolves robot ownership
first, then destroys those resources, then finalizes recording.

Evidence: prototype control/recovery report; tabletop August 14–15 and September
4–5 logs. See [runbook](runbook.md) and [debugging](../reference/debugging.md).

