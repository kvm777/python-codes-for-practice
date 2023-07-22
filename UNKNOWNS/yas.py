def grtsum(n):
    n=str(n)
    x=int(n[0])+int(n[-1])
    y=0
    l=len(n)
    for i in range(1,l-1):
        y+=int(n[i])

    if x>y:
        return x
    else:
        return y

x=int(input())
print(grtsum(x))