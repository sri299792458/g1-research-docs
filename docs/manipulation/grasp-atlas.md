# GraspGen-X and offline qualification

GraspGen-X supplied candidate object-relative grasps. Making them useful for
the physical Dex3 required resolving frame conventions, descriptor semantics,
simulation contacts, support geometry and the meaning of a closing command.
The July grasp-demo repository records that investigation; later tabletop
results correct several of its original hardware assumptions.

## The network's output is not the palm pose

The output is an object/point-cloud-from-canonical-grasp transform. Compose
the descriptor's fixed grasp-to-palm transform exactly once to obtain the
palm target. Pregrasp is another constructed pose, not an alternative name
for that output frame.

The network consumes 12 sweep-volume descriptor values. It does not read the
current URDF or predict an object's final physical finger joint state. The
released hand and current revision-1 Dex3 geometry differed, and the first
literal-looking descriptor for the current hand performed poorly.

```{figure} ../assets/images/dex3_rev1_descriptor_states.png
:alt: Rendered left and right Dex3 hands in open, half and closed states with descriptor boxes and coordinate axes.

The original descriptor audit. Blue/open and yellow/half boxes represent the
learned proxy; the closed endpoint is illustrated separately. This is rendered
model geometry, not a physical measurement. [Provenance](../reference/media.md).
```

A crossed 120-proposal study separated proposal conditioning from evaluation
geometry. Released proposals passed 110 times on the old hand and 118 on the
current hand. The initial current descriptor passed only five and 16 times,
respectively. Across all 16 box-group combinations, changing only open extents
raised 16/120 to 111/120; a simple 53° frame rotation gave 0/120. Fresh-seed
checks gave 467/480 for the current aperture-semantic descriptor and 472/480
for the released proxy.

The retained descriptor therefore acts as learned conditioning, not a literal
physical enclosure. Its open extents/center were `[0.10, 0.06, 0.04]` and
`[0, 0, 0.07]` metres; half-close values were `[0.04, 0.06, 0.04]` and
`[0.007, 0, 0.06]`. Exact physical geometry still governs evaluation.

## Three different questions

| Qualification | Question | What a pass does not establish |
|---|---|---|
| Intrinsic retention | Can this hand/object/contact setup retain the object? | Table access or robot reachability |
| Supported pickup | Can it approach and close from this resting pose? | A collision-free whole-arm route |
| Robot execution | Can the measured robot execute and recover the complete task? | Generalization to every object/support |

Early Newton hand-only tests prescribed the root through the table. Those
tests could not judge intrinsic grasp quality, and an ejected object reaching
height was not a valid lift. Later evaluation separated these questions.

## Physics configuration changed the result

A USD self-collision regression made repeated identical grasps unstable.
Disabling collisions within the hand produced 10/10 passes in the repeated
check while retaining hand/object contact. Hashing only the root USD would
miss a changed physics sublayer, so provenance must include referenced layers.

The audited VIRAL implementation used `ImplicitActuator` despite an ideal-PD
label in YAML. The evaluated simulation profile used 200 Hz TGS, thumb-0
`kp=2, kd=0.1`, other joints `kp=0.5, kd=0.1`, increased armature and zeroed
joint friction. These are simulation settings, not hardware gains. The cube
mass was measured as 30 g; T/U masses were estimated at 181.1/211.3 g.

Under the final documented 4,096-proposal-per-object profile:

| Object | Intrinsic passes | Fraction | Grasp families |
|---|---:|---:|---:|
| 45 mm cube | 2,437 | 59.50% | 40 |
| T | 1,240 | 30.27% | 39 |
| U | 675 | 16.48% | 28 |

Earlier totals used another physics profile. Family-primary replay passed
39/40, 30/39 and 20/28, respectively; the remaining cases stay in the record.
Contact reporting changed from a summed vector, which could cancel opposing
contacts, to maximum body-pair norm. Rechecking all 12,288 trials changed no
pass/fail verdicts while improving the diagnostic quantity.

## Why simulated closed joints were the wrong hardware command

The actual 40 mm cube received new inference: 3,178/4,096 intrinsic passes,
then an initial 15-grasp shortlist. On physical run `190430`, the arm arrived
within 3.61 mm and 2.99° of the intended grasp but the close stalled. In its
simulation, the cube had moved 14.87 mm and 14.52° during closing.

The recorded simulated joint vector was an achieved outcome after object
motion. It was not the descriptor's fixed closing intent. Requalification with
a stationary cube and the fixed close admitted five 40 mm grasps. Later
60 mm work admitted 57 out of 3,279 intrinsic passes, with modeled clearances
of 5.008–15.988 mm against a 5 mm floor.

The controller now evaluates contact relative to commissioned measured
empty-close postures. See [pickup and stacking](tasks.md). Older grasp-demo
instructions to send `isaac_closed_q` and use the tripod are superseded.

Evidence: complete July/August grasp-demo log, followed by tabletop physical
close corrections. [Source identities](../reference/sources.md).
