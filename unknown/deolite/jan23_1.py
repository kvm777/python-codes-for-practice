a,b,c = map(int,input().split())

f=[]
l=sorted([a,b,c])
for i in range(l[0]):
    for j in range(l[1]):
        for k in range(l[2]):
            x=[i+1,j+1,k+1]
            if x not in f and len(x)==len(set(x)):
                f.append(x)

print(len(f))



