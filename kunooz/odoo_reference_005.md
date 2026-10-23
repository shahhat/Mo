# Odoo reference: ROS-K-005 (product.template 45547)

Read on 2026-10-23 from the owner's signed-in Odoo session in the desktop's built-in browser (read-only, no API key).
Odoo 19.0 Enterprise, `islamic-treasures.odoo.com`.

## 1. Record

| field | value on 45547 |
|---|---|
| name | `مسباح كهرمان دمنكاني` → shown as `[ROS-K-005] مسباح كهرمان دمنكاني` |
| description_sale (sales description) | `خراطة المبدع صايم` (the subtitle) |
| description (internal note) | `بس ضيف السعر و بعدين اطبع الباركود` (a person's note, not part of the template) |
| default_code (Internal Reference) | `ROS-K-005` |
| barcode | `ROS-K-005` (the code itself; printed as Code 128-B) |
| type / is_storable | Goods / tracked in stock (`consu`, `is_storable = true`), tracking none |
| categ_id (internal category) | 36 `المسابيح ` |
| public_categ_ids (website category) | 3 `Amber` |
| list_price / standard_price | 0 / 0 (price on request) |
| taxes | none |
| sale_ok / purchase_ok / available_in_pos | true / true / true |
| allow_out_of_stock_order | true (Odoo default) |
| is_published | **false** (page ready, not published) |
| weight, volume, tags, ribbon, SEO title/description | empty |
| responsible | Islamic Treasures (uid 2) |

### Website description (`description_ecommerce`, HTML)
```
<p>{lead: name + subtitle + one sentence}</p>
<ul><li>{spec}: {value}</li> … (6 specs)</ul>
<p>رقم القطعة: ROS-K-005 · السعر عند الطلب</p>
<p><a href="https://wa.me/96555555249?text=السلام عليكم، أستفسر عن القطعة ROS-K-005 — مسباح كهرمان دمنكاني">استفسر عن القطعة واتساب</a>
 · <a href="https://kunooz-catalog.vercel.app/k/ROS-K-005">صور القطعة وفيلمها</a></p>
```
Lead and specs are the catalog's (`meta_ros_k.json` style), not the sheet paragraph.

## 2. Images

| image | source | note |
|---|---|---|
| main (`image_1920`) | `kunooz/site/img/ROS-K-005-1.jpg` | byte-identical (249,638 B, 1500 px) |
| eCommerce extra media (`product.image`) 144, 145, 146 | `ROS-K-005-2`, `-3`, `-5` | named after the file; all `sequence` 10; the catalog's `-4` (1200×1500) and `-6` (1500×785) were **not** uploaded: only the square photos went up |

## 3. Certificate, display card, label = PDF files made outside Odoo

They are not Odoo reports. They were rendered on the owner's machine and attached to the product.

| file | how it was made | size | in Odoo |
|---|---|---|---|
| `شهادة-ROS-K-005.pdf` | `نظام-القطع/تجربة-فعلية/build_print.py` (HTML → Chrome PDF): logo, «شهادة قطعة», photo 1, name, subtitle, specs table, code, «تاريخ البيع: ……», seal, QR → `kunooz-catalog.vercel.app/k/<code>` | A5 148×210 mm | product.document 4 (attachment 15503) |
| `كارت-العرض-ROS-K-005.pdf` | same script: logo, name, code, QR | 90×48 mm | product.document 5 (attachment 15504) |
| `ليبل-ROS-K-005.pdf` | `build_label.py`: logo, Code 128-B of the code, code, name, no price | 101.6×63.5 mm (Zebra ZD888 roll, print with Fit) | product.document 6 (attachment 15526) |

All three: `shown_on_product_page = false`, `attached_on_sale = hidden` (internal files, not on the shop).

A custom Odoo report also exists since 21-10 17:30: «ليبل الكنوز» (`kunooz.report_kunooz_label`, paper «Kunooz Zebra 102x64»), bound to Products → Print.
It prints the same label from the record (Code128 of the barcode, code, name), so it works for any product with a barcode.

## 4. Chatter (21-10-2026)

1. 04:24:17 – Product created.
2. 04:24:22 – note with the certificate + card attached:
   «ملف القطعة جاهز (جايرو ميديا). الليبل: زر «طباعة الملصقات» فوق. الشهادة وكارت العرض: الملفين المرفقين هنا، افتح أي واحد واطبعه. الـ QR يفتح: kunooz-catalog.vercel.app/k/ROS-K-005»
3. 17:26:52 – note with the label attached:
   «ليبل الكنوز على مقاس رول Zebra ZD888 (من غير سعر): افتح الملف المرفق واطبعه على ZD888 واختار Fit / ملء الصفحة.»

## 5. What happened to the piece after creation (not part of the template)

- 16:35 – stock set to 1 (inventory adjustment).
- 17:05 – **sold in the POS at 0.000 KWD** (order «Islamic Treasures Gallary - 000452»). Stock is now 0.
  The trial sheet said «لا تكمّل البيع»; this sale probably needs reversing (owner to check with the shop).

## 6. Data the sources do not have (not filled)

price, weight, bead count/size for most pieces, origin, certificate number, sale date.
The 22 pieces were searched by code (ROS-K-*, ROS-B-015/017): none exist in Odoo. The same physical pieces may exist in the
older inventory under other names (there are 561 older rosary products); that cannot be matched without the owner.
