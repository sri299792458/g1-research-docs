<!-- Opening draft for discussion with the author. Not yet reviewed or approved. -->

# Working with the Unitree G1

This documentation brings together what I learned while working with the Unitree
G1 during summer 2026. Its purpose is to help other researchers get started,
understand the tools developed along the way, and build on the work.

I approached the summer as an investigation of the robot's capabilities and
limitations. That meant learning its hardware and software interfaces, examining
how its models matched the physical robot, and developing tools and operating
procedures to support research on top of the SDK.

The work included exploring Dex3 pressure sensing, developing an initial MuJoCo
simulation backend, using printed AprilCubes for pose estimation, and calibrating
the head-mounted RealSense camera with hand-mounted targets. It also included
offline grasp proposals with GraspGen-X, control and safety tooling, CuRobo motion
planning for cube stacking, and extending SPARK-style recording to the G1.

Much of the useful knowledge came from iteration on the physical system:
understanding a failed run, checking an assumption, changing an approach, and
recording what the next experiment established. Those lessons explain why the
tools and procedures took their current form.

The aim of these pages is to preserve that reasoning alongside practical
instructions and supporting evidence. A future lab member should be able to
understand the starting conditions, follow the work, recognize its remaining
limitations, and contribute improvements without having to reconstruct its
history from scratch.
