# First-draft review queue

The first draft covers all located summer work and later corrections through
September 7. The next step is a focused discussion of particular sections,
with the source evidence already assembled. These gaps are visible so they
can be resolved without inventing installation facts or performance claims.

## Author and hardware review

| Topic | Input needed | Why it matters |
|---|---|---|
| Dex3 installation | Actual JST extension part/series, both connector ends, pinout, length, route and replacement sequence | This tacit installation knowledge is not recoverable from the code |
| Current robot | Photograph of support, harness, hands, waist configuration and camera witness mark | The physical configuration changed between June and September |
| Marker mounts | Final prints on both hands, third-pad contact, screw fit and target orientation | CAD dimensions alone do not prove the physical mount seats correctly |
| Torso carrier | Which revision was printed/fitted and which checks actually passed | The documented design is not yet a qualified torso reference |
| Summer boundaries | Final historical cutoff and preferred author name/credit | September corrections must remain even if the narrative ends in August |
| Licensing | Documentation license and asset attribution review | A public repository is not itself a blanket reuse license |

## Demonstrations to select together

Prioritize one complete cube manipulation run, one useful failure/correction,
a calibration capture showing the actual markers, and a passive tactile
visualization. For each, retain the run ID, date, source version and outcome.
If a clip stops before return or cleanup, say so in the caption.

The [media catalog](media.md) already identifies reviewed source figures and
available MuJoCo release videos. Physical photos/videos can be added as the
author supplies them. Synthetic replacement images would not establish the
hardware details these sections need.

## Evidence and reproducibility gaps

- Archive the uncommitted tabletop log, calibration ledger and linked retained
  artifacts under their recorded hashes. The current inventory is not a backup.
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

Start with [pickup and stacking](../manipulation/tasks.md) and
[control ownership](../control/ownership.md): they contain the most reusable
hardware lessons and the clearest end-to-end story. Then review
[calibration results](../calibration/results.md), followed by installation/media.
The author can choose a different entry point without restructuring the whole
guide.
