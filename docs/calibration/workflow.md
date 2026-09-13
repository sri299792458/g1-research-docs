# Camera and arm calibration

Calibration connected the manually pitched head camera, measured G1 joints
and printed wrist targets. The central difficulty was that the nominal arm FK
did not explain all observed target motion. Optimizing a camera transform alone
could not make that inconsistency disappear.

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

## How the capture workflow evolved

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
These are reported offline checks, not a completed new robot run.

## From a fit to a deployment

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
