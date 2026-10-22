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

## 2. Odoo (islamic-treasures.odoo.com), via the Claude desktop app's built-in browser

Run this in a **local** Claude desktop session (the built-in browser pane, already signed in as the owner). Do not use the API.

1. Open `https://islamic-treasures.odoo.com/odoo/action-stock.product_template_action_product/45547` (ROS-K-005).
   Write down every field that is filled on every tab (name format, internal reference, category, product type,
   sales/website description, eCommerce media, website category, tags, attachments in the chatter / documents, published state).
   This is the template; copy its structure exactly and nothing that is specific to 005 (price, cost, weight, bead count, Saim).
2. For each row of `kunooz/odoo_ros_k.csv` (22 rows):
   - Search Odoo by internal reference first; if the product exists, update it instead of creating a duplicate.
     ROS-K-022 and ROS-K-023 were ROS-B-015 and ROS-B-017 until 2026-10-22 (`previous_code`): if those exist in Odoo, rename them, do not create new ones.
   - Create (or Duplicate 45547 and then clear everything piece-specific) with: internal reference = `code`;
     name in the same pattern as 45547; description = `description_ar (sheet)` exactly as written in the sheet;
     main image = `main_image`; extra media = `extra_images` in that order; same category / type / tags / website settings as 45547;
     attachments of the same kind 45547 has (if 45547 carries the film, the 20 pieces have none, so skip it).
   - Price: leave empty / same "on request" handling as 45547 unless the owner gives prices. Do not invent numbers.
3. Rows with a `sheet_note` need the owner's eye before publishing:
   - ROS-K-004: SAiM stamp on the minaret base; the owner confirmed in the description session that this stamp = "خراطة المبدع صايم".
   - ROS-K-010: beads look near-black and opaque in normal light; the sheet note asks to confirm it belongs in the transparent category.
   - ROS-K-022 / 023: moved from ROS-B (no insects visible); 2 photos and 1 photo only.

## Open items

- Descriptions are the shortened round-2 texts (session «أوصاف المسابيح للكتالوج», branch `claude/gallant-feynman-hj18ei`). Catalog specs keep details from the longer round-1 text that round 2 cut for length (cut-only edit, no fact removed as wrong).
- ROS-K-016 and 022 have 2 photos, ROS-K-023 has 1, ROS-K-015/019/021 have 3: thinner than the rest of the category.
- Odoo product data for 45547 was not readable from the cloud session (login required), so the exact Odoo field list is decided in step 2.1, not here.
