# Repository Governance

## Working principle

This repository is an evidence-controlled archive. Data structure and evidence quality matter more than speed of interpretation.

## Branch policy

Current default branch: `main`.

Recommended working branches:

- `catalog/master-catalog-build`
- `images/label-crops`
- `research/saint-notes-pilot`
- `manuscript/theological-framework`
- `provenance/certificate-register`

Use pull requests for major data or manuscript changes once the initial scaffold stabilizes.

## Issue labels

Recommended labels:

- `archive`
- `images`
- `catalog`
- `data`
- `research`
- `manuscript`
- `provenance`
- `theology`
- `publication`
- `sprint-01`
- `needs-review`
- `blocked`

## Milestones

Recommended milestones:

1. `Sprint 01 — Catalog completion`
2. `Sprint 02 — Theca and certificate review`
3. `Sprint 03 — Saint research pilot`
4. `Sprint 04 — Theological framework`
5. `Sprint 05 — Press proposal package`

## Review rules

A catalog row is reviewable only when it has:

- Stable `record_id`.
- Section assignment.
- Source image.
- Visible label transcription.
- Confidence grade.
- Verification status.

A manuscript claim is reviewable only when it has:

- Clearly identified evidence layer.
- Source or citation placeholder.
- No authentication overclaim.

## Protected claims

The following language should be avoided unless documentary support exists:

- authenticated relic
- confirmed relic
- first-class relic
- episcopally sealed
- certified by
- original certificate
- provenance established

Acceptable image-only language:

- visible label reads
- display identifies the relic as
- theca inscription appears to read
- image evidence supports
- pending certificate review

## Repository health checks

Run:

```bash
python scripts/validate_catalog.py
```

before pushing catalog or image-reference changes.
