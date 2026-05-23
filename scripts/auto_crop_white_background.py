#!/usr/bin/env python3
"""Auto-crop and visually classify isolated relic/object photos.

This is a researcher-aide tool. It crops objects photographed on a white or
near-white background and assigns a non-canonical visual class to help narrow
review work.

It does not determine first-, second-, or third-class relic status. Canonical
relic class requires documentary evidence such as a theca inscription,
authentication document, custody record, or other provenance evidence.
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

VISUAL_CLASSES = {
    "VCLASS-001": "round_or_oval_theca_or_medallion_candidate",
    "VCLASS-002": "cross_or_openwork_reliquary_candidate",
    "VCLASS-003": "horizontal_label_or_document_strip_candidate",
    "VCLASS-004": "vertical_card_certificate_or_tall_mount_candidate",
    "VCLASS-005": "rectangular_card_certificate_or_case_detail_candidate",
    "VCLASS-006": "irregular_theca_reliquary_or_object_candidate",
    "VCLASS-007": "small_fragment_or_loose_material_candidate",
    "VCLASS-008": "seal_or_wax_impression_candidate",
    "VCLASS-999": "unclassified_visual_object",
}


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
    border = max(1, min(width, w // 4, h // 4))
    sample: list[tuple[int, int, int]] = []
    for y in range(h):
        for x in range(w):
            if x < border or x >= w - border or y < border or y >= h - border:
                sample.append(px[x, y])
    return sample


def median_background(image: Image.Image, border_width: int) -> tuple[int, int, int]:
    sample = border_sample(image, border_width)
    if not sample:
        return (255, 255, 255)
    return (
        int(statistics.median(pixel[0] for pixel in sample)),
        int(statistics.median(pixel[1] for pixel in sample)),
        int(statistics.median(pixel[2] for pixel in sample)),
    )


def pixel_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def foreground_points(
    image: Image.Image,
    background: tuple[int, int, int],
    tolerance: int,
    alpha_threshold: int,
    scan_step: int,
) -> list[tuple[int, int]]:
    rgba = image.convert("RGBA")
    w, h = rgba.size
    px = rgba.load()
    step = max(1, scan_step)
    points: list[tuple[int, int]] = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = px[x, y]
            if a <= alpha_threshold:
                continue
            if pixel_distance((r, g, b), background) > tolerance:
                points.append((x, y))
    return points


def bbox_from_points(
    points: list[tuple[int, int]],
    image_size: tuple[int, int],
    scan_step: int,
) -> tuple[int, int, int, int] | None:
    if not points:
        return None
    w, h = image_size
    step = max(1, scan_step)
    min_x = min(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
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
        return output_dir / rel.parent / f"{rel.stem}{suffix}{rel.suffix.lower()}"
    return output_dir / f"{source.stem}{suffix}{source.suffix.lower()}"


def visual_classification(
    bbox: tuple[int, int, int, int],
    foreground_pixel_count: int,
    image_size: tuple[int, int],
) -> dict[str, str]:
    left, top, right, bottom = bbox
    width = max(1, right - left)
    height = max(1, bottom - top)
    aspect = width / height
    fill = foreground_pixel_count / max(1, width * height)
    image_fill = (width * height) / max(1, image_size[0] * image_size[1])

    if width < 120 and height < 120:
        class_id = "VCLASS-007"
        confidence = "low"
        rationale = "Detected object is very small in pixel dimensions."
        next_step = "Retake with macro focus and scale card; inspect whether this is loose material, dust, label artifact, or image noise."
    elif 0.85 <= aspect <= 1.18 and 0.58 <= fill <= 0.92:
        class_id = "VCLASS-001"
        confidence = "medium"
        rationale = "Near-round bounding box and moderate-to-high foreground fill."
        next_step = "Inspect front and reverse; capture theca paper inscription and seal/thread details."
    elif 0.55 <= aspect <= 1.45 and fill < 0.55:
        class_id = "VCLASS-002"
        confidence = "low"
        rationale = "Near-square/tall object with lower fill ratio, consistent with openwork or cross-like negative space."
        next_step = "Review manually for cross arms, ring, suspension loop, and theca placement."
    elif aspect >= 2.6 and fill >= 0.35:
        class_id = "VCLASS-003"
        confidence = "medium"
        rationale = "Wide horizontal object."
        next_step = "Run OCR or manual transcription; likely label strip, document strip, or horizontal certificate detail."
    elif aspect <= 0.45 and fill >= 0.35:
        class_id = "VCLASS-004"
        confidence = "medium"
        rationale = "Tall narrow object."
        next_step = "Inspect whether this is a vertical card, certificate, tall mount, or long reliquary object."
    elif 0.55 <= aspect <= 1.85 and fill >= 0.78 and image_fill > 0.20:
        class_id = "VCLASS-005"
        confidence = "medium"
        rationale = "Rectangular or card-like object with high fill ratio."
        next_step = "Check for certificate text, card borders, typed labels, or mounted display backing."
    elif 0.55 <= aspect <= 1.85 and 0.38 <= fill < 0.78:
        class_id = "VCLASS-006"
        confidence = "low"
        rationale = "Object is bounded but visually irregular."
        next_step = "Manual review required; may be theca, reliquary object, seal, or mixed object/background."
    else:
        class_id = "VCLASS-999"
        confidence = "low"
        rationale = "Geometry did not match a controlled visual class."
        next_step = "Manual review required; retake on cleaner background if needed."

    return {
        "visual_class_id": class_id,
        "visual_class_label": VISUAL_CLASSES[class_id],
        "visual_class_confidence": confidence,
        "visual_class_rationale": rationale,
        "research_next_step": next_step,
    }


def physical_size_estimate(
    bbox: tuple[int, int, int, int], dpi: float | None
) -> tuple[str, str, str]:
    left, top, right, bottom = bbox
    width_px = right - left
    height_px = bottom - top
    if not dpi or dpi <= 0:
        return "", "", "No DPI or scale reference supplied. Physical size cannot be estimated."
    width_mm = width_px / dpi * 25.4
    height_mm = height_px / dpi * 25.4
    return f"{width_mm:.2f}", f"{height_mm:.2f}", "Estimated from supplied DPI; use ruler/scale card for publication-grade measurement."


def base_result(source: Path, status: str, notes: str = "") -> dict[str, str]:
    return {
        "source": str(source),
        "output": "",
        "status": status,
        "background_rgb": "",
        "bbox": "",
        "bbox_width_px": "",
        "bbox_height_px": "",
        "foreground_pixel_count": "",
        "bbox_fill_ratio": "",
        "visual_class_id": "VCLASS-999",
        "visual_class_label": VISUAL_CLASSES["VCLASS-999"],
        "visual_class_confidence": "none",
        "visual_class_rationale": "No reliable foreground object was classified.",
        "canonical_relic_class_status": "requires_theca_or_documentary_verification",
        "estimated_width_mm": "",
        "estimated_height_mm": "",
        "measurement_notes": "",
        "research_next_step": "Manual review required.",
        "notes": notes,
    }


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
    dpi: float | None,
) -> dict[str, str]:
    with Image.open(source) as image:
        image.load()
        background = median_background(image, border_width) if background_mode == "auto" else (255, 255, 255)
        points = foreground_points(image, background, tolerance, alpha_threshold, scan_step)
        bbox = bbox_from_points(points, image.size, scan_step)

        if bbox is None:
            result = base_result(source, "no_foreground_detected", "Check white background, shadows, and tolerance setting.")
            result["background_rgb"] = str(background)
            return result

        padded = pad_bbox(bbox, padding, image.size)
        area = bbox_area(padded)
        if area < min_area:
            result = base_result(source, "foreground_below_min_area", f"Area {area} below min_area {min_area}.")
            result["background_rgb"] = str(background)
            result["bbox"] = str(padded)
            result["bbox_width_px"] = str(padded[2] - padded[0])
            result["bbox_height_px"] = str(padded[3] - padded[1])
            result["foreground_pixel_count"] = str(len(points))
            return result

        output = output_path_for(source, input_root, output_dir, suffix)
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists() and not overwrite:
            status = "skipped_exists"
        else:
            image.crop(padded).save(output, quality=95)
            status = "cropped"

        left, top, right, bottom = bbox
        width_px = max(1, right - left)
        height_px = max(1, bottom - top)
        fill_ratio = len(points) / max(1, width_px * height_px)
        class_result = visual_classification(bbox, len(points), image.size)
        width_mm, height_mm, measurement_notes = physical_size_estimate(bbox, dpi)

        result = {
            "source": str(source),
            "output": str(output),
            "status": status,
            "background_rgb": str(background),
            "bbox": str(padded),
            "bbox_width_px": str(padded[2] - padded[0]),
            "bbox_height_px": str(padded[3] - padded[1]),
            "foreground_pixel_count": str(len(points)),
            "bbox_fill_ratio": f"{fill_ratio:.4f}",
            "canonical_relic_class_status": "requires_theca_or_documentary_verification",
            "estimated_width_mm": width_mm,
            "estimated_height_mm": height_mm,
            "measurement_notes": measurement_notes,
            "notes": "Use --overwrite to replace." if status == "skipped_exists" else "",
        }
        result.update(class_result)
        return result


def write_report(rows: list[dict[str, str]], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "source",
        "output",
        "status",
        "background_rgb",
        "bbox",
        "bbox_width_px",
        "bbox_height_px",
        "foreground_pixel_count",
        "bbox_fill_ratio",
        "visual_class_id",
        "visual_class_label",
        "visual_class_confidence",
        "visual_class_rationale",
        "canonical_relic_class_status",
        "estimated_width_mm",
        "estimated_height_mm",
        "measurement_notes",
        "research_next_step",
        "notes",
    ]
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auto-crop and visually classify isolated object photos.")
    parser.add_argument("--input", required=True, help="Input image or directory.")
    parser.add_argument("--output-dir", required=True, help="Directory for cropped outputs.")
    parser.add_argument("--suffix", default="_autocrop", help="Output filename suffix.")
    parser.add_argument("--background", choices=["white", "auto"], default="auto")
    parser.add_argument("--tolerance", type=int, default=35)
    parser.add_argument("--padding", type=int, default=40)
    parser.add_argument("--border-width", type=int, default=20)
    parser.add_argument("--alpha-threshold", type=int, default=0)
    parser.add_argument("--scan-step", type=int, default=1)
    parser.add_argument("--min-area", type=int, default=1000)
    parser.add_argument("--dpi", type=float, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--report", default="data/auto_crop_report.csv")
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
                dpi=args.dpi,
            )
            rows.append(result)
            print(
                f"{result['status']}: {image_path} -> {result['output']} | "
                f"visual_class={result['visual_class_id']}:{result['visual_class_label']} | "
                f"canonical_status={result['canonical_relic_class_status']}"
            )
        except Exception as exc:  # noqa: BLE001
            result = base_result(image_path, "error", str(exc))
            rows.append(result)
            print(f"ERROR: {image_path}: {exc}")

    write_report(rows, report_path)
    cropped_count = sum(1 for row in rows if row["status"] == "cropped")
    print(f"Wrote report: {report_path}")
    print(f"Cropped {cropped_count} of {len(rows)} image(s).")
    return 0 if cropped_count > 0 else 2


if __name__ == "__main__":
    sys.exit(main())
