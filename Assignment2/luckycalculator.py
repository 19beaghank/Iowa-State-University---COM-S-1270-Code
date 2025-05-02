#Kevin Beaghan 2/15/2025
#Assignment 2 - Practice mathmatical operations, defining functions, and random module to create a lucky calculator

import random

print("""Lucky Calculator
Kevin Beaghan
[COM S 127 1]
""")

def addition(a,b):
    answer = a+b
    return answer

def subtraction(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    if b==0:
        print("ERROR: divisor=0")
        b=1
    answer = a/b
    return answer

def floordivide(a,b):
    if b==0:
        print("ERROR: divisor=0")
        b=1
    answer = a//b
    return answer

def modulus(a,b):
    if b==0:
        print("ERROR: divisor=0")
        b=1
    answer = a%b
    return answer

def exponent(a,b):
    answer = a**b
    return answer

def LuckyNum():
    luck = int(input("Please enter an integer:"))
    luck = random.randrange(0,abs(luck)+1)**random.randrange(0,abs(luck)+1)%random.randrange(1,abs(luck)+2)
    print(f"Your lucky number is:{luck}")

def MathHelp():
    operate = input("Please select an Operation [+], [-], [*], [/], [//], [%], [**]:")
    if operate == "+":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = addition(x,y)
        print(f"{x}+{y}={answer}")
    elif operate == "-":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = subtraction(x,y)
        print(f"{x}-{y}={answer}")
    elif operate == "*":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = multiply(x,y)
        print(f"{x}*{y}={answer}")
    elif operate == "/":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = divide(x,y)
        print(f"{x}/{y}={answer}")
    elif operate == "//":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = floordivide(x,y)
        print(f"{x}//{y}={answer}")
    elif operate == "%":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = modulus(x,y)
        print(f"{x}%{y}={answer}")
    elif operate == "**":
        x = int(input("Please enter an integer:"))
        y = int(input("Please enter another integer:"))
        answer = exponent(x,y)
        print(f"{x}**{y}={answer}")
    else:
        print("""
        ERROR: Please use only +, -, *, /, //, %, or **
        """)
        MathHelp()

def calculator():
    calc = input("""What are you lookin' for?
    Help with [M]ath?
    Feeling [L]ucky?
    [D]one already?
    :""")
    if calc == "M":
        MathHelp()
    elif calc=="L":
        LuckyNum()
    elif calc == "D":
        print("""
        OK, goodbye.""")
    else:
        print("""
        Please enter only M, L, or D.
        """)
        calculator()

if __name__ == "__main__":
    calculator()