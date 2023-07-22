from math import *
n=input()
l=list(map(int,input().split()))

c=0
for i in l:
    x=int(sqrt(i))
    if x*x==i:
        c+=x
        
print(c)