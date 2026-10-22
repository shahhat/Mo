import json, sys
def reqs(sheet_id, title, n):
    R=0.59607846
    last=n+1
    rng=lambda r0,r1,c0,c1: {"sheetId":sheet_id,"startRowIndex":r0,"endRowIndex":r1,"startColumnIndex":c0,"endColumnIndex":c1}
    out=[{"updateSheetProperties":{"properties":{"sheetId":sheet_id,"title":title,"gridProperties":{"rowCount":last,"columnCount":6,"frozenRowCount":1}},"fields":"title,gridProperties.rowCount,gridProperties.columnCount,gridProperties.frozenRowCount"}}]
    for i,w in enumerate([97,407,376,302,302,302]):
        out.append({"updateDimensionProperties":{"range":{"sheetId":sheet_id,"dimension":"COLUMNS","startIndex":i,"endIndex":i+1},"properties":{"pixelSize":w},"fields":"pixelSize"}})
    out.append({"updateDimensionProperties":{"range":{"sheetId":sheet_id,"dimension":"ROWS","startIndex":0,"endIndex":1},"properties":{"pixelSize":92},"fields":"pixelSize"}})
    out.append({"updateDimensionProperties":{"range":{"sheetId":sheet_id,"dimension":"ROWS","startIndex":1,"endIndex":last},"properties":{"pixelSize":330},"fields":"pixelSize"}})
    out.append({"repeatCell":{"range":rng(0,1,0,6),"cell":{"userEnteredFormat":{"backgroundColorStyle":{"rgbColor":{"red":R,"green":0,"blue":0}},"horizontalAlignment":"CENTER","verticalAlignment":"MIDDLE","wrapStrategy":"WRAP","textFormat":{"bold":True,"foregroundColorStyle":{"rgbColor":{"red":1,"green":1,"blue":1}}}}},"fields":"userEnteredFormat.backgroundColorStyle,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy,userEnteredFormat.textFormat"}})
    out.append({"repeatCell":{"range":rng(1,last,0,1),"cell":{"userEnteredFormat":{"backgroundColorStyle":{"rgbColor":{"red":1,"green":0.9490196,"blue":0.8}},"horizontalAlignment":"CENTER","verticalAlignment":"MIDDLE","wrapStrategy":"WRAP","numberFormat":{"type":"TEXT"},"textFormat":{"bold":True,"fontSize":22,"foregroundColorStyle":{"rgbColor":{"red":R,"green":0,"blue":0}}}}},"fields":"userEnteredFormat.backgroundColorStyle,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy,userEnteredFormat.numberFormat,userEnteredFormat.textFormat"}})
    out.append({"repeatCell":{"range":rng(1,last,1,6),"cell":{"userEnteredFormat":{"horizontalAlignment":"CENTER","verticalAlignment":"MIDDLE","wrapStrategy":"WRAP"}},"fields":"userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy"}})
    return out
if __name__=="__main__":
    print(json.dumps(reqs(int(sys.argv[1]),sys.argv[2],int(sys.argv[3])),ensure_ascii=False))
