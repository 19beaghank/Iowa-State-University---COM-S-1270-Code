#Kevin Beaghan 2/21/2025
#Week 5 Lab - Moving week 4 code to modules

def distancespeedtime(s,t):
    distance = s*t
    return distance

def distance():
    speed = float(input("What is the speed (m/s)?"))
    time = float(input("What is the time (s)?"))
    distance =     distancespeedtime(speed,time)
    print(f"The distance traveled is {distance} (m).")

def velocityaccelerationtime(v,a,t):
    velocity = v+(a*t)
    return velocity

def velocity():
    velocity = float(input("What is the initial velicity (m/s)?"))
    acceleration = float(input("What is the acceleration (m/s^2)?"))
    time = float(input("What is the time (s)?"))
    velocity_f =     velocityaccelerationtime(velocity,acceleration,time)
    print(f"The final velocity is {velocity_f} (m/s).")
