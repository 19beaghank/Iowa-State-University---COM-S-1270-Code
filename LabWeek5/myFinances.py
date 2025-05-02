#Kevin Beaghan 2/21/2025
#Week 5 Lab - Moving week 4 code to modules

def annualPercentageRate(i,f,l,d):
    APR = (((i+f)/l)/d)*100
    return APR

def APR():
    interest = float(input("What is the interest charge?"))
    fees = float(input("What are the fees?"))
    loan = float(input("What is the loan amount?"))
    days = float(input("How many days is the loan term?"))
    APR = annualPercentageRate(interest,fees,loan,days)
    print(f"The APR is {APR}.")

def compoundamount(p,r,n,t):
    amount = p*(1+r/100/n)**(n*t)
    return amount

def compamount():
    principal = float(input("What is the primcipal amount?"))
    rate = float(input("What are the interest rate?"))
    number = float(input("What is the number of times the interest compounds per year?"))
    time = float(input("How many rears of interest?"))
    amount =     compoundamount(principal,rate,number,time)
    print(f"The accrued amount is {amount}.")
