#program to get the no with max no of 1's in binaty format of two nos in the adjacent nos... 


def b(a):                       #function for no of 1's in binary format of a number
    a=int(a)
    x=list(str(bin(a)))[2:]
    c=x.count('1')
    return c

n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
f=[]
for i in range(len(l)-1):
    if b(l[i])>b(l[i+1]):
        f.append(l[i])
    elif b(l[i])<b(l[i+1]):
        f.append(l[i+1])
    else:
        f.append(l[i+1])

print(f)
