import sys,os,cv2,time
sys.path.insert(0,'/tmp/kw'); import up
os.makedirs('/tmp/kw/jsr',exist_ok=True)
for p in sys.argv[1:]:
    q='/tmp/kw/jsr/'+os.path.basename(p)
    if os.path.exists(q): continue
    t=time.time(); img=cv2.imread(p)
    if img.shape[0]>700: img=cv2.resize(img,(700,700),interpolation=cv2.INTER_AREA)
    o=up.sr(img); cv2.imwrite(q,o); print(p,img.shape,'->',o.shape,round(time.time()-t,1),flush=True)
