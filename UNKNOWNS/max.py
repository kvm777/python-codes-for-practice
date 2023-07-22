n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

c=2
for i in range(1,len(l)-1):
    x=l[i]
    for i in l[:i]:
        if i<x:
            break
    for i in l[i:]:
        if x<i:
            break
    else:
        c+=1

    #if (any(l[:i])<l[i])==True and (any(l[i:])>l[i])==True:


print(c)