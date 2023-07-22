n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
z=0
for i in l:
    f=[]
    c=1
    while c<=i:
        if i%c==0:
            f.append(c)
        c+=1
    d=0
    e=0
    for k in f:
        if k%2==0:
            e+=1
        else:
            d+=1

    if e==d:
        z+=1

print(z)

