# Instructions for agents

## Source of truth

- Use the `main` branch as the source of approved knowledge.
- Follow the closest applicable `AGENTS.md`.
- Project-specific instructions must remain in the project repository or folder.
- Repository scope boundaries are defined in [docs/Repository_Boundaries.md](docs/Repository_Boundaries.md).

## Change policy

- Do not publish new knowledge directly as approved.
- Prepare reusable improvements in a separate branch and Pull Request.
- Remove client-specific, personal, confidential, and secret information.
- Keep changes focused and explain the reason for each change.

## File policy

- Prefer Markdown for instructions and methodologies.
- Keep reusable source code with a short usage guide and tests where practical.
- Do not commit generated outputs, temporary files, credentials, or heavy project data.
- Do not commit Launcher frontend/backend code, runtime folders, caches, manifests, rendered previews, or logs to this knowledge-base repository.
- Application products must live in separate product repositories.

## Visual Style Policy

- Before creating or modifying any visual artifacts, the agent MUST read [docs/F_ENGINEERING_VISUAL_STYLE.md](docs/F_ENGINEERING_VISUAL_STYLE.md).
- The agent is not permitted to invent new color palettes or schemas.
- The agent is not permitted to use old stylistic solutions if they contradict [docs/F_ENGINEERING_VISUAL_STYLE.md](docs/F_ENGINEERING_VISUAL_STYLE.md).

