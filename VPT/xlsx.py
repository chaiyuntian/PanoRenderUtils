import xlrd
import xlwt

def read_xls(filename, sheet_name = "Sheet1", picked=[]):
    print picked
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name(sheet_name)
    headers = table.row_values(0)
    rsltDict = {}

    for i in range(table.ncols):
        col = table.col_values(i)
        h = headers[i]

        if str(h) in picked:
            col.pop(0)
            print 'contain ', h
            rsltDict[h] = col

    return rsltDict

def write_xls(filename,ops,sheet_name = "report"):

    file = xlwt.Workbook()
    table = file.add_sheet(sheet_name,cell_overwrite_ok=True)

    for o in ops:
        r = o["r"]
        c = o["c"]
        tag = o["tag"]
        v = o["value"]

        style = xlwt.XFStyle()
        
        font = xlwt.Font()

        if tag == True:
            font.colour_index = 0
        else:
            font.colour_index = 0

        style.font = font

        table.write(r,c,v,style)

    file.save(filename)

if __name__ == "__main__":
    #result = read_xls("test.xlsx","Sheet1",picked = ['LG','LGY','LGN','LGYP','LGL','LGI','IES','SKY','NUM'])
    ops = []
    ops.append({"r":0,"c":9,"tag":True,"value":100})
    ops.append({"r":0,"c":0,"tag":False,"value":100})
    write_xls("writetest.xls",ops)
