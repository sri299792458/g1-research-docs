# Operating and recovering

This chapter explains the operator boundaries of the existing tools. It is
not a substitute for knowing the installed robot configuration and the
specific source revision. The latest calibration finger lifecycle has only
offline validation; its old route files are intentionally rejected.

## Before motion

1. Identify the source version, hardware profile, camera profile and selected
   calibration bundle. Record local changes, not just Git HEAD.
2. Confirm the load-bearing harness, physical arm support, clear sweep,
   camera witness mark, and installed hand/marker geometry.
3. Start with inspection. Verify fresh measured body and both hand states,
   the correct FSM, camera frames and CameraInfo, and no competing command owner.
4. Verify the PC2 watchdog installation and normal recovery path for the chosen
   standing or seated mode. A healthy Ethernet ping alone does not establish this.
5. Check storage and the recording subscription contract. Planner warmup during
   preview is command-free; it does not approve a task from stale preflight data.
6. Read the preview and exact acknowledgement. SPACE gates command creation.
   If a prerequisite fails, preserve the retained request and reason.

The source's typed acknowledgement is deliberately explicit:

```text
I CONFIRM THE G1 IS SECURED BY THE LOAD-BEARING HARNESS AND THE WORKSPACE IS CLEAR
```

The task lifecycle and configuration are described in
[pickup and stacking](../manipulation/tasks.md) and
[calibration](../calibration/workflow.md). Use the matching source revision's
launcher and argument documentation; none was executed while writing this guide.

## What a normal seated run does

It acquires the complete measured body, holds the unused arm and fingers,
freezes a supported escape and its exact reverse, and moves to clearance.
It observes the scene again after the load changes. Only then does it select
and install task motion.

A healthy task rejection uses the appropriate frozen reverse: at clearance,
reverse the escape; after a failed low retention lift, lower while closed,
open at support, retreat and return. The hand's arbitrary initial posture is
restored before supported return.

At normal final handback, PC2 restores AI and verifies FSM 0 → Damp 1 →
Seated 3 before the lowcmd publisher closes. Fault recovery stops at verified
zero torque instead of automatically continuing that normal seating sequence.

## Keys have context

| Context | Requested action |
|---|---|
| Bilateral calibration preview, Q | Latch a graceful finish at the next identical anchor, then checked return |
| Bilateral calibration, Ctrl+C | Damp recovery |
| Stack waiting between retained-control episodes, Ctrl+C | Clean seated handback and exit |
| Stack during observation, planning or motion, Ctrl+C | Fault cleanup to zero torque |
| Hardware preview, SPACE | Continue only after immutable inputs and readiness checks |

A frozen preview window is not itself proof of a robot failure. One calibration
Q run completed its return while HighGUI events stopped being serviced. The UI
fix closes the preview and reports the remaining return in the terminal.

## If the remote appears unresponsive

Do not assume the radio or network failed. Direct lowcmd deliberately releases
the service that normally consumes remote requests. Inspect retained cleanup
status to determine whether AI restoration and terminal FSM were verified.

The prototype's `docs/g1_control_state_and_recovery.md` contains the
operator-only raw-SDK recovery procedure and its commissioning history.
Use that exact source with a trained operator and physical support; this guide
does not shorten it into an unqualified “restart AI” command. Restoring a
service can re-enable torque. A successful service call is not an FSM check,
and repeated calls after verified restoration are not useful.

## Inspect the outcome

Read `status.json`, the planner log, contact/retention evidence, and
`raw_episode/episode_manifest.json` together. Distinguish:

- task completed or rejected;
- control returned normally or required fault recovery;
- recording complete or incomplete;
- physical placement independently observed or unscored.

For retained-control stack sessions, one episode ending does not mean ownership
has been handed back; the process remains in its supported wait for the next
SPACE. Each episode still gets a separate run directory and bag.

Evidence: [source catalog](../reference/sources.md), prototype recovery report,
current tabletop README and dated lifecycle corrections.
