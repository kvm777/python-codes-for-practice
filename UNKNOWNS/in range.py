r=list(map(int,input().split()))

s=0
for i in range(r[0],r[1]+1):
    if i%2==0:
        s+=i

print(s)