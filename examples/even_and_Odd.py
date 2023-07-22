n=int(input())
if n%2==0:
    print('evens : ',end=' ')
    for i in range(n,-1,-2):
        print(i,end=' ')
    print()
    print("odds : ",end=' ')
    for i in range(n-1,-1,-2):
        print(i,end=' ')
else:
    print("odds : ",end=' ')
    for i in range(n,-1,-2):
        print(i,end=' ')
    
    print()
    print('evens : ',end=' ')
    for i in range(n-1,-1,-2):
        print(i,end=' ')

