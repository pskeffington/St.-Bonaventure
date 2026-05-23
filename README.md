# St. Bonaventure Reliquary Research & Indexing

This repository is a public research and indexing workspace for a Catholic reliquary associated with St. Bonaventure and containing more than 200 relics. The immediate purpose is to preserve the visual record, identify the physical arrangement of the reliquary, transcribe visible saint labels, and build a source-verified theological and historical archive suitable for parish, academic, and public-history publication.

## Current status

Initial repository scaffold created from the first uploaded image set. The images show a wall-mounted reliquary composed of multiple illuminated wooden display cases with red fabric backing, brass name plates, and individually mounted thecae/reliquaries. The current index is based only on visible labels in the photographs and must be treated as a working transcription until each label, theca inscription, and authentication document is verified.

## Repository structure

```text
data/
  relic_index_visible.csv        Working index of visible labels from uploaded images
  reliquary_sections.csv         Physical section map for the visible reliquary cases
docs/
  cataloging_protocol.md         Rules for transcription, verification, and metadata control
  image_manifest.md              Uploaded image filenames and indexing role
  section_map.md                 Narrative section identification and case layout
manuscript/
  archive_note.md                Draft public-facing archive note
README.md
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

Nothing in this repository should be described as authenticated solely from image evidence. Use `visible_label`, `theca_inscription`, `auth_document`, and `verification_status` separately. A saint label identifies the display position; it does not by itself prove relic identity, class, provenance, or authenticity.

## Next work

1. Add the original 36 image files under `images/original/`.
2. Create cropped label images under `images/crops/labels/`.
3. Create cropped theca images under `images/crops/thecae/`.
4. Reconcile every brass label against the paper inscription inside each theca.
5. Add any certificate/authentication metadata in `data/authentication_register.csv`.
6. Build a publishable historical note for each confirmed relic.
