c=tuple(map(int,input().split()))
d=list(c)
for e in d:
    if e%d[0]!=0:
       print("no")
    else:
        print("yes")


