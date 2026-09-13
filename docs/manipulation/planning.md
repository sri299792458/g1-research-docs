# CuRobo planning contracts

The planning pipeline must return a route that the current controller can
join, execute, reject and reverse. Reaching a Cartesian endpoint is only one
part of that contract.

## Model the measured robot

The tabletop model contains 49 coordinates: seven active arm joints and
42 locked coordinates. Both hands and their marker geometry are represented.
Locked means fixed for a planning problem, not absent from collision geometry.
Refold current measured locked state when reusing a worker.

Map joints by names across DDS, URDF and CuRobo. The hands' index/middle order
is not consistent with an arbitrary seven-element slice. Model topology,
object/fixture profile and attachment configuration determine whether a
cached planner is reusable.

The CPU/ROS controller and GPU planner are separate processes. Planner results
carry the model/scene identity and the start they were solved from. A solver
should not construct a robot publisher or change ownership.

## Preserve alternatives without exhausting GPU memory

Submitting all 1,544 IK candidates at once exhausted memory. Batches of 128
reduced the observed memory requirement to about 4.2 GB. Each candidate received
independent seeds so early goal-set choices did not starve later branches.
The fallback tested the finite pool before declaring the problem unreachable.

CuRobo mutates an input `JointState` in the examined code path. Reusing that
object between attempts quietly changed later starts. Build a fresh per-attempt
state; reuse the expensive planner separately.

## Strict collision checks remain independent

A selected-arm 400 × 400 × 20 mm table patch helped optimization. The observed
cube did not register the entire 1,400 × 700 mm table, so the patch cannot claim
that physical coverage. Independent support-plane validation checks the moving
wrist, hand and payload. It does not certify unseen table edges or every elbow
configuration.

Early selected-shoulder negative buffers and monotonic escape from overlapping
starts were removed. **The current live start must be strictly clear.** Pruning
invariant locked/locked pairs does not remove active-arm collision checks.
Roundoff corrections are limited to numerical error and cannot repair a real
state discontinuity.

The cube payload uses 27 circumscribed cells to preserve conservative coverage.
An alternative attachment path silently retained only two of 16 proposed
spheres, illustrating why the attached model must be inspected after creation.

## Measured state and commanded state are different inputs

Measured state defines geometry and contact. The exact active command defines
the join to an already streaming trajectory. Approximately 0.02 rad of physical
tracking error is not permission to insert that difference as a command jump.
Frozen joins were checked to 1e-9 where exact command continuity was required;
float32 anchoring only addresses scale-dependent numerical roundoff.

A physical table strike led to a 5 mm motion clearance floor. Contact changes
the fingers, so the payload path is checked again with achieved contact
geometry. A contact start may be positively below 5 mm only under the explicit
policy of not moving deeper, reaching the free-space floor and retaining its
exact reverse. A penetrating start is not admitted.

## Complete routes include recovery

Plan pregrasp, approach, lift, placement and all return transitions. If a
boundary replan fails, an already frozen reverse must remain executable. The
August 17 lift/replacement exposed an omitted `return_to_pregrasp` leg; the
object action happened, but the lifecycle failed afterward.

One GPU strict-collision implementation reduced a reported task from 295.81 s
to 39.05 s with the same decisions and bit-identical path. A compatible warm
pool reduced another solve from 15.29 s cold to 1.85 s warm; small GPU
differences remained. These are task-specific timings, not whole-robot cycle
times or universal CuRobo performance claims.

See [ownership](../control/ownership.md) for fixed-rate execution and
[MPC](mpc.md) for the experimental future-window contract.

Evidence: tabletop planning, strict-collision and worker-pool entries.
[Source identities](../reference/sources.md).
