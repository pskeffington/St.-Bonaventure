# Operational Roadmap for Publication

## Mission

Build the St. Bonaventure reliquary project into a publishable theological, historical, and archival work grounded in visual documentation, controlled cataloging, Catholic theology of relic veneration, historical context, and verifiable provenance.

The project must proceed in sequence. Physical description comes before interpretation. Label transcription comes before saint biographies. Theca inscription comes before authentication language. Certificate review controls claims about authenticity, relic class, seal, source, and chain of custody.

## Publication objective

Primary objective: produce a scholarly theological-historical catalog of the reliquary suitable for academic press submission.

Secondary outputs:

- Public-facing digital catalog.
- Parish or diocesan archive package.
- ResearchGate project page.
- GitHub data repository with transparent indexing workflow.
- Optional article-length preview essay for a Catholic history, material religion, museum studies, or church history journal.

## Phase 0 — Repository and evidence stabilization

Status: initiated.

Tasks:

- Preserve all original JPG files under `images/original/`.
- Create immutable image register with SHA-256 checksums.
- Maintain raw transcriptions separately from normalized names.
- Preserve uncertain readings rather than force correction.
- Record every source image supporting each relic record.

Deliverables:

- `data/image_file_register.csv`
- `docs/image_manifest.md`
- `data/reliquary_sections.csv`
- `data/relic_index_visible.csv`

Completion rule:

This phase is complete only after all original image files are committed or externally archived with stable filenames and checksums.

## Phase 1 — Physical section identification

Status: first pass complete; requires review after local image commit.

Working sections:

| Section | Working title | Visible range |
|---|---|---|
| A | A-series and early B transition | Andrew Corsini through Baptista Mantuanus |
| B | B-series and Bonaventure | Beatrice through Bonaventure |
| C | C-series saints and martyr groupings | Bridget/Brigida through Clemens Maria Hofbauer |
| D | Damian and Dominican sequence | Damian through Dominic Savio |
| FG | Franciscan/Gregory/Gemma/Gaspar/Gabriel sequence | Ferdinand III through Hedwig |
| HIJ | Hilary/Ignatius/John/Joseph sequence | Hilary through Joseph of Leonessa |
| LM | Ladislaus through Martin/Matthew/Maurice/Oliver | Ladislaus through Oliver Plunkett |
| P | Paul/Peter/Philip/Pius/Pontian sequence | Patrick through Pontian |
| RST | Robert Bellarmine through Theresa | Robert Bellarmine through Theresa-related labels |
| Overview | Chapel-wide case arrangement | Multiple wall-mounted cases |

Tasks:

- Assign each original image to a physical section.
- Confirm case order from chapel geography, not only filename order.
- Name wall position if known: left wall, right wall, sanctuary side, nave side, rear, side aisle.
- Add case number identifiers: `CASE-01`, `CASE-02`, etc.
- Add panel identifiers within each case if the display is segmented.

Deliverables:

- Revised `data/reliquary_sections.csv` with physical wall/case/panel fields.
- `docs/section_map.md` expanded into a chapel-placement map.
- Optional line drawing or floorplan showing reliquary case placement.

Completion rule:

Every visible case must have a stable `case_id`, physical location, section range, and image support.

## Phase 2 — Relic catalog completion

Status: first pass catalog created; not publication-ready.

Tasks:

- Confirm every brass plate reading from close-up image or crop.
- Create a crop for every brass label.
- Create a crop for every theca.
- Reconcile brass plate, theca label, and normalized saint name.
- Add duplicate-control rules for repeated saints or composite labels.
- Mark group relics separately from individual relics.
- Add fields for relic class only when documented.

Minimum fields for every relic:

| Field | Purpose |
|---|---|
| `record_id` | Stable local ID |
| `case_id` | Physical case |
| `section_id` | Alphabetic/working section |
| `display_order` | Left-to-right order within case |
| `visible_label` | Exact brass plate transcription |
| `normalized_name` | Research-standard name |
| `theca_inscription_visible` | Exact visible theca inscription |
| `group_or_individual` | Individual, group, composite, unknown |
| `source_images` | Supporting image filenames |
| `label_crop` | Cropped brass label path |
| `theca_crop` | Cropped theca path |
| `confidence` | High, medium, low |
| `verification_status` | Controlled status vocabulary |
| `notes` | Variant spellings, conflicts, uncertainty |

Deliverables:

- `data/relic_catalog_master.csv`
- `images/crops/labels/`
- `images/crops/thecae/`
- `data/relic_catalog_audit.csv`

Completion rule:

Every visible relic must have one row, one source image, one status, and one explicit confidence grade.

## Phase 3 — Authentication and provenance register

Status: not started.

Tasks:

- Locate certificates of authenticity, episcopal seals, wax seals, custody notes, donation letters, parish inventory sheets, or diocesan records.
- Create a certificate record for every document.
- Photograph or scan each certificate at archival resolution.
- Transcribe Latin, Italian, French, or English certificate text.
- Record issuer, date, seal, authority, relic description, relic class, and named saint.
- Link certificate IDs to relic record IDs.
- Mark conflicts between display label and certificate language.

Controlled verification statuses:

| Status | Meaning |
|---|---|
| `visible_label_only` | Brass label only; no theca or certificate confirmation |
| `visible_label_plus_theca` | Brass label and visible theca inscription agree or substantially align |
| `certificate_pending` | Certificate known to exist but not reviewed |
| `certificate_verified` | Certificate reviewed and linked |
| `certificate_conflict` | Certificate conflicts with display or theca label |
| `unresolved` | Evidence is insufficient or contradictory |
| `not_a_relic_record` | Display element is not catalogable as a relic |

