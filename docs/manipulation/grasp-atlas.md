# GraspGen-X and offline qualification

GraspGen-X supplies candidate hand poses; it does not decide whether a G1 can
pick an object off a table. The work here adapts its Dex3 conditioning, tests
retention in simulation and reduces the proposals to candidates the task
planner can use.

For the demonstrated cubes, begin with the [runtime object profiles](../perception/targets.md#use-the-profile-that-matches-the-physical-cube)
and their matched shortlists. Use this chapter when changing the hand,
object or qualification procedure, or diagnosing why a simulated grasp failed
on hardware. Regenerating proposals alone does not replace those checks.

## Three different questions

| Qualification | Question | What a pass does not establish |
|---|---|---|
| Intrinsic retention | Can this hand/object/contact setup retain the object? | Table access or robot reachability |
| Supported pickup | Can it approach and close from this resting pose? | A collision-free whole-arm route |
| Robot execution | Can the measured robot execute and recover the complete task? | Generalization to every object/support |

Early Newton hand-only tests prescribed the root through the table. Those
tests could not judge intrinsic grasp quality, and an ejected object reaching
height was not a valid lift. Later evaluation separated these questions.

<figure class="research-video">
  <video controls playsinline preload="none" poster="../_static/dex3-simulated-retention-demo.jpg" width="1280" height="720" aria-label="Simulated Dex3 grasp retention under five disturbances" aria-describedby="retention-demo-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/dex3-simulated-retention-demo.mp4" type="video/mp4">
    Your browser cannot play this video. Use the download link below.
  </video>
  <figcaption id="retention-demo-caption">Rendered replay labelled as recorded Isaac/PhysX states: grasp pose, close/settle, five directional disturbances, then an on-screen retention pass. This is a simulated tug test. Silent, 6 seconds.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/dex3-simulated-retention-demo.mp4">Download the simulated retention demo (MP4)</a></p>
</figure>

The clip illustrates the retention question. Its on-screen pass does not
establish table clearance, arm reachability or hardware grasp success. The
specific replay's candidate ID and generating report have not yet been linked,
so do not use it to reconstruct or extend the aggregate counts below.

## The network's output is not the palm pose

For a point cloud expressed in frame `F`, each proposal is `F_T_G`, mapping
the canonical grasp frame `G` into `F`. The descriptor supplies a fixed
`G_T_palm` transform. Following the [verified frame contract](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/docs/graspgenx_contract.md):

```text
F_T_palm = F_T_G @ G_T_palm
base_T_palm = base_T_F @ F_T_palm
```

Use the descriptor transform once, without inverting it. If the point cloud
is object-local, `base_T_F` is the observed object pose. If the planner controls
another tool link, obtain that additional fixed transform from the robot model.
Pregrasp is a separately constructed approach pose. The network returns pose
candidates and confidence scores; it does not return arm IK, a collision-free
route or seven candidate-specific finger commands.

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
empty-close postures. See [contact interpretation](planning.md#interpreting-contact-before-using-a-payload-route). Older grasp-demo
instructions to send `isaac_closed_q` and use the tripod are superseded.

Evidence: complete July/August grasp-demo log, followed by tabletop physical
close corrections. [Source identities](../reference/sources.md).

## Follow the code

| Implementation concern | Code entry point | Responsibility |
|---|---|---|
| Descriptor/frame | [build_dex3_rev1_descriptors.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/tools/build_dex3_rev1_descriptors.py#L189) · `derive_frame_and_sweep` | Derive the canonical origin and retain the exact conditioning sweep. |
| Raw generation | [run_aprilcube_raw_grasps.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/tools/run_aprilcube_raw_grasps.py#L204) · `run_atlas` | Bind seeds, descriptor and immutable candidate identities. |
| Qualification runner | [run_isaac_atlas_qualification.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/tools/run_isaac_atlas_qualification.py#L145) · `run_shard` | Run and retain the configured Isaac qualification evidence. |
| Shortlist construction | [executable_shortlist.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/g1_aprilcube_demo/grasping/executable_shortlist.py#L257) · `build_shortlist` | Join candidates to contact traces and check provenance and geometry. |
| Support analysis | [support_atlas.py](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/g1_aprilcube_demo/grasping/support_atlas.py#L462) · `evaluate_support` | Evaluate a declared support and approach corridor without claiming a physics pass. |

The linked grasp-demo code is the historical offline implementation. Its shortlist fields are not automatically the final hardware command contract: the stationary-cube/fixed-close qualification described above supersedes use of achieved simulated finger joints as a closing target. Keep that correction when adapting this pipeline.

## Checks and evidence to inspect

Inspect each candidate’s content hash, qualification profile and trace before comparing atlas counts. The [descriptor report](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/docs/dex3_rev1_descriptor.md) explains the ablations, and the [upright pickup replay report](https://github.com/sri299792458/g1-aprilcube-demo/blob/2b7274b11f1862ebfcd05b48ff678d995e55269e/docs/u_legs_upright_supported_pickup_replay1.md) records the simulated support result. The later tabletop record supplies the physical close failure and corrected candidate pools.
