def printmagicNumbers(N,A,B):
    #write your code
    n=N
    a=A
    b=B
    l=[a,b]
    for i in range(n-2):
        a+=b
        b=l[-1]
        l.append(a)
    ev = []
    od = []
    for i in l:
        if i%2==0:
            ev.append(i)
        else:
            od.append(i)

    print(*ev)
    print(*od)

a,b = map(int,input().split())
n=int(input())

printmagicNumbers(n,a,b)
