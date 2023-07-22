
#INPUT: 1 7 11 16 19
#OUTPUT: 19 1 16 7 11

l=list(map(int,input().split()))

l.sort(reverse=True)
print(l)
l1=[]
for i in range(len(l)//2):
    l1.append(l[i])
    l1.append(l[len(l)-1-i])

if len(l)!=0:
    l1.append(l[len(l)//2])

if len(l)==0:
    l1.pop()

print(l1)
