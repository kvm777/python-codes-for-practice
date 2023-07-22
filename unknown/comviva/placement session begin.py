n=int(input())
l=list(map(int,input().split()))

def placement(input1,input2):
    #write code here
    n=input1
    l=input2
    l1=[0]
    for i in range(1,len(l)):
        c=0
        for j in l[:i]:
            if j>l[i]:
                c+=1

        l1.append(c)
    return l1








print(*(placement(n,l)))