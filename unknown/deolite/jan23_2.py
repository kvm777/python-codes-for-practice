s=input()

out=''
x=0
for j in range(len(s)):
    c=0
    t=s[x]
    for i in range(x,len(s)):
        if s[x]!=s[i]:
            x=i
            break
        c+=1
    out+=t+'c'
    print(out)

print(out)
    
