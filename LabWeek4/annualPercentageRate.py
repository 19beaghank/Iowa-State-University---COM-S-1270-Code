#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def annualPercentageRate(i,f,l,d):
    APR = (((i+f)/l)/d)*100
    return APR

def main():
    interest = float(input("What is the interest charge?"))
    fees = float(input("What are the fees?"))
    loan = float(input("What is the loan amount?"))
    days = float(input("How many days is the loan term?"))
    APR = annualPercentageRate(interest,fees,loan,days)
    print(f"The APR is {APR}.")

if __name__ == "__main__":
    main()