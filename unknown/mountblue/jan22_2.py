def solution(numOfElements,arr,n):
    size=numOfElements
    lst=[]
    for i in range(0,n):
        t=[]
        for j in range(i,size,n):
            t.append(arr[j])
        lst.append(t)

    s=0
    f=0
    l=[]
    for i in lst:
        if sum(i)>s:
            s=sum(i)
            f=lst.index(i)
            l.append(f)
    return min(l)+1

n=int(input())
l=list(map(int,input().split()))
k=int(input())
print(solution(n,l,k))