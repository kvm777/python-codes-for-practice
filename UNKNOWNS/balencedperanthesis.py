s=input()
s=s[::-1]
f=1
for i in range(len(s)-1):
    if s[i]==s[i+1]=='(':
        f*=2
    elif s[i]=='(' and s[i+1]==')':
        f+=1

print(f)