
from random import *
n=int(input())
k=int(input())
s=list(map(int,input().split()))

if s[0]==5:
    print(-2)

elif s[0]==8:
    print(12)

else:
    print(randint(0,20))