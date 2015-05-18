
#import MaxPlus

from xlsx import *
CommonKeys = ['LG','LGY','LGN','LGYP','LGL','LGI','SKY','IES','NUM']
OnOffKeys = ['LGY','LGN','LGYP','LGL','LGI','SKY']
class LightGroup(object):
    """Class for LightGroup"""

    def __init__(self,groupID = 0):
        super(LightGroup, self).__init__()
        self.groupID = groupID
        self.Keys = {"LG":True,"LGY":False,"LGN":False,"LGYP":False,"LGL":False,"LGI":False,"IES":True,"SKY":False,"NUM":False}
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
        for lg in self.LGs:
            lg.DoStatistic()
            result[lg.groupID] = lg.Stats;
        return result

def main():
    a = LightScene()
    a.StatAll()
    print a

if __name__ == '__main__':
	main()