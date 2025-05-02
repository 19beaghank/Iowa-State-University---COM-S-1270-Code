#Kevin Beaghan  2/7/2025
#Lab A Week 3 - Using inputs to calculate APY

interest = float(input("What is the interest charge?"))
fees = float(input("What are the fees?"))
loan = float(input("What is the loan amount?"))
days = float(input("How many days is the loan term?"))

APR = (((interest+fees)/loan)/days)*100

print(f"The APR is {APR}.")