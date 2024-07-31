
'''
arrangement of list as 
negatives -- zeroes -- positives..
[9,-10,22,3,-23,0,5,6,-34]
[-10,-23,-34,0,9,22,3,5,6]
'''

# n=int(input())
l=list(map(int,input().split()))
n=[]
p=[]
z=[]
for i in l:
    if i<0:
        n.append(i)
    elif i>0:
        p.append(i)
    else:
        z.append(i)

f=n+z+p
print(*f)