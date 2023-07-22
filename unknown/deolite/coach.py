n=int(input())
c=list(map(int,input().split()))
s=list(map(int,input().split()))
t=['G','S','D','B','A']

f1=[]
k=0
for i in range(len(s)):
    for j in range(1,c[i]+1):
        z=(s[i]/j)+(ord(t[i])*(i+1))
        k+=int(z)
    f1.append(k)
    k=0

print(max(f1),sum(f1))

