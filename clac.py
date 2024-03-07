import math
def rccalc(timeMax,voltage,Resistance,Capacitance):
    val = []
    i = 0
    while i < timeMax:
        val.append(voltage*math.e**(-1*((i/100)/(Resistance*Capacitance))))
        i += 1
    return val

