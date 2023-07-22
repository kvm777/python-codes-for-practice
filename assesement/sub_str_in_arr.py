
#INPUT: mahesh 3
#OUTPUT: mah ahe hes esh


s,n=map(str,input().split())
n=int(n)
l=[]
for i in range(0,len(s)-n+1):
    x=s[i:i+3]
    l.append(x)

print(l)

'''
n=int(n)
l=[]
l1=[]
for i in range(len(s)-n+1):
    for j in range(i,i+n):
        l.append(s[j])
    
    l1.append(''.join(l))
    l=[]

print(*l1)
'''