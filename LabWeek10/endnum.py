#Kevin Beaghan 3/16/2025
#Week 10 Lab - Putting a series of inputted integers and then sorting the chosen number to the end of the list

def listInput():
    integer=""
    inputList = []
    number = input("Enter an integer (* to stop):")
    while number != "*":
        integer=number
        inputList.append(integer)
        number = input("Enter an integer (* to stop):")
    return inputList

def endNum(inputList, num):
    count = inputList.count(num)
    newList = [x for x in inputList if x != num]
    return newList + [num] * count

def main():
    inputList = listInput()
    num = input("Please enter an integer:")
    answer = endNum(inputList, num)
    print(f"When inputList = {inputList} and num = {num} ==> {answer}")

if __name__ == "__main__":
    main()