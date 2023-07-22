n4=int(input())
n1=str(input())
n2=str(input())
n3=str(input())

l=[n1,n2,n3]
e=0
o=0

for i in l:    
    for j in range(len(i)):
        if j%2==0:
            e+=int(i[j])
        else:
            o+=int(i[j])

if n4%2==0:
    print(e-o)
else:
    print(o-e)
    

