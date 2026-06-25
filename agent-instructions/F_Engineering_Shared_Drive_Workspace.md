# F-Engineering Shared Drive Workspace

Status: `Candidate`

Use this instruction when a project is located on the F-Engineering shared drive
or when the user asks to make the shared drive the main working area.

## Primary Working Drive

The primary F-Engineering project workspace is:

`H:\Общие диски\022-F_engineering`

Project folders, client files, drawings, estimates, photos, working drafts, and
final deliverables should stay on this shared drive unless the user explicitly
chooses another location.

## Knowledge Base Locations

GitHub remains the source of truth:

`https://github.com/f-engineering-spb/f-engineering-knowledge-base`

The shared drive may contain a readable local mirror for fast project work:

`H:\Общие диски\022-F_engineering\00_Knowledge_Base\f-engineering-knowledge-base`

At the start of project work, read the knowledge base in this order:

1. `START_HERE.md`
2. `AGENTS.md`
3. `registry/KNOWLEDGE_REGISTRY.md`
4. `registry/APPLICATION_MAP.md`
5. only the task-specific methodology, standard, template, or tool selected by
   the application map.

If both GitHub and the shared-drive mirror are available, prefer GitHub for the
latest approved content and use the shared-drive mirror as a fast local working
reference.

## Project Folder Rules

- Keep project-specific and client-specific files in the project folder.
- Do not copy confidential project data into the knowledge-base repository.
- Store reusable generalized improvements in the knowledge base only after
  removing client-specific data.
- Register new reusable tools, methods, and standards in
  `registry/KNOWLEDGE_REGISTRY.md` and, when applicable,
  `registry/APPLICATION_MAP.md`.

## Reusable Improvements

When a project produces a reusable rule, method, script, checklist, or document
standard:

1. leave the project result in the project folder;
2. extract a generic version;
3. add it under `agent-instructions/`, `methodologies/`, `document-standards/`,
   `templates/`, or `tools/`;
4. add tests or verification steps where practical;
5. publish the clean reusable version to GitHub.

## Estimate And VOR Tasks

For Excel estimates, local estimates, object estimates, VOR/BQ files, and
Grand-Smeta spreadsheet exports, use:

`tools/estimate_scope/`

Then verify important facade quantities through the applicable drawing-audit
methodology.
