a=input()
flag=0
for i in a:
    if a.count(i)==1:
        print(i,end="")
        flag=1

if flag==0:
    print(-1)
