n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==i or j==2*n-i:
            print(i,end=' ')
        else:
            print(" ",end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(1,2*n):
        if j==i or j==2*n-i:
            print(i,end=' ')
        else:
            print(" ",end=' ')
    print()

'''
5
1               1 
  2           2
    3       3
      4   4
        5
      4   4
    3       3
  2           2
1               1
'''