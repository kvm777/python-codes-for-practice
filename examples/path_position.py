n=int(input())
l=r=0

for i in range(1,n+1):
    if i%4==1:
        l+=i*10
    elif i%4==2:
        r+=i*10
    elif i%4==3:
        l-=i*10
    elif i%4==0:
        r-=i*10    
    print(l,r)
print(l,r)

