n=int(input())
m=int(input())

primes=[]
for i in range(n,m):
    if i==0 or i==1:
        continue
    if i==2:
        primes.append(2)
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            primes.append(i)

s=sum(primes)
out=[]
for i in range(1,s+1):
    if s%i==0:
        out.append(i)

print(*out)