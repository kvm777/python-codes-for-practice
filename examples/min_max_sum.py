l=list(map(int,input().split()))

#a,b = min(l),max(l)

'''
n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
'''
#l1=sorted(l)
a=0
for i in l:
    a+=i

print(l)

print(a-min(l))
print(a-max(l))