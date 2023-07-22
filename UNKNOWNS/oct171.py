n=int(input())
l=[]

for i in range(n):
    x=list(map(int,input().split()))
    l.append(x)

print(l)
l1=[]
for i in range(n):
    for j in range(n):
        x=l[i][j]
        l1[j][i]=x
print(l1)
'''
for i in range(n):
    x=l[i].count(1)
    y=l[i].count(0)
    for j in range(n):
        k=l[i][j]
        if j==i and l[i][j]==1:
            x+=1
        elif j==i and l[i][j]==0:
            y+=1
'''