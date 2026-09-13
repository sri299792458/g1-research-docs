# G1 research documentation

Practical documentation for researchers working with the Unitree G1. This project
preserves the tooling, operating procedures, experiments, and lessons developed
by [sri299792458](https://github.com/sri299792458) during summer 2026, with the aim
of helping future lab members understand the robot and build on that work.

**Work in progress:** source reading and discussion are underway. The research
notes are working evidence summaries; the documentation chapters and website are
still being developed with the author. A completed operator guide is not yet
available.

The work spans hardware setup, Dex3 pressure sensing, an initial MuJoCo backend,
AprilCube pose estimation, camera/kinematic calibration, control and safety
tooling, grasp proposals, CuRobo planning, and recording.

- [Running notes](running_notes.md): author intent, decisions, corrections, and progress.
- [Source inventory](research/source_inventory.md): reading coverage and evidence locations.
- [Source snapshot](research/source_snapshot.json): local source revisions and file hashes.
- [G1Pilot reading](research/g1pilot-reading.md): early integration and operating lessons.
- [MuJoCo backend reading](research/g1pilot-mujoco-reading.md): the later simulation work.
- [Maintenance and contributions](CONTRIBUTING.md): how to preserve evidence and make updates.

The author's [Spark Data Collection documentation](https://rpm-lab-umn.github.io/spark-data-collection/)
is a reference for depth, practical procedures, explanations, and supporting media.
The G1 documentation's organization is still open.

## Ownership and continuity

Development is currently local, with Git history maintained here. Connection to
the author's personal GitHub account is deferred until later. Once the summer
documentation is complete, a copy with its Git history will be established in
the lab's GitHub organization for future lab members to maintain and extend.
The planned personal repository will remain available as the author's portfolio record.

The handoff should preserve a tagged summer version, attribution, source
references, and media access. Later lab contributions should be dated so readers
can distinguish the original summer work from subsequent development. The lab
copy and its maintenance location will be linked here when they exist.
