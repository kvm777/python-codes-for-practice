n=int(input())

s=list(map(int,input().split()))
c=0
s1=[]
for i in s:
    if s.count(i)>1:
        if i not in s1:
            s1.append(i)
        
print(sorted(s1))

