# Cube stacking: an integration example

Cube stacking exercised the reusable G1 tools together: calibrated perception,
qualified grasp candidates, CuRobo planning, continuous control, contact checks,
recovery and recording. The task is useful here as evidence of that integration.
A new research project need not reproduce cube pickup to use the control or
recording infrastructure.

## Physical demonstration

<figure class="research-video">
  <video controls playsinline preload="none" poster="../_static/g1-physical-cube-stacking.jpg" width="1920" height="1080" aria-label="Physical G1 cube pickup, stacking and hand withdrawal" aria-describedby="physical-stack-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-physical-cube-stacking.mp4" type="video/mp4">
    Your browser cannot play this video. Use the download link below.
  </video>
  <figcaption id="physical-stack-caption">The physical G1 picks up a marker cube, places it on another, opens its hand and withdraws. The stack remains standing in the final frames as the hand returns toward table support. Harness and wrist targets are visible. Silent, 91 seconds.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-physical-cube-stacking.mp4">Download the physical stacking video (MP4)</a></p>
</figure>

This clip provides visible evidence of pickup, placement and release in one
trial. It does not display the controller's ownership state or recording
completion. The matching bag/run ID has not yet been attached to the footage,
so it is not used to infer a success rate or a verified software handback.

## What another project can reuse

| Component exercised by the demo | Transferable behavior | Read the implementation chapter |
|---|---|---|
| Control ownership | Acquire from measured state, keep holding during slow work, verify handback | [Ownership and safety](../control/ownership.md) |
| Recording | Preserve signals through success or fault cleanup; keep outcome distinct from completeness | [Recording and LeRobot](../data/recording.md) |
| Perception and camera state | Match target/profile and refresh observations after support loads change | [Object pose](../perception/object-pose.md), [camera state](../perception/state-estimation.md) |
| Grasp qualification | Separate candidate proposals, supported access and achieved physical contact | [Grasp qualification](grasp-atlas.md), [contact checks](planning.md#interpreting-contact-before-using-a-payload-route) |
| Planning | Join the current command continuously and include checked recovery routes | [CuRobo integration](planning.md) |

## August 25 demo baseline

Five retained August 25 runs span 15:06–15:17 Minnesota time and record source
commit `d1b0103`. The
published [`main`](https://github.com/sri299792458/g1-dex3-tabletop/tree/7400aff201c2f73ef2a64e546d72bd66cbe87fd6)
preserves that commit's runtime code, tests, configuration and dependency pins.
The run metadata also flags a dirty worktree without identifying a runtime-code
change, so the recorded commit is a baseline rather than proof of every file’s
bytes during execution.

All five run records report completed episodes, supported returns and complete
recording, with control retained between episodes. Those statuses do not supply
an independently scored five-of-five success rate. The [LeRobot export](../data/recording.md#august-25-demonstration-export)
contains these five runs; it is separate from the older dataset shown in the
viewer walkthrough.

September changes remain on their own experimental branch. The coordinator linked here is demo `main`; other chapters label the later
implementation they discuss.

## Direct two-cube transfer

The demonstration uses two 60 mm cubes with distinct marker ID ranges, 10–15
and 20–25. At clearance, the coordinator considers both source/destination
assignments and both arms, then selects one complete pick/place route. Only
one task arm moves at a time. A candidate must work at the grasp endpoint,
placement endpoint and along the connecting transfer.

Intersecting endpoint-feasible pools rejected one 0/57 case in roughly 12 s,
compared with an earlier eight-minute nested route search. This illustrates a
useful planning decision: reject incompatible endpoints before spending time
on full transfers. It is a measurement for that candidate set, not a general
planner speed claim.

The stack route is planned completely at clearance. A separate single-cube
experiment introduced a pregrasp camera-state correction; that behavior is
explained in the [state-estimation chapter](../perception/state-estimation.md#where-this-entered-manipulation)
and is not part of the demonstrated direct-stack route.

## Failures that shaped the reusable tools

| Observation | Change carried into the implementation |
|---|---|
| The arm reached the intended pose but the physical close failed | Use a fixed closing command and measured empty-close references; simulated achieved fingers can encode object motion |
| A lift/replacement occurred but the run failed afterward | Validate the complete return sequence, including `return_to_pregrasp` |
| A grasp attempt was rejected | Permit a bounded retry only after the frozen recovery, a fresh scene and exclusion of the failed candidate |
| An episode completed while the process retained control | Record episode completion and final ownership handback as different events |

The recorded arm default reached 0.2 rad/s after physical commissioning. That
setting and the cube-specific contact/clearance thresholds describe this
configuration; they are not a ready-made operating envelope for another task.

## Plan visualization and recorded outcomes

<figure class="research-video">
  <video controls playsinline preload="none" poster="../_static/curobo-stack-plan-demo.jpg" width="1280" height="720" aria-label="Rendered CuRobo cube-stacking plan" aria-describedby="stack-plan-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/curobo-stack-plan-demo.mp4" type="video/mp4">
    Your browser cannot play this video. Use the download link below.
  </video>
  <figcaption id="stack-plan-caption">Rendered stacking sequence through approach, grasp, lift, transfer and placement. The animation ends at the displayed stack completion; the complete return and ownership handback are outside this clip. Silent, 10 seconds.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/curobo-stack-plan-demo.mp4">Download the stacking-plan visualization (MP4)</a></p>
</figure>

Use this visualization to understand the geometric phases. Measured contact,
physical placement and normal control release require the recorded hardware
evidence described on this page; a rendered plan does not establish those outcomes.

Retained sessions keep control/resources between episodes. SPACE starts a new
episode; Ctrl+C between episodes requests clean handback, while interruption
inside an episode follows its fault/recovery handling. See [recording](../data/recording.md)
for preserving those boundaries.

## Follow the code

Start with [`hardware_stack.py::run_stack`](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/src/g1_dex3_tabletop/hardware_stack.py).
Follow `_find_direct_stack_plan` for candidate/route selection and
`_execute_pick_place` for execution. The component chapters above explain the
interfaces those functions rely on; use the [code index](../reference/code-index.md)
for their pinned symbols.

## Checks and evidence to inspect

[test_tabletop_workflow.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tests/test_tabletop_workflow.py) and [test_stack_workflow.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tests/test_stack_workflow.py) (demo main) encode boundary, return and retry regressions. Inspect recorded close/retention evidence and cleanup outcome separately from task completion. The August runs above are the physical record; source tests alone cannot establish grasp success.
