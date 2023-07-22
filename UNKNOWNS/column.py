k=int(input())
l=list(map(int,input().split()))
n=int(input())
l1=[]
for j in range((len(l)//n)+1):
    x=0
    for i in range(j,len(l),n):
        x+=l[i]
    l1.append(x)
c=0
for i in l1:
    if l1.count(i)>1:
        return l1.index(min(l1))+1
        break
else:
    return l1.index(max(l1))+1
    