n=int(input())
l=[]
for i in range(n):
    l.append(input())

w=input() 


def solve(N,keyboard,word):
    l=keyboard
    w=word
    x=''
    out=''
    for i in l:
        l1 = list(i)
        for j in w: 
            if j not in l1:
                break
        else:
            x=i

    if x in l:
        return 1
    else:
        return 0
