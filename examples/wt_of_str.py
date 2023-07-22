
#weight of string

s1='yagami'
s2='light'
l1=l2=0
for i in s1:
    l1+=(ord(i)%96)
for j in s2:
    l2+=(ord(j)%96)
    
if l1>l2:
    print(1)
elif l1<l2:
    print(2)
else:
    print("equal")