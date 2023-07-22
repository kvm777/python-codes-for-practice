
#swap of 1st and last element

n=int(input("no of elements"))
a=[]
for i in range(n):
    x=int(input("value : "))
    a.append(x)

a[0],a[-1]=a[-1],a[0]
print(a)