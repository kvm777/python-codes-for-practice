
#printing 0s in array at the end of list

l=list(map(int,input().split()))
b=[]
for i in l:
    if i!=0:
        b.append(i)
        l.remove(i)

c=b+l
print(c)
print(*c)
