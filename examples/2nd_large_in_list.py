
#2nd largest element in the list.....
# input : [6,4,9,11,55,80,22,45,23]
# output: 55

n=int(input("no of elements"))
a=[]
for i in range(n):
    x=int(input("value"))
    a.append(x)

c=sorted(a)
print(c[-2])