# Kevin Beaghan 4/28/2025
# [COMS 127 A] Week 15 Lab - Creating two distinct ways to solve the common interview questiona called fizzBuzz

def fizzBuzzDict(integer):
    rules = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    result = []
    for i in range(1, integer + 1):
        output = "".join(value for key, value in rules.items() if i % key == 0)
        result.append(output if output else str(i))
    return result

def  fizzBuzzModulus(integer):
    result = []
    for i in range(1, integer + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Bazz"
        result.append(output if output else str(i))
    return result

def main():
    integer = int(input("Enter an integer: "))
    print(fizzBuzzModulus(integer))
    print(fizzBuzzDict(integer))

if __name__ == "__main__":
    main()