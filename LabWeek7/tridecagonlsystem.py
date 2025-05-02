#Kevin Beaghan 3/6/2025
#Week 7 Lab

#https://runestone.academy/ns/books/published/iowastateuniversity_thinkcspy_spring25/Strings/TurtlesandStringsandLSystems.html
#accessed 3/7/2025

import random
import turtle
import tridecagonturtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character
    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "H":
            t=turtle.Turtle()
            wn=turtle.Screen()
            s = int(input("Choose a side length:"))
            x = int(input("Starting x coordinate?"))
            y = int(input("Starting y coordinate?"))
            tridecagonturtle.tridecagon(s,x,y,t)
            turtle.done()
        elif cmd == "P":
            x = random.randrange(-(wn.window_width()//2), wn.window_width()/2)
            y = random.randrange(-(wn.window_height()//2), wn.window_height()/2)
            t.penup()
            t.goto(x,y)
            t.pendown()

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

if __name__ == "__main__":
    main()