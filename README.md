# St. Bonaventure Reliquary Research & Indexing

Public research and indexing workspace for a Catholic reliquary associated with St. Bonaventure and containing more than 200 relics. The project preserves the visual record, indexes the physical arrangement, transcribes visible labels, and develops a source-verified theological and historical archive suitable for parish, academic, and public-history use.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active archival, provenance, and public-history research workspace; object identity and authenticity remain subject to documentary verification.  
**Last documentation refresh:** 2026-08-17

## Public-interest research boundary

This repository is maintained for archival scholarship, religious material-culture research, public history, provenance documentation, and reproducible indexing.

It does not authenticate relics solely from photographs or visible labels, issue ecclesiastical determinations, replace diocesan or specialist review, assign devotional status, or treat provisional transcriptions as verified provenance. Public claims should preserve the distinction between visible evidence, documentary evidence, scholarly interpretation, and unresolved uncertainty.

## Current research status

- Stage: structured cataloging and provenance-review workspace
- Evidence status: image archive, visible-label index, entity register, and validation tooling available; documentary verification remains incomplete
- Data status: repository-controlled images, structured catalog records, source notes, and publication-support materials
- Primary limitation: visible labels and image evidence alone cannot establish relic identity, class, provenance, or authenticity

The current index should therefore be treated as a working transcription layer rather than a completed authenticated catalog.

## Repository structure

```text
data/
  relic_index_visible.csv          Working index of visible labels
  relic_catalog_master.csv         Master catalog schema
  reliquary_sections.csv           Physical section map
  saint_objects.jsonl              Working saint/entity object register
  saint_object_summary.csv         Current object-count summary
  image_file_register.csv          Image checksum and dimension register
  crop_manifest.csv                Deterministic crop manifest
  visual_class_taxonomy.csv        Researcher-triage taxonomy
  literature_review_sources.csv    Source-verification tracker

docs/
  cataloging_protocol.md           Transcription and verification rules
  image_manifest.md                Image filenames and indexing role
  section_map.md                   Section identification and case layout
  current_status.md                Current working status
  crop_workflow.md                 Coordinate crop workflow
  white_background_auto_crop.md    White-background crop/classification workflow
  operational_roadmap.md           Historical publication roadmap filename
  academic_press_requirements.md   Press-package requirements

scripts/
  validate_catalog.py              Repository/catalog validation
  generate_crops.py                Deterministic crop generation
  auto_crop_white_background.py    White-background crop/classification aide

manuscript/
  archive_note.md                  Draft public-facing archive note
  literature_review.md             Working literature review
  book_proposal_draft.md           Working academic press proposal

templates/
  saint_note_template.md           Research-note template
  press_proposal_template.md       Press-proposal template
```

## Provenance and verification model

Nothing in this repository should be described as authenticated solely from image evidence. Keep these evidence types separate:

- `visible_label`
- `theca_inscription`
- authentication or provenance documents
- scholarly reference sources
- researcher interpretation
- `verification_status`

A visible saint label identifies a display position or transcription candidate; it does not independently prove relic identity, class, provenance, or authenticity.

## Current research priorities

1. Continue catalog validation and provenance review.
2. Generate and review label and theca crops where image quality permits.
3. Populate `data/relic_catalog_master.csv` with explicit evidence status.
4. Add stable physical-location fields such as `case_id`, `panel_id`, and `display_order`.
5. Draft pilot saint notes with source citations and uncertainty labels.
6. Verify Catechism, canon-law, hagiographic, and historical references before publication-weight use.
7. Keep historical milestones in dated documentation rather than using them as the headline project status.

## Documentation standards

- Preserve original image provenance and checksums.
- Keep transcription separate from interpretation.
- Record source citations and verification status for every substantive identity or historical claim.
- Use uncertainty labels when inscriptions, names, or documentary evidence are incomplete.
- Avoid describing provisional catalog records as authenticated objects.
- Keep publication-facing prose traceable to catalog records and source notes.

## Supported contribution

A reproducible archival and public-history framework for indexing, documenting, and researching a reliquary while preserving evidence provenance and uncertainty.

## Unsupported contribution

No image-only authentication, ecclesiastical determination, devotional ruling, or unsupported provenance claim is made.
