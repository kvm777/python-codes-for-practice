
def smallestNumber(x,y):
    num=0

    #write your code
    a=x
    b=y
    d = [a]
    for i in range(10):
        d.append(str(a)+str(i))
    for i in d:
        if int(i)%b==0:
            num = int(i)
            return num  



a,b = map(int,input().split())

print(smallestNumber(a,b))