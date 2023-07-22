
'''
arrangement of list as 
negatives -- zeroes -- positives..
'''

n=int(input())
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