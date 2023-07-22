#distint elements code

from itertools import *
s=input()
l=[]

for i in range(1,len(s)+1):
    c=combinations(s,i)
    for i in c:
        l.append(''.join(list(i)))

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)
print(len(l1))

