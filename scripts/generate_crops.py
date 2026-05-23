#!/usr/bin/env python3
"""Generate label and theca crops from a coordinate manifest.

The script reads data/crop_manifest.csv and writes cropped image files to the
paths specified in the manifest. It is deterministic: the same source image and
coordinates produce the same crop.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "crop_manifest.csv"
VALID_TYPES = {"label", "theca", "certificate", "context"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def parse_int(value: str, field: str, row_num: int) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"row {row_num}: `{field}` must be an integer") from exc
    if parsed < 0:
        raise ValueError(f"row {row_num}: `{field}` must be non-negative")
    return parsed


def generate_crop(row: dict[str, str], row_num: int) -> str | None:
    status = (row.get("status") or "").strip().lower()
    if status and status not in {"ready", "approved", "generate"}:
        return None

    crop_type = (row.get("crop_type") or "").strip().lower()
    if crop_type not in VALID_TYPES:
        raise ValueError(f"row {row_num}: invalid crop_type `{crop_type}`")

    source_image = (row.get("source_image") or "").strip()
    output_path = (row.get("output_path") or "").strip()
    if not source_image:
        raise ValueError(f"row {row_num}: missing source_image")
    if not output_path:
        raise ValueError(f"row {row_num}: missing output_path")

    source_path = ROOT / "images" / "original" / source_image
    if not source_path.exists():
        raise FileNotFoundError(f"row {row_num}: source image missing: {source_path}")

    x = parse_int(row.get("x", ""), "x", row_num)
    y = parse_int(row.get("y", ""), "y", row_num)
    width = parse_int(row.get("width", ""), "width", row_num)
    height = parse_int(row.get("height", ""), "height", row_num)
    if width <= 0 or height <= 0:
        raise ValueError(f"row {row_num}: width and height must be greater than zero")

    output = ROOT / output_path
    output.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(source_path) as image:
        image_width, image_height = image.size
        if x + width > image_width or y + height > image_height:
            raise ValueError(
                f"row {row_num}: crop exceeds image bounds for {source_image} "
                f"({image_width}x{image_height})"
            )
        crop = image.crop((x, y, x + width, y + height))
        crop.save(output, quality=95)
    return output_path


def main() -> int:
    if not MANIFEST.exists():
        fail(f"manifest missing: {MANIFEST}")
        return 1

    generated: list[str] = []
    failures = 0
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for idx, row in enumerate(reader, start=2):
            try:
                output = generate_crop(row, idx)
                if output:
                    generated.append(output)
            except Exception as exc:  # noqa: BLE001 - report all row-level issues clearly
                failures += 1
                fail(str(exc))

    if failures:
        print(f"Crop generation failed with {failures} issue(s).")
        return 1
    print(f"Generated {len(generated)} crop(s).")
    for path in generated:
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
