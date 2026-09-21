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
| `printed-target-collection` | [Printed targets](../perception/targets.md) | September 21 photograph of cubes, wrist carrier and board |
| `cushioned-chair-reference` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | September 21 chair photograph |
| `rigid-chair-reference` | [Physical support](../hardware/robot.md#physical-support-is-part-of-the-experiment) | Supplied 165 × 220 px chair thumbnail |
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

The four layouts are in `docs/assets/hardware-figures.json`. Each records its
source image hashes, panel crops, feature positions and source photograph or
slide. The Dex3 features were checked against rendered slides 6–8. Their
presentation adapts the slide callouts into rings and numbered detail panels;
it is not a screenshot of the whole slide. The head-pitch mark comes from the
author's separately supplied reference photograph.

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

| Asset | Duration / dimensions | SHA-256 |
|---|---|---|
| Arm demo | 34.28 s / 1856 × 1044 | `6c7988b5e4a8e6310b4a687ef6ffb45a3ece6aae6d01292dfe37e54d4f3cb194` |
| Dex3 demo | 18.49 s / 1824 × 1048 | `34a55a030a903bd5ff19a98ec0b569f5fd1afd60c56cdb62ccb2a50db89a3d48` |

These remain download links. Embedded playback of these two originals has not
been tested; the chapter embeds the separate reviewed short clip.

## Author-supplied September media

The collection now contains a nine-slide Dex3 installation deck, five
photographs and eight videos. The originals remain outside this repository.
The [public media catalog](../assets/media.json) retains original/publication
hashes, selected source paths, captions and review limits. Detailed working
reviews remain private.

All photographs and embedded deck images were inspected, along with 326 video
frames sampled across the eight clips and selected full-resolution stacking
frames. Audio in the three physical recordings remains unreviewed.
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

Omit `--asset` to prepare every selected asset. The helper checks source hashes,
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

GitHub currently blocks regular Git files over 100 MiB; Pages sites have a
1 GB published-size limit, and Git LFS is not supported directly by Pages.
These constraints reinforce keeping raw bags and full media collections out
of the documentation repository. Check the current limits when changing hosts:
[large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github),
[Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits),
[LFS restrictions](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).
