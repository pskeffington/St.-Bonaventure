# Contributing

## Repository purpose

This repository supports the structured cataloging and publication of the St. Bonaventure reliquary. Contributions must preserve the distinction between visual evidence, transcription, historical research, theological interpretation, and documentary authentication.

## Evidence hierarchy

Use this order:

1. Original image file.
2. Brass display label transcription.
3. Theca inscription transcription.
4. Certificate or institutional provenance document.
5. Historical research.
6. Theological interpretation.

Do not collapse these layers.

## File rules

- Original images belong in `images/original/`.
- Original images must not be edited, renamed, cropped, or overwritten.
- Label crops belong in `images/crops/labels/`.
- Theca crops belong in `images/crops/thecae/`.
- Certificate images belong in `images/certificates/`.
- Data tables belong in `data/`.
- Research notes belong in `notes/saints/`.
- Book material belongs in `manuscript/`.

## Naming rules

Relic records use stable IDs:

```text
REL-0001
REL-0002
REL-0003
```

Crop names must follow record IDs:

```text
REL-0001_label.jpg
REL-0001_theca.jpg
```

For group relics:

```text
REL-0024_theca_a.jpg
REL-0024_theca_b.jpg
REL-0024_theca_c.jpg
```

## Catalog rules

- Preserve exact brass label spelling in `visible_label`.
- Put corrected or standardized names in `normalized_name`.
- Do not silently correct spelling variants.
- Do not mark any relic as authenticated unless document evidence exists.
- Use notes for uncertainty.
- Use controlled confidence values: `high`, `medium`, `low`.
- Use controlled verification statuses from `docs/cataloging_protocol.md`.

## Validation

Run before pushing:

```bash
python scripts/validate_catalog.py
```

The GitHub Action also runs this validation on push and pull request.

## Commit discipline

Use separate commits for different evidence layers:

- Original images.
- Label/theca crops.
- Data-table updates.
- Saint research notes.
- Manuscript prose.
- Certificate/provenance records.

Do not mix original image commits with generated crops.

## Publication rule

The repository may support theological and historical publication, but the data must remain honest about evidence limits. A visible label is not an authentication document.
