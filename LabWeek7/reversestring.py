#Kevin Beaghan 3/6/2025
#Week 7 Lab - Using different methods to reverse an inputed string

def reverseStringVX(reverse): #to allow palindromecheck access to these
    version = input("Do you want to use version [1], [2], [3], [4], or [5]?")
    if version == "1":
        rev=reverseStringV1(reverse)
    elif version == "2":
        rev=reverseStringV2(reverse)
    elif version == "3":
        rev=reverseStringV3(reverse)
    elif version == "4":
        rev=reverseStringV4(reverse)
    elif version == "5":
        rev=reverseStringV5(reverse)
    else:
        print("Please choose only [1], [2], [3], [4], or [5]")
    return rev

def reverseStringV5(reverse):
    rev = ""
    i = len(reverse)-1
    while i>=0:
        rev += reverse[i]
        i -= 1
    return rev

def reverseStringV4(reverse):
    rev = ""
    for char in reverse:
        rev = char + rev
    return rev

def reverseStringV3(reverse):
    rev = ""
    for i in range(len(reverse)-1, -1, -1):
        rev += reverse[i]
    return rev

def reverseStringV2(reverse):
    return ''.join(reversed(reverse))

def reverseStringV1(reverse):
    return reverse[::-1]

def main():
    reverse = input("Please enter a string:")
    version = input("Do you want to use version [1], [2], [3], [4], or [5]?")
    if version == "1":
        rev=reverseStringV1(reverse)
    elif version == "2":
        rev=reverseStringV2(reverse)
    elif version == "3":
        rev=reverseStringV3(reverse)
    elif version == "4":
        rev=reverseStringV4(reverse)
    elif version == "5":
        rev=reverseStringV5(reverse)
    else:
        print("Please choose only [1], [2], [3], [4], or [5]")
    print(rev)

if __name__ == "__main__":
    main()