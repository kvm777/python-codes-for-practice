n=int(input())
a=list(map(int,input().split()))
m=int(input())

a=sorted(a)
out=max(a)
for i in range(0,len(a)-m+1):
    x=a[i:i+3]
    d=abs(x[0]-x[-1])
    if d<out:
        out=d

print(out)


