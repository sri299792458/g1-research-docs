# Documentation running notes

## 2026-09-13 — Purpose, scope, and collaboration established

### Author's intent

The documentation should be a useful resource for other people who want to work
on the G1. The summer work explored the robot's capabilities and limitations and
built internal tools and safety procedures for research on top of the SDK.
Successful documentation should enable someone else to build on that work.

The author emphasized that generating code is easier than recovering the
judgment earned through iterations on physical hardware. The running notes must
be read line by line and understood deeply; the final codebase alone does not
explain the development process, failures, and physical results.

### Explicit scope and process decisions

- Cover all summer G1 work, not only `g1-dex3-tabletop`.
- Work back and forth with the author; do not write the documentation in one shot.
- The author is still considering how to organize it. No table of contents is accepted.
- Maintain our own `running_notes.md` and Git repository.
- The author can provide images and videos where needed.
- The Spark site is an example reference for documentation style and depth.

### Work described by the author — inventory, not proposed chapters

- Practical Dex3 installation, including the JST extension cables bought for it.
- 3D-printed AprilCubes for object-pose estimation.
- Calibration of the head-mounted RealSense using 3D-printed Dex3 wrist marker mounts.
  The head pitches manually; it is not motorized. Inaccurate G1 forward kinematics
  made calibration difficult. Specific findings must be taken from the evidence
  and the calibration ledger rather than generalized to every error source.
- GraspGen-X for offline grasp proposals.
- Substantial G1 control and safety pipeline development.
- CuRobo trajectory planning for cube stacking.
- Exploration of Dex3 pressure sensors.
- An initial MuJoCo G1 digital twin, motivated by the proprietary default walking
  controller. Its implemented and validated scope remains to be read from sources.
- Extension of SPARK-style logging to G1.

### Work started

Created `g1-research-docs` as a separate local Git repository on
`main`. This is an internal documentation workspace, with no site publication or
reader-facing chapters yet. No source-repository files or Git state were changed.

The initial inventory found 1,328 lines of G1Pilot notes, 1,864 lines of prototype
notes, and 7,403 lines of tabletop notes. A further 126-line AprilCube note file is
present under the tabletop repository's `third_party` directory.

The prototype's lines 2–1,864 have identical line contents to tabletop lines
359–2,221. This is inherited history, not a second independent experiment record.
Record shared coverage explicitly when read; do not double-count results.

Some sources contain uncommitted work, including the tabletop running notes.
Record local file hashes as well as commit IDs so later citations describe the
material actually read. The source snapshot is an inventory, not a backup.

The prior conversation reviewed the Spark site's structure, representative
procedures, design pages, and fixture documentation, plus the G1 calibration
ledger and selected existing documents. Those reads do not constitute a complete
reading of the source running notes. Exact new coverage is maintained in the
source inventory.

### Open items for later discussion

- Exact summer date boundaries: located notes extend into September; inclusion
  in the historical narrative is not yet settled. Later corrections still matter.
- Location and validation scope of the initial MuJoCo digital twin work.
- Precise Dex3 installation and JST cable details, with photographs where useful.
- Which demonstrations, photos, and videos should illustrate individual lessons.
- Reader entry points and documentation organization, after source understanding.

## 2026-09-13 — G1Pilot running notes read completely

Read all 1,328 lines sequentially, in four contiguous ranges. Detailed findings,
source ranges, reported verification, and limitations are preserved in
[`research/g1pilot-reading.md`](research/g1pilot-reading.md).

The reading adds early environment, SDK integration, frame/model, and navigation
work to the summer inventory. It contains 38 issue dispositions and physical
LiDAR/TF and camera-access evidence. Do not confuse offline visualization with
the separately mentioned initial MuJoCo digital twin.

Three examples worth discussing when shaping the eventual documentation:

- The physical PC2 USB path resolved the camera-access failure; the working ZMQ
  stream and unresolved browser playback were different observations.
