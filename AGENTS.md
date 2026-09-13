# Documentation collaboration

Read `running_notes.md` and `research/source_inventory.md` before continuing.

- The author now requests a complete first draft, followed by deeper review of
  individual sections. This supersedes the earlier section-by-section drafting
  restriction. Make reasonable structural choices, finish the draft, and keep
  uncertainty and remaining author/media input explicit.
- Preserve the summer work across repositories. The scope is broader than
  `g1-dex3-tabletop` and is intended to help future G1 researchers build on it.
- Read source running notes line by line. Track exact coverage and source hashes;
  heading searches and inventories do not count as completed reading.
- Preserve failures, operator corrections, practical hardware knowledge, and the
  reasons for decisions. Distinguish proposals, offline checks, physical trials,
  and deployed behavior. Historical instructions may have been superseded.
- Follow evidence links when a claim needs more support. A note reporting a test
  is evidence of the reported result, not a claim that we independently reran it.
- For calibration, read the source repository's `AGENTS.md` and
  `docs/calibration-investigation-ledger.md`; its later corrections govern
  interpretations of older notes. Do not restart investigations for documentation.
- Keep changes in this documentation repository. Reading source repositories does
  not authorize hardware operations or changes to their code, notes, or Git state.
- Maintain this repository's running notes and Git history as work progresses.
- Keep a record of missing information and media needs. Ask focused questions
  during discussion rather than inventing details or requesting every asset at once.
- The user authorized a public repository in their personal GitHub account,
  `sri299792458`, with a later lab-organization copy after completion. Preserve
  personal portfolio attribution and the ability to maintain the lab copy.
- The user subsequently deferred connecting a remote. Continue locally with Git;
  later, they created `sri299792458/g1-research-docs` and authorized connecting
  and publishing the draft so they can read it. `origin` now points there.
- The chosen site stack is Sphinx + MyST Markdown + Furo, after reviewing
  Material's maintenance status and the UW Lab/cuRobo sites. Keep customization
  minimal. The author wants a straightforward lab guide with specific evidence,
  not language implying the scope or maturity of cuRobo.
- Keep machine-specific source locations in ignored `.local/` files. The public
  source snapshot uses repository directory names and hashes. Use public source
  URLs only when they refer to the exact available material; label local-only
  evidence explicitly rather than publishing broken sibling-checkout links.
