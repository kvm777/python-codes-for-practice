n=int(input())
c=10
if n>100:
    n=99
    c+=3
for i in range(10,n+1):
    i=str(i)
    if i[0]>=i[1]:
        c+=1

print(c)
