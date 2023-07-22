from math import *
s=int(input())
n=int(input())
m=int(input())

r=int(((pow(s,n))%1000000007))
r=int(pow(r,m))

print(r)


