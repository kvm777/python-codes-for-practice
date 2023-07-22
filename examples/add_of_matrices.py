#addition of two matrices

m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]

m2=[[9,8,7],
    [6,5,4],
    [3,2,1]]

r=[[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1)):
        r[i][j]=m2[i][j]+m1[i][j]
print(r)
