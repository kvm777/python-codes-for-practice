

#write code here
l=list(map(str,input1.split()))
c=0 
for i in l:
    if i==i[::-1]:
        c+=1

return c


