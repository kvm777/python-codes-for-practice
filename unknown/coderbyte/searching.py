l=list(map(str,input().split()))
t='ow63dpucgf5'
f=''
x=0
for i in l:
    for j in i:
        if i.count(j)>x:
            f=i
            x=i.count(j)
s=len(set(f))
if len(f)==s:
    print(-1)
else:
    f=list(f)
    for i in f:
        if i in t:
            f.remove(i)
            break
    print(''.join(f))


