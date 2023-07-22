
#decrease of odd nos and increase of even nos...
'''
input: 8
       23 54 13 8 67 5 1 55
       
output: 67 55 23 13 5 1 8 54
'''

n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
l2=sorted(l2)[::-1]
l1=sorted(l1)
print(*l2,*l1)
