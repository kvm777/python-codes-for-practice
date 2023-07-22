from itertools import *
n,m = map(int,input().split())
l=[]
for i in range(n):
    l.append(input())

l1=[]
p=permutations(l)
for i in p:
    l1.append(''.join(list(i)))
max=0
for i in l1:
    t=0
    if i[0]=='0':
        i=i[1:]
    for j in range(1,len(i)):
        if i[j]=='0':
            t1=i[:j+1]
            t+=t1.count('1')
    if max<t:
        max=t

print(max)


'''
2 4
1011
0111
output: 4

2nd testcase:
3 3
101
110
010
output: 14
'''