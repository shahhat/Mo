import json, sys
from rows import codes, img
cat=sys.argv[1]
H=["no.","IMAGES","Description","Item Name\n(Khaled Folder)","Item Category","Notes"]
rows=[H]+[[str(i+1), img(c), None, c, "Rosary", None] for i,c in enumerate(codes(cat))]
print(json.dumps(rows,ensure_ascii=False))
