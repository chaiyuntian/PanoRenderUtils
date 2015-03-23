__all__=['sRGB2XYZ','sRGB2Y','XYZ2xyY','xyY2XYZ']

def sRGB2XYZ(r,g,b):
    r=r/255.0
    g=g/255.0
    b=b/255.0
    a=0.055
    #1.0+a
    r = pow((r+a)/1.055, 2.4) if r>0.04045 else r/12.92
    g = pow((g+a)/1.055,2.4) if g>0.04045 else g/12.92
    b = pow((b+a)/1.055,2.4) if b>0.04045 else b/12.92
    X = r * 0.4124 + g * 0.3576 + b * 0.1805
    Y = r * 0.2126 + g * 0.715158 + b * 0.0722
    Z = r * 0.0193 + g * 0.1192 + b * 0.9502
    return X,Y,Z

def sRGB2Y(r,g,b):
    r=r/255.0
    g=g/255.0
    b=b/255.0
    #1.0+a
    r = pow((r+0.055)/1.055, 2.4) if r>0.04045 else r/12.92
    g = pow((g+0.055)/1.055,2.4) if g>0.04045 else g/12.92
    b = pow((b+0.055)/1.055,2.4) if b>0.04045 else b/12.92
    Y = r * 0.212656 + g * 0.715158 + b * 0.0721856
    return Y

def XYZ2xyY(X,Y,Z):
    d=X+Y+Z
    if d==0:
        return 0,0,0
    else:
        return X/d,Y/d,Y

def xyY2XYZ(x,y,Y):
    if y==0:
        return 0,0,0
    return x/y*Y,Y,(1-x-y)/y*Y

import numpy

if __name__=='__main__':
    from time import clock
    start=clock()
    for i in range(1600*900):
        print sRGB2Y(0.4,0.4,0.4)
    finish=clock()
    
    print "finished",(finish-start)
    
    
