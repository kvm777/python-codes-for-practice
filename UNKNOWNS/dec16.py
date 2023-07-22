def removingOccurances(input1,input2):
    #write code here...
    s=input1
    x=input2
    s1=''
    for i in s:
        if i!=x:
            s1+=i

    return s1

s=input()
x=input()
print(removingOccurances(s,x))
