n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

s=set(l)
f=[]
x=[]
c=0
if len(s)==len(l):
    print('NA')
else:
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j and l[i]==l[j]:
                l1=sorted([l[i],l[j]])
                if l1 not in x:
                    x.append(abs(i-j))
                    c+=1

    print(len(x)//2,max(x))
