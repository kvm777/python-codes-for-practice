s1=input().lower()
s2=input().lower()

s3=s1
c=0
for i in s1:
    if i not in s2:
        c+=1

for i in s2:
    if i not in s1:
        c+=1

print(c)

