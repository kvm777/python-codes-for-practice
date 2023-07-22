t=list(map(int,input().split()))
c=0
for i in t:
    if i<0:
        c+=1

print(c)