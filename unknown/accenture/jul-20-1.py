def SubArray(arr, k):
    #write your code here
    s=sum(arr[:k])
    out=arr[:k]
    for i in range(len(arr)-k):
        x=sum(arr[i:i+k])
        if(x<s):
            s=x
            out = arr[i:i+k]
    for i in out:
        print(str(i),end=" ")

  
l = list(map(int,input().split()))
k = int(input())

SubArray(l,k)