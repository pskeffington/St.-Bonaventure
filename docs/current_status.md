# Current Status

Updated at end of day, 2026-05-23.

## Counts

| Item | Count |
|---|---:|
| Original JPG files | 36 |
| Visible relic records | 112 |
| Working saint/entity objects | 113 |
| Identity-review objects | 19 |
| Label-review objects | 5 |
| Canonical-status review objects | 3 |
| Sensitive review objects | 1 |

## Completed

- Original images committed under `images/original/`.
- Image register created with checksums and dimensions.
- Visible relic index created.
- Section map created.
- Saint object register created.
- Source register created.
- Literature review drafted.
- Catechism of the Catholic Church designated as the key doctrinal source.
- Validation script added.
- GitHub Actions validation workflow added.
- Contribution, governance, and local workflow documents added.
- Deterministic crop manifest workflow added.
- White-background auto-crop script added.
- Visual classification aide added.
- Visual class taxonomy added.
- End-of-day notes added at `docs/end_of_day_2026-05-23.md`.

## Current scripts

| Script | Function |
|---|---|
| `scripts/validate_catalog.py` | Validates repository structure, image references, checksums, and catalog fields |
| `scripts/generate_crops.py` | Generates crops from coordinates in `data/crop_manifest.csv` |
| `scripts/auto_crop_white_background.py` | Auto-crops isolated white-background object photos and assigns visual classes |

## Current data files

| File | Function |
|---|---|
| `data/relic_index_visible.csv` | Working visible-label relic index |
| `data/relic_catalog_master.csv` | Master catalog schema, not yet populated |
| `data/saint_objects.jsonl` | Working saint/entity objects |
| `data/saint_object_summary.csv` | Saint-object count summary |
| `data/image_file_register.csv` | Image checksum and dimension register |
| `data/crop_manifest.csv` | Manual crop-coordinate manifest |
| `data/visual_class_taxonomy.csv` | Controlled taxonomy for visual classification aide |
| `data/literature_review_sources.csv` | Literature/source verification tracker |

## Open issues

| Issue | Work | Status |
|---|---|---|
| #1 | Commit original image archive | Closed |
| #2 | Generate label and theca crops | Open |
| #3 | Populate master relic catalog | Open |
| #4 | Create pilot saint notes | Open |
| #5 | Monitor validation workflow | Open |
| #6 | Verify source metadata and references | Open |

## Next order of work

1. Confirm validation workflow status.
2. Work with current images for provisional crop/catalog development.
3. Prepare photographer instructions for publication-grade relic images.
4. Generate label and theca crops where possible.
5. Populate `data/relic_catalog_master.csv`.
6. Add `case_id`, `panel_id`, and `display_order`.
7. Draft pilot saint notes.
8. Verify Catechism paragraph references, canon-law references, and literature metadata.

## Readiness

The project is in controlled archive-building status. It is not final publication copy.

## Evidence rule

Visible labels support indexing, not authentication. Final claims about relic class, custody, authenticity, and provenance require theca-level and documentary review.
