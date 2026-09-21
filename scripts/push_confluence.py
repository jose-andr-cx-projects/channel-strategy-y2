#!/usr/bin/env python3
"""
Controlled write-back of reviewed Markdown pages to Confluence Cloud.

This is intentionally not a general two-way sync.

It updates only pages explicitly listed in a manifest, verifies that the
Confluence version still matches the version exported into Markdown, and
optionally archives explicitly listed superseded pages.

Required environment variables:
    CONFLUENCE_BASE_URL
    CONFLUENCE_EMAIL
    CONFLUENCE_API_TOKEN

Usage:
    python scripts/push_confluence.py --manifest scripts/confluence_writeback_2026-09-21.json
    python scripts/push_confluence.py --manifest scripts/confluence_writeback_2026-09-21.json --apply

Safety:
- Dry-run is the default.
- --apply is required to write.
- Every update is preflighted before any write occurs.
- If the live Confluence version differs from the exported frontmatter version,
  the run stops rather than overwriting newer organisational content.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import markdown
import requests
import yaml
from requests.auth import HTTPBasicAuth


BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.getenv("CONFLUENCE_EMAIL", "")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
REQUEST_TIMEOUT = 30


@dataclass
class UpdatePlan:
    path: Path
    page_id: str
    expected_version: int
    current_version: int
    current_title: str
    new_title: str
    storage_html: str
    space_key: str


def validate_config() -> None:
    missing = [
        name
        for name, value in (
            ("CONFLUENCE_BASE_URL", BASE_URL),
            ("CONFLUENCE_EMAIL", EMAIL),
            ("CONFLUENCE_API_TOKEN", API_TOKEN),
        )
        if not value
    ]
    if missing:
        raise SystemExit(
            "Missing required environment variables: " + ", ".join(missing)
        )


def session() -> requests.Session:
    s = requests.Session()
    s.auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    s.headers.update({"Accept": "application/json"})
    return s


def api_url(path: str) -> str:
    return f"{BASE_URL}/wiki{path}"


def read_markdown_page(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, flags=re.S)
    if not match:
        raise ValueError(f"{path}: YAML frontmatter not found")

    meta = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)

    body = re.sub(
        r"^> \*\*Source note:\*\*.*?\n\s*",
        "",
        body,
        count=1,
        flags=re.M,
    )

    return meta, body.strip() + "\n"


def markdown_to_storage(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def get_page(s: requests.Session, page_id: str) -> dict[str, Any]:
    response = s.get(
        api_url(f"/rest/api/content/{page_id}"),
        params={"expand": "body.storage,version,space"},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def preflight_update(
    s: requests.Session, path: Path, force: bool = False
) -> UpdatePlan:
    meta, md_body = read_markdown_page(path)

    if meta.get("source_system") != "confluence":
        raise ValueError(f"{path}: source_system is not confluence")

    page_id = str(meta.get("confluence_page_id", "")).strip()
    expected_raw = meta.get("confluence_version")
    new_title = str(meta.get("title", "")).strip()

    if not page_id or expected_raw in (None, "") or not new_title:
        raise ValueError(
            f"{path}: confluence_page_id, confluence_version and title are required"
        )

    expected_version = int(expected_raw)
    live = get_page(s, page_id)
    current_version = int(live["version"]["number"])
    current_title = live["title"]
    space_key = live["space"]["key"]

    if current_version != expected_version and not force:
        raise RuntimeError(
            f"{path}: version conflict for page {page_id}. "
            f"Exported version={expected_version}, live version={current_version}. "
            "No pages have been written."
        )

    return UpdatePlan(
        path=path,
        page_id=page_id,
        expected_version=expected_version,
        current_version=current_version,
        current_title=current_title,
        new_title=new_title,
        storage_html=markdown_to_storage(md_body),
        space_key=space_key,
    )


def apply_update(s: requests.Session, plan: UpdatePlan) -> None:
    payload = {
        "id": plan.page_id,
        "type": "page",
        "title": plan.new_title,
        "space": {"key": plan.space_key},
        "body": {
            "storage": {
                "value": plan.storage_html,
                "representation": "storage",
            }
        },
        "version": {
            "number": plan.current_version + 1,
            "message": "Synced from reviewed Channel Strategy Y2 Markdown",
            "minorEdit": False,
        },
    }

    response = s.put(
        api_url(f"/rest/api/content/{plan.page_id}"),
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()


def archive_pages(s: requests.Session, page_ids: list[str]) -> None:
    if not page_ids:
        return

    payload = {"pages": [{"id": int(page_id)} for page_id in page_ids]}
    response = s.post(
        api_url("/rest/api/content/archive"),
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the preflighted changes. Without this flag, dry-run only.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow update despite version mismatch. Avoid unless manually reviewed.",
    )
    args = parser.parse_args()

    validate_config()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    update_paths = [Path(item["path"]) for item in manifest.get("updates", [])]
    archive_ids = [str(x) for x in manifest.get("archive_page_ids", [])]

    s = session()

    plans: list[UpdatePlan] = []
    for path in update_paths:
        if not path.exists():
            raise FileNotFoundError(f"Manifest path does not exist: {path}")
        plans.append(preflight_update(s, path, force=args.force))

    print("Confluence write-back preflight")
    print("==============================")
    for plan in plans:
        print(
            f"UPDATE {plan.page_id}: "
            f"v{plan.current_version} -> v{plan.current_version + 1} | "
            f"{plan.current_title!r} -> {plan.new_title!r} | {plan.path}"
        )

    for page_id in archive_ids:
        print(f"ARCHIVE {page_id}")

    if not args.apply:
        print("\nDry-run only. Re-run with --apply after review.")
        return

    for plan in plans:
        apply_update(s, plan)
        print(f"Updated page {plan.page_id}: {plan.new_title}")

    if archive_ids:
        archive_pages(s, archive_ids)
        print("Submitted archive request for: " + ", ".join(archive_ids))

    print("Confluence write-back completed.")


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as exc:
        body = ""
        if exc.response is not None:
            body = exc.response.text[:1000]
        print(f"Confluence API error: {exc}\n{body}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Write-back failed: {exc}", file=sys.stderr)
        sys.exit(1)
