import math
# Declares Global variables for use in all functions. 
timeMax = 0 # Amount of Time to push the graph to
voltage = 0 # Initial DC Voltage Source
RVal = 0 #Value for Resistor in Series. 
CVal = 0 #Value for Capacitor in Series. 

#Sets Global Variables
def Valueset(V,R,C,T):
    global voltage, RVal, CVal, timeMax
    voltage = float(V)
    RVal = float(R)
    CVal = float(C)
    timeMax = float(T)

#Real Value Calculation of the function
def rcsolcalc():
    global voltage, RVal, CVal, timeMax
    Rcords = [] #Cord list for Graphe, and Table
    i = 0
    while i < timeMax: #Starts a loop that stops when it's equal to asked time.
        newCords = (i,) 
        Volt = ((voltage*math.e**(-1*((i/100)/(RVal*CVal)))),) # Add newly calculated Voltage to the next spot on the list.
        newCords += Volt
        Rcords.append(newCords)
        i += 1
    return Rcords

#euler calculation for the Fuction. 
def eulers(step):
    global voltage, RVal, CVal, timeMax
    step = float(step)
    # i = 1 for initialization. 
    i = 1
    x = [0] # Time steps 
    Yval = [voltage] # Intital Voltage
    Vval = [-1*(Yval[i-1]/(RVal*CVal))] # First DV/DT
    deltaY = [Vval[i-1] * step/100] # First step of Delta Y
    Nval = [0] # how many times it was taken. 
    intialEcords = (0,0,voltage,-1*(Yval[i-1]/(RVal*CVal)),Vval[i-1] * step/100) # Cord list for table, First set of cords are put in. 
    Ecords = [intialEcords]
    while i < timeMax: #Starts a loop that stops when it's equal to asked time.
       x.append(x[i-1] + step/100) # Increments the time step. 
       Yval.append(Yval[i-1] + deltaY[i-1]) # New Y val calculation. 
       Vval.append(-1*(Yval[i] / (RVal * CVal))) # DV/Dt Calculation. 
       deltaY.append(Vval[i] * step/100) # New Delta Y calculation. 
       Nval.append(i) # Step calculation. 
       newEcords = (Nval[i],x[i],Yval[i],Vval[i],deltaY[i])
       Ecords.append(newEcords)
       i += 1
    return Ecords

    



