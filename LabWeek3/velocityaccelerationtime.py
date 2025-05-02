#Kevin Beaghan  2/7/2025
#Lab A Week 3 - Using inputs to calculate a final velocity

velocity_initial = float(input("What is the initial velicity (m/s)?"))
acceleration = float(input("What is the acceleration (m/s^2)?"))
time = float(input("What is the time (s)?"))

velocity_final = velocity_initial+(acceleration*time)

print(f"The final velocity is {velocity_final} (m/s).")