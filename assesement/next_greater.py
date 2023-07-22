
#INPUT: 2 7 5 6 1  ---------Space separated integers denoting the next greater element of array element
#OUTPUT: 7 -1 6 -1 -1
        #7 is next greater of 2 ... hence print 7

l=list(map(int,input().split()))

l1=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            l1.append(l[j])
            break
    
    else:
        l1.append(-1)

print(l1)