# Remaining review needs

This page tracks specific gaps that the source and available media cannot yet
resolve. The guide's structure follows reusable systems; the next revision
should improve a concrete explanation or supply missing evidence, rather than
expand every experiment into an operating tutorial.

## Author and hardware review

| Topic | Input needed | Why it matters |
|---|---|---|
| Dex3 installation | Deck now establishes the 4-pin, 300 mm JST-GH extension and photographed routing/fitting; still need pinout, power-isolation steps, present fastener condition and linked boot video | Complete the walkthrough without generalizing this robot's damaged threads or using slide order as an operating procedure |
| Current robot | Head-pitch witness mark now photographed; still record the complete intended support, harness, hands and waist configuration together | The physical configuration changed between June and September |
| Marker mounts | Final prints on both hands, third-pad contact, screw fit and target orientation | CAD dimensions alone do not prove the physical mount seats correctly |
| Torso carrier | Lower M6 reach, measured upper engagement, and complete V7 assembly/board repeatability | V7/R2 is current; partial coupon trials and recorded CAD checks do not qualify the torso reference |
| Licensing | Documentation license and asset attribution review | A public repository is not itself a blanket reuse license |

## Demonstrations to select together

The supplied physical stacking video now shows pickup, placement, release
and hand withdrawal. Match it to the retained bag/run ID and cleanup outcome;
the footage alone does not establish software ownership handback. The standing
calibration video now shows the wrist markers and physical pose sequence;
attach its exact session ID as well. A useful failure/correction clip would
complement the embedded physical, tactile, planning, simulation and viewer demos.
For each, retain the run ID, date, source version and outcome. If a clip stops
before return or cleanup, say so in the caption.

The [media catalog](media.md) identifies reviewed source figures, available
MuJoCo release videos and the selected September publication copies. The
retention and stacking-plan demos are rendered/simulated; keep physical success
claims tied to physical runs. Synthetic replacement images would not establish
the hardware details these sections need.

## Evidence and reproducibility gaps

- Preserve private journals and full experimental artifacts in backed-up storage
  with an explicit lab handoff. Public implementation links now resolve to
  committed source; availability of raw experimental evidence is separate.
- Preserve access to the published Drive datasets during the lab handoff.
  The stacking archive is LeRobot; calibration retains its original capture
  format, selected fit inputs and bundle.
- Review the operator runbook against the exact intended deployment revision.
  Some setup scripts retain local workspace assumptions.
- Keep September capture success separate from control release: September 5
  returned normally; September 7 accepted captures but failed finger restoration.
- The newest manually preclosed calibration workflow needs regenerated cores
  and physical validation. Old closed-route geometry is not reusable as-is.
- Moving-target MPC remains experimental. The rejected padding approach and
  held calibration sweep/issue/patch are not new tasks for this documentation.
- Independently annotate physical placement/stack success before reporting a
  success rate from the 13 completed recording boundaries.
- Reproduce the MuJoCo setup in a clean workspace and reconcile its older
  model-shape diagnostic. The pretrained OpenHomie policy is linked in the
  chapter; sampled demo frames were reviewed, without a quantitative stability test.

## Continuing the review

Prioritize missing facts that prevent a researcher from reproducing the setup
or understanding the control/recording interfaces. The installation pinout and
power procedure, final mount fit and exact media-to-run associations above
need hardware or author evidence. An editorial rewrite cannot fill them.

For each technical revision, check that the reader can identify the inputs,
expected output, constraints, failure behavior and relevant implementation.
Keep task-specific examples when they explain those points. Review the
[control lifecycle](../control/ownership.md) and [recording contract](../data/recording.md)
against the intended application before extending either.

Desktop layout remains the current presentation target. Revisit mobile
navigation, wide tables and diagram interaction during the final presentation
pass after the chapter content is settled.
