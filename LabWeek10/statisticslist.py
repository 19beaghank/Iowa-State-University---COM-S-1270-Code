#Kevin Beaghan 3/16/2025
#Week 10 Lab - Finding the mean and median of a list of randomly generated integers 

import random

def generateInput():
    inputList=[]
    length = random.randrange(200, 501)
    for num in range(length):
        x = random.randint(1,2001)
        inputList.append(x)
    return inputList

def findMean(inputList):
    sum = 0
    for num in inputList:
        sum+=num
    mean = sum/len(inputList)
    return mean

def findMedian(inputList):
    inputList.sort()
    if len(inputList) % 2 == 1:
        median = inputList[len(inputList) // 2]
    else:
        median = (inputList[len(inputList) // 2 - 1] + inputList[len(inputList) // 2]) / 2
    return median

def main():
    inputList=generateInput()
    median = findMedian(inputList)
    mean = findMean(inputList)
    print(f"The median is:{median} and the mean is:{mean}")

if __name__ == "__main__":
    main()