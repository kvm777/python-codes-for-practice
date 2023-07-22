
#2nd largest element in the list.....

n=int(input("no of elements"))
a=[]
for i in range(n):
    x=int(input("value"))
    a.append(x)

c=sorted(a)
print(c[-2])