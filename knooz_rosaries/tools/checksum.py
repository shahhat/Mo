import json, sys, re
from rows import codes, img
def cs(s): return sum(ord(ch)*(i+1) for i,ch in enumerate(s))
def expected(cat, heroes=None):
    heroes=heroes or {}
    out=[]
    for c in codes(cat):
        f=img(c, heroes.get(c,1)); fid=re.search(r'id=([^&]+)',f).group(1); out.append(cs(fid))
    return out
def formulas(n):
    return [[f'=LET(id,REGEXEXTRACT(FORMULATEXT(B{r}),"id=([^&]+)"),n,LEN(id),SUMPRODUCT(CODE(MID(id,SEQUENCE(n),1))*SEQUENCE(n)))'] for r in range(2,n+2)]
if __name__=='__main__':
    cat=sys.argv[1]; e=expected(cat); print(len(e), e, 'total', sum(e))
    if len(sys.argv)>2 and sys.argv[2]=='f': print(json.dumps(formulas(len(e))))
