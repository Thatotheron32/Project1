# Clean Up code is needed
import math
timeMax = 0
voltage = 0
RVal = 0
CVal = 0
#Sets Global Variables +
def Valueset(V,R,C,T):
    global voltage, RVal, CVal, timeMax
    voltage = V
    RVal = R
    CVal = C
    timeMax = T

#Real Value Cal of the function
def rccalc():
    global voltage, RVal, CVal, timeMax
    val = []
    i = 0
    while i < timeMax:
        val.append(voltage*math.e**(-1*((i/100)/(RVal*CVal))))
        i += 1
    return val

#eulers form for
def eulers(step):
    global voltage, RVal, CVal, timeMax
    i = 1
    x = [0]
    Yval = [voltage]
    Vval = [(Yval[i-1]-(Yval[i-1]/(RVal*CVal)))]
    deltaY = [Vval[i-1] * step]
    Nval = [0]
    while i < timeMax:
       x.append(x[i-1] + step)
       Yval.append(Yval[i-1] + deltaY[i-1]) # issue with adding two list need to look into -dongyu 2:36AM 3/19
       Vval.append(Yval[i] - (Yval[i] / (RVal * CVal)))
       deltaY.append(Vval[i] * step)
       Nval.append(i)
       i += 1
    return Vval, x,

    



