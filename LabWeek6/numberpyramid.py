#Kevin Beaghan  2/28/2025
#Week 6 Lab - using inputs to generate a pyramid that counts more numbers as the base increases


def numberPyramid(num):
    num_int = int(num)
    for i in range(1,num_int+1):
        print(" "*(num_int-i), end=" ")
        for l in range(1,i+1):
            L = str(l)
            print(L , end=" ")
        print(end="\n")

def main():
    num = input("Please enter a positive integer:")
    numberPyramid(num)

if __name__ == "__main__":
    main()