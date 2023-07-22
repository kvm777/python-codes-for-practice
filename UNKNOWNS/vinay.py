l=list(map(str,input().split()))

for i in l:
    for j in l:
        if any(i)==any(j):
            print(any(i),any(j))
            print(i,j,'yes')
else:
    print('false')

