# Camera and arm calibration

The calibration connects head-camera measurements to the arm model used for
manipulation. It compensates for disagreement between nominal FK and observed
wrist targets, but it does not establish a uniquely correct mechanical model.

## Start with the demonstrated bundle

The August stacking system uses
[`dex3_shared_20260812_selected_free.json`](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/config/calibrations/dex3_shared_20260812_selected_free.json)
from demo `main`. It contains the selected shared-camera, bilateral-target and
seven-offset fit. Keep the matching robot model, fitted parameters, target
registrations and camera configuration together. The [results page](results.md#the-august-12-stacking-baseline)
connects that bundle to its data and physical use.

Check the [head-pitch witness mark](../hardware/camera.md) before reusing it.
Changing the head pose or remounting a wrist marker changes the geometry;
a saved bundle is not automatically valid for a newly assembled robot.

## Choose the relevant workflow

| Your task | Use | Status |
|---|---|---|
| Understand/reproduce the stacking baseline | August bundle and demo `main` | Used by the documented physical manipulation runs |
| Reanalyse retained measurements | Session artifacts, a declared model and grouped validation | Offline analysis; retain candidate outputs separately |
| Develop the later automated collector | [September branch](https://github.com/sri299792458/g1-dex3-tabletop/tree/59c21b1388c636176dea67ea7ed3e253f8510783) and collection contracts below | Latest preclosed-hand lifecycle needs regenerated routes and physical validation |

No September candidate replaced the deployed August bundle. Before proposing
new experiments, read the [results](results.md) and [completed investigations](investigation.md).
The collection code described below is the September implementation, not the
procedure that originally produced the August bundle.

## The model being fitted

Let `X = base_T_camera`, `F(q) = base_T_palm(q)` and
`Y = palm_T_marker`. The predicted target in camera coordinates is

```text
camera_T_marker = inverse(X) · F(q_measured + offsets) · Y
pixel prediction = project(camera_T_marker · marker_corner, camera model)
```

Each hand has its own target transform. A bilateral session shares one camera
transform and uses the matching arm's measured joints. Selected joint offsets
are effective model corrections unless independently identified as encoder
zeros. A low residual does not uniquely assign error to camera, mounting,
joint offset or link geometry.

Moving the head changes the full six-dimensional camera extrinsic. Moving or
remounting a target changes its registration. The September 5 and 7 camera
positions were deliberately different, so their fits need separate run
registrations. Constant within one run does not imply constant across runs.

## Capture a measurement, not just a pose estimate

<figure class="research-video video-portrait">
  <video controls playsinline preload="none" poster="../_static/g1-standing-calibration.jpg" width="720" height="1280" aria-label="Standing G1 calibration motions with wrist markers" aria-describedby="calibration-demo-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-standing-calibration.mp4" type="video/mp4">
    Your browser cannot play this video. Use the download link below.
  </video>
  <figcaption id="calibration-demo-caption">Physical calibration footage: the standing G1 moves its arms through different configurations, with printed wrist markers and the overhead harness visible. The recording ends during the pose sequence. Silent, 2 minutes 9 seconds.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-standing-calibration.mp4">Download the standing-calibration video (MP4)</a></p>
</figure>

The supplied file is dated September 7 in its capture metadata. It illustrates
the physical arrangement and arm motion; it does not display the head-camera
images, accepted-capture counts, fitted residuals or final cleanup. Its exact
session ID still needs linking. It also does not validate the later manually
preclosed-hand procedure described below.

The capture system stores lossless seven-frame image bursts, decoded corners,
camera profile, measured-state brackets and robust state summaries. A medoid
is an actual retained frame rather than an invented average image. Hashes bind
the session to the model, route and detector configuration.

Keep all frames from one held pose together in validation folds. Splitting
adjacent frames between training and validation leaks nearly identical
measurements and overstates generalization. Repeated anchors test consistency;
they should not appear as independent training examples on both sides of a fold.

Record rejected captures too. A summary saying “not visible” cannot later
explain whether fingers, a cable, exposure or a stale frame caused the problem.
This is why the later standing recorder includes the full camera streams.

## Experimental collection and route contracts

Manual GUIDE/HOLD teaching established supported and held poses, stationary
bursts and bounded replay. GUIDE did not establish a general certified
freedrive mode. The operator removed their support only after HOLD was active.

Automated bilateral work then introduced finite target sets, explicit
collision pairs, line-of-sight checks and reversible routes. One rejected
candidate exposed missing shoulder/torso collision pairs; a previous
100-target plan was no longer usable after those pairs were included.

The newer design separates a reusable core route around closed visual anchors
from an adapter generated for the live starting state. Active-arm excitation
requires the active marker; inactive-marker observations are optional there.
Both markers are required at bilateral anchors. Physical CAD marker rays test
arm/hand occlusion, while fitted effective target coordinates remain part of
the calibration model only.

```{admonition} Current procedure is newer than the last physical run
:class: warning

The final September 7 workflow requires the operator to preclose the hands.
It holds their measured posture and removes automatic closing/restoration.
Old route cores must be regenerated for that geometry. The implementation
has offline checks; this latest lifecycle has not been physically validated.
```

Readiness compares all 14 measured hand joints with saved references: within
0.08 rad, stationary over 0.5 s with at most 0.01 rad spread. It is checked
before SPACE, after SPACE and during acquisition. Shoulder search caps were
bounded at 0.08/0.10/0.12/0.14 rad. The source reports 635 tests with nine skips
and a GPU preparation check with 10.4566 mm clearance against a 5 mm requirement.
These are historical source-reported checks, not a completed new robot run.
Separately, publication checks exercised 317 selected offline regressions with
seven skipped; neither check set establishes physical commissioning.

## From a fit to a deployment

| Artifact | What it establishes | What it does not establish |
|---|---|---|
| Raw session | Images, decoded corners, measured joints and rejected attempts | A valid model fit |
| Exported dataset | Samples passed the export rules and retain their identities | Correctness of those rules under every noise condition |
| Solver output and grouped report | A declared model's fit and held-pose error | Unique physical cause or task accuracy |
| Candidate bundle | A reproducible model/configuration artifact | Automatic approval or selection for hardware |


Retain the raw session and grouped validation report with every candidate
bundle. Compare the same data split and model parameterization before treating
a lower pixel number as an improvement. Review anchor consistency, active-pose
error and any physical control outcome separately.

The deployed stacking baseline remained the August 12 selected-offset bundle.
No September candidate should be described as a replacement merely because a
solver produced it. See [results](results.md) and the [investigation record](investigation.md)
before changing the model or proposing another calibration test.

The source provides separate offline dataset and solve entry points:

```bash
./tools/g1_tabletop.sh build-bilateral-calibration-dataset \
  --session /path/to/retained-session --output /path/to/dataset.json
./tools/g1_tabletop.sh solve-bilateral-calibration \
  --dataset /path/to/dataset.json --output-directory /path/to/solve
```

Replace the paths with a retained session and a new analysis output location.
These source-documented commands do not imply that a session will pass the
export gates. Collection and solving do not overwrite the deployed bundle;
hardware launch still selects it explicitly with `--calibration-bundle`.

Evidence: prototype/tabletop logs and the calibration investigation ledger.
[Source identities](../reference/sources.md).

## Follow the code

| Implementation concern | Code entry point | Responsibility |
|---|---|---|
| Collection lifecycle | [hardware_bilateral_calibration.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/hardware_bilateral_calibration.py) · `run_collect_bilateral_calibration` (September branch) | Orchestrate frozen inputs, ownership, captures and return. |
| Live adapter | [adapter.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/adapter.py) · `plan_owned_adapter` (September branch) | Bind the adapter to the commands actually held after acquisition. |
| Burst evidence | [capture.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/capture.py) · `BilateralLiveBurstSource.capture_burst` (September branch) | Retain current decoded corners and measured-state evidence. |
| Raw session and dataset | [session.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/session.py) · `BilateralSessionStore.build_dataset` (September branch) | Reconstruct accepted samples from retained, verified artifacts. |
| Model fit | [solver.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/solver.py) · `solve_bilateral_dataset` (September branch) | Run the declared solver and independently evaluate its output. |
| Grouped validation | [validation.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/validation.py) · `validate_and_select_bilateral_model` (September branch) | Compare models on held groups before selecting an eligible candidate. |
| Bundle export | [bundle.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/src/g1_dex3_tabletop/calibration/bundle.py#L34) · `write_bilateral_calibration_bundle` | Preserve the solution and validation provenance in a separate artifact. |

For collector changes, start at the coordinator, then follow capture, session,
solver and validation according to the concern you are changing. For the pixel model, start with [projection.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/calibration/projection.py) · `BilateralCalibrationProjection.project_side` (September branch). Exporting a bundle does not change the bundle selected by a hardware launcher. Before interpreting residuals, read the [results](results.md), [investigation record](investigation.md) and the [public runtime summary](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/docs/september-calibration.md).

## Checks and evidence to inspect

[test_bilateral_calibration.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/tests/test_bilateral_calibration.py) (September branch) covers hash binding, projection, grouped model selection and same-frame evidence; [test_standing_calibration_control.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/tests/test_standing_calibration_control.py) (September branch) covers the ownership lifecycle. The final manually preclosed workflow has reported offline checks only. Preserve that distinction from the earlier physical collections above.
