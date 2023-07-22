
#symmetric word or not

n=input()

if n[:(len(n)//2)] == n[(len(n)//2):len(n)]:
    print('symmetric thing')
else:
    print('not') 