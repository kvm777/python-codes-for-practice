s=input()

l=[]
for i in s:
    l.append(ord(i))

a=l.count(max(l))
c=chr(min(l))
print(l)
f=''
for i in range(a):
    f+=c

print(f)