- Repeated messages can replay a stale autonomous command. The mux fix had a
  specific scope and did not substitute for a lower-level watchdog.
- An apparently plausible solver time-scaling change was rejected after checking
  that the solver already returned a per-step increment.

The early arm emergency helper, live-state initialization change, and balancing
fixes must retain their recorded limitations. Later hardware commissioning and
operator corrections govern any future executable procedure.

Asked the author where to find the initial MuJoCo digital twin repository/folder
and notes. No answer was available when this entry was written. The question is
about locating existing work, not approval to create or run a simulator.

The initial Git commit is `a0f1ed9`. Commits in this new workspace use the explicit
agent identity `Codex <codex@localhost>` because no global user identity was
configured. Global Git configuration was not changed.

Remaining sequential reading is recorded as pending in the source inventory.
No reader-facing chapter, final table of contents, or website has been drafted.

Documentation checks: all local Markdown link targets exist, the source snapshot
parses as JSON, all nine snapshotted source files still match their initial
SHA-256 hashes, and `git diff --check` passes. These are documentation checks;
none independently validate the robot software discussed in the source notes.

## 2026-09-13 — Author supplied the remote G1Pilot MuJoCo source

The author answered the digital-twin source question with
`https://github.com/sri299792458/g1pilot/tree/dev`.

The local checkout ends at `72acc80` (June 21). The linked branch is at
`6b5af59` (July 1), two commits later, with `72b820f` (June 30) between them.
Those commits add the locked-waist MuJoCo/OpenHomie backend and Dex3 integration.
The original local scan did not cover this later code; its limited scope is now
explicit in both reading files and the source inventory.

Created a separate clone at `.sources/g1pilot-dev` inside this documentation
workspace and ignored `.sources/` in Git. Retrieved history there to inspect
the two added commits and the disposition of the notes. The source working
checkout and its existing local changes were left untouched.

The July 1 commit removes `running_notes.md` and ignores local notes. Its parent
contains the exact same 1,328-line log already read (SHA-256
`9cc8316d60d8e83f7fb68d6bf5b1bf5e9d9913eac62c1a3df91d9ea6a5378f6a`).
No additional MuJoCo iteration record was recovered from that tracked file.
Asked whether later notes exist on another machine or in another folder.
That follow-up remains unanswered at this entry.

Read the remote README, simulation modules, launch/environment script,
diagnostic, and model generators completely. Saved the findings and source
boundaries in [`research/g1pilot-mujoco-reading.md`](research/g1pilot-mujoco-reading.md)
and commit/file provenance in
[`research/g1pilot-dev-source.json`](research/g1pilot-dev-source.json).

The substantive architecture is a MuJoCo plant that owns physics and OpenHomie
lower-body policy execution while accepting G1Pilot arm/Dex3 intent over
Unitree-style DDS contracts. It models the locked waist and both seven-joint
hands. Inspecting the generated XML established 41 actuators and 89 sensor
elements; this was an XML parse, not a simulator run.

Located the July 1 release's RViz arm-control video, Dex3 open/close video, and
reachability-map asset through the README and release API. Metadata was checked;
media and map content have not been reviewed. Record these as available assets,
not newly verified physical/simulation performance.

The source reading also records model-shape differences in an older diagnostic
path and interface limits to reconcile before writing runnable guides. No code
fix, policy run, hardware command, or model-generation run was performed.
The prototype/tabletop log readings remain pending; no final organization or
reader-facing chapter has been drafted.

## 2026-09-13 — MuJoCo scope confirmed; media storage discussed

The author answered the follow-up about later MuJoCo notes: "no only that much
was done". The available implementation and demos describe the initial work;
there are no additional notes to recover. Closed that source-location question
in the reading notes and inventory. Do not keep requesting missing records or
infer a larger completed simulation-validation program.

The author then asked how media should generally be stored for the documentation.
This is a design discussion, not an instruction to upload, migrate, or publish
assets. The recommendation offered is:

