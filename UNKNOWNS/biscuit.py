n=int(input())
k=int(input())
l=list(range(1,n+1))



for i in range(n):
    print(l)
    l.remove(l[k-1])
    l.insert(k-1,0)
    l=l[k:]+l[:k]

for i in l:
    if i==0:
        l.remove(i)

print(l)
