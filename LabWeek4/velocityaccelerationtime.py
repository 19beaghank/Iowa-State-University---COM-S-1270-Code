#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def velocityaccelerationtime(v,a,t):
    velocity= v+(a*t)
    return velocity

def main():
    velocity = float(input("What is the initial velicity (m/s)?"))
    acceleration = float(input("What is the acceleration (m/s^2)?"))
    time = float(input("What is the time (s)?"))
    velocity_f =     velocityaccelerationtime(velocity,acceleration,time)
    print(f"The final velocity is {velocity_f} (m/s).")

if __name__ == "__main__":
    main()