def changecase(inputStr,choice):
    #wrire your code...
    s=inputStr
    n=choice
    s1=''
    if n==1:
        s=list(s)
        for i in range(len(s)):
            if s[i]==' ':
                s[i+1]=s[i+1].upper()
            if s[i]!=' ':
                s1+=s[i]
    
    if n==2:
        for i in range(len(s)):
            if s[i]==' ':
                s1+='-'
            else:
                s1+=s[i]

    if n==3:
        for i in range(len(s)):
            if s[i]==' ':
                s1+='_'
            else:
                s1+=s[i]
    
    if n==4:
        s=list(s)
        s1+=s[0].upper()
        for i in range(1,len(s)):
            if s[i]==' ':
                s[i+1]=s[i+1].upper()
            if s[i]!=' ':
                s1+=s[i]

    return s1

s=input()
n=int(input())
print(changecase(s,n))