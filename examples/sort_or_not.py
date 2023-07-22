n=int(input())
l=list(map(int,input().split()))

l1=sorted(l)

if l1==l:
    print("true")
else:
    print("false")