import numpy as np

def cutLog10(Y):
    if Y==0:
        Y=2.22E-16
    return np.log10(Y)


def reinhardCalcAB(imgY, key=0.18, phi=8.0, whiteLimit=1E20,Lw=0,logAvgLum=0):
    '''img is a numpy array of all the Y values'''
    if logAvgLum==0:
        ulog10=np.frompyfunc(cutLog10,1,1)
        logY=ulog10(imgY)
        
        c = np.average(logY)
        print "Log Sum Average ", c
        logAvgLum=10.0**(np.average(logY))
        print 'logAvgLum:',logAvgLum
    if Lw==0:
        Lw =np.max(imgY)
    if Lw > whiteLimit:
        Lw = whiteLimit
    A= key /logAvgLum
    B = Lw**2;
    print 'A=',A
    print 'B=',B
    return A,B

def CalcKeyCalcAB(imgY, display=200.0, phi=8.0, whiteLimit=1E20,Lw=0,logAvgLum=0):
    '''img is a numpy array of all the Y values'''
    avgY = np.mean(imgY)
    #avgY = np.average(imgY)
    
    key = calcKey(avgY,display)
    
    if logAvgLum==0:
        ulog10=np.frompyfunc(cutLog10,1,1)
        logY=ulog10(imgY)
        c = np.average(logY)
        print "Log Sum Average ", c
        logAvgLum=10.0**(np.average(logY))
        print 'logAvgLum:',logAvgLum
    if Lw==0:
        Lw =np.max(imgY)
    if Lw > whiteLimit:
        Lw = whiteLimit
    A= key /logAvgLum
    B = Lw**2;
    print 'Key=',key
    print 'A=',A
    print 'B=',B
    return key,A,B

def reinhard02calc_single(X0,Y0,Z0,A,B):
    if A==0 or B==0:
        return 0,0,0
    X1=A*X0
    Y1=A*Y0
    Z1=A*Z0
    Y=Y1*(1+Y1/B)/(1+Y1)
    if Y1==0:
        return 0,0,0
    Z=Z1/Y1*Y
    X=X1/Y1*Y
    return X,Y,Z
    
def reinhard02Calc(X0,Y0,Z0,A,B):
    uEqn4=np.frompyfunc(reinhard02calc_single,5,3)
    X,Y,Z=uEqn4(X0,Y0,Z0,A,B)
    return X,Y,Z
    

def calcKey(avgY,display):
    # The following fomular Authored by XiaoDan&Yawen
    # Key = 6.0*avg^(0.68)/(display^0.477)
    return 6.0*(avgY**0.68)/(display**0.477)
