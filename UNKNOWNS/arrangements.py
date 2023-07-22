n=int(input())
s=list(map(int,input().split()))

p=[]
n=[]
for i in s:
    if i%2!=0:
        n.append(i)
    else:
        p.append(i)
p=sorted(p)
n=sorted(n)


f=[]
for i in range(1,len(s)+1):
    if i%2!=0:
        f.append(n[0])
        n.remove(n[0])
    else:
        f.append(p[0])
        p.remove(p[0])

print(*f)