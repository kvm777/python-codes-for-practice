ch=input()
ch=list(ch)
vo='aeiouAEIOU'
vo=list(vo)
inx=[]
vow=[]                                  #reverse of vowels in a string
fin=[]                                                              
for i in range(len(ch)):
    if ch[i] in vo:
        vow.append(ch[i])
        inx.append(i)
vow=vow[::-1]
ind=0
for i in range(len(ch)):
    if i in inx:
        fin.append(vow[ind])
        ind+=1
    else:
        fin.append(ch[i])
fin=''.join(fin)
print(fin)        

        
