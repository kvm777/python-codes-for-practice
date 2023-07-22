
    #read only region 
    s=input1
    c=0

    for i in s:
        if s.count(i)>c:
            v=i
            c=s.count(i)

    return v


