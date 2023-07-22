        
        #read only region 
        s=input2

        s.sort()
        for i in range(len(s)-1):
            if s[i]+1!=s[i+1]:
                c=0
                break
        else:
            c=1

        return c

        