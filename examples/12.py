
#tcs digital qn.
'''
input:10    output:5
explination:
    find the count of operations... by subtacting largest factor of a number 
    10 -> 5 -> 4 -> 2 -> 1
input:8     output:4
    8 -> 4 -> 2 -> 1
'''

n=int(input())
c=1
l=[]
while n>1:                    #no of steps for getting zero by diviors
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    n=n-l[-1]
    print(n)
    c+=1
print(c)