# Calibration results and limits

The summer produced useful effective calibration and substantial evidence
about where the model disagreed with the robot. Pixel residuals, successful
capture and completed manipulation are different outcomes; this page keeps
their conditions visible.

## Early effective corrections

The manual session contained 39 observations and 273 images. A camera/target
extrinsic fit gave approximately 8.205 px residual. Adding an effective
shoulder-roll correction of +4.346° reduced it to 4.875 px; allowing all offsets
gave 4.363 px. The extra parameters did not by themselves identify a physical
cause. Capture 028 was later confirmed to involve stream lag, not demonstrated
compliance. Removing it barely changed the shoulder correction.

In a right-hand 62-primary study, fixing the marker at its CAD transform gave
23.045 px holdout error versus 9.737 px when it was free. The effective marker
correction was 13.638 mm and 4.621°. Those are fitted compensation values,
not measurements of how far the printed mount was misplaced.

## The August 12 stacking baseline

The original bilateral dataset contained 41 left and 62 right observations.
The selected model fitted a shared camera, two target transforms and seven
joint offsets, for 25 parameters. Its grouped cross-validation error was
5.409 px overall: 5.162 left and 5.566 right, with 4.952 px training error.

The [bundle](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/config/calibrations/dex3_shared_20260812_selected_free.json)
is included in demo `main`. It was used by the five retained August 25 demo
runs and the earlier 13 completed August 21 stack requests. That is a useful
deployment connection, but 13 completed recordings are not 13 independently
scored stacking successes. The five August 25 completion records also need
separate physical outcome annotation. The bundle does not establish absolute FK
accuracy everywhere in the workspace.

## September 5: broader capture, export still blocked

Session `20260905T231145` accepted 55 captures: 23 left, 24 right and eight
anchors, totaling 385 images and 48 pose groups. It recorded 17 rejected
attempts and 19 retries, then returned through Q and released without a fault.
Its six-topic standing bag omitted the camera streams; images of failed views
cannot be recovered from that recording.

| Model on this session | Grouped CV, overall | Important qualification |
|---|---:|---|
| Camera and targets | 22.95 px | Native FK did not explain the full route |
| Shoulder correction model | 5.94 px | Effective correction |
| Selected seven offsets | 5.43 px | Active-pose error remained 7.95 px |

Stationary observations were around 2 px. Mixing them with excited arm poses
improves the overall number. The numerical similarity between 5.43 px here
and August's 5.409 px is not an equal-condition comparison.

The normal exporter rejected apparent anchor PnP translation spans of about
19.8 mm left and 10.65 mm right. Pooling all frames and both targets reduced
the joint estimate to about 3.94 mm, and synthetic noise checks showed the
original gate was uncertain. Neither analysis proves 20 mm physical camera
drift or establishes a validated replacement acceptance gate.

## September 7: complete images, unsuccessful cleanup

Session `20260907T133509` accepted 49 holds, yielding 343 images and 686 marker
observations. Its 14-topic bag contained 2,298,946 messages and approximately
28.43 GB. All captures were accepted, but finger restoration failed: left
index-proximal residual was 0.092489 rad against a 0.08 rad criterion after
576 commands over six seconds. Cleanup entered Damp. This was not a normal
completed release, and it motivated the manually preclosed workflow.

Repeated configurations were consistent after measured-state compensation,
with residuals of 0.107–0.361 px. Opposite-approach raw differences of roughly
3.71–16 px reduced substantially after accounting for measured configuration.
However, all 12 A/B pairs failed the measured-FK pose-equivalence gates. The
experiment therefore cannot isolate a cause at an identical hand pose.

The camera was deliberately moved between sessions. Measured joints, separate
camera registrations and the operator's corrections are required when
interpreting the comparison. Command tracking error is normal control behavior;
calibration already uses measured state.

## What remains established

The August effective bundle supported the documented manipulation baseline.
The September work showed that nominal geometry, parameter compensation and
validation design matter. It did not produce a newly deployed bundle or a
unique physical diagnosis. The [geometry investigation](investigation.md)
explains why a plausible 5 mm wrist correction needs careful interpretation.

Evidence: dated tabletop log entries, original bundle evaluation and the
calibration investigation ledger. [Source identities](../reference/sources.md).
