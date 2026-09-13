# Exploring Dex3 pressure sensing

The pressure tools made the right Dex3's raw tactile messages inspectable in
ROS and RViz. The study established active slots, untouched noise and a usable
visualization mapping on the physical hand marked `214-R-T`. It did not
calibrate raw counts into force.

## Start with the raw message

`unitree_hg/msg/HandState` contains nine pressure groups with 12 cells each:
108 raw pressure slots per hand. Each group also contains temperature values,
`lost` and `reserve` fields. On the inspected right hand, 33 slots responded
as taxels and 75 remained exactly at the unused value `30000`.

| Group ID | Active cell indices |
|---|---|
| 0, 2, 4, 6, 7, 8 | 0, 2, 9, 11 |
| 1, 3, 5 | 3, 6, 8 |

An initial 45-sample, 4.87 s audit established the layout. A later 210-sample,
20 s untouched baseline confirmed that every inactive slot stayed at `30000`.
The map begins from an external diagram, but repeated live touches are the
authority for this particular hand's placement.

## Topic rate changes what you can observe

The source measured approximately 9.1 Hz on `/lf/dex3/right/state` and
750–770 Hz on `/dex3/right/state` in short runs. The lower rate was useful
for guided mapping and RViz; fast taps or slip need the higher-rate stream.
Recheck rates on the actual firmware and network rather than treating these
historical measurements as specifications.

The tools subscribe to state and publish visualization markers plus optional
joint states. They do not publish hand commands. After following the source
workspace setup, a passive raw observation is:

```bash
ros2 topic echo --once --full-length /dex3/right/state unitree_hg/msg/HandState
```

The default visualizer uses the lower-rate topic:

```bash
ros2 launch dex3_pressure_tools dex3_pressure_visualizer.launch.py
```

If an existing launch already owns robot description and joint-state defaults,
use the documented flags to avoid duplicate publishers. See the repository
README and `docs/LAB_PROTOCOLS.md` for the complete launch context.

## Baseline and display model

```text
valid = finite(raw) and abs(raw - 30000) > 1000
baseline = median(valid untouched samples)
noise = p99(abs(untouched samples - baseline))
delta = max(raw - baseline, 0)
```

The untouched rerun had median/max standard deviation about 5.9/7.5 counts
and median/max p99 absolute drift 16/24 counts. No active taxel drifted by
50 counts or more. That supported a 50-count visualization threshold on this
hand under these conditions.

The free-touch session contained 1,274 samples over 139.7 s. Across active
taxels, peak delta had median 2,280 and maximum 13,800 counts; 22/33 exceeded
500. A 500-count “definite touch” display threshold was conservative relative
to those observations, not a force threshold in newtons.

Rebaseline while untouched. Do not let an existing contact become the zero
reference. Preserve raw arrays and validity masks alongside the display; a
color overlay alone cannot reveal an unused slot or baseline mistake.

## Mapping the fingers

Physical RViz checks established right-hand motor order as thumb 0/1/2,
middle 0/1, index 0/1. The explicit 33-taxel YAML stores marker poses on named
links. A misplaced visual taxel should be changed after repeated touch evidence,
not simply because a mirrored diagram looks more plausible.

Later cube manipulation explored pressure as required grasp evidence and
replaced that gate with opposed joint shortfall relative to measured empty
close. That result does not invalidate the sensor study. It says pressure
was not a reliable required signal for those cube contacts and placement.

Evidence: `dex3_pressure_tools` README, observations, signal model and mapping
documents at the [recorded revision](../reference/sources.md).
