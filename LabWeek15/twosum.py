# Kevin Beaghan 4/28/2025
# [COMS 127 A] Week 15 Lab - Creating multiple approaces to solve the Two Sum problem

def twoSumDictAll(numbers, target):
    num_dict = {}
    pairs = []
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            for index in num_dict[complement]:
                pairs.append([index, i])
        num_dict.setdefault(num, []).append(i)
    return pairs if pairs else None 

def twoSumLoopsAll(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append([i, j])
    return pairs if pairs else None

def twoSumDict(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None

def twoSumLoops(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None

def main():
    numbers = [1,0,3,5,2]
    target = 4
    print(twoSumLoops(numbers, target))
    print(twoSumDict(numbers, target))
    print(twoSumLoopsAll(numbers, target))
    print(twoSumDictAll(numbers, target))

if __name__ == "__main__":
    main()