#Kevin Beaghan 2/14/2025
#Lab Week 4 - Using Main function, random module and inputs to generate random products

import random

def randomproduct(a,b,c):
    product = 1
    for i in range(a):
        range_total = random.randrange(b,c+1)
        product = product*range_total
    return product

def main():
    integer = int(input("Please enter an integer:"))
    range_low = int(input("Please enter another integer:"))
    range_high = int(input("Please enter an integer greater than the previous one:"))
    answer = randomproduct(integer, range_low, range_high)
    print(f"Your answer is {answer}")


if __name__ == "__main__":
    main()