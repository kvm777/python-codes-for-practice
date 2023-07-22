
#capitalise the repeated letters

s1,s2 = map(str,input().split())

s3=s1+""+s2
s4=[]
for i in s3:
    if (s3.count(i)>1):
        a= i.upper()
        s4.append(a)

    if (s3.count(i)==1):
        s4.append(i)

print(s4)
s5=''.join(s4)
print(s5)