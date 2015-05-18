'''
    utility functions
'''
import MaxPlus

lightTypes = ['VRayIES','VRayLight']

def Exec(s):
	try:
		r = MaxPlus.Core.EvalMAXScript(s)
		return r
	except:
		return ""

def Name(name):
    return Exec('$'+name)

def bType(objName,typename):
    return Exec('classof $'+ objName +"== " + typename)

def getType(objName):
	return Exec('classof $'+ objName).Get().GetClassName()
	
def getIES(objName):
	return Exec('$'+ objName + '.ies_file').Get()

def SphereAt(x,y,z,r=5.0):
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    obj.ParameterBlock.Radius.Value = r
    sphere = MaxPlus.Factory.CreateNode(obj)
    sphere.SetPosition(MaxPlus.Point3(x, y, z))

if __name__ == '__main__':
	print getType("i1_007")
	if getType("i1_007")=='VRayIES':
		print getIES("i1_007")