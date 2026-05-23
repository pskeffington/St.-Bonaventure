# Image Manifest

## Uploaded image set used in the first pass

The first indexing pass used the 36 uploaded JPG photographs listed below. These files should be committed under `images/original/` during local sync. A checksum and dimension inventory is stored in `data/image_file_register.csv`.

| Filename | First-pass role |
|---|---|
| IMG_3202.JPG | Chapel-wide overview showing multiple wall-mounted reliquary cases |
| IMG_3203.JPG | Overview case with Lucy/Lucille and Joseph of Leonessa |
| IMG_3204.JPG | R/S/T case; Stanislaus Kostka through Theresa Margaret of the Sacred Heart |
| IMG_3205.JPG | Simon sequence; Sebastian, Silvia, Simon, Simon Stock, Simon of Trent |
| IMG_3207.JPG | P/R case; Pius, Pontian, Robert Bellarmine, Rose of Lima |
| IMG_3208.JPG | P/R case continuation; Pius, Pontian, Robert Bellarmine, Rose of Lima |
| IMG_3209.JPG | Peter/Philip sequence |
| IMG_3210.JPG | Paul of the Cross sequence |
| IMG_3211.JPG | Matthew, Maurice, Oliver Plunkett sequence |
| IMG_3212.JPG | Left-side L/M sequence with Marcellus/Orione/Barat labels |
| IMG_3213.JPG | Maria Goretti, Mark, Mark Evangelist, Martin de Porres sequence |
| IMG_3214.JPG | Lucius, Luigi Orione, Madeleine Sophia Barat, Marcellus, Margaret/Marina sequence |
| IMG_3215.JPG | Ladislaus, Lawrence, Lawrence of Brindisi, Longinus, Louis Grignion sequence |
| IMG_3216.JPG | Longinus close-up |
| IMG_3217.JPG | Josaphat through Joseph Pignatelli sequence |
| IMG_3218.JPG | John of the Cross / John Vianney sequence |
| IMG_3219.JPG | John de Brebeuf through John of Capistrano |
| IMG_3220.JPG | John and Paul, John Berchmans, John Cantius / John Kanty |
| IMG_3221.JPG | Ignatius, Imelda Lambertini, Jacinta and Francisco Marto |
| IMG_3222.JPG | Hilary, Hippolytus of Rome, Ignatius of Loyola |
| IMG_3223.JPG | Gregory/Hedwig sequence |
| IMG_3224.JPG | Gabriel of Our Lady of Sorrows, Gaspar del Bufalo, Gemma Galgani |
| IMG_3225.JPG | Francis of Rome, Francis Solano, Gabriel Lalemant |
| IMG_3226.JPG | Francis of Assisi and Clare; Francis of Hieronymo |
| IMG_3227.JPG | Ferdinand III of Castile, Florian, Francis de Sales, Francis of Assisi |
| IMG_3228.JPG | Damian/Dominic sequence |
| IMG_3229.JPG | Charles Garnier, Charles Lwanga, Christina, Claire, Clemens Maria Hofbauer |
| IMG_3230.JPG | Cassian, Catherine Laboure, Cecilia/Valerian/Tiburtius, Charbel Makhlouf |
| IMG_3231.JPG | Callixtus, Camillus de Lellis, Canadian Martyrs sequence |
| IMG_3232.JPG | Bridget of Sweden, Brigida, Callixtus I, Camillus de Lellis sequence |
| IMG_3233.JPG | Bernard of Clairvaux, Blandina, Bonaventure |
| IMG_3234.JPG | Beatrice of Silva, Benedict XI, Benedict Joseph Labre, Bernard transition |
| IMG_3235.JPG | Beatrice, Beatrice of Silva, Benedict XI |
| IMG_3236.JPG | Antony Mary Pucci, Antonius of Florence, Apollonia, Arnold Janssen, Baptista Mantuanus |
| IMG_3237.JPG | Andrew Corsini, Angelo, Anicetus, Anna Marie Taigi |
| IMG_3238.JPG | Joseph of Leonessa close-up |

## Binary-file handling

The repository currently contains text indexes and manifests. Original JPG files should be added locally under:

```text
images/original/
```

Recommended local commands:

```bash
mkdir -p images/original images/crops/labels images/crops/thecae
cp /path/to/IMG_32*.JPG images/original/
git add images/original data docs manuscript README.md
git commit -m "Add original reliquary image set"
git push
```

## Next image-processing tasks

- Generate cropped brass-label images.
- Generate cropped theca images.
- Record image checksums after local commit.
- Reconcile every brass label against the paper theca inscription.
- Mark uncertain source-image links before publication.
