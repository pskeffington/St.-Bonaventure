# White-Background Auto-Crop Workflow

## Purpose

`scripts/auto_crop_white_background.py` crops isolated relic, theca, certificate, or object images photographed on a white or near-white background.

It detects pixels that differ from the background, finds the bounding box, adds padding, saves a cropped image, and writes a CSV report with basic visual measurements.

## Important limit

This script is for isolated object photographs on white/light backgrounds. It is not designed for the red-lined wall reliquary case photographs. For the red case images, use manual crop coordinates or the coordinate manifest workflow.

## Canonical relic class limit

The script cannot determine canonical relic class from size and shape alone.

It therefore reports two separate fields:

| Field | Meaning |
|---|---|
| `visual_design_guess` | Shape/container/design estimate from image geometry |
| `canonical_relic_class_guess` | Always `not_determinable_from_image_alone` |

Canonical class requires theca inscription, certificate, or provenance evidence. A photo can suggest that an item is a theca, medallion, cross-shaped reliquary, document strip, or certificate, but it cannot prove first-class, second-class, or third-class relic status.

## Install dependency

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Single-image crop

Example:

```bash
python scripts/auto_crop_white_background.py \
  --input images/white_background/REL-0001_full.jpg \
  --output-dir images/crops/auto \
  --padding 50 \
  --tolerance 35 \
  --overwrite
```

## Directory batch crop

Example:

```bash
python scripts/auto_crop_white_background.py \
  --input images/white_background \
  --output-dir images/crops/auto \
  --padding 50 \
  --tolerance 35 \
  --overwrite
```

## Optional physical-size estimate

Physical size cannot be known from pixels unless there is a scale reference. If the photographer includes a ruler/scale card and you know pixels per inch, pass DPI:

```bash
python scripts/auto_crop_white_background.py \
  --input images/white_background \
  --output-dir images/crops/auto \
  --dpi 300 \
  --overwrite
```

For publication-grade work, require a ruler or scale card in at least one reference image per photography setup.

## Output report

The script writes cropped images to the output directory and writes a CSV report:

```text
data/auto_crop_report.csv
```

The report includes:

- source image
- output image
- crop status
- detected bounding box
- crop dimensions in pixels
- foreground pixel count
- fill ratio
- visual design guess
- visual design confidence
- canonical relic class guess
- estimated physical dimensions if DPI was supplied

## Visual design guesses

Possible design guesses include:

```text
round_or_oval_theca_or_medallion
openwork_or_cross_shaped_reliquary_candidate
horizontal_label_or_document_strip
vertical_card_certificate_or_tall_reliquary
rectangular_card_certificate_or_case_detail
irregular_theca_reliquary_or_object
unclassified_visual_object
```

These are design/object-shape categories, not theological or canonical classes.

## Recommended tuning

If too much background remains:

```bash
--tolerance 25
```

If the crop cuts into the relic/object:

```bash
--padding 80
```

If shadows are being detected as part of the object:

```bash
--tolerance 50
```

## Example full command

```bash
python scripts/auto_crop_white_background.py \
  --input images/white_background \
  --output-dir images/crops/auto \
  --background auto \
  --tolerance 40 \
  --padding 60 \
  --overwrite
```

## Photography guidance for future publication images

For every relic/theca/object photo, ask the photographer to capture:

- one full object image on white or neutral background
- one close theca-inscription image
- one close relic-material image where permitted
- one image with a scale card or ruler
- one reverse/back image if seals or threads are visible
- one color reference card image per session if available

Use stable filenames tied to catalog IDs once assigned:

```text
REL-0001_full.jpg
REL-0001_theca_front.jpg
REL-0001_theca_label.jpg
REL-0001_scale.jpg
REL-0001_reverse.jpg
```

## Commit outputs

After review:

```bash
git add scripts/auto_crop_white_background.py docs/white_background_auto_crop.md data/auto_crop_report.csv images/crops/auto
git commit -m "Add white-background auto-crops"
git push origin main
```
