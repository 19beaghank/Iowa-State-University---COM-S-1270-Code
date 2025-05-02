#Kevin Beaghan 3/6/2025
#Week 7 Lab - Using different methods to check if an inputed string is a palindrome

import reversestring

def palindromeCheckV2(palindrome):
    start = 0
    end = len(palindrome)-1
    while start<end:
        if palindrome[start] != palindrome[end]:
            return False
        start +=1
        end-=1
    return True

def palindromeCheckV1(palindrome):
    palin = reversestring.reverseStringVX(palindrome)
    if palin == palindrome:
        return True
    else:
        return False

def main():
    palindrome = input("Please enter a string:")
    version = input("Do you want to use version [1] or [2]?")
    if version == "1":
        pali = palindromeCheckV1(palindrome)
    elif version == "2":
        pali = palindromeCheckV2(palindrome)
    else:
        print("Please choose only [1] or [2]")
    if pali:
        print(f"{palindrome} is a palindrome")
    else:
        print(f"{palindrome} is not a palindrome")

if __name__ == "__main__":
    main()