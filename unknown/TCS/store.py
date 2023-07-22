from statistics import *
n,t=map(int,input().split())
l1=[]
for i in range(n):
    x=list(map(int,input().split()))
    l1.append(x)
f=[]
for i in l1:
    i=sorted(i)
    ans=median(i)
    f.append(ans)
print(f)
