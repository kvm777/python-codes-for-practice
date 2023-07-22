def print_subset(arr, K) :
    x = pow(2, len(arr))
    for i in rang

# Driver code
arr = [ ]
n = int(input(“Enter length of array : “))
s=int(input(“Enter sum : “))
for i in range(n):
    ele=int(input(“Enter element : “))
    arr.append(ele)
print_subset(arr, s)