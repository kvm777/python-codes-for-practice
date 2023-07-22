k=int(input())
n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
c=0
s1=[]
for i in range(n):
    for j in range(n):
        s3=sorted([s[i],s[j]])
        if s[i]+s[j]==k and s3 not in s1:
            s1.append(s3)
            c+=1

print(c)
