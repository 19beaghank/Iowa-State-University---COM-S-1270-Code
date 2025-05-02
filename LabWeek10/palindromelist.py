#Kevin Beaghan 3/16/2025
#Week 10 Lab - Putting inputed strings into a list and finding if the list is a palindrome

def listInput():
    inputstring= ""
    inputList = []
    string = input("Enter an string (* to stop):")
    while string != "*":
        inputstring=string
        inputList.append(inputstring)
        string = input("Enter an string (* to stop):")
    return inputList

def  palindromeList(inputList):
    for i in range(len(inputList) // 2):
        if inputList[i] != inputList[-(i + 1)]:
            return False
    return True

def main():
    inputList = listInput()
    print(palindromeList(inputList))

if __name__ == "__main__":
    main()