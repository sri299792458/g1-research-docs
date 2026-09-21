# First-draft review queue

The first draft covers all located summer work and later corrections through
September 13. The next step is a focused discussion of particular sections,
with the source evidence already assembled. These gaps are visible so they
can be resolved without inventing installation facts or performance claims.

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
- Review MuJoCo video content and reconcile its older model-shape diagnostic
  before advertising runnable simulation verification.

## Suggested review order

Desktop layout is the current presentation target. Review mobile navigation,
wide code tables and diagram interaction during the final presentation pass,
after the chapter content and desktop layout are settled.

The first detailed revision is [control ownership](../control/ownership.md):
acquisition, continuous holding during planning, task rejection versus control
fault, and verified handback. Review whether a new researcher can follow each
responsibility into its implementation and understand the failure that led to it.

Next, deepen [pickup and stacking](../manipulation/tasks.md) into a complete
worked attempt, connecting the physical demonstration to observations, grasp
selection, planned routes, contact checks and retained artifacts. Then review
[calibration results](../calibration/results.md) for what the evidence permits
another researcher to trust or change. Installation details remain a separate
practical priority; the supplied photos and videos are now embedded.
