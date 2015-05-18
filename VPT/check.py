'''
    Creates a simple text representation of the scene graph
'''
import MaxPlus
from utils import *
'''
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
'''
import xlsx

#from regex import matchGroup,matchItem
import re
from light import *

group_exp = re.compile(r'^(LG{0,1}[YyNnTtLlIi]||YP)(\d{1,})$')

item_exp = re.compile(r'^(LG){0,1}([^0-9]{1,})(\d{1,})\S{0,}_(\d{1,})$')
#re.compile(r'^(LG){0,1}([YnNnTtLl]||YP)(\d{1,})\S{0,}_(\d{1,})$')

ies_exp = re.compile(r'[^\\]{1,}\.(ies|IES)$')

def matchIES(iespath):

    m = re.search(ies_exp,iespath)
    result = ""
    if m:
        result = m.group(0)
    return str(result)

def matchGroup(gname):
    m = re.match(group_exp,gname)
    if m:
        typeheader = m.group(1)
        groupID = int(m.group(2))
        return str(typeheader).upper(),groupID
    else:
        return False

def matchItem(gname):
    m = re.match(item_exp,gname)
    if m:
        typeheader = m.group(2)
        groupID = int(m.group(3))
        itemID = int(m.group(4))
        return str(typeheader).upper(),groupID,itemID
    else:
        return False


CommonKeys = ['LG','LGY','LGN','LGYP','LGL','LGI','SKY','IES','NUM']
OnOffKeys = ['LGY','LGN','LGYP','LGL','LGI','SKY']
class LightGroup(object):
    """Class for LightGroup"""

    def __init__(self,groupID = 0):
        super(LightGroup, self).__init__()
        self.groupID = groupID
        self.Keys = {"LG":True,"LGY":False,"LGN":False,"LGYP":False,"LGL":False,"LGI":False,"IES":True,"SKY":False,"NUM":True}
        self.P = {}
        self.Stats = {"LG":groupID,"Y":0,"N":0,"YP":0,"L":0,"I":0,"IES":False,"SKY":False,"NUM":False}
        self.P["LG"] = groupID    # Light Group ID
        self.P["Y"] = []    # Lit Model
        self.P["N"] = []    # Unlit Model
        self.P["YP"] = []   # Lighting piece
        self.P["L"] = []    # VRayLight
        self.P["I"] = []    # VRayIES
        self.P["IES"] = "default.ies"   # IES file
        self.P["SKY"] = False   # SkyLight
        self.P["NUM"] = 0 # LegalGroupMembers
        self.LightMembers = [] #
    
    def TurnON_Property(self,propertyKey,onoff = True):
        if(self.Keys.has_key(propertyKey)):
            self.Keys[propertyKey] = onoff

    def SetPByKey(self,key,value):
        if self.P.has_key(key):
            self.P[key] = value
        else:
            pass

    def GetOnProperty(self):
        result = []
        for k in self.Keys.keys():
            print k
            if self.Keys[k]==True:
                pass
                result.append(k)
        return result

    # starndard
    def GetSTD(self):
        OnKeys = self.GetOnProperty()
        std = {"groupID":self.groupID,"Keys":OnKeys,"IES":self.P["IES"]}
        return std

    def __str__(self):
        return str({"GID":self.groupID,"P_OnOff":self.Keys,"P":self.P,"STD":self.GetSTD()})
    
    # check where is the problem
    # use a outer Checker Function to deny the dependency of the MaxPlus Module
    def Check(self,Checker=None):
        if Checker==None:
            return None

        result = Checker(self.GetSTD(),Self.Stats)
        return result

    def DoStatistic(self):
        statkeys = ["Y","N","YP","L","I"]
        for k in statkeys:
            self.Stats[k] = len(self.P[k])
        self.Stats["NUM"] = self.P["NUM"]
        return self.Stats

class LightScene(object):
    """docstring for LightScene"""
    def __init__(self, xlsName = "test.xlsx"):
        super(LightScene, self).__init__()
        self.source = xlsName
        self.LGs = {}
        try:
            table = read_xls(xlsName,"Sheet1",picked = CommonKeys)

        except:
            print "Xlsx format regulation is not satisfied!"
            return None

        self.LGNum = len(table["LG"])
        
        print self.LGNum
        for i in range(self.LGNum):
            g = LightGroup(int(table["LG"][i]))
            g.SetPByKey("IES",str(table["IES"][i]))
            g.SetPByKey("NUM",int(table["NUM"][i]))
            for ky in OnOffKeys:
                if str(table[ky][i]) == "v" or str(table[ky][i]) == "V":
                    g.TurnON_Property(ky,True)
            print g
            if self.LGs.has_key(g.groupID):
                print "Group ID:%d existed!"%g.groupID
            else:
                self.LGs[g.groupID] = g

    def check(self):
        pass

    def __str__(self):
        s = ""
        for lg in self.LGs:
            s = s +", "+str(lg.__str__()) 
        return str({"source":self.source,"LGs":str(s)})

    def StatAll(self):
        result ={}
        for k in self.LGs.keys():
            self.LGs[k].DoStatistic()
            result[self.LGs[k].groupID] = self.LGs[k].Stats;
        return result

    def StatToTableRecord(self):
        operations = []
        
        operations.append()



