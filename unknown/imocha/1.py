s=input()
s1=s[::-1]
a1=[]
b1=[]
for i in range(len(s)):
    if s[i]=='a':
        a1.append(i)
    
for i in range(len(s)):
    if s[i]=='b':
        b1.append(i)

a1=sorted(a1)
b1=sorted(b1)
m1=a1[0]
m2=a1[-1]
for i in range(len(a1)-1):
    x=abs(a1[i]-a1[i+1])
    if x>m1:
        m1=x
    if x<m2:
        m2=x

m3=0
m4=len(s)
for i in range(len(b1)-1):
    x=abs(b1[i]-b1[i+1])
    if x>m3:
        m3=x
    if x<m4:
        m4=x

print(m1,m2,m3,m4)
print(a1,b1)