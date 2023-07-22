l=list(map(int,input().split()))
n=l[0]
l=sorted(list(l[1:]))
e=[]
od=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        od.append(i)
        
od=od[::-1]
f=[]
while len(od)!=0 or len(e)!=0:
    if len(od)>0:
        f.append(od[-1])
        od.pop()
    if len(e)>0:
        f.append(e[-1])
        e.pop()
print(*f)
