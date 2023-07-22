def josephus(n,k=2):
    if (n == 1):
        return 1
    else:   
        return (josephus(n - 1, k) + k+2) % n+1


n = int(input())
print(josephus(n,2))

