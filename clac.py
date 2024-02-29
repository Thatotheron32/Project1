import math
def rccalc(timeMax,voltage):
    val = []
    i = 0
    while i < timeMax:
        val.append(math.e**(-1*((i/100)/(10*0.001))))
        i += 1
    return val

