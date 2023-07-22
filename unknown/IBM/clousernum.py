def clousersum(inputNum):
    #write your code here
    n=str(inputNum)
    l=len(n)
    x=0
    if l%2==0:
        for i in range(l//2):
            k=int(n[i]+n[l-1-i])
            x+=k
    else:
        for i in range(l//2):
            k=int(n[i]+n[l-1-i])
            x+=k
        x+=int(n[l//2])
    
    return x



n=int(input())
print(clousersum(n))



