        
        
        #write code here
        n=N
        a=A
        
        if len(a)%2!=0:
            a.remove(a[0])
            b1=a[:len(a)//2]
            b2=a[len(a)//2:]
        else:
            b1=a[:len(a)//2]
            b2=a[len(a)//2:]
            b1.remove(min(b1))
            b2.remove(max(b2))

        return (sum(b1)-sum(b2))








