#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def distancespeedtime(s,t):
    distance = s*t
    return distance

def main():
    speed = float(input("What is the speed (m/s)?"))
    time = float(input("What is the time (s)?"))
    distance =     distancespeedtime(speed,time)
    print(f"The distance traveled is {distance} (m).")

if __name__ == "__main__":
    main()