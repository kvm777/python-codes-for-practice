from itertools import combinations
n,k=map(int,input().split())

l=list(map(int,input().split()))

c=combinations(l,4)
f=0

for i in c:
    if sum(list(i))==k:
        f=1
print(f)