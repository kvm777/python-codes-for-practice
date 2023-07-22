from functools import reduce
import itertools


from itertools import *
n=int(input())
x=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n):
    c=combinations(l,i)
    l1=[]
    for i in c:
        print(list(i))
        
        if list(i) in l:
            
            if len(list(i))==1:
                if i[0]<x:
                    f+=1
            else:
                x1= reduce(lambda x,y:x^y ,list(i))
                if x1<x:
                    f+=1
                print(x1,list(i))
            #print(list(i),f)
print(f)

