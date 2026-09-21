# Sources and attribution

This guide synthesizes the author's running notes, code, experiment reports
and corrections. Unless explicitly stated otherwise, test counts and physical
results are **reported by those records**, not independently rerun for this
documentation. Reading and static inspection did not send robot commands.

## Primary reading coverage

| Source | Complete coverage | Identity / availability |
|---|---:|---|
| G1Pilot June log | 1,328 lines | `72acc803edefe583c24f53e76a21d8d4ed10ed14`; [pinned notes](https://github.com/sri299792458/g1pilot/blob/72acc803edefe583c24f53e76a21d8d4ed10ed14/running_notes.md) |
| G1Pilot MuJoCo implementation | README, backend, launch/environment, generators and diagnostic | [dev snapshot](https://github.com/sri299792458/g1pilot/tree/6b5af59b109e2ee687920fdf66ded6182725e945) |
| Grasp/assembly demo | 3,209 log lines; 204 README lines | [pinned notes](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/running_notes.md) |
| Tabletop | 7,403 log lines | Local working tree based on `cf1b27704c82d877d23ff5a3c157df3218f02402`; includes uncommitted work |
| Calibration prototype | 1,864 log lines | `97a78a5c9c48701400820922f0966cc3d3a9b7bc`; local inspected source |
| Vendored AprilCube fork | 126 log lines | `g1-dex3-tabletop/third_party/aprilcube/running_notes.md`; local inspected source |
| Calibration investigation ledger | 368 lines, 85 entries and 46 model conditions | Local `g1-dex3-tabletop/docs/calibration-investigation-ledger.md` |
| Dex3 pressure tools | README, observations, protocols, signal model, mapping, dependencies | Local `e0b706df507160799b70732c7cc3244924ce8f5e` snapshot |

Prototype lines 2–1,864 equal tabletop lines 359–2,221. They are inherited
history, not independent experiments. All located primary running notes were
read sequentially. Heading inventories alone did not count as reading.

## Recovering the exact evidence

The documentation repository contains:

- `research/source_snapshot.json`: source revisions, working-tree status and SHA-256 hashes;
- `research/source_inventory.md`: reading coverage and source boundaries;
- `research/tabletop-reading.md` and `research/grasp-demo-reading.md`: detailed working summaries;
- `research/g1pilot-reading.md` and `research/g1pilot-mujoco-reading.md`: early integration and simulation evidence;
- `research/g1pilot-dev-source.json`: exact remote implementation provenance;
- `research/documentation-media-review.md` and `research/documentation-media-inventory.json`:
  September media findings, original hashes and camera-launcher code identities;
- `docs/assets/code-map.json`: code-map file hashes, symbol locations and verified public URLs;
- `running_notes.md`: documentation decisions and author corrections.

For example, the tabletop log hash is
`9b159c235fd6fdb086249d9025c3083f439292fe3a884c6f6ae4ffcfddcc3d91`
and the calibration-ledger hash is
`1acfd5b1ec9e9a626f918cb33cbc4bc0f59763d57f2fda7c1d1557d6bd5039d8`.
A commit alone does not reproduce their uncommitted contents. The snapshot
identifies evidence but does not back it up. Archiving those records and their
linked experiment artifacts is a concrete [handoff item](review.md).

Machine-specific checkout locations stay in ignored `.local/` files. Public
pages do not link to sibling directories that would be absent from another
person's clone. Where exact public evidence is available, links pin a commit.

## How conflicting records are resolved

Later operator corrections and the calibration ledger govern interpretations
of older experiments. Dated successful runs can supersede an earlier README's
“not yet tested” statement, but they do not prove that one intervening code
change caused the improvement. A proposed next step in an old note is not an
instruction to run it now.

The technical guide includes corrections through September 7, 2026. The
author has not yet finalized the historical summer cutoff. Keeping those
corrections prevents publishing procedures already known to be obsolete.

## Attribution and continuity

The research and original notes are the work of
[sri299792458](https://github.com/sri299792458), building on Unitree's SDK/models,
AprilCube, GraspGen-X, CuRobo, Isaac/PhysX, Newton, MuJoCo, OpenHomie,
GR00T, ROS, Pinocchio/OpenSoT and SPARK. The documentation draft was assembled
with coding-assistant support and awaits the author's substantive review.
Dependency inclusion does not imply original authorship of the dependency.

The [SPARK documentation](https://rpm-lab-umn.github.io/spark-data-collection/)
is the author's reference for practical depth and presentation. The personal
repository will preserve the summer portfolio record; a later lab copy should
retain history, attribution, source access and media ownership.

No new blanket license has been assigned in this draft. Preserve existing
upstream notices when copying code or assets, and settle the documentation
license with the author before the final lab handoff.
