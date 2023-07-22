s=input()[::-1]
r=0
for i in range(len(s)):
    for j in range(1,len(s)):
        s1=s[i:j+1]
        l=len(s1)
        if l>=2 and s1==s1[::-1] and s1 in s:
            print(s1)
            r+=(l**2)
            s=s[j:]

print(r)