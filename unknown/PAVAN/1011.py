
n=input()

d=int(n,2)
c=0
while d>0:
    if d%2==0:
        d=d//2
    else:
        d-=1
    c+=1

print(c)

