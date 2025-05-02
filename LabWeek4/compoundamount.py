#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def compoundamount(p,r,n,t):
    amount = p*(1+r/100/n)**(n*t)
    return amount

def main():
    principal = float(input("What is the primcipal amount?"))
    rate = float(input("What are the interest rate"))
    number = float(input("What is the number of times the interest compounds per year?"))
    time = float(input("How many rears of interest?"))
    amount =     compoundamount(principal,rate,number,time)
    print(f"The accrued amount is {amount}.")

if __name__ == "__main__":
    main()