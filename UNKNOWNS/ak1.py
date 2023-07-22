n=int(input())
s=list(map(int,input().split()))
c=0
while len(s)>0:
    x=s[0]
    s.remove(x)
    
    for j in s:
        if j!=x:
            s.remove(j)
    c+=1
print(c)






