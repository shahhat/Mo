import re, json, sys, html, subprocess, concurrent.futures as cf
CATS = [
 ("ROS-K",     "16fZ1TasLd4kD65skRIEsJ00lWujT2lhg", "مسابيح كهرب شفافه - ROS-K"),
 ("ROS-KS",    "1aQjGxvwAS9nqIb8XwWeRAwMX2VMX8HMB", "مسابيح كهرب صاك - ROS-KS"),
 ("ROS-S",     "1XFPYA8wa-RVfpLJBjCgiksihRQSxik2y", "مسابيح حجر واحد - ROS-S"),
 ("ROS-B",     "1ouOcEa6Vn26mYZ_FULWb7qyF-PxHujQe", "مسابيح حشرية ROS-B"),
 ("ROS-Amb-G", "1ZekLSDv6Zfw7A2avkKZQc7yGilH3P3Ma", "الكهرمان الالماني ROS-Amb-G"),
 ("ROS",       "16sGXBEoaSm1NtyyGsAaaIvM9iGaQvHQF", "مسابيح منوعه - ROS"),
]
ENTRY = re.compile(r'<div class="flip-entry" id="entry-([^"]+)".*?<a href="([^"]+)".*?class="flip-entry-title">([^<]*)</div>', re.S)
def listing(fid):
    for attempt in range(4):
        r = subprocess.run(["curl","-sS","-L","--max-time","40",f"https://drive.google.com/embeddedfolderview?id={fid}"],capture_output=True,text=True)
        if r.returncode==0 and 'flip-entries' in r.stdout: break
    out=[]
    for m in ENTRY.finditer(r.stdout):
        i,href,t = m.group(1), m.group(2), html.unescape(m.group(3)).strip()
        kind = "folder" if "/folders/" in href else "file"
        out.append({"id":i,"title":t,"kind":kind})
    return out
inv=[]
for prefix,fid,name in CATS:
    pieces = listing(fid)
    print(prefix, len(pieces), "entries", sum(p['kind']=='folder' for p in pieces), "folders", file=sys.stderr)
    with cf.ThreadPoolExecutor(12) as ex:
        res = list(ex.map(lambda p: listing(p['id']) if p['kind']=='folder' else [], pieces))
    for p,files in zip(pieces,res):
        p["files"]=files
    inv.append({"prefix":prefix,"folder_id":fid,"name":name,"entries":pieces})
json.dump(inv, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