- Keep optimized publication images, diagrams, video posters, and captions with
  the documentation source so page edits and their visual evidence travel together.
- Keep larger demonstration videos in versioned GitHub Release assets initially;
  the existing G1Pilot media release provides a working organizational precedent.
  Use explicit release tags and filenames. Test actual embedded playback before
  choosing Release URLs as the site's playback source; download distribution
  and a streaming player are different requirements.
- Preserve original photos/videos in backed-up, lab-owned storage, separately
  from the selected and compressed publication copies.
- Track a small media index in Git containing each item's date, description,
  simulation/physical context, source run where available, original location,
  public URL, and checksum. This index is proposed, not yet created.
- Prefer a lab-owned published-media location for continuity. The exact host,
  ownership, naming conventions, and embedded-player choice remain undecided.

Reference-site check: Spark's homepage currently embeds an MP4 from its own
`data_pipeline/docs/assets/videos/` directory and keeps annotated images under
`assets/images/`. That is feasible for a small curated media set; it should not
automatically become storage for every raw recording.

Official GitHub documentation checked September 13:

- [Regular Git file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github):
  files above 100 MiB are blocked; large binaries can be distributed with Releases.
- [Release quotas](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases):
  up to 1,000 assets per release, each under 2 GiB.
- [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits):
  published sites may be no larger than 1 GB.
- [Git LFS limitations](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage):
  GitHub documents that LFS cannot be used with GitHub Pages sites. No LFS-based
  site workflow is proposed here.

No media was uploaded, copied to a public host, or altered during this discussion.

## 2026-09-13 — Public personal repository and future lab maintenance agreed

The author emphasized ease of maintenance and extension by future lab members.
They requested that documentation start as a public repository in their personal
GitHub account. After completion, the lab's GitHub organization should receive a
copy for continued development. The author wants to retain their personal copy
for their resume/portfolio.

Recorded this ownership plan in the README and `CONTRIBUTING.md`. Preserve Git
history and attribution during the future handoff and tag the completed summer
version so subsequent lab extensions remain distinguishable. Exact organization
repository, tag, site technology, and final documentation navigation remain open.

Prepared the repository for public readers: added the project introduction and
maintenance guidance, replaced broken sibling-checkout links with exact public
references or explicitly labeled source paths, and made source provenance
portable. Absolute checkout locations now live in ignored
`.local/source_locations.json`; source-file hashes and commit IDs are unchanged.
Earlier local setup commits remain historical records; no Git history was rewritten.

GitHub's connected account is confirmed as `sri299792458`. The intended name is
`g1-research-docs`, matching the existing workspace. A repository lookup returned
404. The available GitHub connector can manipulate files, commits, and refs in
existing repositories, but exposes no repository-creation action. This shell has
no GitHub CLI, configured Git credential helper, or GitHub token environment.
Publication therefore requires the author to create the public repository first.
The documentation is prepared locally; no public repository or site has yet
been created through this session. No additional permission to publish is needed:
the user's request already supplies it.

Preparation checks passed: all relative Markdown links resolve within the
repository, research JSON parses, all nine original source hashes still match,
and `.local/` plus `.sources/` are excluded from the public candidate. A targeted
scan of tracked history and current files found no GitHub token or private-key
patterns. `git diff --check` passes. These checks prepare the files for the
requested publication; they are not a claim that a remote upload has occurred.

## 2026-09-13 — Remote connection deferred; continue locally

The author instructed: "just create locally we can connect to remote later".
The local repository already exists, so retain it and continue the collaborative
documentation work there. GitHub repository creation, authentication, and remote
connection are deferred; no user action on them is pending or blocking progress.

The eventual personal portfolio repository and later lab copy remain the
ownership plan. Updated the README, contribution guidance, and agent continuity
instructions to reflect local development. No remote is configured. All prior
reading records, source hashes, and commits are retained.

## 2026-09-13 — Installation discussion deferred; short opening draft started

