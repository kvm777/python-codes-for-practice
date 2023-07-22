s=str(input())
s=s[::-1]
f=0
for i in range(len(s)):
    for j in range(len(s[i:])):
        f+=int(s[j])
print(f)

