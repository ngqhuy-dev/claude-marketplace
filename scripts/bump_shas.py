#!/usr/bin/env python3
"""Bump every plugin's pinned `sha` in marketplace.json to its upstream HEAD.

Edits the file textually so formatting is preserved. Prints a Markdown
summary of changes to stdout (used as the PR body). Exit code is always 0;
an unreachable upstream is reported and skipped.
"""
import json
import subprocess
import sys
from pathlib import Path

MANIFEST = Path(__file__).resolve().parent.parent / ".claude-plugin" / "marketplace.json"


def remote_head(url: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "ls-remote", url, "HEAD"],
            capture_output=True, text=True, timeout=60, check=True,
        ).stdout
    except (subprocess.SubprocessError, OSError) as exc:
        print(f"warning: cannot reach {url}: {exc}", file=sys.stderr)
        return None
    return out.split()[0] if out.strip() else None


def repo_web_url(url: str) -> str:
    return url.removesuffix(".git")


def main() -> None:
    text = MANIFEST.read_text(encoding="utf-8")
    data = json.loads(text)

    heads: dict[str, str | None] = {}
    rows: list[str] = []
    replacements: dict[str, str] = {}

    for plugin in data.get("plugins", []):
        src = plugin.get("source")
        if not isinstance(src, dict) or "sha" not in src or "url" not in src:
            continue
        url = src["url"]
        if url not in heads:
            heads[url] = remote_head(url)
        new = heads[url]
        old = src["sha"]
        if not new or new == old:
            continue
        replacements[old] = new
        web = repo_web_url(url)
        rows.append(
            f"| `{plugin['name']}` | [`{old[:7]}...{new[:7]}`]({web}/compare/{old}...{new}) |"
        )

    for old, new in replacements.items():
        text = text.replace(f'"sha": "{old}"', f'"sha": "{new}"')

    if not rows:
        print("All plugins are already at upstream HEAD.")
        return

    MANIFEST.write_text(text, encoding="utf-8")
    json.loads(text)  # sanity check: still valid JSON

    print("Bumps pinned plugin SHAs to upstream HEAD.\n")
    print("| Plugin | Diff |")
    print("| --- | --- |")
    print("\n".join(rows))
    print("\nReview the upstream diffs before merging.")


if __name__ == "__main__":
    main()
