#Kevin Beaghan 2/4/2025
#Functions demo for lecture 5

# def multiplyplustwo(a,b):
#     answer = a*b+2
#     return answer

# sln = multiplyplustwo(3,6)
# print(sln)


# def printname(n,nr):
#     for i in range(nr):
#         print(n)

# name = input("Name?")
# number = int(input("Fav number?"))
# printname(name,number)
# print("The End")


# def cubeval(number):
#     answer = number*number*number
#     return answer

# val = int(input("Integer?"))
# numb = cubeval(val)
# print(numb)

def powerval(number,power):
    for i in range(power):
        answer = number**power
    return answer

val = int(input("Integer?"))
pow = int(input("Power?"))
numb = powerval(val, pow)
print(numb)