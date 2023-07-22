n=int(input())

#s=list(map(int,input().split()))
s=[]
for i in range(n):
    k=int(input())
    s.append(k)


c=1
k=s[0]
for i in range(1,len(s)):
    if s[i]>k:
        k=s[i]
        if s[i]>s[i-1]:
            c+=1

print(c)
