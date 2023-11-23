
def function(input1,input2):
    #write code here
    l=input1
    n=input2
    c=0
    for i in l:
        s=len(i)
        k=i[-n:]+i[:s-n]
        if k==i:
            c+=1

    return c


