from math import *
a=list(map(int,input().split()))
v= floor(sum(a)/len(a))

if a.count(v)<2:
    print(-1)
else:
    x=a.index(v)
    y=len(a)-a[::-1].index(v)-1
    print(abs(x-y))


