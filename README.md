# St. Bonaventure Reliquary Research & Indexing

This repository is a public research and indexing workspace for a Catholic reliquary associated with St. Bonaventure and containing more than 200 relics. The purpose is to preserve the visual record, identify the physical arrangement of the reliquary, transcribe visible saint labels, and build a source-verified theological and historical archive suitable for parish, academic, and public-history publication.

## Current status

Updated at end of day, 2026-05-23.

The current repository state contains the committed original image archive, a visible-label relic index, a saint/entity object register, source-control documentation, publication-roadmap materials, a working literature review, validation tooling, crop-generation tooling, and a visual classification aide for future white-background object photographs.

Current working counts:

| Item | Count |
|---|---:|
| Original JPG files | 36 |
| Visible relic records | 112 |
| Working saint/entity objects | 113 |
| Identity-review objects | 19 |
| Label-review objects | 5 |
| Canonical-status review objects | 3 |
| Sensitive review objects | 1 |

The current index is based on visible labels in the photographs and must be treated as a working transcription until each label, theca inscription, and authentication document is verified.

## Repository structure

```text
data/
  relic_index_visible.csv          Working index of visible labels from uploaded images
  relic_catalog_master.csv         Master catalog schema; not yet populated
  reliquary_sections.csv           Physical section map for visible cases
  saint_objects.jsonl              Working saint/entity object register
  saint_object_summary.csv         Current object-count summary
  image_file_register.csv          Original image checksum and dimension register
  crop_manifest.csv                Coordinate manifest for deterministic crop generation
  visual_class_taxonomy.csv        Visual classification taxonomy for researcher triage
  literature_review_sources.csv    Source-verification tracker

docs/
  cataloging_protocol.md           Rules for transcription, verification, and metadata control
  image_manifest.md                Uploaded image filenames and indexing role
  section_map.md                   Narrative section identification and case layout
  current_status.md                Current working status
  end_of_day_2026-05-23.md         End-of-day project notes
  crop_workflow.md                 Coordinate crop workflow
  white_background_auto_crop.md    White-background crop/classification workflow
  operational_roadmap.md           Publication roadmap
  academic_press_requirements.md   Press-package requirements

scripts/
  validate_catalog.py              Repository/catalog validation
  generate_crops.py                Deterministic crops from crop_manifest.csv
  auto_crop_white_background.py    White-background auto-crop and visual classification aide

manuscript/
  archive_note.md                  Draft public-facing archive note
  literature_review.md             Working literature review
  book_proposal_draft.md           Working academic press proposal

templates/
  saint_note_template.md           Research-note template
  press_proposal_template.md       Press-proposal template
```

## Section logic

The reliquary appears to be organized primarily by saint name, broadly alphabetical, across a sequence of horizontal wall cases. The first pass divides the photographed structure into case sections rather than theological categories. This preserves physical provenance before interpretive classification.

Current working sections:

- Section A: A-series saints and early B-series transition
- Section B: B-series saints, including Beatrice, Benedict, Bernard, Blandina, Bonaventure
- Section C: C-series saints and related martyr groupings
- Section D: D-series saints, including Damian and Dominican saints
- Section E/F/G: Franciscan, Passionist, Jesuit, and Gregory/Gemma/Gaspar/Gabriel groupings visible across the same sequence
- Section H/I/J: Hilary through Joseph/John groupings
- Section L/M: Ladislaus through Martin/Matthew/Maurice/Oliver sequence
- Section P: Paul, Peter, Philip, Pius, Pontian sequence
- Section R/S/T: Robert Bellarmine through Rose, Simon, Stanislaus, Stephen, and Theresa sequence

## Handling rule

Nothing in this repository should be described as authenticated solely from image evidence. Use `visible_label`, `theca_inscription`, document/provenance fields, and `verification_status` separately. A saint label identifies the display position; it does not by itself prove relic identity, class, provenance, or authenticity.

## Current next work

1. Confirm the validation workflow status.
2. Use current wall-case images for provisional crop/catalog development only.
3. Prepare photographer instructions for publication-grade relic/object images.
4. Generate label and theca crops where possible.
5. Populate `data/relic_catalog_master.csv`.
6. Add `case_id`, `panel_id`, and `display_order`.
7. Draft pilot saint notes.
8. Verify Catechism paragraph references, canon-law references, and literature metadata.
