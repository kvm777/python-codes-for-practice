#read only region 
s=list(map(str,input().split()))

c=0
for i in s:
    k=len(i)
    if k>2 and i==i[::-1]:
        c+=1
    elif k%2==0 and k>2:
        s1=i[:k//2]
        s2=i[k//2:]
        if s1==s1[::-1] or s2==s2[::-1]:
            c+=1
    elif k%2!=0 and k>2:
        s1=i[:k//2]
        s2=i[k//2+1:]
        if s1==s1[::-1] or s2==s2[::-1]:
            c+=1

            
print(c)


