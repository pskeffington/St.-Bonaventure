# Local Workflow

## Pull latest changes

```bash
git pull origin main
```

## Validate repository state

```bash
python scripts/validate_catalog.py
```

Expected result:

```text
Catalog validation passed.
```

## Work on catalog data

Use a branch for major catalog changes:

```bash
git checkout -b catalog/master-catalog-build
```

Edit:

```text
data/relic_catalog_master.csv
```

Then validate:

```bash
python scripts/validate_catalog.py
```

Commit:

```bash
git add data/relic_catalog_master.csv
git commit -m "Populate master relic catalog"
git push -u origin catalog/master-catalog-build
```

## Work on crops

Use a branch:

```bash
git checkout -b images/label-theca-crops
```

Add crops:

```text
images/crops/labels/
images/crops/thecae/
```

Commit separately from catalog edits:

```bash
git add images/crops/labels images/crops/thecae
git commit -m "Add label and theca crops"
git push -u origin images/label-theca-crops
```

## Work on saint notes

Use a branch:

```bash
git checkout -b research/saint-notes-pilot
```

Create notes under:

```text
notes/saints/
```

Commit:

```bash
git add notes/saints
git commit -m "Add pilot saint notes"
git push -u origin research/saint-notes-pilot
```

## Do not do this

Do not edit original images.
Do not rename original images.
Do not mix original image changes with crops.
Do not mark records authenticated from images alone.
Do not overwrite CSV headers.
