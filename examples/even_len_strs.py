
#find the even length strings in given input

n=list(map(str,input().split()))

for i in n:
    if len(i)%2==0:
        print(i)