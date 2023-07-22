n=int(input())
m=n
c=0
if n==1:
    print(1)
else:
    for i in range(2,n+1):
        if n%i==0:
            n=n//i
            c+=1
        if n==1:
            break
    print(c+m)


