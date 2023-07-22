

#repeat the alphabets in str by input as  a3b2c4 ------  the output is aaabbcccc

n=input()
l=[]
for i in range(0,len(n),2):
    l.extend([n[i]*int(n[i+1])])
    #l.append(*([n[i-1]*int(n[i])]))
    #  for j in range(int(n[i])):
    #   l.append(n[i-1])

print(l)
l=''.join(l)
print(l)
