from itertools import *
x=int(input())
n,c=1,0
while(c<x):
    n+=1
    for i in range(2,n+1):
        if(n%i==0):
            break
    if(i==n):
        c=c+1
l=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i==2 :
            l.append(i)
        elif i%j==0:
            break
    else:
        l.append(i)

l=l+l[:len(l)//2]
f=[]

for i in range(1,len(l)+1):
    p=combinations(l,i)
    for i in p:
        if sorted(list(i)) not in f:
            f.append(sorted(list(i)))

c=0
for i in f:
    if sum(i)==n:
        print(i)
        c+=1

print(c)