n=int(input())

for j in range(n):
    s=input()
    u=[]
    l=[]
    k=[]
    for i in s:
        if i.isupper()==True:
            u.append(i)
        elif i.islower()==True:
            l.append(i)
        else:
            k.append(i)
    f=l+u+k
    if len(f)>0:
        print(''.join(f))
    else:
        print('NULL')