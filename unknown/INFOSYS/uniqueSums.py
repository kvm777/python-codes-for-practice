from itertools import combinations

def SumsOfSubarrays(arr):
    n = len(arr)
    out = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            s = sum(arr[i:j])
            if s not in out:
                out.append(s)
    return len(out)


    ...
n = int(input())
a = list(map(int, input().split()))
# a = []
# for i in range(n):
#     a.append(int(input()))

print(SumsOfSubarrays(a))