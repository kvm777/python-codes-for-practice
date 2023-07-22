s=input()
n=int(input())
l=[]
for i in range(n):
    a,b = map(int,input().split())
    x=0
    y=0
    for i in range(a,b):
        if s[i]=='|':
            x=i
            break
    for j in range(b,a,-1):
        if s[j]=='|':
            y=j
            break
    l.append(abs(x-y))

print(l)

