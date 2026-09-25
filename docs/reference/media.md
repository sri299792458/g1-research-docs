# Media catalog and storage

Keep selected images, diagrams and captions in this repository. Keep large
videos in versioned release assets, and original recordings in backed-up lab
storage. The goal is for a future maintainer to understand an asset, locate its
source and replace its host without rewriting the explanation around it.

The selected stacking dataset and calibration captures use separate
Google Drive downloads, listed on the [dataset page](../data/recording.md#dataset-downloads).
They are not embedded video assets. Keep a versioned README and checksums with
each download, and verify access without the owner's signed-in account before
adding its link to the guide.

## Included figures

The following original PNGs were visually inspected and copied unchanged from
`g1-aprilcube-demo`; identical copies are retained in the consolidated
`main` at `2b7274b11f1862ebfcd05b48ff678d995e55269e`:

| Stable ID | Figure | What it shows |
|---|---|---|
| `dex3-descriptor-states` | [Descriptor audit](../manipulation/grasp-atlas.md) | Rendered right/left open, half and closed states with learned descriptor proxy boxes |
| `u-support-orientations` | [U supports](../manipulation/assembly.md) | Six geometric support orientations; printed counts are geometric candidates |
| `assembly-scene` | [Assembly scene](../manipulation/assembly.md) | A rendered G1/table/part planning scene, not a photograph |

Two additional CAD views are copied unchanged from the fixture repository at
`f295def18bd936031fba325d4e8bdfc71fea671a`:

| Stable ID | Figure | What it shows |
|---|---|---|
| `dex3-dorsal-mount-cad` | [Wrist-marker placement](../perception/targets.md#dex3-dorsal-markers) | Right-hand plate, screw arrangement and support pads; a CAD view, not a physical fit measurement |
| `g1-torso-v7-cad` | [V7 torso structure](../perception/targets.md#torso-charuco-carrier) | Modeled crossbars, side plates and board; the assembly still has unresolved fit checks |

The machine-readable catalog is `docs/assets/media.json`. It records exact
source paths, commit, SHA-256, context, review status and caption. The source
PNG labels describe their original experiments; the surrounding chapter
supplies later corrections and scope.

## Photographs and installation figures

Selected photographs from the author's September collection are included in
Git. Their framing, dimensions and decoded pixels are unchanged; embedded
location and other EXIF/text metadata were removed from the publication copies.
The originals and the PowerPoint remain separate source records.

| Stable ID | Where it is used | Source |
|---|---|---|
| `realsense-pc2-usb-ports` | [Camera troubleshooting](../hardware/camera.md) | August 3 phone photograph |
| `realsense-head-pitch-witness-mark` | [Head-pitch reference](../hardware/camera.md#head-pitch-witness-mark) | September 21 photograph; author identifies the white witness mark |
| `g1-wrist-spacing-caliper` | [Wrist-spacing investigation](../calibration/investigation.md#the-46-mm-versus-51-mm-wrist-spacing) | Author-supplied original photograph; caliper display reads 51.38 mm; the chapter distinguishes that reading from verified joint-axis spacing |
| `printed-target-collection` | [Printed targets](../perception/targets.md) | September 21 photograph of cubes, wrist carrier and board |
| `cushioned-chair-reference` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | Chair with its cushion; September 21 photograph |
| `rigid-chair-reference` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | Same chair with the cushion removed; author-supplied 850 × 1133 px photograph |
| `chair-support-comparison` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | Both original chair photographs, combined side by side in one figure |
| `dex3-connector-routing` | [Hand fitting](../hardware/robot.md#fitting-the-hand) | `Dex3 Hands.pptx`, slide 7, `ppt/media/image11.png` |
| `dex3-hand-seated` | [Hand fitting](../hardware/robot.md#fitting-the-hand) | Same slide, `ppt/media/image10.png` |
| `dex3-cable-routing` | [Cable routing](../hardware/robot.md#cable-routing-and-repeated-swaps) | Slides 4 and 8, `ppt/media/image2.jpg` |
| `dex3-wrist-fasteners` | [Hand fitting](../hardware/robot.md#fitting-the-hand) | Slide 6, `ppt/media/image5.jpg` |

The installation figures now retain the features indicated by the slide
annotations, with overview photographs, enlarged details and numbered callouts.
They identify hardware and the recorded fitting sequence; the electrical pinout
and complete power-isolation procedure still need author review.

## Annotated hardware figures

Use an overview to locate a feature and a close-up when the detail would be too
small at normal page width. Keep each caption and instruction in Markdown below
the figure. The hardware pages use editable SVG overlays, so labels, circles
and leader arrows stay separate from the original photo pixels.

The layouts are in `docs/assets/hardware-figures.json`. Each records its
source image hashes, panel crops, feature positions and source photograph or
slide. The Dex3 features were checked against rendered slides 6–8. Their
presentation adapts the slide callouts into rings and numbered detail panels;
it is not a screenshot of the whole slide. The head-pitch mark comes from the
author's separately supplied reference photograph.

The chair comparison uses the same layout system to place two cropped
photographs side by side in a single image, with one Markdown caption. The
author confirms they show the same chair with and without its cushion. Both
complete chairs remain visible; the crops remove excess background without
stretching either photograph.

To adjust a figure, edit its layout and regenerate it:

```bash
python3 tools/build_hardware_figures.py
python3 tools/build_hardware_figures.py --check
```

This standard-library helper uses the checked-in publication photographs;
neither PowerPoint nor LibreOffice is required. It verifies their hashes before
rendering. SVGs embed those photos, so a downloaded SVG is self-contained.
Review feature placement, magnification, alt text and the Markdown caption on
desktop after a change. The CI check catches stale generated figures.

## Embedded demonstrations

The [September media release](https://github.com/sri299792458/g1-research-docs/releases/tag/media-2026-09-21)
hosts the publication videos. Each player has native controls, a local poster,
a descriptive caption and a separate download link. Videos load on request
and do not autoplay. All publication copies are silent; the original seat,
physical-stacking and calibration movies retain audio that has not been
reviewed here.

| Stable ID | Chapter | Evidence shown |
|---|---|---|
| `g1-physical-cube-stacking` | [Pickup and stacking](../manipulation/tasks.md#physical-demonstration) | Physical pickup, stack, release and hand withdrawal; no software handback display |
| `g1-standing-calibration` | [Calibration capture](../calibration/workflow.md#capture-a-measurement-not-just-a-pose-estimate) | Physical pose sequence with wrist markers; no fit or cleanup result displayed |
| `dex3-tactile-rviz-demo` | [Tactile sensing](../sensing/pressure.md#seeing-the-pressure-display) | Changing taxel visualization; not calibrated force |
| `dex3-simulated-retention-demo` | [Grasp qualification](../manipulation/grasp-atlas.md) | Rendered Isaac/PhysX retention replay |
| `curobo-stack-plan-demo` | [Stacking plan](../manipulation/tasks.md#plan-visualization-and-recorded-outcomes) | Rendered geometric phases through placement |
| `mujoco-rviz-short-demo` | [MuJoCo](../simulation/mujoco.md#demonstrations) | Side-by-side RViz and simulation |
| `g1-cushion-seat-setup` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | Seated robot, harness, targets and arm movement |
| `g1-lerobot-viewer-walkthrough` | [Dataset inspection](../data/recording.md#inspecting-an-exported-dataset) | Images, traces, 3D replay and diagnostics |

The release's checksum file identifies the hosted copies. The catalog records
each original hash separately from the publication hash, along with the
encoding recipe and poster timestamp. The full visual duration is retained;
the physical videos are compressed for web playback, not sped up. The viewer's
odd source height is padded by one row for H.264 encoding.

## Other available MuJoCo videos

These assets are published in the existing
[G1Pilot July 1 release](https://github.com/sri299792458/g1pilot/releases/tag/mujoco-demo-media-2026-07-01):

- [RViz and arm demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-rviz-arm-demo.mp4), 12,915,563 bytes;
- [Dex3 open/close demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-dex3-open-close-demo.mp4), 1,649,508 bytes.

Both files were downloaded and hashed for the simulation chapter. Frames at
10% and 70% of each clip were inspected: the arm video shows RViz beside changing
MuJoCo arm poses; the hand video shows terminal open/close commands and different
finger configurations. This is sampled visual evidence, not a continuous
stability or tracking assessment. Neither file has an audio stream.

| Asset | Duration / dimensions |
|---|---|
| Arm demo | 34.28 s / 1856 × 1044 |
| Dex3 demo | 18.49 s / 1824 × 1048 |

Exact hashes are retained in the [machine-readable catalog](../assets/media.json).

These remain download links. Embedded playback of these two originals has not
been tested; the chapter embeds the separate reviewed short clip.

## Author-supplied September media

The collection now contains a nine-slide Dex3 installation deck, five
photographs and eight videos. The originals remain outside this repository.
The [public media catalog](../assets/media.json) retains original/publication
hashes, selected source paths, captions and review limits. Detailed working
reviews remain private.

Photographs, embedded deck images and sampled video frames were inspected.
Audio in the three physical recordings remains unreviewed.
The short MuJoCo clip is a separate file from the July release assets reviewed
above. The deck's linked boot-calibration movie was not present in the folder.

## Recreating a publication copy

The ordinary site build needs only this repository. To prepare media again,
obtain the matching original collection and install `ffmpeg`/`ffprobe`, then
run the standard-library Python helper from the repository root:

```bash
python3 tools/prepare_media.py \
  --source-dir /path/to/originals \
  --video-dir .local/publication-media \
  --asset g1-physical-cube-stacking
```

Omit `--asset` to prepare all assets that have a `preparation` recipe in the
catalog. Unchanged source-repository figures are copied from their pinned
source paths; generated SVG layouts use the separate figure helper above.
The preparation helper checks source hashes,
writes selected images/posters under `docs/assets/`, puts video outputs in the
specified directory and updates their catalog hashes. Review the resulting
diff and playback before uploading. Encoder versions can change file bytes,
so record the new output hash rather than expecting byte-identical transcodes.
Use a new versioned release when changing a published video; retain the old
asset for existing references. The helper never uploads or changes originals.

## Adding a new asset

1. Choose a stable descriptive ID, such as `dex3-extension-routing`.
2. Record the run/date, hardware or simulation context, creator and exact source.
3. Preserve the original in the lab archive. Add a publication copy and its
   checksum to the catalog; keep an accessible caption and meaningful alt text.
4. Explain what the asset establishes, including the phase shown and any
   outcome that happens outside the clip.
5. Check the rendered page on desktop during drafting; mobile presentation is
   deferred to the final review. For video, test playback, controls and the
   download fallback separately.

Use ordinary Markdown images and simple HTML video only when needed. Avoid
autoplay, credentials and expiring signed URLs. Stable, intentionally shared
Drive download links are appropriate for the datasets above. An unedited
failure clip can be more informative than a polished success montage when its
caption explains the first failure and the later correction.

## Ownership during the lab handoff

GitHub Release links are a practical starting host, not the original archive.
The lab copy must either retain access to those assets or copy them to a
lab-owned release and update catalog URLs. A repository copy alone does not
copy another repository's release assets.

Keep raw bags and full media collections outside the documentation build.
Before changing storage, check the host’s current file-size, Pages and LFS rules:
[large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github),
[Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits),
[LFS restrictions](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).
