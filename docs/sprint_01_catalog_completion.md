# Sprint 01 — Catalog Completion and Evidence Control

## Objective

Move the project from a visible-label first pass to a controlled master catalog ready for theological and historical research.

## Priority order

### 1. Stabilize image archive

Create folders locally:

```bash
mkdir -p images/original images/crops/labels images/crops/thecae images/certificates notes/saints
```

Move all original JPG files into:

```text
images/original/
```

Commit them:

```bash
git add images/original
git commit -m "Add original reliquary image set"
git push
```

### 2. Generate label crops

For every visible brass plate, create one crop named:

```text
images/crops/labels/REL-0001_label.jpg
```

Use the record ID from `data/relic_index_visible.csv`.

### 3. Generate theca crops

For every theca, create one crop named:

```text
images/crops/thecae/REL-0001_theca.jpg
```

If multiple thecae correspond to one group label, use suffixes:

```text
REL-0024_theca_a.jpg
REL-0024_theca_b.jpg
REL-0024_theca_c.jpg
```

### 4. Build master catalog

Populate `data/relic_catalog_master.csv` from `data/relic_index_visible.csv`.

Add:

- `case_id`
- `panel_id`
- `display_order`
- `group_or_individual`
- `label_crop`
- `theca_crop`
- `publication_status`

### 5. Correct uncertain readings

Immediate audit targets:

- S. Charbel Makhlouf / Makhlouf spelling.
- S. Gabriel Lalemant / Lalement spelling.
- S. Francis of Hieronymo; likely Francis de Geronimo.
- S. Francis of Rome; likely Frances of Rome.
- S. Oliver Plukett; standard Oliver Plunkett.
- S. Madeline Sophia Barat; standard Madeleine Sophie Barat.
- S. Joachim partial entry.
- Group labels with multiple thecae.
- Duplicate Paul of the Cross labels.

### 6. Authentication register

Populate `data/authentication_register.csv` only after document review. Do not infer document existence from the display.

### 7. Saint notes pilot batch

Create ten pilot notes under `notes/saints/`:

- REL-0016 Bonaventure
- REL-0038 Francis of Assisi
- REL-0039 Francis of Assisi and Clare
- REL-0054 Ignatius of Loyola
- REL-0074 Longinus
- REL-0084 Martin de Porres
- REL-0087 Oliver Plunkett
- REL-0094 Peter Canisius
- REL-0101 Robert Bellarmine
- REL-0108 Stanislaus Kostka

Each note should follow the template in `templates/saint_note_template.md` once created.

## Completion criteria

Sprint 01 is complete when:

- All images are stored under `images/original/`.
- Every visible relic has a label crop.
- Every visible relic has a theca crop or a note explaining why unavailable.
- `relic_catalog_master.csv` is populated.
- First ten saint notes exist.
- Uncertain readings are flagged, not silently corrected.
