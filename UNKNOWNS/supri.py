a=int(input())
c=0
n=a
while n>0:
    k=1
    l=1
    m=1
    if n%2==0:
        n=n//(2**k)
        c+=1
        k+=1
    elif n%3==0:
        n=n//(3**l)
        c+=1
        l+=1
    elif n%5==0:
        n=n//(5**m)
        c+=1
        m+=1
print(a+c)