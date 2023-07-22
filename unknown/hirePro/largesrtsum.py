n=int(input())
f=0
f1=0
for i in range(n+1,0,-1):
    x=str(i)
    t=0
    for j in x:
        t+=int(j)
    if t>f:
        f=t
        f1=i

print(f)
print(f1)