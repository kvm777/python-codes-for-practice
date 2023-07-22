def none(n):
    #write your code....
    l=[]
    e,o=0,0
    for i in range(n+1):
        if i%2==0:
            e=e+i
        else:
            o+=i
    l=[e,o]
    print(l)
    print(e,o)


a=int(input())
none(a)