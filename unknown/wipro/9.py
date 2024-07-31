# ch=input()
# ch=list(ch)
# vo='aeiouAEIOU'
# vo=list(vo)
# inx=[]
# vow=[]                                  #reverse of vowels in a string
# fin=[]                                                              
# for i in range(len(ch)):
#     if ch[i] in vo:
#         vow.append(ch[i])
#         inx.append(i)
# vow=vow[::-1]
# ind=0
# for i in range(len(ch)):
#     if i in inx:
#         fin.append(vow[ind])
#         ind+=1
#     else:
#         fin.append(ch[i])
# fin=''.join(fin)
# print(fin)        

s = input()

v = "aeiouAEIOU"
idx=[]
vow=[]
# vow = vow[::-1]

for i in range(len(s)):
    if s[i] in v:
        idx.append(i)
        vow.append(s[i])
s1=""
for i in range(len(s)):
    if i in idx:
        s1+=vow[-1]
        vow.pop()
    else:
        s1+=s[i]

print(s1)