Deliverables:

- `data/authentication_register.csv`
- `docs/certificate_transcription_protocol.md`
- `images/certificates/`
- `data/provenance_conflicts.csv`

Completion rule:

No relic may be described as authenticated in the manuscript unless it is linked to certificate, seal, inventory, or institutional provenance evidence.

## Phase 4 — Theological framework

Status: planned.

Core theological question:

What does this reliquary reveal about Catholic memory, sanctity, intercession, material devotion, and the local preservation of universal Church history?

Required theological components:

- Catholic doctrine on the veneration of saints and relics.
- Distinction between worship due to God alone and veneration/honor given to saints.
- Relics as material signs of sanctity, martyrdom, ecclesial memory, and communion of saints.
- Historical continuity of relic veneration in Christian practice.
- The pastoral and catechetical function of reliquaries.
- Ethical handling of relics: reverence, documentation, custody, and avoidance of sensationalism.

Book-theology chapters should not merely retell saint biographies. They must interpret the collection as a Catholic archive of sanctity.

Deliverables:

- `manuscript/theological_framework.md`
- `data/theological_theme_index.csv`
- Chapter-level bibliography.

Completion rule:

Every theological claim must be supported by Scripture, conciliar/catechetical teaching, canon law, patristic witness, liturgical tradition, or peer-reviewed scholarship.

## Phase 5 — Historical and hagiographic research

Status: planned.

Tasks:

- Build a short scholarly note for each saint or group.
- Identify saint type: apostle, martyr, pope, bishop, Doctor, founder, mystic, missionary, confessor, virgin, layperson, child saint, local/regional devotion.
- Record feast day, century, geography, order/community, and major source traditions.
- Separate verified historical fact from hagiographic tradition.
- Identify why the saint matters within the reliquary collection.

Deliverables:

- `data/saint_research_register.csv`
- `notes/saints/REL-####.md`
- `data/order_affiliation_index.csv`
- `data/feast_calendar_index.csv`

Completion rule:

Each relic record must have a concise historical note and a source-backed theological/catechetical note before inclusion in the book catalog section.

## Phase 6 — Book architecture

Status: planned.

Working title:

`The St. Bonaventure Reliquary: A Catholic Archive of Sanctity, Memory, and Material Devotion`

Proposed structure:

1. Introduction: The Reliquary as Archive
2. Catholic Theology of Relics
3. Reliquaries, Thecae, Seals, and Sacred Custody
4. The Physical Installation: Chapel, Cases, and Visual Order
5. Cataloging Method and Evidence Rules
6. The Apostolic and Early Martyr Witness
7. Popes, Bishops, Doctors, and Teachers
8. Founders, Reformers, Missionaries, and Religious Orders
9. Women Saints, Virgin Martyrs, Mystics, and Lay Witnesses
10. Composite and Group Relics: Martyr Communities and Shared Devotion
11. St. Bonaventure in the Collection
12. The Full Catalog of Visible Relics
13. Provenance, Authentication, and Open Questions
14. Conclusion: Local Custody of Universal Memory

Appendices:

- Full relic catalog.
- Section map.
- Image manifest.
- Authentication register.
- Glossary of relic terminology.
- Abbreviations in theca labels.
- Feast-day calendar.
- Bibliography.

Completion rule:

The book must present the catalog as evidence-backed scholarship, not as devotional assertion alone.

## Phase 7 — Academic press package

Status: planned.

Required package:

- Working title and subtitle.
- 1,500–3,000 word proposal narrative.
- Clear argument and contribution.
- Table of contents.
- Chapter abstracts.
- Estimated manuscript length.
- Sample chapter.
- Author biography and qualifications.
- Market/audience statement.
- Comparable books.
- Image/figure plan.
- Permissions statement.
- Status of manuscript completion.
- Timetable to completion.
- Evidence of institutional support, if available.

Best sample chapter:

Chapter 5, `Cataloging Method and Evidence Rules`, or Chapter 2, `Catholic Theology of Relics`, depending on target press. For a theology press, use Chapter 2. For a history/material-culture press, use Chapter 5.

Completion rule:

Do not submit until the catalog is internally consistent, all image permissions are clear, and authentication language is controlled.

## Phase 8 — Public release strategy

Status: planned.

Suggested release sequence:

1. GitHub repository: working archive and data transparency.
2. ResearchGate project: public project description and image-safe summary.
3. Parish/diocesan review copy: pastoral and custodial review.
4. Conference poster or short presentation: method and significance.
5. Journal article: `Cataloging a Parish Reliquary as a Catholic Archive of Sanctity`.
6. Academic press proposal.
7. Full manuscript submission.

## Risk controls

| Risk | Control |
|---|---|
| Overclaiming authenticity | Use verification-status fields and evidence hierarchy |
| Misreading Latin abbreviations | Preserve raw theca transcription and add expert review |
| Confusing display label with certificate identity | Keep display, theca, and certificate fields separate |
| Duplicate saints | Assign physical record IDs before theological consolidation |
| Weak academic contribution | Frame the reliquary as material Catholic memory, not only a list of saints |
| Image rights uncertainty | Resolve parish/owner permission before public image publication |
| Press rejection | Build article and digital catalog first to demonstrate scholarly value |

## Immediate next actions

- Commit all 36 original images locally under `images/original/`.
- Generate label and theca crops.
- Upgrade `relic_index_visible.csv` into `relic_catalog_master.csv`.
- Create `case_id` and `display_order` fields.
- Build first 10 saint notes as a model.
- Draft the theological framework chapter.
- Draft the academic press proposal.
