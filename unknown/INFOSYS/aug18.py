from itertools import *
def Problem(n,k,l):
    out = []
    for i in range(len(l),0,-1):
        p = combinations(l,i)
        for j in p:
            # print(list(j))
            arr = j
            idx = [j.index(t) for t in arr]
            print(idx)
            for i in range(len(arr)-1):
                if(arr[i] + k < arr[i+1]):
                    break
                # if(l[] > l[arr[i+1]]):
                #     break
            # else:
            #     return arr
    return 1


n = int(input())
k = int(input())  
l = list(map(int, input().split()))
print(Problem(n,k,l))
