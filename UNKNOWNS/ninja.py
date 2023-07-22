from itertools import *
n,k=map(int,input().split())

l=list(range(n))

p=permutations(l,len(l))
l1=[]
for i in p:
    l1.append(list(i))
f=0
for i in l1:
    c=0
    for j in range(len(i)):
        if i[j]==j:
            c+=1
    if c>=k:
        f+=1

print(f)





