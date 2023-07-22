

x=int(input())
l=list(map(int,input().split()))         #kth shortest ele
p=int(input())

l1=sorted(l)
print(l1[p-1])


