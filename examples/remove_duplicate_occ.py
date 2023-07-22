
#remove duplicate words from string

n=list(input().split())
'''
l=[]
for i in n:
    if i not in l:
        l.append(i)

print(' '.join(l))
'''
n=set(n)
print(*list(n))