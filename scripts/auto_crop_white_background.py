#!/usr/bin/env python3
"""Auto-crop relic/object images photographed on a white or near-white background.

This script detects the bounding box of pixels that differ from a white/background
field, adds padding, and writes cropped images. It is designed for isolated relic,
theca, certificate, or object photographs placed on a white/light background.

It is not intended to segment the red-lined reliquary display cases. For those,
use manual crop coordinates or a separate object-detection workflow.
"""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from pathlib import Path
from typing import Iterable

from PIL import Image

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}


def iter_images(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield input_path
        return
    for path in sorted(input_path.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path


def border_sample(image: Image.Image, width: int) -> list[tuple[int, int, int]]:
    rgb = image.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    sample: list[tuple[int, int, int]] = []
    border = max(1, min(width, w // 4, h // 4))

    for y in range(h):
        for x in range(w):
            if x < border or x >= w - border or y < border or y >= h - border:
                sample.append(px[x, y])
    return sample


def median_background(image: Image.Image, border_width: int) -> tuple[int, int, int]:
    sample = border_sample(image, border_width)
    if not sample:
        return (255, 255, 255)
    r = int(statistics.median(pixel[0] for pixel in sample))
    g = int(statistics.median(pixel[1] for pixel in sample))
    b = int(statistics.median(pixel[2] for pixel in sample))
    return (r, g, b)


def pixel_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def find_foreground_bbox(
    image: Image.Image,
    background: tuple[int, int, int],
    tolerance: int,
    alpha_threshold: int,
    scan_step: int,
) -> tuple[int, int, int, int] | None:
    rgba = image.convert("RGBA")
    w, h = rgba.size
    px = rgba.load()

    min_x = w
    min_y = h
    max_x = -1
    max_y = -1

    step = max(1, scan_step)
    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = px[x, y]
            if a <= alpha_threshold:
                continue
            if pixel_distance((r, g, b), background) > tolerance:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    if max_x < min_x or max_y < min_y:
        return None

    # Expand by scan step so sparse scanning does not under-crop.
    return (
        max(0, min_x - step),
        max(0, min_y - step),
        min(w, max_x + step + 1),
        min(h, max_y + step + 1),
    )


def pad_bbox(
    bbox: tuple[int, int, int, int],
    padding: int,
    image_size: tuple[int, int],
) -> tuple[int, int, int, int]:
    left, top, right, bottom = bbox
    w, h = image_size
    pad = max(0, padding)
    return (
        max(0, left - pad),
        max(0, top - pad),
        min(w, right + pad),
        min(h, bottom + pad),
    )


def bbox_area(bbox: tuple[int, int, int, int]) -> int:
    left, top, right, bottom = bbox
    return max(0, right - left) * max(0, bottom - top)


def output_path_for(source: Path, input_root: Path, output_dir: Path, suffix: str) -> Path:
    if input_root.is_dir():
        rel = source.relative_to(input_root)
        stem_path = output_dir / rel.parent / f"{rel.stem}{suffix}{rel.suffix.lower()}"
        return stem_path
    return output_dir / f"{source.stem}{suffix}{source.suffix.lower()}"


def crop_one(
    source: Path,
    input_root: Path,
    output_dir: Path,
    suffix: str,
    background_mode: str,
    tolerance: int,
    padding: int,
    border_width: int,
    alpha_threshold: int,
    scan_step: int,
    min_area: int,
    overwrite: bool,
) -> dict[str, str]:
    with Image.open(source) as image:
        image.load()
        if background_mode == "auto":
            background = median_background(image, border_width)
        else:
            background = (255, 255, 255)

        bbox = find_foreground_bbox(
            image=image,
            background=background,
            tolerance=tolerance,
            alpha_threshold=alpha_threshold,
            scan_step=scan_step,
        )
        if bbox is None:
            return {
                "source": str(source),
                "output": "",
                "status": "no_foreground_detected",
                "background_rgb": str(background),
                "bbox": "",
                "notes": "Increase tolerance downward or check that background is white/light.",
            }

        padded = pad_bbox(bbox, padding, image.size)
        area = bbox_area(padded)
        if area < min_area:
            return {
                "source": str(source),
                "output": "",
                "status": "foreground_below_min_area",
                "background_rgb": str(background),
                "bbox": str(padded),
                "notes": f"Area {area} below min_area {min_area}.",
            }

        output = output_path_for(source, input_root, output_dir, suffix)
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists() and not overwrite:
            return {
                "source": str(source),
                "output": str(output),
                "status": "skipped_exists",
                "background_rgb": str(background),
                "bbox": str(padded),
                "notes": "Use --overwrite to replace.",
            }

        cropped = image.crop(padded)
        cropped.save(output, quality=95)
        return {
            "source": str(source),
            "output": str(output),
            "status": "cropped",
            "background_rgb": str(background),
            "bbox": str(padded),
            "notes": "",
        }


def write_report(rows: list[dict[str, str]], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["source", "output", "status", "background_rgb", "bbox", "notes"]
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Auto-crop objects photographed on white or near-white backgrounds."
    )
    parser.add_argument("--input", required=True, help="Input image or directory.")
    parser.add_argument("--output-dir", required=True, help="Directory for cropped outputs.")
    parser.add_argument("--suffix", default="_autocrop", help="Output filename suffix.")
    parser.add_argument(
        "--background",
        choices=["white", "auto"],
        default="auto",
        help="Use pure white or median border color as background.",
    )
    parser.add_argument(
        "--tolerance",
        type=int,
        default=35,
        help="Foreground threshold. Lower is stricter; higher ignores more near-background pixels.",
    )
    parser.add_argument("--padding", type=int, default=40, help="Padding in pixels around detected object.")
    parser.add_argument(
        "--border-width",
        type=int,
        default=20,
        help="Border width in pixels used for automatic background sampling.",
    )
    parser.add_argument(
        "--alpha-threshold",
        type=int,
        default=0,
        help="Ignore pixels with alpha at or below this value.",
    )
    parser.add_argument(
        "--scan-step",
        type=int,
        default=1,
        help="Pixel step for scanning. Use 1 for best accuracy.",
    )
    parser.add_argument(
        "--min-area",
        type=int,
        default=1000,
        help="Minimum crop area in pixels before output is accepted.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing crops.")
    parser.add_argument(
        "--report",
        default="data/auto_crop_report.csv",
        help="CSV report path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    report_path = Path(args.report).expanduser()

    if not input_path.exists():
        print(f"ERROR: input path does not exist: {input_path}")
        return 1

    images = list(iter_images(input_path))
    if not images:
        print(f"ERROR: no supported images found in {input_path}")
        return 1

    rows: list[dict[str, str]] = []
    for image_path in images:
        try:
            result = crop_one(
                source=image_path,
                input_root=input_path,
                output_dir=output_dir,
                suffix=args.suffix,
                background_mode=args.background,
                tolerance=args.tolerance,
                padding=args.padding,
                border_width=args.border_width,
                alpha_threshold=args.alpha_threshold,
                scan_step=args.scan_step,
                min_area=args.min_area,
                overwrite=args.overwrite,
            )
            rows.append(result)
            print(f"{result['status']}: {image_path} -> {result['output']}")
        except Exception as exc:  # noqa: BLE001 - image batch job should continue across files
            rows.append(
                {
                    "source": str(image_path),
                    "output": "",
                    "status": "error",
                    "background_rgb": "",
                    "bbox": "",
                    "notes": str(exc),
                }
            )
            print(f"ERROR: {image_path}: {exc}")

    write_report(rows, report_path)
    cropped_count = sum(1 for row in rows if row["status"] == "cropped")
    print(f"Wrote report: {report_path}")
    print(f"Cropped {cropped_count} of {len(rows)} image(s).")
    return 0 if cropped_count > 0 else 2


if __name__ == "__main__":
    sys.exit(main())
