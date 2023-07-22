from itertools import *
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
c=0
a1=[]
for i in range(n):
    c=combinations(a,i)
    c1=[]
    for i in c:
        c1.append(list(i))
    
    print(c1)
    for i in c1:
        x=1
        for j in i:
            if j>x:
                x=j
        c+=int(x)
        
    c1=[]

print(c)