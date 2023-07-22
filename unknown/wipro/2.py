n=input()
l=0
for i in n:
    i=int(i)                            # sum of prime digits
    if i==1 or i==0:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l+=i
print(l)

