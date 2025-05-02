#Kevin Beaghan 2/14/2025
#Lab Week 4 - Using Main function, iteratione and inputs to estimate square roots of numbers

def sqrtint(x,i):
    # https://www.cuemath.com/algebra/square-root-of-2/
    # Accessed 2/14/2025
    y=(x+1)/2
    for j in range(i-1):
        y = (x/y+y)/2
    return y

def main():
    number = int(input("Please enter the number you want to know the root of:"))
    iter = int(input("How many iterations of approzimation?"))
    sqrt = sqrtint(number,iter)
    print(f"The approximated square root of your integer is {sqrt}.")

if __name__ == "__main__":
    main()