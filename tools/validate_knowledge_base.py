from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {
    "Draft",
    "Candidate",
    "Pilot",
    "Review",
    "Approved",
    "Deprecated",
    "Archived",
}
MOJIBAKE_MARKERS = ("Рџ", "Рґ", "Рё", "СЃ", "вЂ", "Ð", "????")
REGISTRY_ROW = re.compile(r"^\|\s*([A-Z]{2}-\d{3})\s*\|\s*`([^`]+)`\s*\|.*\|\s*([^|`]+?)\s*\|$")
MOJIBAKE_EXAMPLE_FILES = {
    Path("agent-instructions/Cyrillic_UTF8_Handling.md"),
    Path("tools/validate_knowledge_base.py"),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def iter_text_files() -> list[Path]:
    allowed = {".md", ".py", ".yml", ".yaml", ".json", ".txt", ".html", ".css", ".js"}
    ignored_parts = {".git", "__pycache__", ".pytest_cache"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in allowed:
            files.append(path)
    return files


def check_utf8_and_mojibake() -> None:
    for path in iter_text_files():
        relative = path.relative_to(ROOT)
        if relative in MOJIBAKE_EXAMPLE_FILES:
            continue
        text = read_text(path)
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                fail(f"{relative} contains possible mojibake marker: {marker}")


def check_registry_paths_and_statuses() -> None:
    registry = ROOT / "registry" / "KNOWLEDGE_REGISTRY.md"
    text = read_text(registry)
    seen_ids: set[str] = set()
    found_rows = 0

    for line in text.splitlines():
        match = REGISTRY_ROW.match(line)
        if not match:
            continue
        item_id, material, status = match.groups()
        found_rows += 1
        status = status.strip()

        if item_id in seen_ids:
            fail(f"Duplicate registry ID: {item_id}")
        seen_ids.add(item_id)

        if status not in VALID_STATUSES:
            fail(f"{item_id} has invalid status: {status}")

        material_path = ROOT / material
        if material.endswith("/"):
            if not material_path.is_dir():
                fail(f"{item_id} points to missing directory: {material}")
        elif not material_path.exists():
            fail(f"{item_id} points to missing file: {material}")

    if found_rows == 0:
        fail("No knowledge registry rows were detected")


def check_required_files() -> None:
    required = [
        "START_HERE.md",
        "AGENTS.md",
        "registry/KNOWLEDGE_REGISTRY.md",
        "registry/APPLICATION_MAP.md",
        "registry/RULE_CONFLICTS.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/CODEOWNERS",
        "docs/GitHub_Knowledge_Base_Workflow.md",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"Required file is missing: {relative}")


def main() -> None:
    check_required_files()
    check_utf8_and_mojibake()
    check_registry_paths_and_statuses()
    print("Knowledge base checks passed.")


if __name__ == "__main__":
    main()
