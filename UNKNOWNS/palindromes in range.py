s=int(input())
e=int(input())
f=[]
for i in range(s,e+1):
    if str(i)==str(i)[::-1]:
        f.append(str(i))

print(f)