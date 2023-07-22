from re import I


n=int(input())
l=list(map(int,input().split()))
k=int(input())

s=[]
c=0
s1=[]
for i in l:
    s.append(i)
    if sum(s)>10:
        c+=1
        s1.append(i)
        s=[]






