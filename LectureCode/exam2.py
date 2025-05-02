# def isPrime(n):
#     if n <=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i ==0:
#             return False
#     return True
# def listprimes(howmany):
#     primes=[]
#     if howmany <=0:
#         return primes
#     x=1
#     while len(primes)<howmany:
#         if isPrime(x) == True:
#             primes.append(x)
#         x+=1
#     return primes


# x = 128
# y="programing"
# z=x>100
# print(z)
# z="gram" in y
# print(z)
# z= x%8==0 and x%7!=0
# print(z)
# z=len(y)>5
# print(z)
# z=x%len(y)==0
# print(z)
# z= y[0]=="p" and y[len(y)-1]=="g"
# print(z)


# def foo(a,b,c):
#     result = False
#     if a>b and c!=5:
#         result = True
#     if a == 10 or b%2 == 0:
#         result = True
#     if a+b==c:
#         result=False
#     return result

# def foo1(a,b,c):
#     result = ((a > b and c != 5) or (a == 10 or b % 2 == 0)) and not (a + b == c)
#     return result


# def calculateTotal(shirt, mug, tax):
#     free_mugs = shirt // 3
#     paid_mugs = max(0, mug - free_mugs)
#     total_items = shirt + paid_mugs
#     item_cost = (shirt * 15) + (paid_mugs * 5)
#     if total_items < 50:
#         item_cost += 30
#     total_cost = (item_cost * (1 + tax)) +20
#     return total_cost


# def transformString(S):
#     result = []
#     i = 0
#     while i < len(S):
#         if i + 2 < len(S) and S[i] == S[i + 1] == S[i + 2]:
#             result.append("X")
#             i += 3
#         elif i + 1 < len(S) and S[i] == S[i + 1]:
#             result.append(S[i] * 3)
#             i += 2
#         else:
#             result.append(S[i])
#             i += 1
#     return "".join(result)