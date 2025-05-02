#Kevin Beaghan  2/7/2025
#Lab A Week 3 - Using inputs to calculate a compound amount

principal = float(input("What is the primcipal amount?"))
rate = float(input("What are the interest rate"))
number = float(input("What is the number of times the interest compounds per year?"))
time = float(input("How many rears of interest?"))

amount = principal*(1+rate/100/number)**(number*time)

print(f"The accrued amount is {amount}.")