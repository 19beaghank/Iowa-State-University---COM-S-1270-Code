# Kevin Beaghan 4/28/2025
# [COMS 127 A] Week 15 Lab - Creating two distinct ways to reverse a string

def  reverseRecursive(string):
    if len(string) <= 1:
        return string
    return reverseRecursive(string[1:]) + string[0]

def reverseIterative(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    string = input("Enter a string: ")
    print(reverseIterative(string))
    print(reverseRecursive(string))

if __name__ == "__main__":
    main()