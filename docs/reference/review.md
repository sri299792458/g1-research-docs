# Remaining review needs

This page tracks missing facts and reproduction checks. It distinguishes
information an author or hardware inspection must supply from software checks
that another contributor can carry out.

## Author and hardware review

| Topic | Input needed | Why it matters |
|---|---|---|
| Dex3 installation | Deck now establishes the 4-pin, 300 mm JST-GH extension and photographed routing/fitting; still need pinout, power-isolation steps, present fastener condition and linked boot video | Complete the walkthrough without generalizing this robot's damaged threads or using slide order as an operating procedure |
| Current robot | Head-pitch witness mark now photographed; still record the complete intended support, harness, hands and waist configuration together | The physical configuration changed between June and September |
| Marker mounts | Final prints on both hands, third-pad contact, screw fit and target orientation | CAD dimensions alone do not prove the physical mount seats correctly |
| Torso carrier | Lower M6 reach, measured upper engagement, and complete V7 assembly/board repeatability | V7/R2 is current; partial coupon trials and recorded CAD checks do not qualify the torso reference |
| Licensing | Documentation license and asset attribution review | A public repository is not itself a blanket reuse license |

## Connect demonstrations to their source runs

The supplied physical stacking video now shows pickup, placement, release
and hand withdrawal. Match it to the retained bag/run ID and cleanup outcome;
the footage alone does not establish software ownership handback. The standing
calibration video now shows the wrist markers and physical pose sequence;
attach its exact session ID as well. The simulated retention clip also needs its
candidate ID and generating report.
For each, retain the run ID, date, source version and outcome. If a clip stops
before return or cleanup, say so in the caption.

The [media catalog](media.md) identifies source figures and publication copies.
The retention and stacking-plan demos are rendered/simulated; keep physical
success claims tied to physical runs.

## Evidence and reproducibility gaps

- Restore the [missing AprilCube runtime pin](sources.md#aprilcube-runtime-pin-availability)
  or update it through a tested source change. Public print files are available,
  but this currently blocks a fresh recursive tabletop checkout.
- Review the operator runbook against the exact intended deployment revision.
  Test installation in a clean workspace; the setup chapter identifies remaining
  lab paths, message dependencies and PC2 prerequisites.
- The newest manually preclosed calibration workflow needs regenerated cores
  and physical validation before it can be an operating procedure. Old closed-route
  geometry is not reusable as-is; this is a capability limit, not a documentation
  instruction to run an experiment.
- Independently annotate physical placement/stack success before reporting a
  success rate from the August 21 or August 25 completion records.
- Reproduce the MuJoCo setup in a clean workspace and reconcile its older
  model-shape diagnostic. The pretrained OpenHomie policy is linked in the
  chapter; sampled demo frames were reviewed, without a quantitative stability test.
- The [public dataset viewer](../data/viewing.md) loads the five demo episodes
  and both video streams. Its clean dependency installation still needs a separate
  reproduction; the walkthrough's additional local viewer changes are not all public.
- Assembly reproduction needs the generated assets and qualification pools
  listed by the source. Published scripts and selected reports are not a full
  historical experiment archive.

## Handoff and presentation

Preserve private experimental records separately, retain access to the Drive
datasets and release videos, and resolve the license/attribution review before
the lab handoff. [Maintenance](maintenance.md#publication-and-handoff) describes
the required repository, storage and ownership updates.

Desktop layout remains the current presentation target. Revisit mobile
navigation, wide tables and diagram interaction during the final presentation
pass after the chapter content is settled.
