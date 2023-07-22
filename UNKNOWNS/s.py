x=int(input())
n=int(input())
c=0
for i in range(1,n+1):
    if i%2==0:
        c-=(x**((2*i)-1))
    else:
        c+=(x**((2*i)-1))

print(c)



