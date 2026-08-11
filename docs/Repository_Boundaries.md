# Repository boundaries

This repository is the F-Engineering knowledge base. It stores approved instructions, rules, workflows, reusable business-process descriptions, and governance documents.

It is not an application runtime and must not contain working copies of products such as F-Engineering Launcher.

## Belongs here

- approved Markdown instructions and methodologies;
- governance rules and contribution workflows;
- reusable business-process module descriptions;
- visual and interaction standards;
- small helper scripts used to validate the knowledge base itself.

## Does not belong here

- Launcher frontend or backend application code;
- local runtime folders, caches, manifests, rendered previews, logs, or generated outputs;
- customer object folders, PDF/DWG/Excel/Word source packages, or copied project documents;
- experimental prototypes that are not approved knowledge-base material;
- temporary probe files.

## Product repositories

Application products must live in their own repositories. For example, F-Engineering Launcher should be developed in a separate repository such as:

```text
f-engineering-spb/f-engineering-launcher
```

The knowledge base may contain a short reference page that points to an external product repository, but it must not duplicate the product code or runtime state.

## Local runtime rule

A product can be cloned or exported from GitHub to a local `C:` workspace for execution. Google Drive can store source documents and transfer archives, but it should not be the live runtime folder for Launcher.
