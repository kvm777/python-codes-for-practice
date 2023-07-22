s1=input()
s2=input()
a=[]                             
for i in s1:
    if i in s2:
        pass
    else:
        a.append(i)
for i in s2:
    if i in s1:
        pass
    else:
        a.append(i)

b=0
c=0
for i in s1:
    if s1.count(i)!=s2.count(i) and i not in a:
        c=abs(s1.count(i)-s2.count(i))
        b+=c
print(c)
print(len(a)+c)