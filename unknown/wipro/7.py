l=list(map(str,input().split()))
n=int(input())
l1=[]
for i in l:
    if l.count(i)>=n:
        if i not in l1:
            l1.append(i)
    
for i in l1:
    print(i,end=' ')
