#Kevin Beaghan  2/28/2025
#Week 6 Lab - using inputs to generate a multiplication table between 2 positive integers

def multiplicationTable(lownum,highnum):
    for i in range(lownum, highnum+1):
        for j in range(lownum, highnum+1):
            print(i*j, end="\t")
        print(end ="\n")
        

def main():
    lownum = int(input("Please enter a positive integer:"))
    highnum = int(input("Please enter a larger positive integer:"))
    multiplicationTable(lownum,highnum)

if __name__ == "__main__":
    main()