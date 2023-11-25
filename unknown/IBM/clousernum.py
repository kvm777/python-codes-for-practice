def clousersum(inputNum):
    #write your code here
    # convert the integer to string
    n=str(inputNum) #"12345"
    l=len(n)        # 5
    x=0
    # if l%2==0:
        # for i in range(l//2): 
        #     k=int(n[i]+n[l-1-i]) # 4-1  = 3
        #     x+=k
    # else:
    #     for i in range(l//2): #1234567 , l = 7, l//2 = 3, 0->2
    #         k=int(n[i]+n[l-1-i])
    #         x+=k
    #     x+=int(n[l//2])

    for i in range(l//2): 
        k=int(n[i]+n[l-1-i]) 
        x+=k
    

    if l%2 !=0:
        x+= int(n[l//2])

    return x


n=int(input())
print(clousersum(n))



"""
input: 12345
output: 15 + 24 + 3  = 42
       0123 
input: 1234
output: 14 + 23 = 37
"""





