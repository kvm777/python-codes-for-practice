a=int(input())
b=int(input())
primes=[]
for i in range(a,b):
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

print(primes)
        
