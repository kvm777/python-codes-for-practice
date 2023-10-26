def Problem(n):
    if n<=3:
        return 1
    i=1
    c=0
    while((i*i)<=n):
        i+=1
        c+=1
    return c

n=int(input())
print(Problem(n))