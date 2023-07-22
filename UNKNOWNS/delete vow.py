s=input()
l=[]
v='aeiouAEIOU'
for i in s:
    if i not in v:
        l.append(i)

print(''.join(l))
