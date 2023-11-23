def isPrime(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
        

# k = int(input())
# print(isPrime(k))

def nthOrdernumber(a,b):
    primes = []
    nxt = a+1
    while(len(primes)<b):
        if isPrime(nxt):
            primes.append(nxt)
        nxt+=1

    return primes



a,b = map(int,input().split())
print(nthOrdernumber(a,b))



"""
nxt b primes of given number (a)
input: 17 5
Output: [19, 23, 29, 31, 37]


"""