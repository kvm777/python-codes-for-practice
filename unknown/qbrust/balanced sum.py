def balancedSum(arr):
    #write your code here
    s=arr
    for i in range(len(s)-1):
        x=sum(s[:i])
        y=sum(s[i+1:])
        if x==y:
            return i



l=list(map(int,input().split()))
print(balancedSum(l))