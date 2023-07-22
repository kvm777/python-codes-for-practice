n=input()
max=0
c=''
for i in n:
    if n.count(i)>max:
        c=i
print(c)