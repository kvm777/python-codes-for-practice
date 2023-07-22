
#alpha order

s1= 'mahesh'
s2= 'rajesh'

s3=s1+s2
print(s3)               #maheshrajesh
print(*sorted(s3))      #a a e e h h h j m r s s  
l2=list(s3)
l2.sort()
l=[]
for i in l2:
    print(i,end='')     #aaeehhhjmrss
print()
print(l2)               #['a', 'a', 'e', 'e', 'h', 'h', 'h', 'j', 'm', 'r', 's', 's']
'''
l=[]
for i in s3:
    l.append(i)

l1=sorted(l)
for i in l1:
    print(i,end="")
'''

print(*l2)              #a a e e h h h j m r s s