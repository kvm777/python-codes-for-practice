def d(n):
    i=1
    k=[]
    while i<=n:
        if n%i==0:
            k.append(i)
        i+=1
    return k


l=list(set(map(int,input().split())))
n=int(input())

f=[]
for i in range(n-1):
    if d(l[i])==d(l[i+1])==[1]:
        if l[i]<l[i+1]:
            f.append(l[i])

print(f)
