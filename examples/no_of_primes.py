n=int(input())
l=list(map(int,input().split()))

c=0
for i in l:
    if i==0 or i==1:
        continue
    if i==2:
        c+=1
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            c+=1 
        
            

print(c)
