#!/usr/bin/env python3
"""Validate St. Bonaventure reliquary catalog repository structure.

This script performs repository-local checks only. It does not authenticate relics,
interpret theological claims, or alter data. It verifies that CSV inventories and
image references remain internally coherent.
"""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "data/relic_index_visible.csv",
    "data/reliquary_sections.csv",
    "data/image_file_register.csv",
    "data/relic_catalog_master.csv",
    "data/authentication_register.csv",
    "data/saint_research_register.csv",
    "docs/cataloging_protocol.md",
    "docs/operational_roadmap.md",
    "docs/academic_press_requirements.md",
    "templates/saint_note_template.md",
]

REQUIRED_ORIGINAL_IMAGES = [
    "IMG_3202.JPG",
    "IMG_3203.JPG",
    "IMG_3204.JPG",
    "IMG_3205.JPG",
    "IMG_3207.JPG",
    "IMG_3208.JPG",
    "IMG_3209.JPG",
    "IMG_3210.JPG",
    "IMG_3211.JPG",
    "IMG_3212.JPG",
    "IMG_3213.JPG",
    "IMG_3214.JPG",
    "IMG_3215.JPG",
    "IMG_3216.JPG",
    "IMG_3217.JPG",
    "IMG_3218.JPG",
    "IMG_3219.JPG",
    "IMG_3220.JPG",
    "IMG_3221.JPG",
    "IMG_3222.JPG",
    "IMG_3223.JPG",
    "IMG_3224.JPG",
    "IMG_3225.JPG",
    "IMG_3226.JPG",
    "IMG_3227.JPG",
    "IMG_3228.JPG",
    "IMG_3229.JPG",
    "IMG_3230.JPG",
    "IMG_3231.JPG",
    "IMG_3232.JPG",
    "IMG_3233.JPG",
    "IMG_3234.JPG",
    "IMG_3235.JPG",
    "IMG_3236.JPG",
    "IMG_3237.JPG",
    "IMG_3238.JPG",
]

VISIBLE_INDEX_COLUMNS = {
    "record_id",
    "section_id",
    "visible_label",
    "normalized_name",
    "source_images",
    "confidence",
    "verification_status",
}

MASTER_CATALOG_COLUMNS = {
    "record_id",
    "case_id",
    "panel_id",
    "section_id",
    "display_order",
    "visible_label",
    "normalized_name",
    "group_or_individual",
    "source_images",
    "label_crop",
    "theca_crop",
    "confidence",
    "verification_status",
    "publication_status",
}

VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_VERIFICATION_STATUSES = {
    "visible_label_only",
    "visible_label_plus_theca",
    "certificate_pending",
    "certificate_verified",
    "certificate_conflict",
    "unresolved",
    "not_a_relic_record",
}


def error(message: str) -> None:
    print(f"ERROR: {message}")


def warn(message: str) -> None:
    print(f"WARN: {message}")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def split_source_images(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.replace(",", ";").split(";") if part.strip()]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_columns(rows: list[dict[str, str]], required: set[str], file_label: str) -> int:
    if not rows:
        warn(f"{file_label} has no data rows")
        return 0
    present = set(rows[0].keys())
    missing = sorted(required - present)
    if missing:
        error(f"{file_label} missing columns: {', '.join(missing)}")
        return 1
    return 0


def check_required_files() -> int:
    failures = 0
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            error(f"required file missing: {rel_path}")
            failures += 1
    return failures


def check_original_images() -> int:
    failures = 0
    image_dir = ROOT / "images" / "original"
    if not image_dir.exists():
        error("images/original directory missing")
        return 1

    for filename in REQUIRED_ORIGINAL_IMAGES:
        path = image_dir / filename
        if not path.exists():
            error(f"missing original image: images/original/{filename}")
            failures += 1

    unexpected = sorted(
        p.name for p in image_dir.glob("IMG_*.JPG") if p.name not in REQUIRED_ORIGINAL_IMAGES
    )
    for filename in unexpected:
        warn(f"unexpected original image present: images/original/{filename}")
    return failures


def check_image_register() -> int:
    failures = 0
    register_path = ROOT / "data" / "image_file_register.csv"
    if not register_path.exists():
        return 1

    rows = read_csv(register_path)
    register_by_name = {row.get("filename", ""): row for row in rows}

    for filename in REQUIRED_ORIGINAL_IMAGES:
        row = register_by_name.get(filename)
        if not row:
            error(f"image register missing row for {filename}")
            failures += 1
            continue
        image_path = ROOT / "images" / "original" / filename
        if image_path.exists() and row.get("sha256"):
            actual_hash = sha256_file(image_path)
            if actual_hash != row["sha256"]:
                error(f"SHA-256 mismatch for {filename}: register={row['sha256']} actual={actual_hash}")
                failures += 1
    return failures


def check_visible_index() -> int:
    failures = 0
    path = ROOT / "data" / "relic_index_visible.csv"
    if not path.exists():
        return 1

    rows = read_csv(path)
    failures += require_columns(rows, VISIBLE_INDEX_COLUMNS, "data/relic_index_visible.csv")

    seen_record_ids: set[str] = set()
    valid_image_names = set(REQUIRED_ORIGINAL_IMAGES)

    for row in rows:
        record_id = row.get("record_id", "").strip()
        if not record_id:
            error("visible index row missing record_id")
            failures += 1
            continue
        if record_id in seen_record_ids:
            error(f"duplicate record_id in visible index: {record_id}")
            failures += 1
        seen_record_ids.add(record_id)

        confidence = row.get("confidence", "").strip()
        if confidence and confidence not in VALID_CONFIDENCE:
            error(f"{record_id}: invalid confidence `{confidence}`")
            failures += 1

        status = row.get("verification_status", "").strip()
        if status and status not in VALID_VERIFICATION_STATUSES:
            error(f"{record_id}: invalid verification_status `{status}`")
            failures += 1

        for image_name in split_source_images(row.get("source_images", "")):
            if image_name not in valid_image_names:
                error(f"{record_id}: source image not in expected original image set: {image_name}")
                failures += 1
            elif not (ROOT / "images" / "original" / image_name).exists():
                error(f"{record_id}: source image file missing: images/original/{image_name}")
                failures += 1
    return failures


def check_master_catalog_schema() -> int:
    path = ROOT / "data" / "relic_catalog_master.csv"
    if not path.exists():
        return 1
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        present = set(reader.fieldnames or [])
    missing = sorted(MASTER_CATALOG_COLUMNS - present)
    if missing:
        error(f"data/relic_catalog_master.csv missing columns: {', '.join(missing)}")
        return 1
    return 0


def main() -> int:
    failures = 0
    failures += check_required_files()
    failures += check_original_images()
    failures += check_image_register()
    failures += check_visible_index()
    failures += check_master_catalog_schema()

    if failures:
        print(f"Catalog validation failed with {failures} issue(s).")
        return 1
    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
