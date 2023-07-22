

#INSERTION SORT

def insertionsort(arr):

    for i in range(1,len(arr)):
        key=arr[i]

        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    print(arr)

arr=[5,4,57,42,765,33,44,64,75,3,76]
insertionsort(arr)
