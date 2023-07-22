        
        #write code here
        def count(s,n):
            k=0
            if n==0 or n==1:
                k=1

            t=0

            if '1'<=s[n-1]<='9':
                t=count(s,n-1)
                k=t
            
            if s[n-2]=='1' or s[n-2]=='2' and s[n-1]<='6':
                t+=count(s,n-2)

            return t

        s=input1
        n=len(s)
        return count(s,n)

