s=input()

n=list('0123456789')
f=0
for i in range(len(s)):
    if s[i] in n:
        s1=''
        for j in range(i,len(s)):
            if s[j] not in n:
                break
            else:
                s1+=s[j]

        if f<int(s1):
            f=int(s1)

print(f)
            