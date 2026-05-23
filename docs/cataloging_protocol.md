# Cataloging Protocol

## Purpose

This protocol controls how the St. Bonaventure reliquary is indexed. The governing rule is separation of visual transcription from theological, historical, and canonical claims.

## Core fields

Each relic record should preserve the following fields:

- `record_id`: stable local identifier.
- `section_id`: physical display section.
- `visible_label`: transcription of the brass display plate.
- `normalized_name`: modern normalized saint name for research use.
- `theca_inscription_visible`: transcription of the visible paper label inside the theca, when legible.
- `source_images`: image filenames supporting the record.
- `confidence`: high, medium, low.
- `verification_status`: visible_label_only, visible_label_plus_theca, certificate_verified, unresolved, rejected.
- `notes`: transcription issues, variant spellings, duplicates, or conflicts.

## Transcription rules

Transcribe the brass label exactly before normalizing. Preserve spelling variants such as `S. APOLONIA`, `S. OLIVER PLUKETT`, or `S. GABRIEL LALEMENT` in the visible label field even when the normalized name is corrected.

Use `S.` as displayed when the plate uses `S.`. Do not expand silently to Saint in the transcription field. Expansion belongs in prose, not in the raw transcription.

Do not infer relic class from the name plate. A brass label identifies the display position, not the relic class.

## Theca rules

A theca inscription may support, refine, or conflict with the brass label. Treat it as a separate evidence layer. Abbreviations such as `M.`, `C.`, `V.`, `Ep.`, `Ab.`, or `P.` should be transcribed as visible and interpreted only in notes after review.

## Authentication rules

A relic should not be marked authenticated unless there is a certificate, seal documentation, reliquary provenance record, parish inventory, or other institutional documentation. Image evidence alone is never enough for authentication status.

## Confidence rules

High confidence means the brass label is fully legible in a close-up or clear wide shot. Medium confidence means the label is legible but angled, partially obstructed, or dependent on more than one photograph. Low confidence means the label is partial, edge-cut, blurred, or inferred from a theca inscription.

## File handling

Original images should be stored without alteration under `images/original/`. Cropped labels should be stored under `images/crops/labels/`. Cropped thecae should be stored under `images/crops/thecae/`. Do not overwrite originals.

## Publication rule

The public archive should distinguish three layers: physical display, historical identity of the saint, and verified relic provenance. These layers must not be collapsed.
