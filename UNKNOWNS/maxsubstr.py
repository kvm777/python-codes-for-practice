l=list(map(str,input().split()))

s=l[0]
for i in l:
    if l.count(i)>l.count(s):
        s=i

print(s)