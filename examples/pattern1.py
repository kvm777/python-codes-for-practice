n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n-i+1:
            print(j,end=" ")
        else:
            print("*",end=" ")
    print()

'''
1 * * * 5 
* 2 * 4 *
* * 3 * *
* 2 * 4 *
1 * * * 5
'''

    