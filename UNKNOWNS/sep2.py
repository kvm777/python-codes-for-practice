#leetCode Referance...

def maxProfit(arr):
    minpri =arr[0]
    maxpro = 0

    for i in arr[1:]:
        maxpro = max(maxpro, i-minpri)
        minpri = min(minpri, i)
    return maxpro


n= int(input())
l = list(map(int,input().split()))
print(maxProfit(l))