n=int(input())

ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch+=1
    print()

'''
5
A
BC
DEF
GHIJ
KLMNO
'''