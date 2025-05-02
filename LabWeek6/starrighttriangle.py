#Kevin Beaghan  2/28/2025
#Week 6 Lab - Using input to print out a pyramid make of *s

def starRightTriangle(num):
    num_int = int(num)
    for i in range(1,num_int+1):
        print("*"*i)

def main():
    num = input("Please enter a positive integer:")
    starRightTriangle(num)

if __name__ == "__main__":
    main()