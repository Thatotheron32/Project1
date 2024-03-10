import math
timeMax = 0
voltage = 0
RVal = 0
CVal = 0
#Sets Global Variables 
9def Valueset(V,R,C,T):
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
    Vval = [-1*(voltage)/(RVal*CVal)]
    Sval = [0]
    Nval = [0]
    while i < timeMax:
       Sval.append(Sval[i-1] + step)
       Vval.append(Vval[i-1] + step*(-1*((voltage)/(RVal*CVal))))
       Nval.append(i)
       i += 1
    return Vval, Sval,

    



