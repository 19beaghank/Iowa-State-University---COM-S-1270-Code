#Kevin Beaghan 2/14/2025
#Lab Week 4 - Using Main function, turtle and inputs to draw a tridecagon 

import turtle

def tridecagon(s,x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range (13):
        t.forward(s)
        t.left(180-11*180/13)

wn=turtle.Screen()
Frank=turtle.Turtle()

def main():
    size = int(input("Choose a side length:"))
    x = int(input("Starting x coordinate?"))
    y = int(input("Starting y coordinate?"))
    tridecagon(size,x,y,Frank)
    turtle.done()

if __name__ == "__main__":
    main()