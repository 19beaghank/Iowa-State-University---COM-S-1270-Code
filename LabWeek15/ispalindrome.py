# Kevin Beaghan 4/28/2025
# [COMS 127 A] Week 15 Lab - Creating two distinct ways to check if a string is a palindrome

def  isPalindromeRecursive(string):
    string = string.lower().replace(" ", "")
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindromeRecursive(string[1:-1])

def isPalindromeIterative(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def main():
    string = input("Enter a string: ")
    print(isPalindromeIterative(string))
    print(isPalindromeRecursive(string))

if __name__ == "__main__":
    main()