# F-Engineering Launcher — product model v0.1.2

**Status:** `Candidate`
**Scope:** reusable product model; no client documents or generated outputs are stored here.

> [!IMPORTANT]
> F-Engineering Launcher is a single workspace that takes a user from source documentation through an appropriate processing module to a ready result and its viewing, without manual navigation through folders.

## Product flow

```text
Object → tree or structure → input selection → module template → telemetry
       → created module → output file → viewer
```

The input may be one folder, one file, or a package of files of one format. A package is selected in the **Tree** through a format filter such as DWG, PDF, Excel, Word, PNG, or JPG. Repeating the active format action clears the package.

## Three left-panel modes

| Mode | Role | Valid module input |
|---|---|---|
| Tree | Original folder/file location and fast format selection | Folder, file, or same-format package |
| Structure | Review of entities: plans, elevations, sections, specifications, documents, images | Folder or one file |
| Modules | Catalog of created modules for the object and compatible templates for the current input | Open a created module or run a template |

> [!NOTE]
> Batch selection belongs to the Tree, not the Structure. A structural entity can contain several formats, so using it as a technical package selector could mix incompatible source files.

## Module lifecycle

1. With no active input, the user opens the object’s created-module catalog.
2. With an active folder, file, or batch, the user sees only compatible templates.
3. Play starts one template and shows progress, current item, stage, warnings, and estimated time.
4. Completion creates or updates an identified module and its output file.
5. Created modules are for viewing, renaming, or deliberate deletion with confirmation; the user works with the current result rather than a visible version history.

## Viewer requirements

The right viewer is the primary interface area. It must not be reduced for module controls. It supports file/result viewing, zoom, fit, pan, scrollbars, navigation hiding, viewer expansion, and fullscreen mode. A generated HTML navigator opens inside the same viewer and can be expanded as a standalone work surface.

## Mobile mirror

The mobile mirror preserves the same product flow, including format batch selection and module telemetry. It is a self-contained demonstration artifact; presentation images may be embedded for transport, but customer documents and project data are never included in this knowledge base.

## Verified v0.1.2 behaviours

- files of several formats open in the viewer;
- a DWG-format action selects a multi-file package;
- Modules show the package count and compatible templates;
- telemetry counts the selected package rather than an arbitrary object total;
- the mobile mirror repeats the same selection path.

## Boundary

This document fixes the interaction model only. Actual local-agent integration, Python scripts, OCR, DWG conversion, indexing, and file operations are separate module implementations and must be connected one at a time without changing this product flow.
