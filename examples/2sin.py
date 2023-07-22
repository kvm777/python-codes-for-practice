
#output with the nos of powers of 2 ....
'''
input:
5
1 2 7 8 16
output:
4
[1, 2, 8, 16]
'''

n=int(input())
l=list(map(int,input().split()))
c=0
d=[]
for i in l:
    if i==1:
        c+=1
        d.append(i)
    
    else:
        b=str(bin(i))
        if b.count('1')==1:
            c+=1
            d.append(i)
            
'''
    elif i%(2**any(range(2,100)))==0:
        c+=1
        d.append(i)
'''
print(c)
print(d)
        

