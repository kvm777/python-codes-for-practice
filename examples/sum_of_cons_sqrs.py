l=list(map(int,input().split()))

res=0
l1=[]
for i in range(len(l)):
    if i%2!=0:
        l1.append(l[i])
        res+=((l1[0]+l1[1])**2)
        print(res)
        l1=[]
    else:
        l1.append(l[i])

   

