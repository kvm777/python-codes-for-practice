n=int(input())

s=list(map(int,input().split()))

for i in s:
    i=str(i)
    if i==i[::-1]:
        print('wins')
    else:
        print('looses')



         