n=int(input())
l=[]
for i in range(n):
    l.append(input())
s=set(l)
print(len(s))
d={}
for i in l:
    d[i]=l.count(i)

f=[]
for i in d.keys():
    f.append([d[i],i])

f=sorted(f)[::-1]
print(f)
f1=[]
f2=[]
for i in f:
    f1.append(f[0])
    f2.append(f[1])
for i in range(len(f2)):
    if f1.count(f1[i])==1:
        print(f2[i])
    else:
        
for i in f:
    print(i[1])


