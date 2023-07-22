
    #write code here
    n1=input1
    s=input2
    n3=input3
    l=[]
    v=[]
    if n3==1:
        return max(s)
    else:
        for i in range(len(s)):
            for j in range(len(s)):
                x=abs(s[i]-s[j])
                if s[i]!=s[j]:
                    v.append(x)
                    l.append((s[i],s[j]))

        m=min(v)
        z=v.index(m)
    
        l[z]=sorted(l[z])
        return l[z]



