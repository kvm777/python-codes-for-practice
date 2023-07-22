n=int(input())

ch=80
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
    ch+=1
    print()

'''
6
P
QQ
RRR
SSSS
TTTTT
UUUUUU
'''