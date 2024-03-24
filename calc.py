import math
# Declares Global variables for use in all functions. 
timeMax = 0 # Amount of Time to push the graph to
voltage = 0 # Initial DC Voltage Source
RVal = 0 #Value for Resistor in Series. 
CVal = 0 #Value for Capacitor in Series. 

#Sets Global Variables
def Valueset(V,R,C,T):
    global voltage, RVal, CVal, timeMax
    voltage = V
    RVal = R
    CVal = C
    timeMax = T

#Real Value Calculation of the function
def rccalc():
    global voltage, RVal, CVal, timeMax
    val = [] #List of calcuated Voltage Values.
    i = 0
    while i < timeMax: #Starts a loop that stops when it's equal to asked time.
        val.append(voltage*math.e**(-1*((i/100)/(RVal*CVal)))) # Add newly calculated Voltage to the next spot on the list.
        i += 1
    return val

#euler calculation for the Fuction. 
def eulers(step):
    global voltage, RVal, CVal, timeMax
    # i = 1 for initialization. 
    i = 1
    x = [0] # Time steps 
    Yval = [voltage] # Intital Voltage
    Vval = [-1*(Yval[i-1]/(RVal*CVal))] # First DV/DT
    deltaY = [Vval[i-1] * step] # First step of Delta Y
    Nval = [0] # how many times it was taken. 
    while i < timeMax: #Starts a loop that stops when it's equal to asked time.
       x.append(x[i-1] + step) # Increments the time step. 
       Yval.append(Yval[i-1] + deltaY[i-1]) # New Y val calculation. 
       Vval.append(-1*(Yval[i] / (RVal * CVal))) # DV/Dt Calculation. 
       deltaY.append(Vval[i] * step) # New Delta Y calculation. 
       Nval.append(i) # Step calculation. 
       i += 1
    return Yval,Vval, x,deltaY, Nval

    



