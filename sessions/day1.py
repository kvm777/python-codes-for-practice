# strings.

# s = "python"
# s[0] = "c"

# s = "c" + s[1:]
# print(s)


# s = "fffw55*)"
# print(s.isalnum())

# s = "python"

# print(s.partition("t"))

# print(s.index("o"))

# str[start idx: last idx +1: step]

# print(s[2:5])
# print(s[:5])

# print(s[::2])




# s = "hello world"

# 1) count of "l"
# 2) reverse string without using slicing.
# 3) len of str witout using len() method
# 4) unique characters in string. "hewrd"
# 5) count of each letter


# s1 = "hello world"

# d={}
# for i in s1:
#     d[i] = s1.count(i)
    # print(i,":",d[i])


# print("next")
# for i in d:
#     print(i,":",d[i])


# s2 = "hello world"

# d = {}

# key and value  ->items

# for i in s2:
#     d[i] = s2.count(i)


# print(d)
# print(d.items())
# print(d.keys())



"""
input: 7
output: prime

input : 4
output: not prime

"""

# def isprime(num):
#     # if num == 0 or num == 1:
#     #     return "not prime"
#     # if num == 2:
#     #     return "prime"
#     if num>=2:
#         c = 0
#         for i in range(1,num+1):
#             if num%i == 0:      
#                 c+=1
            
#         if c == 2:
#             return "prime"
#         else:
#             return "not prime"
#     else:
#         return "not prime"

# n = int(input())
# print(isprime(n))


# for else
# break

# def isprime1(num):
#     if num == 0 or num ==1:
#         return "not"
#     if num == 2:
#         return "prime"
    
#     for i in range(2,num//2 +1):
#         if num%i == 0:
#             return "not prime"
#             break
#     else:
#         return "prime"

#     pass

# n = int(input())
# print(isprime1(n))


# n = int(input())

# l = []
# for i in range(n):
#     x = input()
#     l.append(x)

# print(l)


l = list(map(int,input().split()))

# s = input()
# print(s.split())

# l = list(map(int, s.split()))


print(l)