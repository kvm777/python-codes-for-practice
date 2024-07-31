from itertools import *

# def greater(num):
#     arr = list(str(num))
#     c = permutations(arr,len(arr))

#     arr1 = []
#     for i in c:
#         arr1.append(int(''.join(i)))

#     arr1.sort()
#     if num == max(arr1):
#         return num
#     else:
#         for i in range(len(arr1)):
#             if arr1[i] == num:
#                 return arr1[i+1]


def nextGreater(num):
    s = list(str(num))
    out=s[0]
    l = list(map(int, s[1:]))
    if l == sorted(l)[::-1]:
        return num
    else:
        m = min(l[2:])
        out+=str(m)
        print(out)
        l.pop(l.index(m))
        l.sort()
        l = list(map(str, l))
        out+=''.join(l)
        return out       
            
n = int(input())
# print(greater(n))
print(nextGreater(n))


"""
1243


"""