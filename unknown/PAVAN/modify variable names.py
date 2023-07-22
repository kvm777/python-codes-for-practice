
s=input()
c=''
j=''
for i in s:
    if  i=='_':
        c=s
        break
else:
    j=s

f=''
if len(c)>0:
    c=list(map(str,c.split('_')))
    f=c[0]
    for i in range(1,len(c)):
        k=c[i][0].upper()
        f+=k+c[i][1:]

else:
    f=j[0]
    for i in range(1,len(j)):
        if j[i].isupper()==True:
            f+='_'
            f+=j[i].lower()
        else:
            f+=j[i]
        
print(f)



