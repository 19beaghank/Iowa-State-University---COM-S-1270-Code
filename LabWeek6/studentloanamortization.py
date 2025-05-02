#Kevin Beaghan  2/28/2025
#Week 6 Lab - 

#https://www.investopedia.com/terms/a/amortization.asp
#accessed 2/28/2025

def studentLoanAmortization(p, r, y):
    print("Period\tTotal Payment Due\tCompound Interest\tPrincipal Due\tPrincipal Balance")
    months = y*12
    rate = r/12
    q = (1+rate)**months
    monthly = p*(rate*q/(q-1))
    interest = p*r/months
    balance = p-monthly+interest
    principal_due = monthly-interest
    for i in range(1,months+1):
        print(f"{i}\t{round(monthly, 2)}\t\t\t{round(interest,2)}\t\t\t{round(principal_due,2)}\t\t{round(balance,2)}")
        interest = balance*r/months
        principal_due = monthly-interest
        balance = balance-monthly+interest

def main():
    principle = float(input("Please enter the principle amount:"))
    rate = float(input("Please enter the yearly interest rate (as a decimal):"))
    years = int(input("Please enter the number of years:"))
    studentLoanAmortization(principle, rate, years)

if __name__ == "__main__":
    main()