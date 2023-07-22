
n=int(input())
l=list(map(int,input().split()))


def lastmodified(input1,input2):
    #write code here
    c=input1
    l=input2[::-1]
    for i in l:
        if i!=9:
            return c
        else:
            c-=1
    else:
        return c


print(lastmodified(n,l))

'''
input1:6
input2:9 8 7 8 9 9

output:4
'''
