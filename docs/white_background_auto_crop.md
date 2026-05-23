# White-Background Auto-Crop Workflow

## Purpose

`scripts/auto_crop_white_background.py` crops isolated relic, theca, certificate, or object images photographed on a white or near-white background.

It detects pixels that differ from the background, finds the bounding box, adds padding, and saves a cropped image.

## Important limit

This script is for isolated object photographs on white/light backgrounds. It is not designed for the red-lined wall reliquary case photographs. For the red case images, use manual crop coordinates or the coordinate manifest workflow.

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

## Output

The script writes cropped images to the output directory and writes a CSV report:

```text
data/auto_crop_report.csv
```

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

## Commit outputs

After review:

```bash
git add scripts/auto_crop_white_background.py docs/white_background_auto_crop.md data/auto_crop_report.csv images/crops/auto
git commit -m "Add white-background auto-crops"
git push origin main
```
