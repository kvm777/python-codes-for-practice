
#binary search---------sorting is manditory

def binarysearch(arr,k):
    l=arr
    start=0
    end=len(l)-1
    while start<=end:
        mid=(start+end)//2

        if l[mid]>k:
            end=mid-1
        elif l[mid]<k:
            start=mid+1
        else:
            return mid
    return -1

l=[2,3,5,6,7,12,14]
k=12
val=binarysearch(l,k)
print(val)
