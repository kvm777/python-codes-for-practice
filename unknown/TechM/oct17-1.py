def getOutput(n,k):
    s =str(n)
    s1 = s[k:] + s[:k]

    return int(s1)





n = int(input())
k = int(input())

print(getOutput(n,k))

