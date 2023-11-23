n=int(input())
m=int(input())
k=int(input())
c=0
for i in range(n+1,m+1):
    if i%k==0:
        c+=1

print(c)

"""
exploination: 4, 8 are the 2 multiples of 4

input:  3
        10
        4
output: 2
"""
