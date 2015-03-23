import numpy as np
from PIL import Image
from colorSpace import sRGB2XYZ
import os
from tonemap import *
import string
from time import clock
start=clock()
ufunc=np.frompyfunc(sRGB2XYZ,3,3)

camera='Camera006'
groups=['damenwaiqiangdengzu',
        'jinshuzhupeishedengzu',
        'menkoudengzu',
        'waiqiangdengzu',
        'yiguishedengzu',
        'zhongxinzoulangvrayies',
        'leddengtiaozong',
        'leddengtiaozu']
ies='GA-MB-4000lm-4000k.ies'
sep='_'
faces=['bk','dn','fr','lf','dn','rt']
imageRoot='image'
imageFormat='.png'
effectList=[]
for group in groups:
    sixface=[]
    for face in faces:
        filepath=imageRoot+os.sep+string.join([camera,group,ies,face],'_')+imageFormat
        print filepath
        im = Image.open(filepath)
        ar=np.array(im)
        print ar.shape
        sixface.append(ar)
    et=np.vstack(sixface)
    effectList.append(et)

print effectList
finish=clock()
print "finished  reading image,used time:",(finish-start)

sumX=effectList[1][:,:,0]*0
sumY=effectList[1][:,:,1]*0
sumZ=effectList[1][:,:,2]*0

print "SumX:",sumX,
print "SumY:",sumY,
print "SumZ:",sumZ

for mx in effectList:
    X0,Y0,Z0=ufunc(mx[:,:,0],mx[:,:,1],mx[:,:,2])
    sumX=sumX+X0
    sumY=sumY+Y0
    sumZ=sumZ+Z0
    
print "SumX:",sumX,
print "SumY:",sumY,
print "SumZ:",sumZ

A,B=reinhardCalcAB(sumY)

X,Y,Z=reinhard02Calc(sumX,sumY,sumZ,A,B)

#print "X",X,
#print "Y",Y,
#print "Z",Z

finish=clock()
print "finished used time:",(finish-start)
'''
print "Log Y"
print logY
n1=np.array([X,Y,Z])
n1.shape=(600,600,3)

print n1.shape
print np.sum(Y)/len(Y)
# calculate with Y
'''


