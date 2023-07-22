l=list(map(str,input().split()))

n1=l[0]
n2=l[1]

n3=[]

for i in range(len(n1)):
    if n1[i]==n2[i]=='1' :
        n3.append(str(1))
    else:
        n3.append(str(0))

r=''.join(n3)
print(r)
    