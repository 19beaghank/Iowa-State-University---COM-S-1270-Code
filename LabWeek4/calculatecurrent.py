#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def calculatecurrent(r,v):
    current = v/r
    return current

def main():
    resistance = float(input("What is the resistance"))
    voltage = float(input("What is the voltage?"))
    current = calculatecurrent(resistance, voltage)
    print(f"The current is {current}.")

if __name__ == "__main__":
    main()