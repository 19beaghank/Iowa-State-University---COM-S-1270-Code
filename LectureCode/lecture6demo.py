#Kevin Beaghan 2/6/2025
#Lecture 6 demo - fns

# def foo(a,b):
#     a += 1
#     b += 1
#     return a,b

# c=foo(3,4)
# print(c)
# print(c[0])
# print(c[1])

# c,d=foo(3,4)
# print(c)
# print(d)

# def foo():
#     x = 0
#     x+= 1

# print(x)

# def foo(a,b):
#     a+=1
#     b+=1

# foo(1,1)
# print(a,b)

# x=3
# def foo(x):
#     x=0
#     x+=1
#     print(x)

# foo(x)
# print(x)
# print(foo(x))

# var = 3

# def foo():
#     global var
#     var+=1

# print(var)
# foo()
# print(var)

import module1


def valplustwo(val):
    return val +2

def main():
    val = int(input("integer?"))
    answer = module1.valplustwo(val)
    print(f"answer is {answer}")

if __name__ == "__main__":
    main()