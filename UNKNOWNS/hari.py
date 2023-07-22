from itertools import *
def solution (no of elemys,,,,,,,):  
    
    n=noofElements
    m=modulo_divisor
    s=arr

    p=[]

    for i in range(1,n+1):
        x=combinations(s,i)
        for j in x:
            p.append(list(j))
        x=[]

    c=0
    for i in p:
        v=sum(i)%m
        if v>c:
            c=v
    return c
