def stock(l,k):
    l=sorted(l)
    x=l[k-1]
    return x

l=list(map(int,input().split()))
k=int(input())

print(stock(l,k))



 