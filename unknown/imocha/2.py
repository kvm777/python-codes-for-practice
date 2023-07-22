s=input()

v='aeiouAEIOU'
c=1
for i in range(len(s)):
    for j in range(len(s)):
        x=s[i:j+1]
        for k in x:
            if k in v:
                break
        else:
            x1=len(x)
        if x1>c:
            c=x1

print(c)
        