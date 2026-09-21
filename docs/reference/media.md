# Media catalog and storage

Keep selected images, diagrams and captions in this repository. Keep large
videos in versioned release assets, and original recordings in backed-up lab
storage. The goal is for a future maintainer to understand an asset, locate its
source and replace its host without rewriting the explanation around it.

## Included figures

The following original PNGs were visually inspected and copied unchanged from
`g1-aprilcube-demo` at `f190470742f43101e9a22affaca80554722706ac`:

| Stable ID | Figure | What it shows |
|---|---|---|
| `dex3-descriptor-states` | [Descriptor audit](../manipulation/grasp-atlas.md) | Rendered right/left open, half and closed states with learned descriptor proxy boxes |
| `u-support-orientations` | [U supports](../manipulation/assembly.md) | Six geometric support orientations; printed counts are geometric candidates |
| `assembly-scene` | [Assembly scene](../manipulation/assembly.md) | A rendered G1/table/part planning scene, not a photograph |

The machine-readable catalog is `docs/assets/media.json`. It records exact
source paths, commit, SHA-256, context, review status and caption. The source
PNG labels describe their original experiments; the surrounding chapter
supplies later corrections and scope.

## Available MuJoCo videos

These assets are published in the existing
[G1Pilot July 1 release](https://github.com/sri299792458/g1pilot/releases/tag/mujoco-demo-media-2026-07-01):

- [RViz and arm demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-rviz-arm-demo.mp4), 12,915,563 bytes;
- [Dex3 open/close demo](https://github.com/sri299792458/g1pilot/releases/download/mujoco-demo-media-2026-07-01/g1pilot-mujoco-dex3-open-close-demo.mp4), 1,649,508 bytes.

Release metadata was inspected; video content and embedded playback have not
yet been reviewed for this draft. They are explicit download links, with no
claim of browser streaming or physical-robot footage. Add a reviewed poster
and caption when selecting them for an embedded demonstration.

## Author-supplied September media

The September 21 review covers a nine-slide Dex3 installation deck, three
photographs and six videos. The originals remain outside this repository;
publication copies and hosting have not yet been selected. Review records are
in [the research notes](https://github.com/sri299792458/g1-research-docs/blob/main/research/documentation-media-review.md)
and [the source inventory](https://github.com/sri299792458/g1-research-docs/blob/main/research/documentation-media-inventory.json),
including exact hashes, proposed captions and coverage limits.

| Material | Intended use |
|---|---|
| Dex3 installation deck | Torso/wrist access, 4-pin 300 mm JST-GH extensions, connector routing and repeatable cable slack |
| PC2 port photograph | RealSense USB negotiation troubleshooting |
| Printed-target photograph | Physical cubes, wrist-marker carrier and ChArUco board |
| Cushion-seat video and rigid-chair thumbnail | Physical-support context; not a controlled chair comparison |
| Tactile RViz clip | Spatial pressure visualization |
| Retention and CuRobo clips | Simulated grasp qualification and rendered stacking plan |
| Short MuJoCo/RViz clip | Side-by-side simulation demonstration |
| LeRobot viewer recording | Images, traces, annotations, 3D replay and dataset inspection |

All photographs and embedded deck images were inspected, along with 170 video
frames sampled across the six clips. The seat recording's audio remains
unreviewed. The short MuJoCo clip is a separate file; its review does not change
the metadata-only status of the July release assets above. The deck's linked
boot-calibration movie was not present in the folder.

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
autoplay, personal cloud share tokens and expiring signed URLs. An unedited
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
