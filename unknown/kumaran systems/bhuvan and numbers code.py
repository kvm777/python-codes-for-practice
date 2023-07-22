x,y=map(str,input().split())
x1=''
y1=''
x2=''
y2=''
l=[]
for i in x:
    if i!='5':
        x1+=i
    else:
        x1+='6'
l.append(int(x1))
for i in x:
    if i!='6':
        x2+=i
    else:
        x2+='5'
l.append(int(x2))
for i in y:
    if i!='5':
        y1+=i
    else:
        y1+='6'
l.append(int(y1))

for i in y:
    if i!='6':
        y2+=i
    else:
        y2+='5'
l.append(int(y2))

print(min(l[0],l[1])+min(l[2],l[3]),max(l[0],l[1])+max(l[2],l[3]))
