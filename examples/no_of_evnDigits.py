a=input()
a1=list(a)
b=['0','2','4','6','8']

c=0
for i in a1:
    if i in b:
        c+=1

print(c)
