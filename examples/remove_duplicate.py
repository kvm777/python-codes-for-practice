n=int(input("no of elements"))
a=[]
for i in range(n):
    x=int(input("value:"))
    a.append(x)

c=set(a)
d=list(c)
print(d)