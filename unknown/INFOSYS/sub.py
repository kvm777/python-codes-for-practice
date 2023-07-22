def solve(N,A,M,S):

    #write code here
    b=A*M
    s=S
    l1=[]
    for i in range(len(b)):
        for j in range(i+1,len(b)+1):
            x=b[i:j]
            if sum(x)<=s:
                l1.append(x)

    return len(l1)

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=int(input())
s=int(input())

print(solve(n,l,m,s))