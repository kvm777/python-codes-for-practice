
# eular totient code...  refergooogle or something else...

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def eular(n):
    c = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            c += 1
    return c

n = int(input())

for i in range(n):
    a = int(input())
    print(eular(a))


