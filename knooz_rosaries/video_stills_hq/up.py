# Stage 2: Real-ESRGAN x4 (tiled, CPU) -> 3600 px square, light finishing, brand logo, JPEG q95.
import spandrel,torch,cv2,numpy as np,sys,os,json,time
from PIL import Image
torch.set_num_threads(4)
M=spandrel.ModelLoader().load_from_file('/tmp/kw/models/RealESRGAN_x4plus.pth').eval()
M.model.to(torch.bfloat16)
def sr(img,tile=300,pad=16):
    x=torch.from_numpy(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)).permute(2,0,1).float()/255
    C,H,W=x.shape; out=torch.zeros(C,H*4,W*4)
    with torch.no_grad():
        for y0 in range(0,H,tile):
            for x0 in range(0,W,tile):
                ya,xa=max(0,y0-pad),max(0,x0-pad); yb,xb=min(H,y0+tile+pad),min(W,x0+tile+pad)
                o=M.model(x[:,ya:yb,xa:xb][None].to(torch.bfloat16))[0].float()
                ty,tx=y0-ya,x0-xa; h,w=min(tile,H-y0),min(tile,W-x0)
                out[:,y0*4:(y0+h)*4,x0*4:(x0+w)*4]=o[:,ty*4:(ty+h)*4,tx*4:(tx+w)*4]
    return cv2.cvtColor((out.clamp(0,1).permute(1,2,0).numpy()*255).round().astype(np.uint8),cv2.COLOR_RGB2BGR)
if __name__=='__main__':
    for p in sys.argv[1:]:
        q='/tmp/kw/srout/'+os.path.basename(p)
        if os.path.exists(q): continue
        t=time.time(); img=cv2.imread(p)
        if img.shape[0]>900: img=cv2.resize(img,(900,900),interpolation=cv2.INTER_AREA)
        o=sr(img)
        cv2.imwrite(q,o); print(p,img.shape,'->',o.shape,round(time.time()-t,1),'s',flush=True)
