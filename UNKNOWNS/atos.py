n=list(str(bin(int(input()))))


s=n[2:][::-1]

a=str(n.count('1'))
b=0
c=0

for i in range(len(s)):
    if s[i]=='1':
        b=str(i)
        break

for i in range(len(s)-1,0,-1):
    if s[i]=='1':
        c=str(i)
        break

print(str(a)+'#'+str(b)+'#'+str(c))