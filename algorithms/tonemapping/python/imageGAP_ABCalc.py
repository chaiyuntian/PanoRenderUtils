import numpy as np
from PIL import Image
from colorSpace import sRGB2Y
import os
from tonemap import *
import string
from time import clock
start=clock()
#ufunc=np.frompyfunc(sRGB2XYZ,3,3)
#AB calculation only needs Y
ufunc=np.frompyfunc(sRGB2Y,3,1)

def calAB_FromImageList(imageNameList = [],imageRoot='IMAGES',imageFormat='.jpg'):

    if len(imageNameList)<=0:
        print "No image name specified!"
        return
    
    effectList=[]
    for imageName in imageNameList:
        filepath=imageRoot+os.sep+imageName+imageFormat
        print filepath
        im = Image.open(filepath)
        ar=np.array(im)
        effectList.append(ar)
        
    #initialize the sum array
    sumY=effectList[0][:,:,1]*0

    for mx in effectList:
        Y0=ufunc(mx[:,:,0],mx[:,:,1],mx[:,:,2])
        sumY=sumY+Y0
        del(Y0)
    print "finished Sum used time:",(clock()-start)
    #A,B=reinhardCalcAB(sumY)
    Key,A,B = CalcKeyCalcAB(sumY)
    finish=clock()
    print "finished used time:",(finish-start)
    

calAB_FromImageList(["Ambient_Spot_Day","Focus_Track_Day"])
