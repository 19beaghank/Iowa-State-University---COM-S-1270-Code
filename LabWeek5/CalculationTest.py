#Kevin Beaghan 2/21/2025
#Week 5 Lab - Using while loop for terminating imported calculation tests

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    running = True
    while running:
        help = input("Do you need help with [Finances], [OhmsLaw], [Physics], or [Shapes]?")
        if help == "Finances":
            finance = input("Do you want to calculate [APR] or compound [amount]?")
            if finance == "APR":
                myFinances.APR()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]")
                    break
            elif finance == "amount":
                myFinances.compamount()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]") 
        elif help == "Physics":
            phys = input("Do you need to calculate [distance] or [velocity]?")
            if phys == "distance":
                myPhysics.distance()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]") 
            elif phys == "velocity":
                myPhysics.velocity()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]") 
        elif help == "OhmsLaw":
            ohm = input("Do you need help calculating [current], [voltage], or [resistance]?")
            if ohm == "current":
                myOhmsLaw.curr()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]") 
            elif ohm == "voltage":
                myOhmsLaw.volt()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]") 
            elif ohm == "resistance":
                myOhmsLaw.resist()
                contin = input("Do you wish to continue, [YES] or [NO]?")
                if contin =="YES":
                    main()
                elif contin == "NO":
                    running = False
                    return running
                else:
                    print("Please only use [YES] or [NO]")
        elif help == "Shapes":
            shape = input("Are you looking at a [rectangle] or a [circle]?")
            if shape == "rectangle":
                rectangle = input("Do you want to calculate [perimeter] or [area]?")
                if rectangle == "perimeter":
                    myShapes.rectperim()
                    contin = input("Do you wish to continue, [YES] or [NO]?")
                    if contin =="YES":
                        main()
                    elif contin == "NO":
                        running = False
                        return running
                    else:
                        print("Please only use [YES] or [NO]") 
                elif rectangle == "area":
                    myShapes.rectarea()
                    contin = input("Do you wish to continue, [YES] or [NO]?")
                    if contin =="YES":
                        main()
                    elif contin == "NO":
                        running = False
                        return running
                    else:
                        print("Please only use [YES] or [NO]")
            elif shape == "circle":
                circle = input("Do you want to calculate [circumference] or [area]?")
                if circle == "circumference":
                    myShapes.circcirc()
                    contin = input("Do you wish to continue, [YES] or [NO]?")
                    if contin =="YES":
                        main()
                    elif contin == "NO":
                        running = False
                        return running
                    else:
                        print("Please only use [YES] or [NO]")
                elif circle == "area":
                    myShapes.circarea()
                    contin = input("Do you wish to continue, [YES] or [NO]?")
                    if contin =="YES":
                        main()
                    elif contin == "NO":
                        running = False
                        return running
                    else:
                        print("Please only use [YES] or [NO]")
        else:
            print("""Please only choose [Finances], [OhmsLaw], [Physics], or [Shapes]?
            """)
            main()

if __name__ == "__main__":
    main()