#Kevin Beaghan 2/21/2025
#Week 5 Lab - Moving week 4 code to modules

def calculatevoltage(r,c):
    voltage = c*r
    return voltage

def volt():
    current = float(input("What is the current?"))
    resistance = float(input("What is the resistance?"))
    voltage =     calculatevoltage(resistance,current)
    print(f"The Voltage is {voltage}.")

def calculateresistance(c,v):
    resistance = v/c
    return resistance

def resist():
    current = float(input("What is the current?"))
    voltage = float(input("What is the voltage?"))
    resistance =     calculateresistance(current,voltage)
    print(f"The resistance is {resistance}.")

def calculatecurrent(r,v):
    current = v/r
    return current

def curr():
    resistance = float(input("What is the resistance?"))
    voltage = float(input("What is the voltage?"))
    current = calculatecurrent(resistance, voltage)
    print(f"The current is {current}.")
