n=int(input())
l=int(input())
r=int(input())

d=[[0 for i in range(r-l-1)]
    for i in range(n)]

f=0
for i in range(n):
    d[i][0]=1

for i in range(1,len(d[0])):
    d[0][i]=d[0][i-1]+1

f=d[0][r-l]

for i in range(1,n):
    for j in range(1,len(d[0])):
        d[i][j]=d[i-1][j]+d[i][j-1]

    f+=d[i][r-l]

print(f)