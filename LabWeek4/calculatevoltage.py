#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def calculatevoltage(r,c):
    voltage = c*r
    return voltage

current = float(input("What is the current?"))
resistance = float(input("What is the resistance?"))

def main():
    current = float(input("What is the current?"))
    resistance = float(input("What is the resistance?"))
    voltage =     calculatevoltage(resistance,current)
    print(f"The Voltage is {voltage}.")

if __name__ == "__main__":
    main()