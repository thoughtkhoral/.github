#!/usr/bin/env python3
"""Validate local and ThoughtKhoral GitHub Markdown links in checked-out docs."""

import argparse
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


COMPONENTS = (
    "thought-khoral-contracts",
    "thought-khoral-room-gateway",
    "thought-khoral-workspace-ui",
    "thought-khoral-memory-engine",
    "thought-khoral-agent-gateway",
    "thought-khoral-platform",
)
SKIP_DIRECTORIES = {
    ".git", ".github", ".superpowers", ".worktrees", "node_modules", "target", "vendor", "dist"
}
LINK = re.compile(r"\]\(([^)]+)\)")


def markdown_files(root: Path):
    for directory, subdirs, files in os.walk(root):
        subdirs[:] = [name for name in subdirs if name not in SKIP_DIRECTORIES]
        for name in files:
            if name.endswith(".md"):
                yield Path(directory) / name


def link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<"):
        return target.split(">", 1)[0][1:]
    return target.split(" ", 1)[0]


def check_link(source: Path, target: str, repositories: dict[str, Path]) -> str | None:
    parsed = urlsplit(target)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc.lower() != "github.com":
            return None
        parts = [unquote(part) for part in parsed.path.strip("/").split("/")]
        if len(parts) < 2 or parts[0].lower() != "thoughtkhoral":
            return None
        repository = repositories.get(parts[1])
        if repository is None or not repository.is_dir():
            return f"unknown or absent organization repository: {target}"
        if len(parts) >= 4 and parts[2] in {"blob", "tree"} and parts[3] == "main":
            destination = repository.joinpath(*parts[4:])
            if not destination.exists():
                return f"missing organization target: {target}"
        return None
    if parsed.scheme or target.startswith("//") or not parsed.path:
        return None
    destination = source.parent / unquote(parsed.path)
    if not destination.exists():
        return f"missing local target: {target}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="project home checkout")
    parser.add_argument("--org", type=Path, required=True, help="organization .github checkout")
    parser.add_argument("--require-components", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    org = args.org.resolve()
    repositories = {"thought-khoral": root, ".github": org}
    repositories.update({name: root / name for name in COMPONENTS})

    if not root.is_dir() or not org.is_dir():
        parser.error("both --root and --org must exist")
    absent = [name for name in COMPONENTS if not repositories[name].is_dir()]
    if args.require_components and absent:
        for name in absent:
            print(f"MISSING repository checkout: {name}")
        return 1

    checked_files = 0
    checked_links = 0
    failures = []
    for source in (*markdown_files(root), *markdown_files(org)):
        checked_files += 1
        in_code_fence = False
        for line_number, line in enumerate(source.read_text(errors="replace").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue
            for match in LINK.finditer(line):
                target = link_target(match.group(1))
                checked_links += 1
                error = check_link(source, target, repositories)
                if error:
                    failures.append(f"{source}:{line_number}: {error}")

    for failure in failures:
        print(failure)
    print(f"checked {checked_links} Markdown links in {checked_files} files; {len(failures)} broken")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
