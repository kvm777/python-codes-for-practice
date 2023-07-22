        
    #write code here
    s1=list(input1)
    s2=list(input2)
    c=0
    s='aeiouAEIOU'
    for i in s1:
        if i in s:
            if i in s1 and i in s2:
                s1.remove(i)
                s2.remove(i)
                c+=1

    return str(c)


    



