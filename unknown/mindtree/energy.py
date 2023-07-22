s=list(map(int,input().split()))
n=int(input())
l1=[]
for i in range(len(s)-n+1):
    l2=[]
    for j in range(i,i+3):
        l2.append(s[j])

    if min(l2)<0:
        l1.append(min(l2))
    else:
        l1.append(0)

print(l1)