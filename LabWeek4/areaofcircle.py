#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

import math

def areaOfCircle(r):
    area = math.pi*(r**2)
    return area

def main():
    radius = float(input("What is the circles radius?"))
    area = areaOfCircle(radius)
    print(f"The area of your circle is {area}.")

if __name__ == "__main__":
    main()