The author declined starting with the physical setup/Dex3 installation interview,
preferring to build momentum and return to those details later. Keep that topic
in scope, but do not repeat the JST-extension question as the immediate next step.

Prepared a short opening draft in `docs/index.md` from the author's already stated
motivation and summary of the summer work. This gives the discussion a concrete
piece of prose to refine without requiring more hardware recollection first.
The overview is an assistant-proposed starting point, not an author-approved
chapter order. The draft has not yet been reviewed or approved by the author.

The first-person voice is proposed for the summer introduction; it is not a
decision about the voice of all future technical pages. No detailed procedure,
experiment result, or calibration conclusion was inferred from unread source
logs. Prototype/tabletop sequential reading remains pending. No site framework,
final navigation, or remote publication was added.

## 2026-09-13 — Complete first draft authorized

The author changed the writing process: prepare the complete first draft now,
then review and deepen particular sections together. They explicitly allow the
time needed for a difficult, thorough task. This supersedes the earlier
restriction against drafting the complete documentation in one pass.

Continue locally with Git. Read the remaining source logs fully, reconcile later
corrections, and produce a navigable documentation draft with practical guides,
design explanations, experimental results, and maintenance guidance. Mark missing
installation details, media, and unresolved evidence instead of inventing them.
No new hardware experiment or remote publication is part of this request.

## 2026-09-13 — Complete primary-source reading and first-draft site

Read all tabletop 7,403 lines and the identical inherited prototype block, AprilCube126 lines, plus newly located public grasp-demo3,209 lines. Combined with G1Pilot1,328 already read, all located primary running notes are covered. Detailed reading records preserve retractions, physical/offline distinctions and current calibration limits. Added MkDocs Material navigation and initial chapters, using an isolated docs venv and frozen requirements. System venv lacked ensurepip; uv created the environment without system changes. No source repository, robot, or remote was modified. Remaining work: complete every chapter, media/provenance catalog, render/build/link verification, final Git checkpoint.

## 2026-09-13 — Full chapter draft and framework decision

Prepared all 28 reader-facing pages covering the located summer work. Pages
retain failures, current operating boundaries, calibration model limits and
physical versus simulated outcomes. Added three visually inspected, unchanged
grasp-demo PNGs and a media catalog. The two MuJoCo videos remain metadata-only
references; no claim of reviewed playback was added.

The author asked whether MkDocs Material was still a good current choice.
Official sources showed maintenance mode and the Zensical successor, still
labelled alpha. After the author supplied UW Lab and cuRobo examples, inspected
their actual configuration: Sphinx Book Theme and Furo respectively, both with
MyST support. Selected Sphinx + MyST Markdown + Furo, with minimal CSS, a pinned
Python 3.10-compatible environment and a strict build. Removed the temporary
MkDocs configuration and dependencies. Initial strict Sphinx build passed.

The author clarified that using the same framework should not make the work
appear pretentious or imply cuRobo's scope. Treat it as a readable practical
lab guide; use specific results and limits rather than inflated maturity claims.

The author created the public `sri299792458/g1-research-docs` repository and
asked to see the draft there. This supersedes the earlier local-only decision.
Connected origin, found no existing remote commits, and prepared a Pages
workflow. HTTPS/SSH initially lacked authentication. Installed GitHub CLI in
the user's local tools directory after verifying the official archive checksum;
the author completed browser authentication. Confirmed the intended account
and a successful dry-run push. Actual publication and browser checks follow.

## 2026-09-13 — First draft published and verified

Pushed the complete local Git history and first-draft commit `7ed6020` to
`sri299792458/g1-research-docs`. Enabled GitHub Pages with GitHub Actions as
the build source. The first workflow's build passed, but deployment initially
returned 404 because it reached Pages before site enablement completed.
Reran only the failed job after enablement; both build and deploy succeeded.

Live guide: https://sri299792458.github.io/g1-research-docs/

Verification completed:

