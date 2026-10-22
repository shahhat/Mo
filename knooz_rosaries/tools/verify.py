import json, sys, re
from build import rows
from checksum import cs
def tcs(s): return sum(ord(ch)*(i+1) for i,ch in enumerate(s))
def expected(cat):
    out=[]
    for r in rows(cat):
        fid=re.search(r'id=([^&]+)',r[1]).group(1)
        out.append(f"{cs(fid)}|{tcs(r[2])}|{r[3]}")
    return out
def formulas(n, start=2):
    f='=LET(id,REGEXEXTRACT(FORMULATEXT(B{r}),"id=([^&]+)"),n,LEN(id),t,C{r},m,LEN(t),SUMPRODUCT(CODE(MID(id,SEQUENCE(n),1))*SEQUENCE(n))&"|"&SUMPRODUCT(UNICODE(MID(t,SEQUENCE(m),1))*SEQUENCE(m))&"|"&D{r})'
    return [[f.format(r=r)] for r in range(start,start+n)]
if __name__=='__main__':
    cat=sys.argv[1]; mode=sys.argv[2]
    if mode=='f': print(json.dumps(formulas(len(rows(cat)))))
    elif mode=='e': print(json.dumps(expected(cat)))
    elif mode=='cmp':
        got=[x[0] if x else '' for x in json.load(open(sys.argv[3]))['values']]
        exp=expected(cat); bad=[(i+2,g,e) for i,(g,e) in enumerate(zip(got,exp)) if g!=e]
        print('rows',len(got),'expected',len(exp),'mismatches',len(bad)); print(bad[:10])
