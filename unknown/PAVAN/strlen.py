a=list(map(str,input().split()))
n=len(a)
result=0
for i in range(n):
    s1=a[i]
    l1=len(a[i])

    unmap={}
    for c in s1:
        if c in unmap:
            unmap+=1
        unmap=1
for j in range(i+1,n):
    s2=a[j]
    l2=len(a[j])
    flag=False

    for k in range(len(s2)):
        if s2[k] in unmap:
            flaf=True
            break
    if flag==False:
        result=max(result,l1*l2)

print(result)

