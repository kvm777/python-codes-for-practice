
    #write code here
    s1=arr1
    s2=arr2
    c=0
    for i in range(len(s1)):
        for j in range(len(str(s1[i]))):
            a=int(s2[i][j])
            b=int(s1[i][j])
            x=abs(a-b)
            c+=x
            
    return c

    




