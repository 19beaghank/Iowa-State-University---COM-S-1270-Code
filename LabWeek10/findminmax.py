#Kevin Beaghan 3/16/2025
#Week 10 Lab - Using lists to find the min and max values of a seriese of inputed integers

def listInput():
    integer=""
    inputList = []
    number = input("Enter an integer (* to stop):")
    while number != "*":
        integer=number
        inputList.append(integer)
        number = input("Enter an integer (* to stop):")
    return inputList

def findMax(inputList):
    max = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] > max:
            max = inputList[i]
    return max

def  findMin(inputList):
    min = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] < min:
            min = inputList[i]
    return min

def main():
    inputList = listInput()
    for i in range(len(inputList)):
        inputList[i] = int(inputList[i])
    min = findMin(inputList)
    max = findMax(inputList)
    print(f"The minimum is:{min} and the maximum is:{max}")

if __name__ == "__main__":
    main()