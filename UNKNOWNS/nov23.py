
#not excicuted....

def friendGroups(input1):
    n=input1
    c=1
    l=[[2,3]]
    for i in range(4,n+2):
        for j in range(len(l)):
            for k in l[j]:
                if i%k==0:
                    l[j].append(i)
        else:
            l.append([])
            l[len(l)].append(i)
            c+=1
    return c
        

n=int(input())
print(friendGroups(n))