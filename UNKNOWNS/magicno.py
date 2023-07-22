n=input()
l=list(map(str,input().split()))
s=int(input())
p=int(input())
l1=[]
for i in l:
    if len(i)==s:
        l1.append(int(i))

l1.sort()
print(l1[p-1])

