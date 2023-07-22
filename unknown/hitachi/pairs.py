from itertools import *

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
k=l
l1=[]
f=0
for i in range(n):
    for j in range(n):
        x=[l[i],k[j]]
        if x not in l1:
            l1.append(x)
            f+=1

print(f)
print(l1)

