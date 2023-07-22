s=input()
n=len(s)
s1=''
l=[]
for i in range(n):                       #max ele in sub arr str
    l.append(s[i])
    if i%2!=0:
        s1+=max(l)
        l=[]

l1=''.join(l)
j=''.join(s1)
print(j+l1)

