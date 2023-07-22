
#sorted of 2D array as input.......

n1= int(input("no of rows"))
n2= int(input("no of columns"))
lst=[]
for i in range(1,n1):
    for j in range(n2+1):
        k=int(input())
        lst.append(k)
    print()
print(lst)
l1=sorted(lst)

print(l1)


