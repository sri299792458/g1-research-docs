# Writing diagrams

Use **Mermaid** for code flow, message sequences and state transitions in this
guide. Keep its text alongside the explanation so a future maintainer can
review changes in Git. The diagram should answer one question that its
surrounding paragraph makes explicit.

## Decide whether a diagram helps

First write the question the reader needs answered. If the diagram adds only
boxes around terms already listed in a paragraph, omit it. A chapter does not
need a diagram at its start, or anywhere else.

For example, a reader choosing a wrist mount needs the right/left print files,
marker IDs and an assembly view. A graph from “CAD” to “physical geometry”
does not help them fit the part. A reader changing control ownership does need
to see which process can recover the robot if the laptop stops responding.

Use a table for choices or parameter comparisons, a numbered procedure for
operator actions, and photographs or CAD views for physical identification.
Keep a diagram when it explains branching, concurrency, a feedback path or
a spatial relationship that is harder to follow in prose.

## Connect a useful diagram to implementation

Explain its question and scope immediately before it. Introduce unfamiliar
terms and state what arrows mean. Follow with the relevant behavior and code
links; a separate code table is useful when readers need several entry points,
but is not a mandatory companion to every visual.

Use the [code index](code-index.md) for exact source versions. Do not draw a
rejected experiment as the current runtime, or merge two coordinators merely
because they use the same planner. Keep significant conditions in the prose
so the page remains useful without viewing the rendered graph.

## Choose the diagram for the question

| Question | Mermaid type | Example in the G1 work |
|---|---|---|
| What information flows between components? | `flowchart` | Observations, planner inputs and controller output |
| Who sends what, and in what order? | `sequenceDiagram` | Controller/worker exchange or watchdog startup |
| Which transitions are allowed? | `stateDiagram-v2` | Task phases and normal versus fault recovery |

Separate diagrams when the question changes. A runtime path, an offline
analysis path and an ownership state machine usually need separate views.
For physical geometry, use a CAD view or annotated photograph when it conveys
mounting surfaces, axes or dimensions more accurately than boxes and arrows.

## Write ordinary Markdown

The MyST configuration recognizes standard Mermaid fences. For example:

````markdown
```mermaid
flowchart LR
  accTitle: Documentation update workflow
  accDescr: Edit a page, build and review it, then publish the change.
  E["Edit a page"] --> B["Build and review"]
  B --> P["Publish"]
```
````

This syntax is also understood by GitHub's Markdown renderer. GitHub controls
its own Mermaid version, so check compatibility before using newer syntax.
The Sphinx renderer version is pinned in `docs/conf.py`.

## Keep the explanation readable

Use short labels with concrete nouns or verbs. Label arrows when their meaning
is otherwise ambiguous: a measured state, a command, an acknowledgement and a
recovery request are different relationships. Use a line break within a label
when needed, as in `"Observe robot<br/>and scene"`.

Start with roughly three to seven nodes. If an overview needs many more,
split it and link to the detailed chapter. Keep the main direction consistent
and avoid wrapping feedback arrows around an entire page merely to include
every relationship.

Add `accTitle` and `accDescr` for an accessible title and description. Explain
the important relationship in the surrounding prose too. Do not use color
alone to distinguish success from failure, measured from commanded, or
simulation from hardware.

The site supplies a neutral light theme, a dark theme, readable sizing and
an **Expand** control. In-page graphs retain their intrinsic dimensions;
the expanded viewer fits the complete graph. Narrow screens scroll wide diagrams horizontally.
Keep appearance settings in `docs/conf.py` and `assets/stylesheets/extra.css`
instead of repeating a custom theme in each diagram.

## Verify the rendered result

Run the normal strict Sphinx build, then open the changed page in a browser.
Mermaid renders in JavaScript, so a successful Sphinx build alone does not
prove that a diagram parses or lays out correctly. Check labels, arrow
endpoints, light/dark mode and the Expand/Escape controls. Desktop review is the current
priority; check smaller screens when revisiting responsive layout.

Do not describe an offline check as a physical transition that was tested.
When drawing control or recovery sequences, trace the exact source ordering
and preserve the conditions in the corresponding chapter.

References: [Mermaid syntax](https://mermaid.js.org/intro/syntax-reference.html),
[accessibility](https://mermaid.js.org/config/accessibility.html), and
[GitHub Mermaid support](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).
