
#printing 0s in array at the end of list

# input: [0,4,5,7,0,1,0,3,8]
# output: [4,5,7,1,3,8,0,0,0]

l=list(map(int,input().split()))
b=[]
for i in l:
    if i!=0:
        b.append(i)
        l.remove(i)

c=b+l
print(c)
print(*c)
