#!/usr/bin/env python3
"""Narrow deterministic governance lint checks for AI_WORKFLOW.

Rule 1:
Check Markdown references that look like actual workflow repository file paths
and ensure they resolve to files that exist in this repository.

Rule 2:
For each .ai/prompts/*.md file that contains the literal heading
"## Required Output", require at least one heading line (any heading level,
one to six "#" characters) after that point whose text starts with
"Prompt For Next Role", or any line after that point containing the literal
substring "NEXT_ROLE_PROMPT". Files without the "## Required Output" heading
are not checked by this rule.

This is intentionally not a general Markdown linter, external link checker,
anchor checker, reference-label checker, or semantic governance validator.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]

OPTIONAL_MUTABLE_CONTEXT_PATHS = {
    ".ai/CURRENT_STATE.md",
    ".ai/NEXT_PATCH_BRIEF.md",
    ".ai/HANDOFF.md",
    ".ai/DECISIONS_LOG.md",
}

ROOT_REFERENCE_NAMES = {
    "ARCHITECT_RULES.md",
    "BEGIN_HERE.md",
    "README.md",
    "SOLO_AI_ENGINEERING_METHOD.md",
}

CHECKED_REPO_PATH_PREFIXES = (
    ".ai/",
    ".github/",
    "scripts/",
)

EXAMPLE_PATH_PREFIXES = (
    "path/to/",
)

PROMPTS_DIR = REPO_ROOT / ".ai" / "prompts"

REQUIRED_OUTPUT_HEADING = "## Required Output"
NEXT_ROLE_HEADING_TEXT = "Prompt For Next Role"
NEXT_ROLE_SUBSTRING = "NEXT_ROLE_PROMPT"

HEADING_LINE_RE = re.compile(r"^#{1,6}\s+(.*)$")
FENCE_MARKER_RE = re.compile(r"^\s*(```|~~~)")
MARKDOWN_LINK_TARGET_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*([^)\s]+)(?:\s+[^)]*)?\)")
REFERENCE_LINK_DEFINITION_RE = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(\S+)")
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")


def to_repo_posix_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def markdown_parent_posix_path(markdown_file: Path) -> str:
    parent = markdown_file.parent.relative_to(REPO_ROOT).as_posix()
    if parent == ".":
        return ""
    return parent


def is_ignored_tree(path: Path) -> bool:
    return ".git" in path.relative_to(REPO_ROOT).parts


def existing_repo_files() -> set[str]:
    return {
        to_repo_posix_path(path)
        for path in REPO_ROOT.rglob("*")
        if path.is_file() and not is_ignored_tree(path)
    }


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.rglob("*.md")
        if path.is_file() and not is_ignored_tree(path)
    )


def strip_markdown_fragment_or_query(reference: str) -> str:
    return reference.split("#", 1)[0].split("?", 1)[0]


def is_url_or_anchor(reference: str) -> bool:
    lowered = reference.lower()
    return (
        "://" in reference
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
        or lowered.startswith("urn:")
        or reference.startswith("#")
    )


def collapse_posix_path(base_path: str, reference: str) -> str | None:
    if reference.startswith("/"):
        raw_parts = PurePosixPath(reference.lstrip("/")).parts
    else:
        raw_parts = PurePosixPath(base_path, reference).parts

    collapsed_parts: list[str] = []

    for part in raw_parts:
        if part in ("", "."):
            continue
        if part == "..":
            if not collapsed_parts:
                return None
            collapsed_parts.pop()
            continue
        collapsed_parts.append(part)

    if not collapsed_parts:
        return None

    return PurePosixPath(*collapsed_parts).as_posix()


def is_repo_root_like_path(candidate: str) -> bool:
    return candidate in ROOT_REFERENCE_NAMES or candidate.startswith(CHECKED_REPO_PATH_PREFIXES)


def normalize_reference_text(reference: str) -> str | None:
    candidate = unquote(reference).strip().strip("'\"")
    candidate = candidate.strip(".,;:")

    if candidate.startswith("<") and candidate.endswith(">"):
        candidate = candidate[1:-1].strip()
    elif "<" in candidate or ">" in candidate:
        return None

    if not candidate or is_url_or_anchor(candidate):
        return None

    candidate = strip_markdown_fragment_or_query(candidate).strip().strip(".,;:")

    if not candidate or is_url_or_anchor(candidate):
        return None

    if candidate.endswith("/"):
        return None

    if any(marker in candidate for marker in ("*", "[", "]", "{", "}")):
        return None

    if "\\" in candidate:
        return None

    while candidate.startswith("./"):
        candidate = candidate[2:]

    if not candidate:
        return None

    if candidate.startswith(EXAMPLE_PATH_PREFIXES):
        return None

    return candidate


def normalize_candidate(reference: str, markdown_file: Path, reference_kind: str) -> str | None:
    candidate = normalize_reference_text(reference)

    if candidate is None:
        return None

    if reference_kind == "inline_code":
        if ".." in PurePosixPath(candidate).parts:
            return None
        normalized = candidate.lstrip("/")
        if not looks_like_checked_repo_file_path(normalized):
            return None
    else:
        if not PurePosixPath(candidate).suffix:
            return None
        normalized = collapse_posix_path(markdown_parent_posix_path(markdown_file), candidate)
        if normalized is None:
            return None
        if not looks_like_checked_repo_file_path(normalized):
            return None

    if normalized in OPTIONAL_MUTABLE_CONTEXT_PATHS:
        return None

    return normalized


def looks_like_checked_repo_file_path(candidate: str) -> bool:
    if candidate in ROOT_REFERENCE_NAMES:
        return True

    if candidate.startswith(CHECKED_REPO_PATH_PREFIXES):
        return bool(PurePosixPath(candidate).suffix)

    return False


def iter_markdown_references(markdown_file: Path):
    in_fenced_code = False

    for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE_MARKER_RE.match(line):
            in_fenced_code = not in_fenced_code
            continue

        if in_fenced_code:
            continue

        seen_on_line: set[tuple[str, str]] = set()

        for match in REFERENCE_LINK_DEFINITION_RE.finditer(line):
            reference = match.group(1)
            key = ("markdown_link", reference)
            if key not in seen_on_line:
                seen_on_line.add(key)
                yield line_number, reference, "markdown_link"

        for match in MARKDOWN_LINK_TARGET_RE.finditer(line):
            reference = match.group(1)
            key = ("markdown_link", reference)
            if key not in seen_on_line:
                seen_on_line.add(key)
                yield line_number, reference, "markdown_link"

        for match in INLINE_CODE_RE.finditer(line):
            reference = match.group(1).strip()
            if any(character.isspace() for character in reference):
                continue
            key = ("inline_code", reference)
            if key not in seen_on_line:
                seen_on_line.add(key)
                yield line_number, reference, "inline_code"


def prompt_files() -> list[Path]:
    if not PROMPTS_DIR.is_dir():
        return []

    return sorted(
        path
        for path in PROMPTS_DIR.glob("*.md")
        if path.is_file() and not is_ignored_tree(path)
    )


def has_next_role_heading_after_required_output(markdown_file: Path) -> bool | None:
    lines = markdown_file.read_text(encoding="utf-8").splitlines()
    required_output_line_index: int | None = None

    for line_index, line in enumerate(lines):
        if line.strip() == REQUIRED_OUTPUT_HEADING:
            required_output_line_index = line_index
            break

    if required_output_line_index is None:
        return None

    for line in lines[required_output_line_index + 1:]:
        stripped_line = line.strip()

        heading_match = HEADING_LINE_RE.match(stripped_line)
        if heading_match and heading_match.group(1).startswith(NEXT_ROLE_HEADING_TEXT):
            return True

        if NEXT_ROLE_SUBSTRING in stripped_line:
            return True

    return False


def main() -> int:
    repo_files = existing_repo_files()
    failures: list[str] = []

    for markdown_file in markdown_files():
        markdown_path = to_repo_posix_path(markdown_file)

        for line_number, raw_reference, reference_kind in iter_markdown_references(markdown_file):
            candidate = normalize_candidate(raw_reference, markdown_file, reference_kind)

            if candidate is None:
                continue

            if candidate not in repo_files:
                failures.append(
                    f"{markdown_path}:{line_number}: {candidate}: "
                    "referenced workflow repository path does not resolve to an existing file"
                )

    for prompt_file in prompt_files():
        prompt_path = to_repo_posix_path(prompt_file)
        has_next_role_heading = has_next_role_heading_after_required_output(prompt_file)

        if has_next_role_heading is False:
            failures.append(
                f"{prompt_path}: missing required next-role heading "
                f"(expected a heading whose text starts with "
                f"'{NEXT_ROLE_HEADING_TEXT}' at any heading level, or a line "
                f"containing '{NEXT_ROLE_SUBSTRING}') after "
                f"'{REQUIRED_OUTPUT_HEADING}'"
            )

    if failures:
        print("governance-lint: found unresolved Markdown workflow file references", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print("governance-lint: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
