# Summer timeline

Dates come from the source journals. September follow-up is included because
it changes the interpretation of earlier calibration and manipulation results.

| Period | Work and turning point | Outcome |
|---|---|---|
| June 21 | G1Pilot dependencies, dry mode, topic/TF and command repairs; camera/LiDAR diagnosis | Development base; physical camera USB fault identified |
| June 25 | Passive Dex3 raw audit, baseline, free-touch study and RViz mapping | 33 active taxels on the inspected right hand; raw counts remain uncalibrated |
| June 30–July 1 | MuJoCo G1/Dex3 and OpenHomie | Initial backend and two demos |
| July 13–15 | AprilCube rounding and H2D printing | Compact 40 mm/R3 print selected |
| July 18–21 | Dex3 descriptor and batched grasp tests | Conditioning error isolated with crossed-hand and factorial tests |
| July 22 | VIRAL-profile contact atlases | 4,096 proposals per object, explicit physics provenance |
| July 22–29 | Assembly, support-conditioned U tests, 100K sampling, Lightning-Grasp | Tested kinematic assembly; broad-face U pickup unsolved |
| August 1–4 | Calibration formulation, captures, teaching/replay | Arm-correlated model error identified |
| August 9–12 | Fixture CAD, dorsal mounts, seated recovery and hand preparation | Physical mount correction, control commissioning, calibration datasets |
| August 13–15 | Focused tabletop repo, CuRobo worker, MCAP | Failed grasp reveals misuse of simulated finger endpoints |
| August 16–19 | Rigid-seat study, observer, retention revisions | Fresh boundary observations and physical pickup/lift trials |
| August 20–21 | Persistent planners, direct stacking, moving-target MPC | Physical stack runs; MPC endpoint conflict retained |
| August 22–24 | Faster conversion; rebuild from Friday baseline | Retained-control stack episodes, 57-candidate pool preserved |
| September 4–5 | Standing bilateral integration and takeover failures | Watchdog, command boundary, serialization and waist issues; 55-capture safe Q return |
| September 7 | 49-capture diagnostic and geometry studies | Repeatable model error, approximately 51 mm wrist evidence; no deployment |
| September 7, final code | Manually preclosed calibration hands | Offline checks; new cores and physical validation pending |

## The recurring pattern

A missing recorder stream became a stricter subscription contract. A stalled
finger became a distinction between simulated outcome and command intent. In
one recorded takeover failure, elbow movement followed a watchdog already
entering recovery. A large grasp atlas became a small candidate set once the
table and closing sweep were included.

The later tools keep those distinctions in artifacts: source hashes, selected
grasp IDs, measured state, active commands, phase names, rejected alternatives,
raw recordings, and control cleanup outcomes. The
[debugging chapter](../reference/debugging.md) turns these examples into a method.

Evidence: [primary journals](../reference/sources.md). The tabletop log contains
inherited prototype entries and sections outside chronological order; later
operator corrections govern the interpretation.
