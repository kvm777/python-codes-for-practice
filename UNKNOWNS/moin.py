n=int(input())
l=[]
for i in range(n):
    l.append(input())

l1=[]
x=ord(l[0][0])
for i in l[0]:
    l1.append(x-ord(l[0][i]))

print(l1)