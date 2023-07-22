
#print of permutations of word

from itertools import *

n=input()

l=permutations(n)
l=sorted(l)
lst = []
for i in list(l):
    lst.append(''.join(i))

print(lst)