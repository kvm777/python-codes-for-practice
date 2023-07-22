from itertools import *

s=input()

c=permutations(s)
l=[]
for i in c:
    l.append(''.join(i))

for i in l:
    if int(i)>int(s):
        print(i)
        break
else:
    print('Not Possible')