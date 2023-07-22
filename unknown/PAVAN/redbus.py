from itertools import *
t=int(input())

for i in range(t):
    n=int(input())
    l=list(str(n))
    p=permutations(l,4)
    l1=[]
    for i in p:
        l1.append(list(i))

    c=n
    f=[]
    for i in l1:
        for j in range(1,len(l)-1):
            a=int(''.join(i[:j+1]))
            b=int(''.join(i[j+1:]))
            x=a+b
            if x<c:
                c=x
                f=[]
                f.append(a+b)
    print(c)