def CheckGroup(node):
    gname = node.Name
    isGroup = bType(gname,"Dummy").Get()
    m = False
    if isGroup:
        m = matchGroup(gname)
        if m:
            print m
            return m
    return False

def CheckItem(node):
    name = node.Name
    isGroup = bType(name,"Dummy").Get()
    m = False
    if isGroup:
       return False
    else:
        m = matchItem(name)
        if m:
            return m
    return False

def SphereAt(x,y,z,r=5.0):
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    obj.ParameterBlock.Radius.Value = r
    sphere = MaxPlus.Factory.CreateNode(obj)
    sphere.SetObjOffsetPosition(MaxPlus.Point3(x, y, z))

LGs = []
group = {}
items = {}
objects = {}
iess = {} 
errors = {}

'''Error Code and Descriptions'''
errorcodes = {
10001:"group type tag and item type tag unmatch!",
10002:"group ID and item ID unmatch!"}

def ErrorTag(code):
    if errorcodes.has_key(code):
        return errorcodes[code]
    else:
        return "Unknown Error"

def addError(header,groupid,itemid,ecode = 10000):
    key = str(header+"|"+str(groupid))
    if errors.has_key(key):
        if errors[key].has_key(ecode):
            errors[key][ecode].append(itemid)
        else:
            errors[key][ecode] = [itemid]
    else:
        errors[key] = {ecode:[itemid]}

def checkAllGroup(node, indent = ''):
    new_name = node.Name.replace(' ','_')
    node.SetName(new_name)
    g =  CheckGroup(node)
    if g:
        h,i = g
        print h,i
        if group.has_key(str(h)):
            group[str(h)].append(i)
        else:
            group[str(h)] = [i]

        for c in node.Children:
            checkAllItem(c,h,i)

    for c in node.Children:
    	checkAllGroup(c)

def checkAllItem(node, header ="h" ,groupid = 0):
    r = CheckItem(node)
    if r:
        h,gId,iId = r
        if h!=header:
            addError(header,groupid,iId,10001)
        if groupid!= gId:
            addError(header,groupid,iId,10002)

        key = h+"|"+str(gId)
        if items.has_key(key):
            items[key].append(iId)
            objects[key].append(node)
        else:
            items[key] = [iId]
            objects[key]= [node]

        name = node.Name
        isIES = getType(name)=='VRayIES'
        
        if isIES:
            ies = matchIES(getIES(name)) #getIES(name)
            if iess.has_key(key):
                iess[key].append(ies)
            else:
                iess[key] = [ies]
            

    for c in node.Children:
        checkAllItem(c,header,groupid)


def GroupChecker(args = {"groupID":0,"Keys":[],"IES":""}):
    gId = args["groupID"]
    ks = args["Keys"]
    ies = args["IES"]


def checkAll(xlspath = "test.xlsx"):

    scene = LightScene(xlspath)

    statkeys = ["Y","N","YP","L","I"]
    
    
    checkAllGroup(MaxPlus.Core.GetRootNode())
    for k in group.keys():
        group[k] = sorted(group[k])


    #checkAllItem(MaxPlus.Core.GetRootNode())
    for k in items.keys():
        items[k] = sorted(items[k])

    '''
    print scene
    print group
    print items
    print iess
    '''

    for k in items.keys():
        s = k.split('|')
        typehead = s[0]
        Id = int(s[1]) 
        if Id>len(scene.LGs):
            continue
        else:

            scene.LGs[Id].SetPByKey(typehead,items[k])

    stat = scene.StatAll()
    print stat

    Headers = {"LG":0,"Y":1,"N":2,"YP":3,"L":4,"I":5,"IES":6,"SKY":7,"NUM":8}

    ops = []

    #Write Headers
    for h in Headers.keys():
        opH = {"r":0,"c":Headers[h],"tag":False,"value":h}
        ops.append(opH)

    for rkey in stat.keys():
        r = int(rkey)
        evalue = int(stat[rkey]["NUM"]) # expected light numbers in the group
        clmNum = Headers["NUM"]
        op0 = {"r":r,"c":clmNum,"tag":False,"value":evalue}
        #print op0
        ops.append(op0)
        for ckey in stat[rkey].keys():
            c = int(Headers[ckey])

            value = stat[rkey][ckey]
            tag = False
            if value==False:
                value = 0
            elif value != evalue:
                tag = True

            if ckey == "LG":
                tag = False

            op1 = {"r":r,"c":c,"tag":tag,"value":value}
            #print op1
            ops.append(op1)


    write_xls("writetest.xls",ops)




    

# TODO Compare Groups and Find what is missing

if __name__ == '__main__':
    checkAll("F:\\PythonScripts\\test.xlsx")


    
