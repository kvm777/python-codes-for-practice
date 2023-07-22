n1=int(input())
n2=list(map(int,input().split()))

for i in range(n1):
    for j in range(n1):
        if n2[i]!=n2[j]:
            print('Yes')
    break
else:
    print('No')
    

