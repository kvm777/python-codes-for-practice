import math

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==math.ceil(n/2) or i==math.ceil(n/2):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()