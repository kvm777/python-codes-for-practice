import math
from itertools import *

# arrays... list


# l = [10, 20, "mah", True, 4.56]

# for i in range(len(l)):
#     if i == len(l)-1:
#         print(l[i])
#     else:
#         print(l[i], end=",")



# print()
# for i in l:
#     if l.index(i) == len(l)-1:
#         print(i)
#     else:
#         print(i, end=",")



# for i in l:
#     if type(i) == int:
#         print(i)



"""
next perfect square..
1 4 9 16 25
"""
# n = int(input())

# def nextPerfectSquare(num):
#     nxt = math.floor(math.sqrt(num)) + 1
#     return nxt*nxt 

# print(nextPerfectSquare(n))



"""
nex b primes of given number a
4 5
[5, 7, 11, 13, 17]
"""
# a = int(input())
# b = int(input())

# a, b = map(int, input().split())

#  l = list(map(int,input().split()))

# def nextPries(num1, num2):
#     l = []
#     t = num1 #t = 4
#     while len(l)<num2:
#         t+=1
#         if t==2:
#             l.append(t)
#         else:
#             for i in range(2,t):
#                 if t%i == 0:
#                     break
#             else:
#                 l.append(t)

#     return l
            
# print(*nextPries(a, b))



"""
input: int 1234
output: 1234 + 4321 = ?

"""

# n = int(input())
# # n2 = int(str(n)[::-1])
# n2 = str(n)
# n2 = n2[::-1]
# n2 = int(n2)

# print(n + n2)
# print(str(n) + str(n2))



"""
aeiou

input: vinayrajupavan   
        iaauaa
        aauaai
output: v a n a yr u j a p a v i n

"""

# s = input()
# # vinay
# # vaniy

# v = "aeiouAUEIOU"
# vow = []
# idx = []
# for i in s:
#     if i in v:
#         vow.append(i)
#         idx.append(s.index(i))
# s1 = ""
# for i in s:
#     if s.index(i) in idx:
#         s1+=vow[-1]
#         vow.pop()
#     else:
#         s1+=i
# print(s1)


"""
itertools  -->>  permutations & combinations

l = [a,b,c,d,e]

cobinations = [a,b,c], [a,c,d], [a,d,e], [a,b,d
            [b,c,a]
"""

# c = [10, 20, 30, 40, 50]

# com = combinations(c,3)

# # print(list(com))
# com_list = []
# for i in com:
#     com_list.append(list(i))


# print("combinations")
# print(com_list)



# per = permutations(c, 3)

# per_list = []

# for i  in per:
#     per_list.append(list(i))

# print("permutations")
# print(per_list)
