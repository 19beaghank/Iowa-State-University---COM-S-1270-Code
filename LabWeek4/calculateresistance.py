#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def calculateresistance(c,v):
    resistance = v/c
    return resistance

def main():
    current = float(input("What is the current?"))
    voltage = float(input("What is the voltage?"))
    resistance =     calculateresistance(current,voltage)
    print(f"The resistance is {resistance}.")

if __name__ == "__main__":
    main()