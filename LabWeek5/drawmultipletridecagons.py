#Kevin Beaghan 2/21/2025
#Week 5 Lab - Moving week 4 code to modules

import turtle

def tridecagon(s,x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range (13):
        t.forward(s)
        t.left(180-11*180/13)

def drawMulpipleTridecagons(s,x,y,nr,sr,t):
    for i in range(nr):
        tridecagon(s,x,y,t)
        x = x+sr

def main():
    wn=turtle.Screen()
    Frank=turtle.Turtle()
    size = int(input("Choose a side length:"))
    x = int(input("Starting x coordinate?"))
    y = int(input("Starting y coordinate?"))
    nr =int(input("How many tridecagons?"))
    sr = int(input("How far apart should they be?"))
    drawMulpipleTridecagons(size,x,y,nr, sr, Frank)
    turtle.done()

if __name__ == "__main__":
    main()