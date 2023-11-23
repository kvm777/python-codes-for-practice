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


"""
explination: 1+5 =6, 2+3+4=9 --->> 9>6
input: 12345
Output: 9
"""