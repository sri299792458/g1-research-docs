# Reading the calibration investigation correctly

Read this before proposing another explanation for the remaining calibration
error. It preserves the completed comparisons that most affect the next
engineering decision. The public conclusions below are usable without the
private working ledger; consult that ledger when available for the full
experiment trail and operator corrections.

| Proposed direction | What has already been learned |
|---|---|
| Add poses or depth | Broad arm excitation and one/two-run RGB-D fits were already tested; depth did not consistently improve held-out RGB results |
| Attribute differences between September sessions to camera drift | The camera was deliberately repositioned; each session needs its own registration |
| Replace measured joints with ideal command tracking | Calibration already uses measured state; ordinary tracking error does not explain the remaining model discrepancy |
| Change wrist spacing from 46 to 51 mm | Broad fits favored it, but the controlled August refit improved only about 7%; changing geometry without refitting made error worse |

The camera explanation was treated as excluded in the retained investigation;
that is the scope of this diagnosis, not a claim that cameras can never be a
source of error. The [results page](results.md) separates the deployed bundle
from later research.

## What the observations do and do not support

The operator accepted camera error as excluded from the remaining diagnosis.
The two September sessions deliberately used different camera positions and
need separate registrations. Marker mounts were treated as constant within a
run, not necessarily across runs. Forearm markers were not physically feasible.
Broad active-pose coverage and single/two-run RGB-D optimizations had already
been completed. “Add more poses,” “use depth,” and “make measured equal commanded”
are therefore not fresh explanations for the unresolved error.

Depth supplied a useful plane constraint but did not consistently improve
held-out RGB fits. Thousands of correlated pixels on one plane are not thousands
of independent geometric constraints. Plane agreement does not observe
translation within the plane or yaw, and residual weights are not measured
uncertainties.

## The 46 mm versus 51 mm wrist spacing

A caliper measurement was approximately 51 mm in the direction parallel to
the gold CAD line; the reviewed photograph appeared to show 51.38 mm. The
precise side-specific value, repeated-measurement uncertainty and motor variant
were not established. A manual version number and `mode_machine=5` do not
identify a 4010 or 5010 motor.

The two-run geometry study used 46 conditions over 104 holds and 208
observations, with pose families withheld across sessions. Shared geometry
was fitted alongside separate run camera/target registrations. One broad
84-parameter comparison favored the 51 mm hypothesis:

| Held-out quantity | 46 mm model | 51 mm model |
|---|---:|---:|
| Broad held-out pixel metric | 8.2807 px | 3.1701 px |
| Diagnostic pixel metric | 18.8714 px | 4.3012 px |
| Plane metric | 6.2373 mm | 2.5828 mm |

These are paired reports within that study, not portable accuracy guarantees.
The broad model also allowed other corrections. A 51 mm model with only
12 joint offsets gave 7.3683/12.0108 px on the corresponding pixel metrics.
It would be incorrect to attribute the broad result entirely to one 5 mm edit.

## The controlled replay on the original August data

Using the original folds and the same 25-parameter model, refitting with the
51 mm geometry changed cross-validation from 5.409 to 5.0305 px: approximately
7% better, with three folds improving and two worsening.

Holding the original fitted parameters fixed and changing only geometry instead
made held-out error worse: 5.409 to 12.649 px. The changed FK point moved exactly
5 mm without an orientation change; the associated image displacement was
about 12.3818 px. These results are compatible. Refitting redistributes error
among camera, target and offsets, whereas the frozen comparison exposes the
effect before that compensation.

The full vendor 5010 arm FK reduced to the same arm-spacing change in the
controlled replay. That does not prove this robot's motor identity. Some joint
origin changes also form unobservable combinations—for example the reviewed
wrist-roll/wrist-pitch origin compensation—so an apparently improved fit does
not uniquely locate an as-built error.

## Current disposition

No September bundle replaced the August stacking baseline. The broader sweep,
GitHub issue and wrist patch remained paused/unapplied in the reviewed record.
This documentation does not reopen them.

Before proposing further work, identify which recorded result would be changed
by the proposed measurement, what new observable it adds, and which assumptions
it can actually distinguish. A camera overlay, a caliper photograph and a
held-out model comparison each answer different questions.

Evidence: calibration investigation ledger and its linked replay artifacts;
tabletop September follow-up. [Source identities](../reference/sources.md).
