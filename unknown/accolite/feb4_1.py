def sol(a):
    if len(a)<=1:
        return 0
    else:
        c=0
        x=0
        for i in a:
            if a.count(i)>c:
                c=a.count(i)
                x=i
        


l=list(map(int,input().split()))
print(sol(l))