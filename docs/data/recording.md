# Recording the G1 and exporting LeRobot

There are two uses for this chapter: inspect the shared recordings, or change
the pipeline that produces them. Start with the downloads below for the five
demo episodes and the calibration measurements. The later sections explain
which signals were retained, how recording avoids interrupting control, and
what is lost when converting raw data to LeRobot.

## Dataset downloads

The [shared Google Drive folder](https://drive.google.com/drive/folders/1YoTbBMbd4Xj_06keI1HKi7g21hk9IyTO) contains both versioned ZIPs,
a [README](https://drive.google.com/file/d/18qAWWbEcFlTzVacYFhH4-JN11d3gTDmn/view) and [archive checksums](https://drive.google.com/file/d/1zlw7vlbo44AKxk2jsWGMWj6GIg_ef1_u/view).
The table gives extracted and download sizes; choose the collection you need.

| Collection | Contents | Extracted / ZIP size | Download |
|---|---|---:|---|
| August 25 stacking | Five LeRobot episodes, 8,272 frames, RGB/depth and state/command data | 697 / 696 MB | [Stacking v1 ZIP](https://drive.google.com/file/d/1JniEt-Y8BRnyQkt_Eeo5KX-0Auv0k5nI/view) |
| August 12 calibration | Two capture sessions used by the calibration bundle; original PNG images, measurement metadata, selected fit inputs and bundle | 1.54 GB / 958 MB | [Calibration v1 ZIP](https://drive.google.com/file/d/1WfSOw_HRhGPFTZsFUM5hRjRxLsztM8-T/view) |

Both versioned ZIPs are available for download. Each includes a README identifying
the source sessions, code revision, format and limitations, plus SHA-256
checksums. Calibration compression is lossless; its source files are unchanged. Keep the LeRobot
`meta/`, `data/` and `videos/` directories together when extracting the stacking
dataset, then open that directory with a compatible local LeRobot viewer.
A Drive download link is not a dataset endpoint for the web viewer.
Follow [Inspect the shared datasets](viewing.md) for extraction checks and
the local browser-viewer setup.

The calibration collection is a separate reproducibility download, not a
LeRobot export. Its fitted bundle is already included in the source repository;
downloading the capture sessions is only necessary for inspecting or refitting
the measurements. A future lab copy should retain both downloads and update
these links if storage ownership changes.

## August 25 demonstration export

The five selected demo runs have been converted locally and reloaded for
verification: **5 episodes, 8,272 frames, about 697 MB**,
at 15 FPS. Original recordings remain intact. The [Drive downloads](#dataset-downloads)
are separate from the source clone, which does not include the dataset videos.

| Episode | Source run | Exported frames |
|---|---|---:|
| 0 | `stack_20260825T200631Z` | 2,307 |
| 1 | `stack_20260825T200920Z` | 1,781 |
| 2 | `stack_20260825T201125Z` | 1,371 |
| 3 | `stack_20260825T201322Z` | 1,641 |
| 4 | `stack_20260825T201700Z` | 1,172 |

The five source run folders occupy about 31.22 GB, mostly uncompressed MCAP.
That is their raw recording size, not the converted dataset size. RGB and native
depth alone produce roughly 3 GB per minute at the recorded resolutions/rates.
Public dataset releases are intended to contain the selected LeRobot exports;
raw evidence remains separately retained.

## Inspecting an exported dataset

<figure class="research-video">
  <video controls playsinline preload="none" poster="../_static/g1-lerobot-viewer-walkthrough.jpg" width="1802" height="1162" aria-label="Walkthrough of a G1 dataset in the LeRobot viewer" aria-describedby="viewer-demo-caption">
    <source src="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-lerobot-viewer-walkthrough.mp4" type="video/mp4">
    Your browser cannot play this video. Use the download link below.
  </video>
  <figcaption id="viewer-demo-caption">Walkthrough of the local G1 dataset: RGB/depth, joint and pressure traces, annotation tools, 3D replay, statistics, episode frames and action diagnostics. The displayed 33 episodes and 63,924 frames describe this export; they are not a count of successful manipulations. Silent, 56 seconds.</figcaption>
  <p class="video-download"><a href="https://github.com/sri299792458/g1-research-docs/releases/download/media-2026-09-21/g1-lerobot-viewer-walkthrough.mp4">Download the dataset-viewer walkthrough (MP4)</a></p>
</figure>

Start with a known episode and compare the visible movement with its named
state and command channels. The 3D replay helps inspect pose changes; return
to RGB and the source recording when judging object contact or placement.
Then inspect the conversion report for dropped samples, timing bounds and
completion status. A functioning viewer is useful inspection tooling, but it
does not replace those source checks.

The walkthrough includes local viewer extensions and a larger export. The
[public-viewer instructions](viewing.md) describe the reproducible RGB/depth
inspection path for the five downloadable demo episodes.

## Calibration captures and LeRobot

The August 12 calibration data used by the stacking bundle is stored differently:
two sessions contain 735 lossless PNG images and image/state/detection metadata.
Together they occupy about 1.54 GB: 884 MB of PNGs and 657 MB of JSON. These
stationary capture bursts are not the continuous MCAP inputs expected by the
stacking converter.

LeRobot can represent images and measured states, but this collection needs a
separate exporter. A reproducible calibration export must preserve original
pixels and timestamps, measured joints, detected corners, camera/target geometry
and pose grouping. Its encoding must be checked by exact image reload and
calibration-data comparisons; the stacking export's lossy RGB/depth settings
are not a calibration-preserving recipe. Such a calibration export has not yet
been produced. The existing calibration bundle is already included with the code.

## What was adapted from SPARK

The recorder adapts the separate-process recording approach from
[SPARK's `data_pipeline/record_episode.py`](https://github.com/RPM-lab-UMN/spark-data-collection/blob/be284c2f8138f383d260526f68613c7a28d364d4/data_pipeline/record_episode.py).
For the G1, the work adds the robot/hand/camera topic contract, recording through
control cleanup, completeness checks and the named state/action conversion.

| Artifact | Use it to answer |
|---|---|
| Raw MCAP and ROS metadata | What images, measured states and commands were recorded, and when? |
| Task JSON and planner logs beside the bag | Which scene, grasp, route, contact decision and cleanup outcome did the program use? |
| `raw_episode/episode_manifest.json` | Did the writer exit cleanly and record every required stream with the expected type? |
| LeRobot dataset and conversion report | Which aligned samples were exported, dropped or encoded for downstream use? |

The raw topic contract does not include the task's inferred object poses or
planner decisions. Keep its companion JSON/logs when diagnosing those choices;
playing a bag or an encoded video alone cannot recover every decision.

The conversion implementation is available on demo `main`. The recorder links
below use September code because this page also describes the expanded standing
profile. The [demo recorder](../reference/code-index.md#code-demo-recorder) remains
the reference for the August runs.

## Record the full lifecycle

The current full contract contains 14 topics:

| Streams | Count | Why retain them |
|---|---:|---|
| Body LowState, secondary IMU | 2 | Measured body and torso state |
| Body command: lowcmd or arm_sdk | 1 | Actual command intent and gains |
| Left/right hand state and command | 4 | Measured fingers, pressure and commanded close |
| RGB image and CameraInfo | 2 | Original visual evidence and projection model |
| Native depth and CameraInfo | 2 | Original depth evidence and geometry |
| Camera gyro, accelerometer, static TF | 3 | Camera motion and sensor relationships |

ROS topic names and the Unitree `rt` DDS partition are separate naming layers.
The recorder must verify expected message types and nonempty subscriptions;
an apparently valid bag that contains only camera topics is not a robot episode.

Recording starts before command ownership and continues through return/fault
cleanup. The tabletop episode begins after SPACE; the later standing profile
records before its motion authorization boundary. Retained stack sessions
produce a separate bag for each task while keeping the control process alive.
The six-topic September 5 standing bag predates full camera recording, so its
failed views cannot be reconstructed afterward.

### Reuse the recorder in another task

Keep the recorder owned by the task coordinator, with this order:

1. Select the profile and output directory; retain source/model/configuration
   provenance with the episode.
2. Start the external writer and require its subscriptions before acquiring
   command ownership.
3. Keep it alive during motion, rejection, return and fault recovery.
4. Resolve ownership, then stop the writer and inspect the completion manifest.

The August body command is ROS `/lowcmd`; the later standing profile uses
`/arm_sdk`. Both retain `/lowstate`, `/secondary_imu`, both Dex3 state/command
pairs, the color/depth image and CameraInfo pairs, raw camera gyro/acceleration
and `/tf_static`. Copy the selected source's `TopicSpec` definitions, not just a
list of topic names: type, required status and timestamp meaning are part of
the contract. See [source entry points](#follow-the-code).

Save application decisions alongside the bag. A new task's inferred object
pose, selected action or rejection reason will not appear in raw state topics
unless the application records it explicitly.

## Keep writing away from control

An external writer stores uncompressed MCAP. Per-task JSON records interpretation,
phase and outcomes separately. PNG encoding, JSON serialization and filesystem
sync previously interrupted control and were moved out of its process.

Camera/ROS resources shut down only after robot ownership is resolved. The
recorder then receives SIGINT and must finish with successful exit, metadata
and its message contract intact. An incomplete bag remains marked incomplete;
a directory existing on disk is not enough.

RGB at 1280 × 720 × 15 Hz uses about 39.86 MiB/s before overhead. Native depth
adds about 8.9 MiB/s, giving roughly 2.9 GiB/min for these streams. Nine synthetic
15 s trials observed control gaps below 10 ms, which is useful load testing
but not a hard timing guarantee for hardware operation.

The skip-camera profile removes four image/CameraInfo topics while retaining
gyro, acceleration and static TF. Perception may still run. Use it only when
the missing image evidence is an intentional recording choice.

### Check recording load without the robot

After preparing the [control and MCAP environment](../start/setup.md#tabletop-control-planning-and-recording),
the synthetic benchmark compares no recording, state/command recording and
state/command plus RGB recording:

```bash
./tools/g1_recording_benchmark.sh --duration-s 15 --trials 3 \
  --output-root /path/to/new-benchmark-output
```

The [benchmark wrapper](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tools/g1_recording_benchmark.sh)
uses localhost-only DDS, default domain 221 and synthetic benchmark topics.
Inspect the timestamped `report.json` for loop gaps and recording results.
This tests software/storage load with synthetic messages; it does not test
real sensor transport, the complete depth workload or hardware recovery.

## Time and completeness

MCAP receipt, ROS headers and sensor ticks are not the same clock and do not
automatically identify exposure time. Analysis maps producers independently.
Retain image/CameraInfo pairs and the device profile, including native unaligned
depth. Do not silently treat RGB-aligned and native depth as interchangeable.

The September 7 calibration record illustrates the value of completeness:
49 holds, 343 retained images, 686 marker observations and a 14-topic,
2,298,946-message bag survived a failed finger-restoration cleanup. Capture
success, task success and normal control release remain separate fields.

## The LeRobot representation

The inspected converter targets LeRobot v0.6.1 in a separate Python 3.12 CPU
environment. Its 15 Hz timeline follows actual RGB samples. It carries:

- 43 measured joint positions, velocities and efforts: 29 body plus two seven-joint hands;
- 43-joint command position, velocity, feedforward, `kp` and `kd` arrays;
- 216 raw pressure slots and four Unitree IMUs;
- RGB and a derived representation of native depth.

The [Dex3 pressure sensing chapter](../sensing/pressure.md) explains active
slots, untouched baselines and taxel locations for interpreting the raw
pressure counts.

State age is bounded at 50 ms. Commands use zero-order hold with a 500 ms age
bound corresponding to the watchdog contract. Terminal timeout packets with
zero blend weight are excluded from training actions. RGB/depth skew is
bounded, and missing/stale samples produce explicit omissions and diagnostics,
not silent repeated observations.

The recorded depth scale is 0.001 m per unit. Training depth encoding uses a
0.15–2 m range and is explicitly lossy. Across 13 retained episodes and
26,191 depth frames, about 8.046 billion pixels were examined: none fell below
the lower bound and 0.1205% were above 2 m under the documented counting policy.
The encoded dataset cannot replace arbitrary future raw-depth analysis.

## Conversion and retention

Use the conversion environment described by
[`setup_lerobot_conversion.sh`](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tools/setup_lerobot_conversion.sh),
separate from control and planning. The script expects local SPARK and LeRobot
checkouts, checks the pinned LeRobot revision and creates a Python 3.12 CPU
virtual environment in the SPARK checkout. Set `G1_TABLETOP_SPARK_ROOT` and
`G1_TABLETOP_LEROBOT_ROOT` for your directories; its defaults are lab-specific.
Review the setup script before using it with an existing environment.

After setup, the source wrapper accepts one retained run at a time:

```bash
./tools/convert_raw_to_lerobot.sh /path/to/retained-run \
  --dataset-id g1-stacking-study \
  --published-root /path/to/new-export-root
```

The output is under the chosen root and dataset ID. On successful conversion
and reload, the tool prints the dataset episode index, published frame count,
`status=verified` and its artifact directory. Inspect those reports and replay
an episode before using the export. This command is a source-checked example;
it was not run against a new recording while editing the guide.

Indexing selects aligned messages before decoding images. This avoids decoding
frames that will be discarded. Preserve numerical alignment and reload checks
when optimizing this stage; a faster encoder does not establish an equivalent
state/action dataset.

Completed tasks are the default conversion input. Including failed runs needs
an explicit override and visible outcome labels. Appending a dataset is an
offline operation, not resuming robot execution.

The source has guarded raw-deletion support only after successful reload and
a `lerobot_replacement.json` receipt. Deletion remains an explicit operator
decision. For lab continuity, retain original evidence needed for calibration,
failure analysis and claims independently of a compact training export.

Evidence: tabletop recording contract, conversion notes and retained episode
audits. [Source identities](../reference/sources.md), [media/storage policy](../reference/media.md).

## Follow the code

| Implementation concern | Code entry point | Responsibility |
|---|---|---|
| Topic contract | [raw_episode_recording.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/raw_episode_recording.py) · `tabletop_raw_topics` (September branch) | Choose the expected streams for the recording profile. |
| Writer startup | [raw_episode_recording.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/raw_episode_recording.py) · `RawEpisodeRecorder.start` (September branch) | Require the recorder to subscribe before continuing. |
| Completion audit | [raw_episode_recording.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/src/g1_dex3_tabletop/raw_episode_recording.py) · `RawEpisodeRecorder.stop` (September branch) | Check exit, MCAP metadata, message types and required nonempty streams. |
| Offline alignment | [lerobot_conversion.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/src/g1_dex3_tabletop/lerobot_conversion.py#L259) · `index_and_align_episode` | Select state and active commands relative to actual RGB samples. |
| Numeric representation | [lerobot_conversion.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/src/g1_dex3_tabletop/lerobot_conversion.py#L573) · `build_numeric_frame` | Construct the named joint, command, pressure and IMU arrays. |
| Dataset export | [lerobot_conversion.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/src/g1_dex3_tabletop/lerobot_conversion.py#L774) · `convert_episode` | Write the derived episode and its conversion evidence. |

A complete bag can contain a failed task or abnormal cleanup. An incomplete bag remains available as evidence but must not be relabelled complete because conversion or video playback works. Preserve the original bag when using the derived dataset.

## Checks and evidence to inspect

[test_raw_episode_recording.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/59c21b1388c636176dea67ea7ed3e253f8510783/tests/test_raw_episode_recording.py) (September branch) includes missing-subscription and empty-required-topic cases. [test_lerobot_conversion.py](https://github.com/sri299792458/g1-dex3-tabletop/blob/7400aff201c2f73ef2a64e546d72bd66cbe87fd6/tests/test_lerobot_conversion.py) checks vector/schema agreement, terminal-command exclusion and depth-bound consistency. The September 7 bag described above demonstrates successful evidence retention through a failed restoration.
