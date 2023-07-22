
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)-k+1):
    if sum(l[i:i+k])%2==0:
        c+=1

if c==0:
    print(-1)
else:
    print(-1)


