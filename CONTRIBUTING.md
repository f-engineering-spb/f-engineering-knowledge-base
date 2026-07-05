# Contributing

## Standard workflow

1. Describe the problem or improvement.
2. Create a focused branch.
3. Make and verify the change.
4. Open a Pull Request.
5. Review the content and resolve comments.
6. Merge into `main`.
7. Update `CHANGELOG.md` when the change affects users.

## Branch names

- `docs/<topic>`
- `methodology/<topic>`
- `tool/<topic>`
- `fix/<topic>`

## Commit messages

Use short messages describing the result:

```text
docs: add mobile HTML requirements
tool: add document validation script
fix: correct broken methodology link
```

## Knowledge publication criteria

An approved knowledge item must:

- be understandable without the source project;
- state its purpose and scope;
- contain no client-specific or confidential information;
- not conflict with current approved rules;
- identify its owner or responsible function.

## What must not be published here

This repository is a knowledge base, not a project archive or publishing host.

Do not commit:

- project reports, client deliverables, estimates, photos, drawings, or rendered outputs;
- generated HTML reports or GitHub Pages deliverables;
- files that contain embedded base64 images or other heavy inline assets;
- client-specific examples that have not been generalized and anonymized.

If a project produces a useful document pattern, extract the reusable rule,
checklist, or template description into Markdown. Keep the actual report in the
project folder or shared drive.

