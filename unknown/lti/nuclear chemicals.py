x=int(input())
k=int(input())
n=int(input())

c=0
l=[x]
f=5
for i in range(1,n):
    f+=k
    l.append(f)

print(sum(l))