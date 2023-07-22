def sol(rows,alphabet):
    x=alphabet
    t=0
    for i in rows:
        for j in range(len(i)):
            if i[j]==x:
                t=j
    x=''
    y=''
    for i in range(t):
        for j in range(t):
            if i==t and j<t:
                y+=rows[i][j]
            elif i<t and j==t:
                x+=rows[i][j]

    return x , y

rows=list(map(str,input().split()))
print(sol(rows,'m'))