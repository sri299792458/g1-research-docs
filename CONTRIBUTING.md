# Maintaining and extending the documentation

The purpose of this repository is to make G1 research work understandable and
reusable by future lab members. Favor plain Markdown, clear file names, relative
links within this repository, and source references that another person can
follow. The website technology and final chapter structure remain open.

## Make changes that another researcher can assess

1. Read the relevant page and its evidence before editing. The source inventory
   records what has been read and which material still needs examination.
2. Keep a change focused on one procedure, result, correction, or topic. Explain
   what changed and why in the commit or pull request.
3. State prerequisites and expected observations for procedures. Preserve the
   reason for a step when a previous failure explains it.
4. Distinguish proposed work, software inspection, offline tests, simulation,
   physical experiments, and deployed behavior. Link the relevant source/run
   and record the date and hardware/software configuration where available.
5. Preserve corrections and unsuccessful experiments that explain the current
   procedure. Historical next steps are not automatically current recommendations.
6. Add a dated entry to `running_notes.md` for material decisions or corrections.
   Update the source inventory when reading coverage changes.

Before submitting, check local links, run `git diff --check`, and review rendered
Markdown. Once a site build is added, document its exact preview/build command
here so every maintainer can use the same workflow.

## Source references

Use a commit-pinned public URL when that exact source is available. Some early
research relies on local notes and uncommitted experiment records. Identify those
as local evidence and retain their file hashes; do not substitute a GitHub link
that points to different contents.

`research/source_snapshot.json` identifies source repositories by directory name,
plus source-file paths, commits, and hashes. Machine-specific checkout locations
belong in ignored `.local/` files. Those locations are useful during research but
are not required to read this repository's public notes.

Check which parts came from upstream projects and which changes were made during
the summer work. A dependency's presence does not establish original authorship.

## Media

Keep selected, optimized images and diagrams with the pages that use them. Larger
videos can be published as versioned Release assets; retain original media in
backed-up lab storage. Record the subject, date, simulation/physical context,
source experiment, published location, and checksum as assets are incorporated.

Describe what a photo or video establishes in its caption. Check embedded
playback as well as download links when the site is built. Do not commit raw
recording directories or credentials used to access storage.

## Personal repository and later lab copy

Development currently takes place in the local Git repository. The first remote
will be in the author's personal GitHub account; connecting it is deferred and
does not block documentation work. When the summer documentation is ready:

1. Tag the completed summer version and record its date and scope.
2. Create the lab copy with Git history and attribution preserved.
3. Confirm that media, source references, site configuration, and build instructions
   work from the lab copy. Account for externally hosted assets during the handoff.
4. Link the personal portfolio version and the lab's maintained version from their
   respective READMEs. Record where ongoing fixes and contributions should go.
5. Date later extensions and retain the original summer tag as a stable reference.

The lab repository, final tag, and publication workflow have not been created.
This records the agreed ownership plan without fixing the final site structure.
