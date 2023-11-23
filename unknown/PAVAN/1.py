
def func(input1):
    n=input1

    l=[0 for i in range(0,n+1)]
    l[0]=l[1]=l[2]=1
    l[3]=2

    for i in range(5,n+1):
        l[i]=l[i-1]+l[i-2]+l[i-5]+l[i-10]

    return l[n]

n = int(input())
print(func(n))




