import math
timeMax = 0
voltage = 0
RVal = 0
CVal = 0
#Sets Global Variables 
def Valueset(V,R,C,T):
    globals()[voltage] = V
    globals()[RVal] = R
    globals()[CVal] = C
    globals()[timeMax] = T

#Real Value Cal of the function
def rccalc():
    val = []
    i = 0
    while i < timeMax:
        val.append(voltage*math.e**(-1*((i/100)/(RVal*CVal))))
        i += 1
    return val
#eulers form for
def eulers(step):
    i = 0
    Vval = []
    Sval = [0]
    Nval = [0]
    while i < timeMax:
       Sval.append(Sval[i] + step)
       Vval.append(Vval[i-1] + step(-1*((voltage)/(RVal*CVal))))
       Nval.append(i)
       i += 1
    return Vval, Sval,

    



