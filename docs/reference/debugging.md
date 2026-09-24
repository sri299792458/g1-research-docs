# Debugging from evidence

Start with the first violated contract in the retained timeline. A late elbow
error, black camera window or planner failure message may be downstream of a
different event. The table below records failures that already changed the
implementation.

| Symptom | Evidence that changed the diagnosis | Retained lesson |
|---|---|---|
| Elbow moves during acquisition | Three DDS constructors consumed about 0.6 s after arming a 0.5 s watchdog | Initialize inert endpoints before arming the lease |
| Standing body tilts during arm control | Waist slots were zero; support torque disappeared and modeled return overlap reached about −8.72 mm | Seed and hold measured waist slots; later successful captures do not isolate this fix causally |
| Command boundary rejected | Measured arm differed from active command by about 0.0203 rad | Geometry uses measured state; trajectory joins use the exact current command |
| Finger ramp keeps returning to old posture | Heartbeat republishes its previous hold | Reuse the command-finger helper during the ramp |
| Control stalls while saving request | 12.3 MB JSON hashing/serialization holds the interpreter for 76–90 ms | Construct/hash in a worker; exchange small references |
| Callback stream appears to die on cleanup | Independent bag sees healthy LowState while local teardown pauses about 209 ms | Resolve control ownership before destroying ROS/resources |
| GPU visible but Torch cannot initialize | CUDA error 999 and `/dev/nvidia-uvm` I/O failure | In recorded incidents, reboot restored the existing environment; package reinstall was not supported by the evidence |
| Camera access fails | Factory camera owner and physical USB path differ from assumed setup | Check ownership, port and profile; browser playback is a separate path |
| Reachable grasp marked unreachable | Goal-set starvation, mutated input state or missing IK branch | Give candidates independent seeds and fresh state objects |
| Correct arm endpoint, failed close | Cube moved significantly during simulated closing | Simulated achieved fingers are not the fixed hardware close command |
| Resting cube looks tilted | Largest-face planar ambiguity survives a small residual | Evaluate all positive-depth hypotheses and resting-pose consensus |
| Calibration anchors appear to drift | Independent planar PnP estimates amplify corner uncertainty | Do not interpret inferred span directly as physical camera travel |
| MPC windows are valid but never finish | Clearance shift exceeds endpoint tolerance under tracking offset | Valid-window count does not establish task feasibility |

For acquisition, timing or cleanup failures, use the [control lifecycle](../control/ownership.md).
For command-boundary or reachability failures, use [planning](../manipulation/planning.md).
For missing signals, check the [recording contract](../data/recording.md#record-the-full-lifecycle)
before interpreting an empty plot. [Camera ownership](../hardware/camera.md#one-camera-owner),
[pose acceptance](../perception/object-pose.md) and [calibration results](../calibration/results.md)
cover the corresponding sensing symptoms.

## A practical reading sequence

1. Identify the run, exact source/model hashes, hardware support and task mode.
2. Read outcome and cleanup status separately. Find the first rejected check.
3. Align task events with raw measured state, commands and image evidence.
4. Determine whether the relevant stream was actually recorded. A missing
   failed-view image cannot be recreated from a successful capture thumbnail.
5. Compare with the latest correction, not just the README at an earlier date.

## Worked example: a cleanup stall

A local callback stream appeared to stop while the task was shutting down.
Treating that symptom as a robot-side LowState failure would have targeted the
wrong component. The independent recording still contained healthy LowState
messages while the local teardown paused for about 209 ms.

| Evidence | What it distinguishes |
|---|---|
| Task status and cleanup errors | The original failure from additional shutdown failures |
| Independent `/lowstate` recording | A robot/network publication gap from a stalled subscriber in the control process |
| Local timing around resource destruction | Whether control resources were torn down while ownership was still active |
| PC2 terminal-state acknowledgement | Recovery completion from an attempted service call |

The resulting rule is to resolve ownership before destroying dependent ROS and
transport resources. The bag supports the diagnosis because it observes the
stream independently; another log line from the stalled process would not
provide the same evidence.

Apply this method to a new run by first checking
`raw_episode/episode_manifest.json`: was `/lowstate` actually recorded, and is
the capture complete? Then compare the relevant receipt-time intervals with
the task/cleanup timeline. Keep sensor header time distinct from bag receipt
and local monotonic time; align clocks explicitly before comparing gaps.
The [runbook's artifact table](../control/runbook.md#inspect-the-outcome)
identifies the fields, and [recording](../data/recording.md#time-and-completeness)
explains the clock limits.

For calibration, start with the [investigation summary](../calibration/investigation.md)
and consult the private detailed ledger when available.
For general operation, use the [ownership chapter](../control/ownership.md)
and [runbook](../control/runbook.md). Changing a guard to get past a symptom
needs evidence that the guard is wrong, not merely that it rejected a run.

Evidence: dated source failures and corrections summarized throughout this
guide. [Source identities](sources.md).
