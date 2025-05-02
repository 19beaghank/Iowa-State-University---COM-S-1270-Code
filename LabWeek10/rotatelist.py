#Kevin Beaghan 3/16/2025
#Week 10 Lab - Using a list of inputed integers and rotating the list a chosen number of spaces

def listInput():
    inputList = []
    number = input("Enter an integer (* to stop):")
    while number != "*":
        inputList.append(number)
        number = input("Enter an integer (* to stop):")
    return inputList

def rotateList(list, num):
    n = len(list)
    num = num % n
    return list[-num:] + list[:-num]

def main():
    inputList = listInput()
    rot = int(input("Please enter an integer:"))
    rotated = rotateList(inputList, rot)
    print(f"When inputList = {inputList} and rot = {rot} ==> {rotated}")

if __name__ == "__main__":
    main()