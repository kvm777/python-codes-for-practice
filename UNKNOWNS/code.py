s=input()
s1=''
for i in s:
    if i=='A':
        s1+='*'
    elif i=='z':
        s1+='@'
    if i.isupper()==True and i!='A':
        i=i.lower()
        s1+=chr(ord(i)-1)
    elif i.islower()==True and i!='z':
        i=i.upper()
        s1+=chr(ord(i)+1)
    elif i.isdigit()==True and i!='0':
        i=int(i)-1
        s1+=str(i)
    elif i==' ':
        s1+='^'
    elif i=='0':
        s1+='|'
    else:
        s1+='~'
print(s1)