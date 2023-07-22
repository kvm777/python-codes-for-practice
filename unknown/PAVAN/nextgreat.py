from itertools import *
n,k=map(int,input().split())

l=len(str(k))

s=list(str(n))
l1=[]
c=combinations(s,l)
for i in c:
    l1.append(int(''.join(i)))

c=combinations(s,l+1)
for i in c:
    l1.append(int(''.join(i)))
l1=sorted(l1)[::-1]
x=l1[0]
for i in l1:
    if i>k and x>i:
        x=i

print(x)

