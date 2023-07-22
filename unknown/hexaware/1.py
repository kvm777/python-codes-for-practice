n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

x=min(l)
f=0
while len(l)>0:

    i = l.index(x)
    f+=x
    if (i+1)<len(l):
        l.remove(l[i+1])
    if (i-1)>=0 : 
        l.remove(l[i-1])
    l.remove(x)
    if len(l)>0:
        x=min(l)

print(f)
