import clac
error = True
while error :
    prompt = "\nPlease give an input for a max time that you would like to run. "
    prompt += "\nPlease enter a time between 200 and 1000 centiseconds.: "
    message = input(prompt)
    message = int(message)
    prompt2 = "\nPlease give an input for a intial voltage "
    prompt2 += "\nPlease enter a Voltage between 1 Volt and 50 Volts"
    if message > 1000:
        print("\nThis time frame is too big, please enter something under 1000 centiseconds.")
    elif message < 1:
        print("\nThis time frame is too small, please enter something after 1 centiseconds.")
    else:
        print("\nHere is the RC circut graph with ", message, " as the time frame for this example." + "\nThis is the exact solution with an equilibrium solution at 0.")
        print(clac.rccalc(message,1))
        
    
    
