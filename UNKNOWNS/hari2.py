s1=input()
s2=input()
s3=''
i=0
j=0
while (i<len(s1)) and (j<len(s2)):
    if ord(s1[i])<=ord(s2[j]):
        s3+=s1[i]
        i+=1
    else:
        s3+=s2[j]
        j+=1
while (i<len(s1)):
    s3+=s1[i]
    i+=1
while (j<len(s2)):
    s3+=s2[i]
    j+=1

print(s3)
