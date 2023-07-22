
#sum of primes in the list.....

l=list(map(int,input().split()))

p=[]
for i in l:
    if i==0 or i==1:
            pass
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            p.append(i)
            
print(sum(p))