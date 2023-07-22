
#linear aearch

def linearsearch(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    else:
        return -1


list=[3,5,32,5,23,7,4,4,44,77,45,54]
k=23
val=linearsearch(list,k)
print(val)