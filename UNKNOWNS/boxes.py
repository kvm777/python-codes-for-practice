
s=list(map(int,input().split()))
s=sorted(s)
c=s[0]
s.remove(s[0])
l1=[]
while len(s)>0:
    s=sorted(s)
    c=c+s[0]
    s.remove(s[0])
    l1.append(c)


print(sum(l1))