- All 28 pages pass a strict Sphinx build, with warnings treated as errors.
- All 1,427 local HTML links and asset references resolve.
- Chromium desktop and 390 px mobile checks render the homepage and Mermaid
  diagram; mobile document width equals viewport width. Grasp images load.
- Search returns nine results for `watchdog`; dark mode renders correctly.
- The public site returns HTTP 200; its diagram, assembly figures and search
  work without browser script errors.
- All 11 files in the local source snapshot still match their recorded hashes.
  All three copied PNGs match the media catalog; exact public source links return 200.
- `git diff --check` and the candidate credential-pattern scan pass. Source
  checkouts, local tools, virtual environments and browser artifacts are ignored.

Updated the source inventory to remove stale framework/publication status and
added the June 25 tactile study to the timeline. The author asked whether MkDocs
is simpler for Pages: acknowledged its simpler initial setup and built-in
`gh-deploy`; the configured Sphinx site now has the same edit/push publication
workflow. Retained Sphinx + MyST + Furo as the selected first-draft presentation.

Remaining work is the intended author review, not another automatic research
campaign: installation/JST details, physical media, source-archive handoff,
license/attribution decisions, and deeper section-by-section correction. These
are collected in `docs/reference/review.md`. No robot operation, calibration
experiment, source-repository change or held investigation was performed.

## 2026-09-13 — Diagram tooling review

The author asked whether the flowchart tooling is the best current option,
anticipating frequent diagrams for code explanations. The published site uses
Mermaid 11.12.1 through sphinxcontrib-mermaid. Browser inspection found an
829.742 × 814 viewBox fitted into a 736 × 500 px viewport, making nominal
16 px labels approximately 10 px high. The overview also combines runtime
control with offline analysis, causing long feedback edges.

Reviewed current official Mermaid layout, sequence and state documentation,
D2 layout/install documentation, and draw.io SVG export. Mermaid's current
documentation describes v12 with bundled/default ELK. Recommendation for
discussion: retain editable Mermaid for code flow, sequences and state
transitions; improve sizing and separate questions into focused diagrams.
D2 is an alternative for architecture layouts, with an additional build tool;
precisely arranged physical/frame illustrations can use editable vector sources
and SVG. No renderer upgrade, diagram redesign or site-style change has been
made as part of this tooling question.

References: https://mermaid.js.org/config/layouts,
https://mermaid.js.org/syntax/sequenceDiagram.html,
https://mermaid.js.org/syntax/stateDiagram.html,
https://d2lang.com/tour/layouts/,
https://www.drawio.com/docs/manual/export/export-to-svg/.

## 2026-09-13 — Mermaid adopted for the guide

The author approved Mermaid for the documentation. Recorded it in AGENTS.md
and added `docs/reference/diagrams.md` with flow/sequence/state selection,
ordinary Markdown fence syntax, accessible descriptions and browser checks.
MyST now recognizes ordinary `mermaid` fences, so the same diagram source can
render on GitHub. Explicitly pinned the already tested browser renderer to
11.12.1; this change does not adopt a new renderer major version.

Replaced the mixed homepage graph with two focused diagrams: observation to
planning/execution, and the separate analysis/conversion uses of retained
recordings. Supporting prose preserves the calibration, grasp-library and
watchdog relationships. Removed the fixed 500 px height, used a neutral light
theme and dark theme, made Expand a readable text control, and retained diagram
width through horizontal scrolling on narrow screens and in the larger viewer.

Strict Sphinx build passes for all 29 pages. Checked 1,508 local links/assets
with no missing targets. Chromium checks cover both rendered overview diagrams,
accessible SVG titles/descriptions, 390 px viewport without document overflow,
horizontal scrolling, Expand/Escape, initial dark rendering and switching back
to light. A test probe needed to wait for the replacement SVG during theme
rerender; the corrected check passed. Sequence/state syntax examples also parse
with the pinned renderer. Desktop labels are approximately 18–19 px instead of
the former roughly 10 px. Changes are ready for the existing Pages workflow.
