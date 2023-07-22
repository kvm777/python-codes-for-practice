def solution(input1):
    #write cod here
    s=input1
    l=[]

    for i in range(len(s)):
        for j in range(1,len(s)+1):
            if i+j<=len(s):
                k=s[i:i+j]
                if k in s and k==k[::-1]:
                    l.append(k)
    c=''               
    x=0        
    print(l)
    for i in l:
        if len(i)>x:
            x=len(i)
            c=i

    print(c)

'''
for i in range(1,len(s)+1):
    p=combinations(s,i)
    for i in p:
        k=''.join(i)
        if i==i[::-1] and k in s:
            l.append(k)
'''
s=input()
solution(s)