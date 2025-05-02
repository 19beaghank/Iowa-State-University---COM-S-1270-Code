#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

import math

def circlecircumference(r):
    circumference = 2*math.pi*r
    return circumference

def main():
    radius = float(input("What is the circles radius?"))
    circumference =     circlecircumference(radius)
    print(f"The circumference of your circle is {circumference}.")

if __name__ == "__main__":
    main()