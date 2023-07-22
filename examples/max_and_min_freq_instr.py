#max and min frequent letters in word

n=input()

d={}
for i in n:
    #d[i] = n.count(i)

    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(max(d,key=d.get))
print(min(d,key=d.get))

