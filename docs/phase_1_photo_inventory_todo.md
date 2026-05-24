# Phase 1 Photo Inventory To-Do List

## Purpose

This checklist defines the first photography pass for inventory and identification of the St. Bonaventure reliquary collection. The goal is not publication-grade object photography. The goal is to create a complete, auditable visual inventory that supports section mapping, visible-label transcription, theca-level identification, and later catalog population.

This phase should preserve the physical arrangement of the reliquary before any interpretive or devotional classification is imposed.

## Scope

Phase 1 photography covers:

- whole-reliquary context images;
- case-by-case section images;
- row and shelf sequence images;
- individual display-position images;
- visible saint-label images;
- theca-front images where accessible;
- reverse/side/context images only where they can be taken without disturbing the object;
- authentication-document images only if already present and safely accessible.

Phase 1 does not cover:

- white-background object photography;
- artistic publication photography;
- removal of relics from thecae;
- cleaning, polishing, repair, or repositioning beyond ordinary safe access;
- claims of authentication based on photographs alone.

## File-naming rule

Use stable, sortable filenames. Do not rely on phone-generated names as the catalog identifier.

Recommended pattern:

```text
SB_PHASE1_CASE-{case_id}_PANEL-{panel_id}_ROW-{row}_POS-{position}_{view}_{YYYYMMDD}_{seq}.jpg
```

Example:

```text
SB_PHASE1_CASE-B_PANEL-01_ROW-02_POS-05_label_20260524_001.jpg
```

Recommended view values:

```text
context
case
panel
row
position
label
theca_front
theca_side
document
uncertain
```

## Before photographing

- Confirm camera date/time is correct.
- Photograph a written session card with date, location, photographer, camera/phone model, and lighting condition.
- Do not delete blurry images in the field; mark them later as rejected or duplicate.
- Photograph each section in sequence from left to right and top to bottom.
- Keep the original image files unchanged.
- Record any object movement, access limits, glare, occlusion, or uncertainty in a session note.

## Shot sequence

### 1. Full reliquary context

Capture the entire reliquary or display wall before close photography.

Required shots:

- full frontal image of the entire reliquary area;
- left oblique context image;
- right oblique context image;
- close context image showing how cases relate to each other;
- any case labels, room labels, or display notes visible near the reliquary.

Inventory purpose:

- establishes physical provenance;
- prevents loss of arrangement data;
- supports later section mapping.

### 2. Case-level images

Photograph each visible case or major horizontal section as a discrete unit.

Required shots for each case:

- straight-on full case image;
- left half of case;
- right half of case;
- top row area;
- middle row area;
- bottom row area;
- any case border, hinge, lock, tag, or construction detail relevant to physical mapping.

Inventory purpose:

- assigns `case_id`;
- supports row and panel mapping;
- anchors individual relic-position records to a physical section.

### 3. Row or shelf sequence images

Photograph each row in order, even if individual labels will also be photographed.

Required shots:

- full row, left-to-right;
- overlapping row segments if one image cannot capture all labels clearly;
- duplicate row image with slightly different angle if glare is present.

Inventory purpose:

- preserves display order;
- supports `display_order` assignment;
- prevents orphan labels detached from their original sequence.

### 4. Individual display-position images

Photograph each visible display position as its own record.

Required shots:

- object/theca and label together;
- object/theca centered;
- label centered;
- wider image showing neighboring objects on both sides when possible.

Inventory purpose:

- creates one working object candidate per display position;
- allows later matching between label, theca, and section map;
- helps detect duplicate saints, uncertain placements, or merged labels.

### 5. Visible-label images

Photograph every visible saint/entity label clearly enough for transcription.

Required shots:

- straight-on label image;
- angled label image if glare or curvature interferes;
- label plus immediately adjacent object;
- label plus neighboring label if display order may be ambiguous.

Inventory purpose:

- supports `visible_label` transcription;
- separates reading confidence from object authentication;
- creates evidence for review flags such as illegible, partial, duplicate, or uncertain.

### 6. Theca-front images

Photograph the front of each theca where accessible without unsafe handling.

Required shots:

- full theca front;
- close view of any visible inscription, seal, thread, wax, paper, or internal label;
- label and theca together.

Inventory purpose:

- supports later distinction between display label and theca inscription;
- preserves evidence for `theca_inscription`, `seal_visible`, `thread_visible`, and `relic_class_claimed` fields if those fields are later used.

### 7. Reverse, side, or document images only if safely accessible

Do not disturb sealed objects to obtain reverse images. If the case or object can be safely viewed from another angle without removal, photograph it.

Optional shots:

- side view of theca;
- reverse view of theca;
- visible authentication paper;
- visible catalog card;
- envelope, tag, or storage note associated with the object.

Inventory purpose:

- documents provenance clues;
- supports later authentication-document matching;
- identifies which objects require follow-up photography.

## Minimum metadata to record per photo group

Use a field notebook, spreadsheet, or later CSV intake file. Record at least:

```text
session_id
photo_filename
case_id
panel_id
row
position
view_type
visible_label_raw
visible_label_confidence
neighbor_left
neighbor_right
glare_or_blur
occlusion
handling_status
notes
```

Recommended confidence values:

```text
clear
probable
partial
illegible
not_visible
```

Recommended handling values:

```text
not_handled
case_opened_only
object_lifted
object_rotated
unsafe_not_attempted
unknown
```

## Inventory-control rules

- One display position should receive one provisional object ID, even if the label is uncertain.
- Do not merge two visible labels into one record unless the physical arrangement clearly shows they belong to the same object.
- Do not split one object into multiple records unless separate labels or thecae support doing so.
- Maintain the original physical order before sorting alphabetically.
- Mark uncertainty explicitly instead of correcting silently.
- Keep `visible_label`, `normalized_name`, `theca_inscription`, and `authentication_document` as separate fields.
- Do not describe any item as authenticated from image evidence alone.

## Phase 1 deliverables

By the end of Phase 1, the repository should have:

- complete original photo archive preserved unchanged;
- session-level photo manifest;
- case and row section map;
- provisional display-position inventory;
- visible-label transcription table;
- uncertain-label review list;
- duplicate-name review list;
- missing-photo review list;
- follow-up photography list for Phase 2.

## Suggested output files

```text
data/photo_session_manifest.csv
data/phase_1_photo_inventory.csv
data/phase_1_visible_label_transcription.csv
data/phase_1_uncertain_labels.csv
data/phase_1_missing_views.csv
docs/phase_1_section_map_notes.md
```

## Immediate field checklist

- Photograph session card.
- Photograph whole reliquary context.
- Photograph each case straight-on.
- Photograph each case in left/right halves.
- Photograph each row in order.
- Photograph each object position with its label.
- Photograph each label close-up.
- Photograph each theca front where accessible.
- Photograph any visible document or provenance note.
- Record glare, blur, occlusion, or access limits.
- Preserve originals and do not rename destructively.
- Build the manifest after the session.
