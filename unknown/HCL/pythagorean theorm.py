from math import *

t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    c=sqrt(a**2+b**2)

    print(int(ceil(c)))


