import json, os, sys
ids=json.load(open('file_ids.json'))
def codes(cat): return sorted(os.path.splitext(f)[0] for f in os.listdir(f'sheets/{cat}'))
def img(code, hero=1):
    fid=ids[f'{code}-{hero}']
    return f'=IMAGE("https://drive.google.com/thumbnail?id={fid}&sz=w800")'
if __name__=='__main__':
    cat=sys.argv[1]
    rows=[[str(i+1), img(c)] for i,c in enumerate(codes(cat))]
    print(json.dumps(rows,ensure_ascii=False))
