t=int(input())

for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s=sorted(s)
    v=0
    for j in range(len(s)):
        k=0
        for i in range(len(s)):
            if s[i]>=s[j]:
                k+=s[j]
        if v<k:
            v=k
    print(v)

