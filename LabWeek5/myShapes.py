#Kevin Beaghan 2/21/2025
#Week 5 Lab - Moving week 4 code to modules

import math

def rectangleperimeter(l,w):
    perimeter = 2*(l+w)
    return perimeter

def rectperim():
    length = float(input("What is the rectangles length?"))
    width = float(input("What is the rectangles width?"))
    perimeter =     rectangleperimeter(length,width)
    print(f"The perimeter of your rectangle is {perimeter}.")

def areaOfCircle(r):
    area = math.pi*(r**2)
    return area

def circarea():
    radius = float(input("What is the circles radius?"))
    area = areaOfCircle(radius)
    print(f"The area of your circle is {area}.")

def areaofrectangle(b,h):
    area = b*h
    return area

def rectarea():
    base = float(input("What is the length of the rectangles base?"))
    height = float(input("What is the rectangles height?"))
    area = areaofrectangle(base, height)
    print(f"The area of your rectangle is {area}.")

def circlecircumference(r):
    circumference = 2*math.pi*r
    return circumference

def circcirc():
    radius = float(input("What is the circles radius?"))
    circumference =    circlecircumference(radius)
    print(f"The circumference of your circle is {circumference}.")
