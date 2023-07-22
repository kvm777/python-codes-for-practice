s='abcdefghijklmnopqrstuvwxyz'

n=int(input())

for i in range(n):
    for j in range(i+1):
        print(s[j],end='')
    print()
