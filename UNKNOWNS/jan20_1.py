def maxmarks(input1,input2):

    #write code here
    n=input1
    a=input2
    if n==len(set(a)):
        return sum(a)
    else:
        f=sum(set(a))
        t=[]
        for i in a:
            if a.count(i)>1:
                t.append(i)
        s = set(t)
        f+=0
        x=max(t)+1
        for i in range(len(t)-len(s)):
            f+=x
            x+=1
        return f


n=int(input())
l=list(map(int,input().split()))
print(maxmarks(n,l))