# ROS-K (مسابيح كهرب شفاف) → Odoo + digital catalog

Branch: `claude/fervent-fermi-hp7sun` in `shahhat/Mo`. Everything below is ready except the two steps that need the owner's own machine: publishing the catalog and entering the products in Odoo.

## Sources (single source of truth)

| what | where |
|---|---|
| Photos | Drive folder "مسابيح كهرب شفاف - ROS-K" (`16fZ1TasLd4kD65skRIEsJ00lWujT2lhg`), one sub-folder per piece |
| Descriptions | Sheet "Knooz (Desc._) Sheet - ROS-K" (`1OOzHcJ5s1AYoM_aFGuweBzRJmKAF3puBocmkBeRtQLk`) in that folder |
| Films | Drive folder `16bNdRwJzBKCGYDw7rBo527gnEfqE_kma`. Only ROS-K-005 has a film ("مسباح كهرمان دمنكاني خراطه المبدع صايم.mp4", already live). The other 22 pieces have no film and go up with photos only |
| Reference product | Odoo product template 45547 = ROS-K-005 |

## 1. Catalog (kunooz-catalog.vercel.app)

`kunooz/site/` is a complete, deploy-ready copy of the live catalog with ROS-K-001…023 filled in
(22 pieces built from Drive; ROS-K-005 kept exactly as live, with its film). 32 pieces in total.
Category totals follow the 2026-10-22 renumbering: كهرب شفاف 23, حشرية 37, الكهرمان الألماني 79.

Publish it from the machine that owns the Vercel project:

```
cd kunooz/site
vercel deploy --prod        # inside the existing kunooz-catalog project
```

`vercel.json` recreates the live `/k/<code>` → `/#/p/<code>` redirect. Check after deploy:
`https://kunooz-catalog.vercel.app/k/ROS-K-001` … `/k/ROS-K-023`.

Rebuild (after the sheet or the Drive folders change):

```
python3 kunooz/fetch.py 16fZ1TasLd4kD65skRIEsJ00lWujT2lhg ROS-K WORK 1OOzHcJ5s1AYoM_aFGuweBzRJmKAF3puBocmkBeRtQLk
python3 kunooz/build.py WORK kunooz/site
```

`build.py` prints a WARNING when a picked photo moved/disappeared or when a sheet description changed since
`meta_ros_k.json` (catalog lead + specs) was written from `sheet_snapshot_ros_k.csv`. Update the lead/specs of those pieces, then delete the snapshot so it is re-taken.

Format rules copied from the live catalog: images long side 1500 px, JPEG q84 progressive 4:2:0, no metadata;
thumbnail = centre square of image 1 at 720 px q82; `light` = thumbnail mean > 0.5 (white-background shots);
pending rows: عدد الخرز، قطر الخرزة، الوزن، المنشأ (not in any source document).

## 2. Odoo (islamic-treasures.odoo.com, Odoo 19.0 Enterprise) via API key, in a cloud session

Owner's decision (2026-10-22): a cloud session enters the 22 pieces through the Odoo API with an API key the owner created.
Owner's rules, verbatim intent: every piece gets exactly what ROS-K-005 got yesterday (certificate, cards/labels, barcode,
description shown on the website). **Do not take decisions alone: if something cannot be reproduced exactly, stop and give the
owner the available options to choose from.**

Access: environment variable `ODOO_API_KEY` (never print it). Odoo 19 JSON-2 API:

```
curl -sS https://islamic-treasures.odoo.com/json/2/<model>/<method> \
  -H "Authorization: bearer $ODOO_API_KEY" -H "Content-Type: application/json" \
  -d '{"ids": [...], "fields": [...]}'          # named arguments of the ORM method
```

First call `res.users/context_get` to confirm the key works (it answers 401 without a key).

### 2.1 Read the reference completely (no writes yet)
ROS-K-005 = `product.template` 45547. Collect, for that record and its variant(s):
- every non-empty field on `product.template` and `product.product` (name pattern, default_code, barcode and its numbering
  scheme, categ_id, type, is_storable, list_price / price handling, description fields, `description_ecommerce` /
  `website_description`, public_categ_ids, product_tag_ids, is_published, website_id, image sizes);
- eCommerce media (`product.image`), all `ir.attachment` on the template and the variant, and the chatter (`mail.message`)
  of 45547 from 2026-10-21/22, which shows what yesterday's session did and what it attached;
- how the certificate and the cards were produced: an Odoo report (`ir.actions.report` / qweb `ir.ui.view` created or
  changed on 2026-10-21), a printed label (barcode label report), or PDF/PNG files attached from outside.
Write the findings to `kunooz/odoo_reference_005.md` and show the owner a short table of what will be repeated per piece.
If any element needs data the sources do not have (weight, bead size, price, certificate number scheme...), list it
and ask; do not fill it.

### 2.2 Create / update the 22 pieces
Data: `kunooz/odoo_ros_k.csv` (one row per piece: code, previous_code, description from the sheet, catalog lead, images).
- Search by `default_code` first; update if it exists. ROS-K-022 / 023 were ROS-B-015 / ROS-B-017 until 2026-10-22: if those
  products exist, rename them, never duplicate.
- Same field structure as 45547; description = the sheet text exactly; images in the csv order, at the same size 45547 uses
  (catalog copies are in `kunooz/site/img/`, originals come from Drive through `kunooz/fetch.py`).
- Barcode, certificate and cards made exactly the way 45547 has them. ROS-K-005 has a film; the 22 pieces have none.
- Price: as 45547 handles it unless the owner gives prices.
- ROS-K-010 stays in كهرب شفاف (owner, 2026-10-22).
- Log every created/updated record id and attachment to `kunooz/odoo_log.json`; commit and push to
  `claude/fervent-fermi-hp7sun`.

### 2.3 Verify
For every piece: open the public shop page and check the description shows like ROS-K-005's; check barcode, certificate and
card attachments exist; report a table code → product id → website URL → certificate/card/barcode status.

### Notes on specific pieces
- ROS-K-004: «بخراطة المبدع صايم» (SAiM stamp on the minaret base, confirmed by the owner).
- ROS-K-010: near-black in normal light, red when backlit; stays in the transparent category (owner).
- ROS-K-022 / 023: moved from ROS-B (no insects visible); 2 photos and 1 photo only.

## Open items

- Descriptions are the shortened round-2 texts (session «أوصاف المسابيح للكتالوج», branch `claude/gallant-feynman-hj18ei`). Catalog specs keep details from the longer round-1 text that round 2 cut for length (cut-only edit, no fact removed as wrong).
- ROS-K-016 and 022 have 2 photos, ROS-K-023 has 1, ROS-K-015/019/021 have 3: thinner than the rest of the category.
- Odoo product data for 45547 was not readable without the API key, so the exact field list and how the certificate/cards were made are established in step 2.1.
