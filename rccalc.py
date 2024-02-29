import math
def rccalc(resValue, capValue, timeMax):
    val = []
    i = 0
    while i < timeMax :
        val[i] = math.e**(-1*(i/(resValue*capValue)))
        i += i
    return val

