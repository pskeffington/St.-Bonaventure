# Crop Workflow

## Can crops be done in Git?

Git can store, version, review, and validate crops. Git itself does not create image crops. Cropping must be performed by a script or image tool, then the generated files are committed to Git.

This repository now supports deterministic crop generation through:

- `data/crop_manifest.csv`
- `scripts/generate_crops.py`
- `requirements.txt`

## Folder targets

```text
images/crops/labels/
images/crops/thecae/
```

## Manifest format

`data/crop_manifest.csv` has this schema:

```csv
record_id,crop_type,source_image,x,y,width,height,output_path,status,notes
```

Field meanings:

| Field | Meaning |
|---|---|
| `record_id` | Relic record ID, e.g. `REL-0001` |
| `crop_type` | `label` or `theca` |
| `source_image` | Original image filename in `images/original/` |
| `x` | Left pixel coordinate |
| `y` | Top pixel coordinate |
| `width` | Crop width in pixels |
| `height` | Crop height in pixels |
| `output_path` | Where the generated crop should be written |
| `status` | Use `ready`, `approved`, or `generate` to generate |
| `notes` | Any uncertainty or review note |

## Example rows

```csv
REL-0001,label,IMG_3237.JPG,100,200,400,120,images/crops/labels/REL-0001_label.jpg,ready,Andrew Corsini brass label
REL-0001,theca,IMG_3237.JPG,100,350,400,400,images/crops/thecae/REL-0001_theca.jpg,ready,Andrew Corsini theca
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_crops.py
```

## Commit generated crops

```bash
git add data/crop_manifest.csv images/crops/labels images/crops/thecae
git commit -m "Add generated label and theca crops"
git push
```

## Recommended workflow

Do not manually rename crops after generation. Put the intended output filename into `crop_manifest.csv`, run the script, inspect outputs, then commit.

## Review rule

Crops should not replace original images. Originals stay untouched under `images/original/`.
