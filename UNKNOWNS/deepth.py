s1=int(input())
s2=int(input())
s1=bin(s1)[2:][::-1]
s2=bin(s2)[2:][::-1]
for i in range(5):
    s1+='0'
    s2+='0'
c=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        c+=1
print(c)
