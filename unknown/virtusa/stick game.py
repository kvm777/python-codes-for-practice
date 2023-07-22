from itertools import *


        #write code here
        l=input2
        f=0
        c=combinations(l,2)
        for i in c:
            x=list(i)
            if sum(x) in l:
                f+=1

        return f


#not fully excicuted
