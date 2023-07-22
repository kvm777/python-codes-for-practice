    
#write code here
s=input()

s1=s[::-1]
s3=s1[0]
c=1
for i in range(1,len(s1)):
    if s1[0]==s1[i]:
        s3+=s1[i]
        c+=1
    else:
        break

self.output1=c
self.output2=s3

return self.output1,self.output2








