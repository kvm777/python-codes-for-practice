n=int(input())
s=list(map(int,input().split()))

r=0
w=0

for i in s:
    r+=i
    if i<0:
        i=-i
        w+=i
    else:
        w+=i

print(w)
print(r)
