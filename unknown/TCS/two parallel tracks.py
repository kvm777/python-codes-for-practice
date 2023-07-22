n=int(input())
m=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l3=list(set(l3))
l3=sorted(l3)
s=len(l3)
if s%2==0:
    k=(l3[s//2-1]+l3[s//2])/2
else: 
    k=l3[s//2]

print('{0:.2f}'.format(k))

