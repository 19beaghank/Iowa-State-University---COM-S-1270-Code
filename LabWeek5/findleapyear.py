#Kevin Beaghan 2/21/2025
#Week 5 Lab - Creating function using if/elif/else statements to determine if a year is a leap year

def isLeap(year):
    if year%400==0:
        return True
    elif year%100 ==0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

def main():
    year = int(input("Please enter a year?"))
    leap = isLeap(year)
    if leap == True:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()